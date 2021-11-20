"""
サービスクラス
S250_UpdateKaigi

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const, C020_DBUtil, C030_MessageUtil, C050_StringUtil

SERVICE_ID = "S250"


def main(kaigiID, kaigiPath, shitsmnUserID, kaitUserID, shitsmnID, seq, strDateTime, endDateTime, kaigiTime, loginUserID):
    # --戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    #json_Info = {}
    # ------------------------------------------------------------------------------------------------
    try:
        # --DB連携基本コード----------------------------------------------------------------------------
        # DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        # --(2)クエリとパラメータを定義
        list_args = []
        sql = "update T130_KAIGI set "
        if not C050_StringUtil.isNull(kaigiPath):
            sql = sql + "KAIGI_PATH = %s , "
            list_args.append(kaigiPath)
        if not C050_StringUtil.isNull(shitsmnUserID):
            sql = sql + "SHITSMN_USERID = %s , "
            list_args.append(shitsmnUserID)
        if not C050_StringUtil.isNull(kaitUserID):
            sql = sql + "KAIT_USERID = %s , "
            list_args.append(kaitUserID)
        if not C050_StringUtil.isNull(shitsmnID):
            sql = sql + "SHITSMN_ID = %s , "
            list_args.append(shitsmnID)
        if not C050_StringUtil.isNull(seq):
            sql = sql + "SEQ = %s , "
            list_args.append(seq)
        if not C050_StringUtil.isNull(strDateTime):
            sql = sql + "STR_DATETIME = %s , "
            list_args.append(strDateTime)
        if not C050_StringUtil.isNull(endDateTime):
            sql = sql + "END_DATETIME = %s , "
            list_args.append(endDateTime)
        if not C050_StringUtil.isNull(kaigiTime):
            sql = sql + "KAIGITIME = %s , "
            list_args.append(kaigiTime)

        sql = sql + "UPDSRV = %s , "
        list_args.append(SERVICE_ID)
        sql = sql + "UPDUSR = %s , "
        list_args.append(loginUserID)
        sql = sql + "UPDDATE = current_timestamp(6)  "
        sql = sql + "where KAIGI_ID = %s ;"
        list_args.append(kaigiID)

        args = tuple(list_args)
        # クエリを実行し、結果を取得
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql, args)
        # DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo, errflg)
        # --------------------------------------------------------------------------------------------
        # メッセージがある場合はリストに追加
        # --------------------------------------------------
        msgID_01 = "S0002"
        tuple_msgPalams_01 = ("会議情報の更新",)
        msgInfo_01 = C030_MessageUtil.getMessageInfo(
            msgID_01, tuple_msgPalams_01)
        list_msgInfo.append(msgInfo_01)
        # --------------------------------------------------
        # 戻り値の共通項目を作成
        json_CommonInfo = {"errflg": errflg, "list_msgInfo": list_msgInfo}
        # 戻り値を作成
        json_service = {
            "json_CommonInfo": json_CommonInfo, "kaigiID": kaigiID}
        return json_service
    # ==例外処理==========================================================================================
    except C020_DBUtil.MySQLDBException as e:
        # エラーフラグを立てる
        errflg = "1"
        # DB接続終了（ロールバック）
        C020_DBUtil.closeDB(json_DBConnectInfo, errflg)
        raise
    except Exception as e:
        raise
    # ====================================================================================================
