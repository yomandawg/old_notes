# Project 04_CRUD
> Create, Read, Update, Delete
> Object Relational Mapping


## 주제
* 데이터를 생성(create), 조회(read), 수정(update), 삭제(delete)할 수 있는 Web Application
* Python Web Framework를 통한 데이터 조작
* Object Relational Mapping에 대한 이해
* Template Variable을 활용한 Template 제작
* 영화 추천 사이트의 영화 정보 데이터 관리


## Skillset
* Python 3
* Flask
* SQLalchemy
* Bootstrap - HTML5/CSS


## 데이터베이스
* **ORM**을 통해 작성한 class *Movie*
* Class 변수
    - 영화명, 영화명(영문), 누적 관객수, 개봉일, 장르, 관람등급, 평점, 포스터 이미지 URL, 영화소개
    ```python
    class Movie(db.Model):
    __tablename__ = "movies"
    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    title_en = db.Column(db.String, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    watch_grade = db.Column(db.String, nullable=False)
    score = db.Column(db.String, nullable=False)
    poster_url = db.Column(db.TEXT, nullable=False)
    description = db.Column(db.TEXT, nullable=False)
    ```


## 페이지
1. 영화 목록
    - URL `/` 또는 `/movie/`를 통해 접근
    - 데이터베이스에 존재하는 모든 영화의 목록이 `Bootstrap card`로 표시
    - `title`, `score`, `poster_url`이미지가 표시
    - `title` 클릭 시 영화 정보 조회 페이지로 가능
    - `영화 등록` 클릭 시 영화 정보 생성 Form 페이지로 이동

2. 영화 정보 생성 *new*
    - URL `/movies/new/`를 통해 접근
    - `Movie` class의 변수 input
    - `POST` method 사용
    - `open_date`는 calendar 입력, `score`은 0.5점 간격, `genre`와 `watch_grade`는 미리 선정된 option들로 선택 가능
    - 필수 영역 미개재시 등록 불가능

3. 영화 정보 생성 *create*
    - URL `/movies/create/`를 통해 접근
    - `POST` method 사용
    - 이전 페이지에서 전송받은 데이터를 데이터베이서에 저장
    - 등록 완료시 영화 목록 페이지로 `redirect`

4. 영화 정보 조회
    - URL `/movies/<int:movie_id>`를 동적 할당하여 접근
        * `movie_id`는 `primary_key`
    - 해당 `primary_key`를 가진 영화의 모든 정보 표시
    - 하단에 목록, 수정, 삭제 링크가 있음

5. 영화 정보 수정 *edit*
    - URL `/movies/<int:movie_id>/edit/`를 동적 할당하여 접근
    - 해당 `primary_key`를 가진 영화의 정보를 수정할 수 있는 Form이 표시
    - 이전 정보가 입력된 채로 표시
        * option기능들도 입력된 채로 표시
    - 재등록시 `request`와 함께 전송됨
    - `POST` method 사용

6. 영화 정보 수정 *update*
    - URL `/movies/<int:movie_id>/update/`를 동적 할당하여 접근
    - 해당 `primary_key`를 가진 영화의 정보를 앞선 페이지의 `request`를 통해 받은 정보로 수정함
    - 수정 완료시 영화 목록 페이지로 `redirect`

7. 영화 정보 삭제
    - URL `/movies/<int:movie_id>/delete/`를 동적 할당하여 접근
    - 해당 `primary_key`를 가진 영화의 정보를 데이터베이스에서 삭제
    - 삭제 완료시 영화 목록 페이지로 `redirect`


## 결과
```
04_crud/
    README.md
    app.py
    Movie.db
    templates/
        index.html
        edit.html
        new.html
        show.html
```