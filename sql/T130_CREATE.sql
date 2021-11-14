#DB選択
USE TEACHERSDB;

DROP TABLE T130_KAIGI;
CREATE TABLE T130_KAIGI (
	KAIGI_ID char(18) NOT NULL,
    KAIGI_PATH varchar(2048) NOT NULL,
    SHITSMN_USERID char(18) NOT NULL,
    KAIT_USERID char(18) NOT NULL,
	SHITSMN_ID char(18) NOT NULL,
	SEQ tinyint(2) NOT NULL,
	STR_DATETIME DATETIME(0) ,
	END_DATETIME DATETIME(0) ,
	KAIGITIME smallint ,
	CRTSRV char(5) NOT NULL,
	CRTUSR char(18) NOT NULL,
	CRTDATE DATETIME(6) NOT NULL,
	UPDSRV char(5) NOT NULL,
	UPDUSR char(18) NOT NULL,
	UPDDATE DATETIME(6) NOT NULL,
	DELFLG char(1) NOT NULL,
	PRIMARY KEY(KAIGI_ID),
    UNIQUE KEY(SHITSMN_ID)
);