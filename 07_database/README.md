# Project_07 Database
> * 데이터를 생성, 조회, 삭제, 수정할 수 있는 Web Apllication 제작
> * Python Web Framework - Django를 통한 데이터 조작
> * Template Variable을 활용한 `templates` 제작
> * Static 경로 설정을 통한 `static` 파일 관리
> * 영화 추천 사이트의 영화 정보 SQL로 데이터 관리

### 사용 기술
* Django 2.1.x
* Python 3.6.x
* Bootstrap CSS/JS
* SQLite3
    - 예시 영화 정보 `data.csv`

### 파일 경로
```
06_django/
    movie_recommendation/
        ...
        static/
            bootstrap/
                ...
            images/
                ...
        templates/
            base.html
            home.html
        settings.py
        urls.py
        views.py
        ...
    movies/
        ...
        migrations/
            ...
            0001._initial.py
        templates/
            movies/
                detail.html
                edit.html
                index.html
                new.html
        ...
        models.py
        urls.py
        views.py
    data.csv
    db.sqlite3
    manage.py
    README.md
```

## 세부 사항
#### 0. 베이스
* static 경로 `movies_recommendation/static/`
    - Bootstrap 파일과 images 파일 관리
    - `settings.py`에서 `STATICFILES_DIR`로 경로 설정
    ```python
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'movie_recommendation', 'static'),
    ]
    ```
* base template 경로 `movies_recommendation/static/`
    - base template 파일 관리
        - `Jinja` block 기능으로 하단 template에 출력
        - `style sheet`, `script`, `<header>`, `<footer>`, `<display>` 등 block화
    - `settings.py`에서 `'DIRS': [os.path.join(BASE_DIR 'movie_recommendation', 'templates')]` 경로 설정
* application URL 관리
    - base는 `/` 경로, application은 application 하단에 있는 URL로 경로 설정
    ```python
    urlpatterns = [
        ...
        path('', views.home, name="home"),
        path('movies/', include('movies.urls')),
    ]
    ```

#### 1. 데이터베이스
* `Movie` from `movies/models.py`
    - Django ORM class
    ```python
    class Movie(models.Model):
        title = models.CharField(max_length=30) # 영화명
        audience = models.IntegerField() # 누적 관객수
        genre = models.CharField(max_length=10) # 장르
        score = models.FloatField() # 평점
        poster_url = models.URLField() # 포스터 이미지 URL
        description = models.TextField() # 영화 소개
    ```

#### 2. 페이지
> `urls.py`를 통한 template variable로 application 내에 있는 별도의 `views.py`의 함수와 기능 연결
> `urls.py`에서 각 경로에 대한 `name`값 지정을 통해 URL호출 용이
1. 영화 목록
    - URL `/movies/`
    - 데이터베이스 테이블 `Movie`에 존재하는 모든 영화 목록이 출력
        - 각 영화의 `title`, `score`이 표시
    - `title` 클릭 시, 해당 영화 정보 조회
    - 최하단에는 `영화 추가` 링크가 있으며 클릭 시 해당 페이지로 이동
    - Bootstrap `table`로 보여줌
2. 영화 정보 조회
    - `movies/<int:movie_id>/`에 따른 동적 할당 URL
        - `movie_id`는 각 영화의 `primary key`
    - 해당 `movie_ id`를 가진 영화의 모든 정보 표시
    - 영화 정보 최하단에는 `목록`, `수정`, `삭제` 링크가 있으며 클릭 시 해당 사항 페이지로 이동
    - Bootstrap `card`로 보여줌
3. 영화 정보 삭제
    - `movie/<int:movie_id>/delete/`에 따른 동적 할당 URL
    - 해당 `movie_id`를 가진 영화를 데이터베이스에서 삭제
    - 영화 정보 목록 페이지로 `redirect`
4. 영화 추가
    - URL `movies/new/`
    - `form`에 새로운 영화 정보 입력 후 제출하면 데이터베이스에 등록완료
    - `POST` 방식
        - Django `CRSF` token 사용
    - 등록된 영화 정보 페이지로 `redirect`