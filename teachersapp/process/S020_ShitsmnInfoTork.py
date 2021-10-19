"""
サービスクラス
S020_ShitsmnInfoTork

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil
from . import S905_SaibnMstShtk

SERVICE_ID = "S020"

def main(shitsmnTitle,shitsmnNaiyo,shitsmnUserID,list_hashTag,list_kaigikibujikn):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_shitsmnInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--(1)採番処理呼び出し-----------------------------------------------------------------------------
        tableID_S100 = C010_Const.S100["tableID"]
        header_S100 = C010_Const.S100["header"]
        newID_S100 = S905_SaibnMstShtk.main(tableID_S100,header_S100)["newID"]
        #--採番処理呼び出し----------------------------------------------------------------------------
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2)クエリとパラメータを定義
        #T100
        sql_T100 = "INSERT INTO T100_SHITSMN VALUES (%s,%s,%s,%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        args_T100 = (newID_S100,shitsmnTitle,shitsmnNaiyo,shitsmnUserID,None,SERVICE_ID,shitsmnUserID,SERVICE_ID,shitsmnUserID,"0")
        #T101
        sql_T101 = "INSERT INTO T101_SHITSMNHASHTAG VALUES (%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        list_args_T101 = []
        for str_hashTag in list_hashTag:
            args_T101 = (newID_S100, str_hashTag,SERVICE_ID, shitsmnUserID, SERVICE_ID, shitsmnUserID, "0")
            list_args_T101.append(args_T101)
        #T102
        sql_T102 = "INSERT INTO T102_KAIGIKBUJKN VALUES (%s,%s,%s,%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        list_args_T102 = []
        seq_T102 = 0
        for json_kaigikibujiknInfo in list_kaigikibujikn :
            seq_T102 += 1
            kaishNchj = json_kaigikibujiknInfo["KAISHNCHJ"]
            ShuryNchj = json_kaigikibujiknInfo["SHURYNCHJ"]
            kaigiJikn = json_kaigikibujiknInfo["KAIGIJIKN"]
            args_T102 = (newID_S100,seq_T102,kaishNchj,ShuryNchj,kaigiJikn,SERVICE_ID, shitsmnUserID, SERVICE_ID, shitsmnUserID, "0")
            list_args_T102.append(args_T102)
        #クエリを実行し、結果を取得
        #T100
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql_T100,args_T100)
        #T101 (ちょっと無駄な処理。非機能の改善可能。)
        for args_T101 in list_args_T101:
            C020_DBUtil.executeSQL(json_DBConnectInfo,sql_T101,args_T101)
        #T102
        for args_T102 in list_args_T102:
            C020_DBUtil.executeSQL(json_DBConnectInfo,sql_T102,args_T102)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------

        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo,"str_shitsmnID":newID_S100}
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