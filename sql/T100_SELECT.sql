#DB選択
USE TEACHERSDB;

#詳細1件
select SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID,CRTDATE,UPDDATE from t100_shitsmn where SHITSMN_ID = "Q20210920000000001" ;

#新着リスト
select SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID,CRTDATE,UPDDATE from t100_shitsmn order by crtdate desc limit 20 ;

select * from t100_shitsmn;
select * from t101_shitsmnhashtag;
select * from t102_kaigikbujkn;
select * from t110_hashtag;
select * from t120_kaitrequest;

select SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID,CRTDATE,UPDDATE 
	from t100_shitsmn t100_main 
    where  t100_main.SHITSMN_ID 
		in 	(
				select MAX(t100.SHITSMN_ID) 
				from	t100_shitsmn t100
				left outer join t101_shitsmnhashtag t101
					on   t100.SHITSMN_ID = t101.SHITSMN_ID
				left outer join t102_kaigikbujkn t102
					on t100.SHITSMN_ID = t102.SHITSMN_ID
				left outer join t120_kaitrequest t120
					on t102.SHITSMN_ID = t120.SHITSMN_ID
						AND t102.SEQ = t120.SEQ
			where "0" = "0"
				AND ((t100.SHITSMN_TITLE like "%マカヒキ%") or (t100.SHITSMN_NAIYO like "%マカヒキ%"))
				#AND t100.SHITSMN_USERID = "tsunesanbk"
				#AND t101.HASHTAG in ("競馬","マカヒキ")
				AND t102.KAISHNCHJ >= "2021-10-15 21:00:00"
				AND t102.KAISHNCHJ <= "2021-10-17 21:00:00"
				#AND t120.KAIT_USERID = "tsunesanBK"
			group by t100.SHITSMN_ID
			)
;


#==以下メモ====================================================================
#条件リスト
select * 
from	t100_shitsmn t100
	left outer join t101_shitsmnhashtag t101
		on   t100.SHITSMN_ID = t101.SHITSMN_ID
			AND t101.HASHTAG in ("競馬","マカヒキ")
	left outer join t102_kaigikbujkn t102
		on t100.SHITSMN_ID = t102.SHITSMN_ID
        #AND t102.KAISHNCHJ <= ""
        #AND t102.KAISHNCHJ >= ""
	left outer join t120_kaitrequest t120
		on t102.SHITSMN_ID = t120.SHITSMN_ID
			AND t102.SEQ = t120.SEQ
			AND t120.KAIT_USERID = "tsunesanBK"
where (t100.SHITSMN_TITLE like "%マカヒキ%" or t100.SHITSMN_NAIYO like "%マカヒキ%")
	and t100.SHITSMN_USERID = "tsunesanbk"
;

select SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID,CRTDATE,UPDDATE 
  from t100_shitsmn t100_main 
     where  
    exists (select 1 from 
          (
     select MAX(t100.SHITSMN_ID) as SHITSMN_ID
     from t100_shitsmn t100
     left outer join t101_shitsmnhashtag t101
      on   t100.SHITSMN_ID = t101.SHITSMN_ID
     left outer join t102_kaigikbujkn t102
      on t100.SHITSMN_ID = t102.SHITSMN_ID
     left outer join t120_kaitrequest t120
      on t102.SHITSMN_ID = t120.SHITSMN_ID
       AND t102.SEQ = t120.SEQ
    where "0" = "0"
     AND ((t100.SHITSMN_TITLE like "%マカヒキ%") or (t100.SHITSMN_NAIYO like "%マカヒキ%"))
     #AND t100.SHITSMN_USERID = "tsunesanbk"
     #AND t101.HASHTAG in ("競馬","マカヒキ")
     AND t102.KAISHNCHJ >= "2021-10-15 21:00:00"
     AND t102.KAISHNCHJ <= "2021-10-17 21:00:00"
     #AND t120.KAIT_USERID = "tsunesanBK"
    group by t100.SHITSMN_ID
    ) 
 t100_sub where t100_main.SHITSMN_ID =  t100_sub.SHITSMN_ID 
 )