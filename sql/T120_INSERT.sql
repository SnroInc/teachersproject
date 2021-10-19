#DB選択
USE TEACHERSDB;

select IFNULL(MAX(RQSEQ),0) + 1 as NEWRQSEQ from T120_KAITREQUEST where SHITSMN_ID = 'Q20210920000000001' and SEQ = 1 ;

INSERT INTO T120_KAITREQUEST VALUES ('Q20210920000000001',1,1,'tsunesanBK','ウマ娘からきました',24,current_timestamp(0),'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO T120_KAITREQUEST VALUES ('Q20210920000000001',1,2,'nabehiki','マカヒキからきました',48,current_timestamp(0),'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO T120_KAITREQUEST VALUES ('Q20210920000000001',2,1,'tsunesanBK','ウマ娘からきました',24,current_timestamp(0),'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO T120_KAITREQUEST VALUES ('Q20210920000000001',2,2,'nabehiki','マカヒキから来ました',48,current_timestamp(0),'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');
INSERT INTO T120_KAITREQUEST VALUES ('Q20210920000000003',1,1,'inoshunelmyster','ロゴタイプィ',48,current_timestamp(0),'S000','SYSTEM',current_timestamp(6),'S000','SYSTEM',current_timestamp(6),'0');


