-- 
-- sqlite> .read 04_expression.sql
-- 
SELECT SUM(누적관객수) FROM movies;
-- "SUM(누적관객수)"
-- 426366183

SELECT 영화이름, MAX(누적관객수) FROM movies;
-- "영화이름","MAX(누적관객수)"
-- "신과함께-죄와 벌",14398110

SELECT 영화이름, MIN(상영시간) FROM movies;
-- "영화이름","MIN(상영시간)"
-- "바다 탐험대 옥토넛 시즌4: 더 파이널"

SELECT AVG(누적관객수) FROM movies WHERE 제작국가='한국';
-- "AVG(누적관객수)"
-- 1627276.06976744

SELECT COUNT(관람등급) FROM movies WHERE 관람등급='청소년관람불가';
-- "COUNT(관람등급)"
-- 27

SELECT COUNT(*) FROM movies WHERE 상영시간>=100 AND 장르='애니메이션';
-- COUNT(*)
-- 22