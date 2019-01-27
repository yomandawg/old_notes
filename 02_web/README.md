# Project 02_Web

* Bootstrap을 이용한 HTML/CSS, JS Component 활용 web front-end

* 영화 추천 사이트 컨셉의 반응형 페이지 꾸미기


### 프로젝트 파일 구성

```
02_web/
        README.md
        01_layout.html
        01_layout.css
        02_movie.html
        02_movie.css
        03_detail_view.html
        03_detail_view.css
        assets/
                *.jpg
```

* **예시 이미지는 `temp/`에 있습니다.**



## 프로젝트 설명

* *다음 설정은 모든 프로젝트 `html`파일에 해당된다.*

> `DOCTYPE`은 **html**로 설정하였다.
>
> 01_LAYOUT.html`에서 확인할 수 있다.
>
> html`의 언어는 `ko`(한국어)이다.
>
> `meta`태그의 인코딩 설정은 `UTF-8`이다.
>
> `meta`태그의 기본 *viewport*설정은 다음과 같다.
>
> 1. `width: device-width`
> 2. `initial-scale: 1.0`
>
> `title`태그는 **영화추천사이트**로 설정했다.

* 사용한 폰트 - Google Fonts
  * Black Hans Sans
  * Noto Serif



### Navigation Bar

* 최상단에 위치한 **navbar**에 대한 설정

* `sticky` 활용

  * navbar이 항상 상단에 고정됨

* 예시 하단 참고

  ![](C:\Users\ERIC\Desktop\New folder\kim_young_jun\project\02_web\temp\navbar.png)

* Font - Noto Serif
* 바탕화면 색상: `Bootstrap CSS`에서 `bg-light`



### Header

* 배경이미지 설정
* Font - Black Hans Sans
* 예시 하단 참고

![](C:\Users\ERIC\Desktop\New folder\kim_young_jun\project\02_web\temp\header.png)

* 배경화면 색상은 `css`에 다음과 같이 설정

  ```html
  div[class*="background"] {
      background-color: #A9A9A9;
      background-size: cover;
      background-image: url('assets/20182544-1.jpg');
      background-position: center center;
  }
  ```

  * url 이미지를 `background-image`로 사용하고, 이미지가 없을 때 `#A9A9A9`색상을 사용한다.



### Footer

* `html` 내용 최하단에 설정하여 항상 하단에 보이게끔 설정

* 왼쪽에 자체적으로 설정한 *닉네임* 오른쪽에 *헤더로 올라가는 링크*로 구성

* 예시 하단 참고

  ![](C:\Users\ERIC\Desktop\New folder\kim_young_jun\project\02_web\temp\footer.png)

* Font - Noto Serif



### 영화 리스트

* `html` 속 `container`에 속함

* `Bootstrap`의 `card`를 이용해 `flex`를 활용한 반응형 웹 구현

* 예시 하단 참고

  ![](C:\Users\ERIC\Desktop\New folder\kim_young_jun\project\02_web\temp\index.png)

* *subtitle*에 `margin` `3rem`인 **영화 목록**과 **underline**을 추가
* 제공된 영화 이미지가 카드 header에 포함
  * `alt` 속성값에 영화 이름
* 각각의 카드에 다음과 같은 항목들을 포함
  * 영화 이름
  * 장르
  * 개봉일
  * 평점
  * 영화 정보 버튼(네이버 링크)

* 반응형 배치
  * 576px 미만: 1개
  * 576px 이상 768px 미만: 2개
  * 768px 이상 992px 미만: 3개
  * 992px 이상: 4개
* `margin`은 `1rem`



### 영화 상세 보기

* `Bootstrap` `modal` 활용

  ![](C:\Users\ERIC\Desktop\New folder\kim_young_jun\project\02_web\temp\carousel.png)

* 카드뷰 이미지를 클릭하면 `modal`이 뜨도록 구성
  * `modal fade`
* 상단 이미지는 `carousel`로 구현
  * 제공된 이미지 3장 나타냄
* modal엔 다음과 같은 정보 제공
  * 관람 연령
  * 누적 관객
  * 줄거리





### Favicon

* 제공된 이미지로 `favicon` 설정