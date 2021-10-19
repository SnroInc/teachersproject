"""
サービスクラス
S100_KaitRQTork

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil

SERVICE_ID = "S100"

def main(shitsmnID,int_seq,kaitUserID,kaitUserComment,rqYukJikn,rqYukKign):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    json_shitsmnInfo = {}
    #------------------------------------------------------------------------------------------------
    try:
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(1)採番処理-----------------------------------------------------------------------------
        sql_rqSeq = "select IFNULL(MAX(RQSEQ),0) + 1 as NEWRQSEQ from T120_KAITREQUEST where SHITSMN_ID = %s and SEQ = %s ;"
        args_rqSeq = (shitsmnID,int_seq,)
        int_rqSeq = C020_DBUtil.executeSQL(json_DBConnectInfo,sql_rqSeq,args_rqSeq)[0]["NEWRQSEQ"]
        #--採番処理呼び出し----------------------------------------------------------------------------
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        #json_DBConnectInfo = C020_DBUtil.connectDB()
        #--(2)クエリとパラメータを定義
        sql = "INSERT INTO T120_KAITREQUEST VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,current_timestamp(6),%s,%s,current_timestamp(6),%s);"
        args = (shitsmnID,int_seq,int_rqSeq,kaitUserID,kaitUserComment,rqYukJikn,rqYukKign,SERVICE_ID,kaitUserID,SERVICE_ID,kaitUserID,"0")
        #クエリを実行し、結果を取得
        #T100
        C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はリストに追加

        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "shitsmnID":shitsmnID, "int_seq":int_seq, "int_rqSeq":int_rqSeq}
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
