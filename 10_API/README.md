# 10) API 서버 구축

>1. 목표
>   RESTful API 서버 구축
>2. 준비 사항
>3. (필수) Python Web Framework
>   Django 2.1.x
>   Python 3.6.x
>4. (선택) 샘플 영화 정보
>   링크
>5. 요구 사항
>6. 데이터베이스 설계
>   db.sqlite3 에서 테이블 간의 관계는 아래와 같습니다.

#### 필드명 자료형 설명
* `Movie`

  title String 영화명
  audience Integer 누적 관객수
  poster_url String 포스터 이미지 URL
  description Text 영화 소개

* `Genre`

  genre_id Integer Genre의 Primary Key(id 값)
  name String 장르 구분

* `Score`

  Score
  content String 한줄평(평가 내용)
  score Integer 평점
  movie_id Integer Movie의 Primary Key(id 값)

2. Seed Data 반영
1. 주어진 movie.json 과 genre.json 을 movies/fixtures/ 디렉토리로 옮깁니다.
4. 아래의 명령어를 통해 반영합니다.
3. admin.py 에 Genre 와 Movie 클래스를 등록한 후, /admin 을 통해 실제로 데이터베이스에 반영
되었는지 확인해봅시다.
3. movies API
아래와 같은 API 요청을 보낼 수 있는 서버를 구축해야 합니다.
허용된 HTTP 요청을 제외하고는 모두 405 Method Not Allowed를 응답합니다.
1. GET /api/v1/genres/
