"""
サービスクラス
S240_CreateKaigi

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const, C020_DBUtil, C030_MessageUtil
from . import S905_SaibnMstShtk

SERVICE_ID = "S240"


def main(kaigiPath, shitsmnUserID, kaitUserID, shitsmnID, seq, strDateTime, endDateTime, kaigiTime, loginUserID):
    # --戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_service = {}
    # ------------------------------------------------------------------------------------------------
    try:
        # --(1)採番処理呼び出し-----------------------------------------------------------------------------
        tableID_S120 = C010_Const.S120["tableID"]
        header_S120 = C010_Const.S120["header"]
        newID_S120 = S905_SaibnMstShtk.main(tableID_S120, header_S120)["newID"]
        # --採番処理呼び出し----------------------------------------------------------------------------
        # --DB連携基本コード----------------------------------------------------------------------------
        # DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        # --(2)クエリとパラメータを定義
        # T100
        sql_T100 = "INSERT INTO T130_KAIGI VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,\
            %s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        args_T100 = (newID_S120, kaigiPath, shitsmnUserID, kaitUserID, shitsmnID, seq, strDateTime,
                     endDateTime, kaigiTime, SERVICE_ID, loginUserID, SERVICE_ID, loginUserID, "0",)

        # クエリを実行し、結果を取得
        # T100
        C020_DBUtil.executeSQL(json_DBConnectInfo, sql_T100, args_T100)

        # DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo, errflg)
        # --------------------------------------------------------------------------------------------

        # メッセージを格納--------------------------------------------------------------
        msgID = "S0002"
        tuple_msgPalams = ("会議の作成",)
        json_msgInfo = C030_MessageUtil.getMessageInfo(
            msgID, tuple_msgPalams)
        list_msgInfo.append(json_msgInfo)
        # メッセージを格納--------------------------------------------------------------

        # 戻り値の共通項目を作成
        json_CommonInfo = {"errflg": errflg, "list_msgInfo": list_msgInfo}
        # 戻り値を作成
        json_service = {"json_CommonInfo": json_CommonInfo,
                        "str_kaigiID": newID_S120}
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
