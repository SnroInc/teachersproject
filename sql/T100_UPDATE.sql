USE TEACHERSDB;

select * from t100_shitsmn where SHITSMN_ID = "Q20211017000000036" ;
update t100_shitsmn 
	set SHITSMN_TITLE = '天皇賞秋',
		SHITSMN_NAIYO = 'グランアレグリア一択ですか？',
        SHITSMN_USERID = 'tsunesanbk',
        KAIGIID = null,
        DELFLG = '0',
        UPDSRV = 'S000',
        UPDUSR = 'tsunesanbk',
        UPDDATE = current_timestamp(6)
	where SHITSMN_ID = "Q20211017000000036"
;