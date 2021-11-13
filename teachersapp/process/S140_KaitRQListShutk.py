"""
サービスクラス
S140_KaitRQListShutk

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil, C030_MessageUtil, C070_IntegerUtil

SERVICE_ID = "S140"

"""
うまくいかない
def main(shitsmnID):
    json_service = main(shitsmnID, None)
    return json_service
"""


def main(shitsmnID, int_seq):
    # --戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    rows = ()
    # ------------------------------------------------------------------------------------------------
    try:
        # --DB連携基本コード----------------------------------------------------------------------------
        # DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        # クエリを定義
        list_args = []
        sql = "select  SHITSMN_ID, SEQ, RQSEQ, KAIT_USERID, KAIT_USERCOMMENT, RQYUKJKN, RQYUKKGN, MATCHINGFLG, CRTUSR, CRTDATE, UPDUSR,UPDDATE from T120_KAITREQUEST where SHITSMN_ID = %s "
        list_args.append(shitsmnID)
        if not C070_IntegerUtil.isNull(int_seq):
            sql = sql + "and SEQ = %s "
            list_args.append(int_seq)
        sql = sql + "and DELFLG = %s ORDER BY SEQ;"
        list_args.append("0")
        # パラメータを定義
        args = tuple(list_args)
        # クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo, sql, args)
        # DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo, errflg)
        # --------------------------------------------------------------------------------------------
        # 0取得件数が0件の場合はエラー

        if len(rows) == 0:
            errflg = "1"
            msgID = "E0002"
            tuple_msgPalams = ("回答リクエスト",)
            json_msgInfo = C030_MessageUtil.getMessageInfo(
                msgID, tuple_msgPalams)
            list_msgInfo.append(json_msgInfo)

        # 戻り値の共通項目を作成
        json_CommonInfo = {"errflg": errflg, "list_msgInfo": list_msgInfo}
        # 戻り値を作成
        json_service = {"json_CommonInfo": json_CommonInfo,
                        "tuple_kaitRQList": rows}
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
