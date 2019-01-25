import requests
import csv
import urllib.request
import os
import time
from datetime import date, timedelta

# KEY_KOBIS = os.getenv("KEY_KOBIS")
# KEY_NAVER = os.getenv("KEY_NAVER")
# PW_NAVER = os.getenv("PW_NAVER")
KEY_KOBIS = "08305de6d4fe4be99dd4e3293b30dfa2"
KEY_NAVER = "xL3zdvWuqpSs08aJTPbk"
PW_NAVER = "CBUZR1B2cH"


def boxoffice(weeks=1, weekGb=0, key=KEY_KOBIS):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}&weeekGb={}'
    boxoffice = csv.writer(open('./csv/boxoffice.csv', 'w', encoding='utf-8', newline=''))
    # boxoffice.writerow(['showRange, 'movieCd', 'movieNm', 'audiAcc'])

    for week in range(weeks):
        targetDt = (date(2019, 1, 13) - timedelta(7*week)).strftime("%Y%m%d")
        url = base_url.format(key, targetDt, weekGb)
        response = requests.get(url).json().get("boxOfficeResult")
        weekdays = [response.get("showRange")]

        for i in range(10):
            result = weekdays + [response.get("weeklyBoxOfficeList")[i].get(value) for value in ["movieCd", "movieNm", "audiAcc"]]
            boxoffice.writerow(result)
    
    return


def movie(key=KEY_KOBIS):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}'
    boxoffice = csv.reader(open("./csv/boxoffice.csv", 'r', encoding="utf-8"))
    movie_info = csv.writer(open('./csv/movie.csv', 'w', encoding="utf-8", newline=''))
    # movie_info.writerow(['영화코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '개봉연도', '상영시간', '장르', '감독명', '배우1', '배우2', '배우3', '관람등급'])

    for row in boxoffice:
        movieCd = row[1]
        url = base_url.format(key, movieCd)
        response = requests.get(url).json().get("movieInfoResult").get("movieInfo")
        
        result = [response.get(value) for value in ["movieCd", "movieNm", "movieNmEn", "movieNmOg", "prdtYear", "showTm"]]
        genre = response.get("genres")[0].get("genreNm")
        director = response.get("directors")[0].get("peopleNm")
        actor = [i.get("peopleNm") for i in response.get("actors")[:3]]
        grade = response.get("audits")[0].get("watchGradeNm")
        result += [genre, director, *actor, grade]
        movie_info.writerow(result)
    
    return


def movie_naver(key=KEY_NAVER, pw=PW_NAVER):
    base_url = 'https://openapi.naver.com/v1/search/movie.json?query={}&display=1'
    headers = {'X-Naver-Client-Id': key, 'X-Naver-Client-Secret': pw }
    movie_info = csv.reader(open("./csv/movie.csv", "r", encoding="utf-8"))
    movie_naver = csv.writer(open("./csv/movie_naver.csv", "w", encoding="utf-8", newline=""))
    # movie_naver.writerow(['movie_name', 'movie_code', 'thumb_url', 'link_url', 'user_rating'])

    for row in movie_info:
        movieCd, movieNm = row[0], row[1]
        url = base_url.format(movieNm)
        response = requests.get(url, headers=headers).json().get("items")[0]
        result = [movieNm, movieCd] + [response.get(value) for value in ["image", "link", "userRating"]]
        movie_naver.writerow(result)
        time.sleep(.100) # naver API 호출 빈도 제한

    return


def image():
    movie_naver = csv.reader(open("./csv/movie_naver.csv", "r", encoding="utf-8"))
    for row in movie_naver:
        movieCd, thumb_url = row[1], row[2]
        urllib.request.urlretrieve(thumb_url, "./images/{}.jpg".format(movieCd))

    return


boxoffice(1)
movie()
movie_naver()
image()