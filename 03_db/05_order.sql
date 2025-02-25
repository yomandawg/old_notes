-- 
-- sqlite> .read 05_order.sql
-- 
SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
-- "영화코드","영화이름","관람등급","감독","개봉연도","누적관객수","상영시간","제작국가","장르"
-- 20150976,"신과함께-죄와 벌","12세이상관람가","김용화",20171220,14398110,139,"한국","판타지"
-- 20090834,"아바타","12세이상관람가","제임스 카메론",20091217,13325055,161,"미국",SF
-- 20186202,"신과함께-인과 연","12세이상관람가","김용화",20180801,12264813,141,"한국","판타지"
-- 20162869,"택시운전사","15세이상관람가","장훈",20170802,12176753,137,"한국","드라마"
-- 20177478,"어벤져스: 인피니티 워","12세이상관람가","안소니 루소",20180425,11176953,149,"미국","액션"

SELECT * FROM movies WHERE 장르='애니메이션' ORDER BY 제작국가 ASC, 누적관객수 DESC LIMIT 10;
-- "영화코드","영화이름","관람등급","감독","개봉연도","누적관객수","상영시간","제작국가","장르"
-- 20182989,"커다랗고 커다랗고 커다란 배","전체관람가","필립 립스키",20180503,89577,77,"덴마크","애니메이션"
-- 20176082,"몬스터 패밀리","전체관람가","호거 태프",20171221,394152,92,"독일","애니메이션"
-- 20189268,"루이스","전체관람가","울프강 라우엔슈타인",20180920,89501,85,"독일","애니메이션"
-- 20179228,"마야2","전체관람가","노엘 클리어리",20180201,55214,84,"독일","애니메이션"
-- 20175223,"래빗 스쿨","전체관람가","우테 폰 뮌쇼폴",20171123,50578,75,"독일","애니메이션"
-- 20176741,"꼬마참새 리차드: 아프리카 원정대","전체관람가","토비 젠켈",20170615,33477,83,"독일","애니메이션"
-- 20172241,"꼬마돼지 베이브의 대모험","전체관람가","테레사 스트로젝",20170615,21755,79,"독일","애니메이션"
-- 20184512,"토니스토리2: 고철왕국의 친구들","전체관람가","토마스 보덴스타인",20180613,12415,81,"독일","애니메이션"
-- 20177761,"오즈: 신기한 마법가루","전체관람가","블라디미르 토로프킨",20170720,54998,90,"러시아","애니메이션"
-- 20182966,"투 프렌즈","전체관람가","빅터 아즈에프",20181129,20419,74,"러시아","애니메이션"

SELECT DISTINCT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;
-- "감독"
-- "드니 빌뇌브"
-- "제임스 카메론"
-- "니테쉬 티와리"
-- "크리스 콜럼버스"
-- "크리스토퍼 놀란"
-- "라이언 존슨"
-- "마이클 베이"
-- "안소니 루소"
-- "이창동"
-- "크리스토퍼 맥쿼리"