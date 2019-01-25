# Python Project: Movie

> Start date: 2019-01-18
>
> Last date: 2019-01-19


## 1. 목표

* python과 Flask microframework를 이용해 데이터 수집 및 파일 저장

* KOBIS, NAVER API 활용으로 영화 파일 저장 및 가공

* 영화평점사이트 제작


## 2. 준비 사항

* Python 3.6

* 활용 library 목록
  - `requests` `csv` `urlib` `os` `time` `datetime`

* 활용 framework
  - Flask

* 활용 API service
  - KOBIS 주간/주말 박스오피스 API
  - KOBIS 영화 상세정보 API
  - Naver 영화 검색 API


# 결과

## 1. movie/movie.py

* 함수를 이용한 서비스 구현

### 함수 목록

```python
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
```
- KOBIS 주간/주말 박스오피스 API를 이용해 *'./csv/boxoffice.csv'* 파일로 다음과 같은 형식으로 정보 저장
  - `boxoffice.writerow(['showRange, 'movieCd', 'movieNm', 'audiAcc'])`

- csv 파일 저장을 위해 `csv` library 사용

- `requests를` 이용해 정보를 crawling할 때, 임의의 날짜 지정을 위하여 `time`과 `timedelta` library 사용


```python
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
```
- KOBIS 영화 정보 API를 이용해 *'./csv/movie.csv'* 파일로 다음과 같은 형식으로 정보 저장
  - `movie_info.writerow(['영화코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '개봉연도', '상영시간', '장르', '감독명', '배우1', '배우2', '배우3', '관람등급'])`
- 앞선 boxoffice 함수에서 저장한 `'boxoffice.csv'` 파일에서 `movieCd` 값을 받아와 KOBIS 영화 정보 API에 넣어 검색하는 방식


```python
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
```
- 네이버 영화 검색 API 사용

- 검색 제한이 있어 1주일만 출력함

- 다음과 같은 형식으로 정보 저장
  - `movie_naver.writerow(['movie_name', 'movie_code', 'thumb_url', 'link_url', 'user_rating'])`

- 앞서 저장한 `movieCd`로 검색하는 방식 구현

- 호출 빈도가 너무 빠르면 제한이 걸려 `time.sleep(.100)`으로 초당 횟수 제한


```python
def image():
    movie_naver = csv.reader(open("./csv/movie_naver.csv", "r", encoding="utf-8"))
    for row in movie_naver:
        movieCd, thumb_url = row[1], row[2]
        urllib.request.urlretrieve(thumb_url, "./images/{}.jpg".format(movieCd))

    return
```
- 앞서 저장한 `thumb_url` 주소 정보를 이용해 image 파일을 `.jpg`형식으로 다운로드



### 2. movieOOP/movieOOP.py

* OOP를 이용해 위 방식 구현

```python
class Movie:
    KEY_KOBIS = os.getenv("KEY_KOBIS")
    KEY_NAVER = os.getenv("KEY_NAVER")
    PW_NAVER = os.getenv("PW_NAVER") 
    def __init__(self, weeks=1, path='.'):
        self.weeks=weeks
        self.path=path

    def boxoffice(self, weekGb=0, key=KEY_KOBIS):
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={}&targetDt={}&weeekGb={}'
        boxoffice = csv.writer(open('{}/csv/boxoffice.csv'.format(self.path), 'w', encoding='utf-8', newline=''))
        # boxoffice.writerow(['showRange, 'movieCd', 'movieNm', 'audiAcc'])

        for week in range(self.weeks):
            targetDt = (date(2019, 1, 13) - timedelta(7*week)).strftime("%Y%m%d")
            url = base_url.format(key, targetDt, weekGb)
            response = requests.get(url).json().get("boxOfficeResult")
            weekdays = [response.get("showRange")]

            for i in range(10):
                result = weekdays + [response.get("weeklyBoxOfficeList")[i].get(value) for value in ["movieCd", "movieNm", "audiAcc"]]
                boxoffice.writerow(result)
        
        return


    def movie(self, key=KEY_KOBIS):
        base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}'
        boxoffice = csv.reader(open("{}/csv/boxoffice.csv".format(self.path), 'r', encoding="utf-8"))
        movie_info = csv.writer(open('{}/csv/movie.csv'.format(self.path), 'w', encoding="utf-8", newline=''))
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


    def movie_naver(self, key=KEY_NAVER, pw=PW_NAVER):
        base_url = 'https://openapi.naver.com/v1/search/movie.json?query={}&display=1'
        headers = {'X-Naver-Client-Id': key, 'X-Naver-Client-Secret': pw }
        movie_info = csv.reader(open("{}/csv/movie.csv".format(self.path), "r", encoding="utf-8"))
        movie_naver = csv.writer(open("{}/csv/movie_naver.csv".format(self.path), "w", encoding="utf-8", newline=""))
        # movie_naver.writerow(['movie_name', 'movie_code', 'thumb_url', 'link_url', 'user_rating'])

        for row in movie_info:
            movieCd, movieNm = row[0], row[1]
            url = base_url.format(movieNm)
            response = requests.get(url, headers=headers).json().get("items")[0]
            result = [movieNm, movieCd] + [response.get(value) for value in ["image", "link", "userRating"]]
            movie_naver.writerow(result)
            time.sleep(.100) # naver API 호출 빈도 제한

        return


    def image(self):
        movie_naver = csv.reader(open("{}/csv/movie_naver.csv".format(self.path), "r", encoding="utf-8"))
        for row in movie_naver:
            movieCd, thumb_url = row[1], row[2]
            urllib.request.urlretrieve(thumb_url, "{}/images/{}.jpg".format(self.path, movieCd))

        return
```
- 전체적인 흐름은 원본과 동일하다.

- 클래스 선언에서 경로와 몇주를 검색할 수 있는지 지정할 수 있게 하였다.

- 클래서 변수에 중요 정보들을 미리 넣어주었다.



## 1. app.py

* Flask microframework를 이용한 웹페이지 구현

```python
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    MovieSearch = Movie(1, './movie/movieOOP')
    MovieSearch.boxoffice()
    MovieSearch.movie()
    MovieSearch.movie_naver()
    MovieSearch.image()

    movie_info = csv.reader(open("{}/csv/movie_naver.csv".format('./movie/movieOOP'), "r", encoding="utf-8"))
    return render_template('index.html', movie_info=movie_info)
```
- `Flask`를 이용해 위의 OOP를 가져와 웹페이지에 구현했다.

- `html` 페이지의 `css`는 `bootstrap` framework에서 예시를 따랐다.

- 앞서 저장한 images의 `thumb_url` 이미지 파일들을 페이지에 나타내고 추가적으로 평점과 네이버 사이트 링크를 첨부했다.