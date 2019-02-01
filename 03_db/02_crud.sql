-- 
--  sqlite> .read 02_crud.sql
-- 
INSERT INTO movies (
    영화코드, 영화이름, 관람등급, 감독, 개봉연도,
    누적관객수, 상영시간, 제작국가, 장르
)
VALUES (
    20182530, '극한직업', '15세이상관람가', '이병헌', '20190123',
    '3138467', '111', '한국', '코미디'
);

SELECT * FROM movies WHERE 영화코드=20040521;
-- 영화코드        영화이름        관람등급        감독    개봉연도        누적관객수      상영시간    제작국가        장르
-- 20040521        클레멘타인      15세관람가      김두영  20040521        67000   100     한국액션
DELETE FROM movies WHERE 영화코드=20040521;

SELECT * FROM movies WHERE 영화코드=20185124;
-- 영화코드        영화이름        관람등급        감독    개봉연도        누적관객수      상영시간    제작국가        장르
-- 20185124        러브 유어셀프 인 서울   전체관람가              20190126        180966  111한국    공연
UPDATE movies SET 감독='없음' WHERE 영화코드=20185124;
SELECT * FROM movies WHERE 영화코드=20185124;
-- 영화코드        영화이름        관람등급        감독    개봉연도        누적관객수      상영시간    제작국가        장르
-- 20185124        러브 유어셀프 인 서울   전체관람가      없음    20190126        180966  111한국    공연