#DB選択
USE TEACHERSDB;

select HASHTAG from T110_HASHTAG where HASHTAG like '天皇賞%' order by COUNTER desc limit 5 ;