"""
サービスクラス
S160_UserInfoKoshn

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil,C050_StringUtil
from . import S905_SaibnMstShtk

SERVICE_ID = "S160"

def main(userID,userName,mailAddress,loginID,loginPass,hyoka,userComment):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    #json_Info = {}
    #------------------------------------------------------------------------------------------------
    try:
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2)クエリとパラメータを定義
        list_args = []
        sql = "update M050_USER set "
        if not C050_StringUtil.isNullCharacter(userName):
            sql = sql + "USERNAME = %s , "
            list_args.append(userName)
        if not C050_StringUtil.isNullCharacter(mailAddress):
            sql = sql + "MAIL_ADDRESS = %s , "
            list_args.append(mailAddress)
        if not C050_StringUtil.isNullCharacter(loginID):
            sql = sql + "LOGINID = %s , "
            list_args.append(loginID)
        if not C050_StringUtil.isNullCharacter(loginPass):
            sql = sql + "LOGINPASS = %s , "
            list_args.append(loginPass)
        if not C050_StringUtil.isNullCharacter(hyoka):
            sql = sql + "HYOKA = %s , "
            list_args.append(hyoka)
        if not C050_StringUtil.isNullCharacter(userComment):
            sql = sql + "USERCOMMENT = %s , "
            list_args.append(userComment)

        sql = sql + "UPDSRV = %s , "
        list_args.append(SERVICE_ID)
        sql = sql + "UPDUSR = %s , "
        list_args.append(userID)
        sql = sql + "UPDDATE = current_timestamp(6)  "
        sql = sql + "where USERID = %s ;"
        list_args.append(userID)

        args = tuple(list_args)
        #クエリを実行し、結果を取得
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はリストに追加
        
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo,"str_userID":userID}
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
