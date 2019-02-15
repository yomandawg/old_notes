# Project 05_detail

> Django Web Framework
>
> Bootstrap CSS, JS

### 목표

* Django Web Framework를 사용한 사이트의 세부 페이지 구성

* Template Variable을 활용한 Template 제작



### 경로

```
05_detail/
	detail/
		...
		static/
		templates/
		...
		admin.py
		views.py
	Django/
		...
		settings.py
		url.py
	...
	README.md
```



---



## Django 설정

* 프로젝트명: **Django**
* 어플리케이션명: *detail*



### Python Files

* Django 세부 설정이 담겨있는 python 파일들

```python
# /Django/settings.py
ALLOWED_HOSTS = [*]

INSTALLED_APPS = [
    ...
    'detail' # my app
]

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

STATIC_URL = '/static/'
```

* HOST에 `*` 추가로 local 주소 사용
* `detail`명의 어플리케이션 추가
* 한국어 설정 `ko-kr`
* 한국 시간대 설정 `Asia/Seoul`
* `static`파일 경로 `/static/`

``` python
# /Django/url.py
from detail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mypage/', views.mypage),
    path('qna/', views.qna),
    path('signup/', views.signup),
    path('<str:not_found>/', views.not_found),
]
```

* url 경로에 맞는 `views` 설정

```python
# /detail/views.py
def index(request):
    return render(request, 'index.html')

def qna(request):
    return render(request, 'qna.html')

def mypage(request):
    return render(request, 'mypage.html')

def signup(request):
    return render(request, 'signup.html')

def not_found(request, not_found):
    return render(request, 'not_found.html', {'not_found': not_found})
```

* url 경로에 맞는 기능 설정



### Static

* Bootstrap CSS/JS 파일과 custom 이미지 파일들

```
/detail/static/
	/bootstrap
		bootstrap.bundle.js
		bootstrap.bundle.min.js
		bootstarp.css
		bootstrap.js
		bootstrap.min.js
	/images
		bg.jpg
		favicon.ico
		muzi.jpg
		post.jpg
		ryan.png
```



### Templates

* Django `detail`앱의 `views`용 `url` 경로에 지정된 html templates들

```
/detail/templates/
	base.html
	index.html
	mypage.html
	not_found.html
	qna.html
	signup.html
```



---



## 어플리케이션 구성

### base.html

* `Jinja`를 이용한 코드 경량화
  * 다른 html파일들에 `{% extends 'base.html' %}`를 통해 `block title`, `block body` 확장

#### Navbar

* `bootstrap navbar component` 사용
* *Home* 클릭시 `/`로 이동
* *Q&A*클릭시 `qna/`로 이동
* *My Page*클릭시 `mypage/`로 이동
* *SignUp*클릭시 `signup/`로 이동

#### Footer

* 페이지 하단에 위치한 정보
* 높이 50px 너비 브라우저 전체 영역
* 좌측에 정보, 우측에 헤더로 올라가는 링크

#### Favicon

* `favicon` 추가



### index.html

* `/`경로 초기 페이지

#### Header

* Navbar 바로 아래 위치
* 높이는 350px, 너비 브라우저 전체 영역
* 배경 이미지 설정



### qna.html

* `qna/` 경로 페이지
* 사용자의 질문을 받기 위한 페이지
* `Bootstrap Form` 사용
  * 제목, 이메일, 내용, Submit
* input tag 사용
* 992px 화면 기준 제목/이메일 칸 이중 row화

