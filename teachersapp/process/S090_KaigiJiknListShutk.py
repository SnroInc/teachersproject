"""
サービスクラス
S090_KaigiJiknListShutk

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil, C030_MessageUtil

SERVICE_ID = "S090"


def main():
    # --戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    rows = []
    # ------------------------------------------------------------------------------------------------
    try:
        # --DB連携基本コード----------------------------------------------------------------------------
        # DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        # クエリを定義
        sql = "select KAIGJKN_CD,KAIGJKN_TIME,KAIGJKN_DISP from M110_KAIGJKN order by HYOJIJN asc ;"
        # パラメータを定義
        args = ()
        # クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo, sql, args)
        # DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo, errflg)
        # --------------------------------------------------------------------------------------------
        # メッセージがある場合はメッセージリストに追加

        # 戻り値の共通項目を作成
        json_CommonInfo = {"errflg": errflg, "list_msgInfo": list_msgInfo}
        # 戻り値を作成
        json_service = {"json_CommonInfo": json_CommonInfo,
                        "tuple_M110_kaigiJiknList": rows}
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
