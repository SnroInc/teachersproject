#DB選択
USE TEACHERSDB;

select * from T120_KAITREQUEST;

update T120_KAITREQUEST 
	set DELFLG = '1' , 
		UPDSRV = 'S0001' ,
		UPDUSR = 'SYSTEM000000000000' ,
		UPDDATE = current_timestamp(6) 
	where SHITSMN_ID = 'Q20210920000000001' 
		and SEQ = 1
        and RQSEQ = 3 ;

