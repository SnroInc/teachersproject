"""
サービスクラス
S030_ShitsmnInfoKoshn

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil,C050_StringUtil

SERVICE_ID = "S030"

def main(shitsmnID,shitsmnTitle,shitsmnNaiyo,shitsmnUserID,kaigiID,list_hashTag,list_kaigikibujikn,updUserID,delflg):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_shitsmnInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2)クエリとパラメータを定義
        #T100
        list_args_T100 = []
        sql_T100 = "update t100_shitsmn \
                    set "
        if not C050_StringUtil.isNullCharacter(shitsmnTitle):
            sql_T100 = sql_T100 + "SHITSMN_TITLE = %s, "
            list_args_T100.append(shitsmnTitle)
        if not C050_StringUtil.isNullCharacter(shitsmnNaiyo):
            sql_T100 = sql_T100 + "SHITSMN_NAIYO = %s, "
            list_args_T100.append(shitsmnNaiyo)
        if not C050_StringUtil.isNullCharacter(shitsmnUserID):
            sql_T100 = sql_T100 + "SHITSMN_USERID = %s, "
            list_args_T100.append(shitsmnUserID)
        if not C050_StringUtil.isNullCharacter(kaigiID):
            sql_T100 = sql_T100 + "KAIGIID = %s, "
            list_args_T100.append(kaigiID)
        #if not C050_StringUtil.isNullCharacter(delflg):
        #    sql_T100 = sql_T100 + "DELFLG = %s,"
        sql_T100 = sql_T100 + "UPDSRV = %s, "
        list_args_T100.append(SERVICE_ID)
        sql_T100 = sql_T100 + "UPDUSR = %s, "
        list_args_T100.append(updUserID)
        sql_T100 = sql_T100 + "UPDDATE = current_timestamp(6) "
        sql_T100 = sql_T100 + "where SHITSMN_ID = %s "
        list_args_T100.append(shitsmnID)
        sql_T100 = sql_T100 + ";"
        args_T100 = tuple(list_args_T100)
        
        #T101(全削除全登録の、DELINによる洗い替え)
        #削除用クエリとパラメータを定義
        sql_T101_del = "delete from T101_SHITSMNHASHTAG where SHITSMN_ID = %s ;"
        args_T101_del = (shitsmnID,)
        #登録用クエリとパラメータを定義
        sql_T101_ins = "INSERT INTO T101_SHITSMNHASHTAG VALUES (%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        list_args_T101_ins = []
        for str_hashTag in list_hashTag:
            args_T101 = (shitsmnID, str_hashTag,SERVICE_ID, updUserID, SERVICE_ID, updUserID, "0",)
            list_args_T101_ins.append(args_T101)
        
        #T102(全削除全登録の、DELINによる洗い替え)
        #削除用クエリとパラメータを定義
        sql_T102_del = "delete from T102_KAIGIKBUJKN where SHITSMN_ID = %s ;"
        args_T102_del = (shitsmnID,)
        #登録用クエリとパラメータを定義
        sql_T102_ins = "INSERT INTO T102_KAIGIKBUJKN VALUES (%s,%s,%s,%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        list_args_T102_ins = []
        seq_T102 = 0
        for json_kaigikibujiknInfo in list_kaigikibujikn :
            seq_T102 += 1
            kaishNchj = json_kaigikibujiknInfo["KAISHNCHJ"]
            ShuryNchj = json_kaigikibujiknInfo["SHURYNCHJ"]
            kaigiJikn = json_kaigikibujiknInfo["KAIGIJIKN"]
            args_T102_ins = (shitsmnID,seq_T102,kaishNchj,ShuryNchj,kaigiJikn,SERVICE_ID, updUserID, SERVICE_ID, updUserID, "0",)
            list_args_T102_ins.append(args_T102_ins)
        
        #クエリを実行し、結果を取得
        #T100
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T100, args_T100)
        #T101 (ちょっと無駄な処理。非機能の改善可能。)
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T101_del, args_T101_del)
        for args_T101_ins in list_args_T101_ins:
            C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T101_ins, args_T101_ins)
        #T102
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T102_del, args_T102_del)
        for args_T102_ins in list_args_T102_ins:
            C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T102_ins, args_T102_ins)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo, errflg)
        #--------------------------------------------------------------------------------------------

        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "str_shitsmnID":shitsmnID}
        return json_service
    #==例外処理==========================================================================================
    except C020_DBUtil.MySQLDBException as e :
        #エラーフラグを立てる
        errflg = "1"
        #DB接続終了（ロールバック）
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        raise
    except Exception as e :
        raise
    #====================================================================================================