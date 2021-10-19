"""
サービスクラス
S120_KaitRQSakj

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C010_Const,C020_DBUtil,C030_MessageUtil,C050_StringUtil

SERVICE_ID = "S120"

def main(userID,shitsmnID,int_seq,int_rqSeq):
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
        #list_args = []
        sql =   "update T120_KAITREQUEST \
                    set DELFLG = %s , \
                        UPDSRV = %s , \
                        UPDUSR = %s , \
                        UPDDATE = current_timestamp(6) \
                    where SHITSMN_ID = %s \
                        and SEQ = %s \
                        and RQSEQ = %s \
                ;"
        args = ("1",SERVICE_ID,userID,shitsmnID,int_seq,int_rqSeq,)
        #クエリを実行し、結果を取得
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
