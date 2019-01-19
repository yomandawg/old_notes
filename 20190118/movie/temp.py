import requests
import csv
import urllib.request
import os
from datetime import date, timedelta

# KEY_KOBIS = os.getenv("KEY_KOBIS")
# KEY_NAVER = os.getenv("KEY_NAVER")
# PW_NAVER = os.getenv("PW_NAVER")

KEY_KOBIS = "08305de6d4fe4be99dd4e3293b30dfa2"
KEY_NAVER = "xL3zdvWuqpSs08aJTPbk"
PW_NAVER = "CBUZR1B2cH"
movieCd = []
movieNm = []
thumb_url = []

# week
# 몇주치를 출력할지 선택 입력합니다.
# weekGb
# 주간/주말/주중을 선택 입력합니다.
# 0 : 주간 (월~일) / 1 : 주말 (금~일) / 2 : 주중 (월~목)
def boxoffice(weeks=1, weekGb=0, key=KEY_KOBIS):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}&weeekGb={}'
    box = csv.writer(open('boxoffice.csv', 'w', encoding='utf-8', newline=''))
    box.writerow(['영화코드', '영화명', '누적관객수'])

    for week in range(weeks):
        targetDt = (date(2019, 1, 13) - timedelta(7*week)).strftime("%Y%m%d")
        url = base_url.format(key, targetDt, weekGb)
        response = requests.get(url).json().get("boxOfficeResult")
        weekdays = response.get("showRange")
        movieCd.append(response.get("weeklyBoxOfficeList")[0].get("movieCd"))

        box.writerow([weekdays])
        for i in range(10):
            result = [response.get("weeklyBoxOfficeList")[i].get(value) for value in ["movieCd", "movieNm", "audiAcc"]]
            box.writerow(result)
        box.writerow([])
    
def movie(movieCd=movieCd, key=KEY_KOBIS):
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}'
    box = csv.writer(open('movie.csv', 'w', encoding='utf-8', newline=''))
    box.writerow(['영화코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '개봉연도', '상영시간', '장르', '감독명', '배우1', '배우2', '배우3', '관람등급'])

    for code in movieCd:
        url = base_url.format(key, code)
        response = requests.get(url).json().get("movieInfoResult").get("movieInfo")
        movieNm.append(response.get("movieNm"))

        result = [response.get(value) for value in ["movieCd", "movieNm", "movieNmEn", "movieNmOg", 'prdtYear', "showTm"]]
        genre = response.get("genres")[0].get("genreNm")
        director = response.get("directors")[0].get("peopleNm")
        actor = [ _.get("peopleNm") for _ in response.get("actors")[:3] ]
        grade =  response.get("audits")[0].get("watchGradeNm")
        result += [genre, director, *actor, grade]
        box.writerow(result)

def movie_naver(movieNm=movieNm, key=KEY_NAVER):
    base_url = 'https://openapi.naver.com/v1/search/movie.json?query={}&display=1'
    headers = {'X-Naver-Client-Id': KEY_NAVER, 'X-Naver-Client-Secret': PW_NAVER }
    box = csv.writer(open('movie_naver.csv', 'w', encoding='utf-8', newline=''))
    box.writerow(['movie_name', 'movie_code', 'thumb_url', 'link_url', 'user_rating'])

    for name, code in zip(movieNm, movieCd):
        url = base_url.format(name)
        response = requests.get(url, headers=headers).json().get("items")[0]
        result = [name, code] + [response.get(value) for value in ["image", "link", "userRating"]]
        thumb_url.append(result[2])
        box.writerow(result)
    
def image(thumb_url=thumb_url):
    for thumb, code in zip(thumb_url, movieCd):
        urllib.request.urlretrieve(thumb, f"./images/{code}.jpg")

boxoffice(2)
movie()
movie_naver()
image()