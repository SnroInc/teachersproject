"""
サービスクラス
S185_UserInfoShutk_SysLogin

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil

SERVICE_ID = "S186"

def main(loginID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    try:
        #チェック処理
        json_checkInfo = check(list_msgInfo,loginID)
        errflg = json_checkInfo["errflg"]
        list_msgInfo = json_checkInfo["list_msgInfo"]
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo}
        return json_service
    #==例外処理==========================================================================================
    except Exception as e :
        raise
    #====================================================================================================

def check(list_msgInfo,loginID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    #------------------------------------------------------------------------------------------------
    try:
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #------------------------------------------------------------------------------------------

        #(1)ユーザID件数チェック----------------------------------------------------------------------
        #クエリを定義
        #削除フラグ見ずにチェック
        sql = "select count(USERID) as COUNTER from M050_USER where LOGINID = %s ;"
        #パラメータを定義
        args = (loginID,)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #取得件数が0件の場合はチェックNG
        userCounter = rows[0]["COUNTER"]
        if userCounter > 0 :
            errflg = "1"
            #「このユーザIDは使えません」
            msgID = "E0004"
            tuple_msgPalams = ("ログインID",)
            json_msgInfo = C030_MessageUtil.getMessageInfo(msgID,tuple_msgPalams)
            list_msgInfo.append(json_msgInfo) 
        print("S186:",list_msgInfo)

        #--------------------------------------------------------------------------------------------
        #--------------------------------------------------------------------------------------------
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        json_checkInfo = {
                    "errflg":errflg,
                    "list_msgInfo":list_msgInfo
                }
        return json_checkInfo
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