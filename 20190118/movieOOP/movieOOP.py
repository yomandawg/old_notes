import requests
import csv
import urllib.request
import os
from datetime import date, timedelta

class MovieOOP:
    KEY_KOBIS = os.getenv("KEY_KOBIS")
    KEY_NAVER = os.getenv("KEY_NAVER")
    PW_NAVER = os.getenv("PW_NAVER")
    movieCd = []
    movieNm = []
    thumb_url = []
    
    def __init__(self, weeks):
        self.weeks = weeks

    # Box Office top 10 출력 for {} weeks
    def boxoffice(self, weekGb=0):
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}&weeekGb={}'
        box = csv.writer(open('boxoffice.csv', 'w', encoding='utf-8', newline=''))
        box.writerow(['영화코드', '영화명', '누적관객수'])

        for week in range(self.weeks):
            targetDt = (date(2019, 1, 13) - timedelta(7*week)).strftime("%Y%m%d")
            url = base_url.format(self.KEY_KOBIS, targetDt, weekGb)
            response = requests.get(url).json().get("boxOfficeResult")
            weekdays = response.get("showRange")
            self.movieCd.append(response.get("weeklyBoxOfficeList")[0].get("movieCd"))

            box.writerow([weekdays])
            for i in range(10):
                result = [response.get("weeklyBoxOfficeList")[i].get(value) for value in ["movieCd", "movieNm", "audiAcc"]]
                box.writerow(result)
            box.writerow([])

    def movie(self, movieCd=movieCd):
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}'
        box = csv.writer(open('movie.csv', 'w', encoding='utf-8', newline=''))
        box.writerow(['영화코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '개봉연도', '상영시간', '장르', '감독명', '배우1', '배우2', '배우3', '관람등급'])

        for code in movieCd:
            url = base_url.format(self.KEY_KOBIS, code)
            response = requests.get(url).json().get("movieInfoResult").get("movieInfo")
            self.movieNm.append(response.get("movieNm"))

            result = [response.get(value) for value in ["movieCd", "movieNm", "movieNmEn", "movieNmOg", 'prdtYear', "showTm"]]
            genre = response.get("genres")[0].get("genreNm")
            director = response.get("directors")[0].get("peopleNm")
            actor = [ _.get("peopleNm") for _ in response.get("actors")[:3] ]
            grade =  response.get("audits")[0].get("watchGradeNm")
            result += [genre, director, *actor, grade]
            box.writerow(result)

    def movie_naver(self, movieNm=movieNm):
        base_url = 'https://openapi.naver.com/v1/search/movie.json?query={}&display=1'
        headers = {'X-Naver-Client-Id': self.KEY_NAVER, 'X-Naver-Client-Secret': self.PW_NAVER }
        box = csv.writer(open('movie_naver.csv', 'w', encoding='utf-8', newline=''))
        box.writerow(['movie_name', 'movie_code', 'thumb_url', 'link_url', 'user_rating'])

        for name, code in zip(movieNm, self.movieCd):
            url = base_url.format(name)
            response = requests.get(url, headers=headers).json().get("items")[0]
            result = [name, code] + [response.get(value) for value in ["image", "link", "userRating"]]
            self.thumb_url.append(result[2])
            box.writerow(result)
    
    def image(self, thumb_url=thumb_url):
        for thumb, code in zip(thumb_url, self.movieCd):
            urllib.request.urlretrieve(thumb, f"./images/{code}.jpg")

movie = MovieOOP(2)
movie.boxoffice()
movie.movie()
movie.movie_naver()
movie.image()