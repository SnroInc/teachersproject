"""
サービスクラス
S070_SHITSMNLISTSHTK_SHINCHK

質問を条件で検索するサービス

引数：  keyword         ：文字列。画面.キーワード
        list_hashTag    ：リスト[文字列]。画面.ハッシュタグを「#」区切りにしたリスト。
        date_From       ：日付型。画面.年月日時分（FROM）
        date_TO         ：日付型。画面.年月日時分（
        flg_selfQ       ："0"or"1"
        flg_selfRQ      ："0"or"1"

戻り値：{共通項目、任意項目1、任意項目2、...}
        └共通項目：{実行結果（エラーフラグ）、メッセージリスト}

"""

from . import C020_DBUtil,C030_MessageUtil,C050_StringUtil,C060_ListUtil

SERVICE_ID = "S070"

def main(keyWord,list_hashTag,date_From,date_To,selfQ_userID, selfRQ_userID):
    #--戻り値用の変数宣言------------------------------------------------------------------------------
    errflg = "0"
    list_msgInfo = []
    rows = ()
    #------------------------------------------------------------------------------------------------
    try:
        #パラメータ取得
        #--DB連携基本コード----------------------------------------------------------------------------
        #DB接続開始、コネクションとカーソルを取得
        json_DBConnectInfo = C020_DBUtil.connectDB()
        #クエリを定義
        list_args = []
        sql = "select SHITSMN_ID,SHITSMN_TITLE,SHITSMN_NAIYO,SHITSMN_USERID,KAIGIID,CRTDATE,UPDDATE \
                from t100_shitsmn t100_main \
                where  exists \
                    (select 1 \
                        from (   \
                                select MAX(t100.SHITSMN_ID) as SHITSMN_ID \
                                    from	t100_shitsmn t100 \
                                    left outer join t101_shitsmnhashtag t101 \
                                        on   t100.SHITSMN_ID = t101.SHITSMN_ID \
                                        AND t101.DELFLG = '0' \
                                    left outer join t102_kaigikbujkn t102 \
                                        on t100.SHITSMN_ID = t102.SHITSMN_ID \
                                        AND t102.DELFLG = '0' \
                                    left outer join t120_kaitrequest t120 \
                                        on t102.SHITSMN_ID = t120.SHITSMN_ID \
                                        AND t102.SEQ = t120.SEQ \
                                        AND t120.DELFLG = '0' \
                                    where t100.DELFLG = '0' "
        if not C050_StringUtil.isNullCharacter(keyWord):
            sql = sql + "               AND ((t100.SHITSMN_TITLE like %s) or (t100.SHITSMN_NAIYO like %s))"
            keyWord = "%" + keyWord + "%"
            list_args.append(keyWord)
            list_args.append(keyWord)
        if not C050_StringUtil.isNullCharacter(selfQ_userID):        
            sql = sql + "               AND t100.SHITSMN_USERID = %s "
            list_args.append(selfQ_userID)
        if not C060_ListUtil.isZeroList(list_hashTag):   
            sql = sql + "               AND t101.HASHTAG in %s "
            list_args.append(list_hashTag)
        if not C050_StringUtil.isNullCharacter(date_From):
            sql = sql + "               AND t102.KAISHNCHJ >= %s " 
            list_args.append(date_From)
        if not C050_StringUtil.isNullCharacter(date_To):   
            sql = sql + "               AND t102.KAISHNCHJ <= %s "
            list_args.append(date_To)
        if not C050_StringUtil.isNullCharacter(selfRQ_userID):   
            sql = sql + "               AND t120.KAIT_USERID = %s " 
            list_args.append(selfRQ_userID)
            sql = sql +     "           group by t100.SHITSMN_ID \
                             ) t100_sub \
                        where t100_main.SHITSMN_ID =  t100_sub.SHITSMN_ID \
                    ) \
                ; "
        #パラメータを定義
        args = tuple(list_args)
        #クエリを実行し、結果を取得
        rows = C020_DBUtil.executeSQL(json_DBConnectInfo,sql,args)
        #DB接続終了
        C020_DBUtil.closeDB(json_DBConnectInfo,errflg)
        #--------------------------------------------------------------------------------------------
        #メッセージがある場合はメッセージリストに追加
        
        #戻り値の共通項目を作成
        json_CommonInfo = {"errflg":errflg, "list_msgInfo" : list_msgInfo}
        #戻り値を作成
        json_service = {"json_CommonInfo":json_CommonInfo, "tuple_T100_shitsmnList_jokn" : rows}
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