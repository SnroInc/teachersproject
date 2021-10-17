"""
サービスクラス
S060_ShitsmnListShutk_Shinchk

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil
from . import S180_HANYOMSTSHTK

SERVICE_ID = "S050"

def main():
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    rows = {}
    #------------------------------------------------------------------------------------------------
    try:
        #パラメータ取得
        #--S180-------------------------------------------------------------------------
        json_S180 = S180_HANYOMSTSHTK.main("SEC0001","01")
        flg_S180 = json_S180["json_CommonInfo"]["errflg"]
        list_msgInfo_S180 = json_S180["json_CommonInfo"]["list_msgInfo"]
        list_M101_hanyoMst_S180 = json_S180["list_M101_hanyoMst"]
        #-------------------------------------------------------------------------------
        kensu = int(list_M101_hanyoMst_S180[0]["NAIYO01"])
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        sql = "select SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID,CRTDATE,UPDDATE from t100_shitsmn order by crtdate desc limit %s ;"
        #パラメータを定義
        args = (kensu,)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はメッセージリストに追加
        msgID = "E0001"
        tuple_msgPalams = ("気づいた時には、術式を解いていた")
        json_msgInfo = C030_MessageUtil.getMessageInfo(msgID,tuple_msgPalams)
        list_msgInfo.append(json_msgInfo) 
        
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "list_T100_shitsmnList_shinchk" : rows}
        return json_service
    #==例外処理==========================================================================================
    except Exception as e :
        #エラーフラグを「2：システムエラー」にする
        errflg = "2"
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        raise
    #====================================================================================================