#DB選択
USE TEACHERSDB;

DROP TABLE S130_KAIG_ID;
CREATE TABLE S130_KAIG_ID (
	SAIBNDATE char(8) NOT NULL,
	SEQ int(9) NOT NULL,
	CRTDATE DATETIME(6) NOT NULL,
	PRIMARY KEY(SAIBNDATE,SEQ)
);
