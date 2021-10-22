#DB選択
USE TEACHERSDB;

update m010_saibnmst 
	set SAIBNVALUE = 1 , 
		UPDSRV = "S0001" ,
		UPDUSR = "tsunesanbk" ,
		UPDDATE = current_timestamp(6) 
	where TABLEID = 'T100' ;
