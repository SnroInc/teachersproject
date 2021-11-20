#DB選択
USE TEACHERSDB;

select * from T130_KAIGI;

update T130_KAIGI 
	set KAIGI_PATH = '' , 
		SHITSMN_USERID = '' ,
        KAIT_USERID = '' ,
        SHITSMN_ID = '' ,
        SEQ = '' ,
        STR_DATETIME = '' ,
        END_DATETIME = '' ,
        KAIGITIME = '' ,
        UPDSRV = '' ,
        UPDUSR = '' ,
        UPDDATE = current_timestamp(6) ,
        DELFLG = ''
	where KAIGI_ID = '';