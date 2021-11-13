"""
サービスクラス
S040_ShitsmnInfoSakj

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil,C050_StringUtil

SERVICE_ID = "S040"

def main(shitsmnID,updUserID):
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
        sql_T100 = "update T100_SHITSMN \
                        set \
                            DELFLG = %s, \
                            UPDSRV = %s, \
                            UPDUSR = %s, \
                            UPDDATE = current_timestamp(6) \
                        where SHITSMN_ID = %s \
                    ;"
        args_T100 = ("1",SERVICE_ID,updUserID,shitsmnID)

        #T101
        #削除用クエリとパラメータを定義
        sql_T101 = "update T101_SHITSMNHASHTAG \
                        set DELFLG = %s, \
                            UPDSRV = %s, \
                            UPDUSR = %s, \
                            UPDDATE = current_timestamp(6) \
                        where SHITSMN_ID = %s \
                    ;"
        args_T101 = ("1",SERVICE_ID,updUserID,shitsmnID)
        
        #T102
        #削除用クエリとパラメータを定義
        sql_T102 = "update T102_KAIGIKBUJKN \
                        set DELFLG = %s, \
                            UPDSRV = %s, \
                            UPDUSR = %s, \
                            UPDDATE = current_timestamp(6) \
                        where SHITSMN_ID = %s \
                    ;"
        args_T102 = ("1",SERVICE_ID,updUserID,shitsmnID)

        #クエリを実行し、結果を取得
        #T100
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T100, args_T100)
        #T101 (ちょっと無駄な処理。非機能の改善可能。)
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T101, args_T101)
        #T102
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T102, args_T102)

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