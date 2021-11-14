"""
サービスクラス
S280_GetKaigiPath

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil, C030_MessageUtil

SERVICE_ID = "S280"


def main():
    # --戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    kaigiPath = ""
    # ------------------------------------------------------------------------------------------------
    try:
        # AIP接続して会議のパスを取得する

        # 取得に失敗した場合はエラー

        if False:
            # 失敗時の処理を記載
            errflg = "1"
            msgID = "E0006"
            tuple_msgPalams = ("会議の作成に",)
            json_msgInfo = C030_MessageUtil.getMessageInfo(
                msgID, tuple_msgPalams)
            list_msgInfo.append(json_msgInfo)
        else:
            # 成功時の処理を記載
            kaigiPath = ""

        # 戻り値の共通項目を作成
        json_CommonInfo = {"errflg": errflg, "list_msgInfo": list_msgInfo}
        # 戻り値を作成
        json_service = {"json_CommonInfo": json_CommonInfo,
                        "kaigiPath": kaigiPath}
        return json_service
    # ==例外処理==========================================================================================
    except C020_DBUtil.MySQLDBException as e:
        # エラーフラグを立てる
        errflg = "1"
        raise
    except Exception as e:
        raise
    # ====================================================================================================
