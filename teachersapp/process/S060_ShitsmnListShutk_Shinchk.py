"""
サービスクラス
S060_SHITSMNLISTSHTK_SHINCHK

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil
from . import S900_HanyoMstShutk

SERVICE_ID = "S060"

def main():
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    rows = ()
    #------------------------------------------------------------------------------------------------
    try:
        #パラメータ取得
        #--S180-------------------------------------------------------------------------
        json_S900 = S900_HanyoMstShutk.main("SEC0001","01")
        flg_S900 = json_S900["json_CommonInfo"]["errflg"]
        list_msgInfo_S900 = json_S900["json_CommonInfo"]["list_msgInfo"]
        tuple_M101_hanyoMst_S900 = json_S900["tuple_M101_hanyoMst"]
        #-------------------------------------------------------------------------------
        kensu = int(tuple_M101_hanyoMst_S900[0]["NAIYO01"])
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        sql = "select SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID,CRTDATE,UPDDATE from t100_shitsmn where DELFLG = '0' order by crtdate desc limit %s ;"
        #パラメータを定義
        args = (kensu,)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はメッセージリストに追加

        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "tuple_T100_shitsmnList_shinchk" : rows}
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