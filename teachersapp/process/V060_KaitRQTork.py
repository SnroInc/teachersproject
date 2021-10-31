"""
ビュークラス
V060_KaitRQTork

エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

import datetime
from django.urls import reverse
from . import (C010_Const,C030_MessageUtil,
                S006_GetKeibaNews,
                S050_ShitsmnInfoShutk,
                S100_KaitRQTork,
                S130_KaitRQShutk
)

def main(request,shitsmnID):
    #--View共通----------------------------------------------
    #戻り値用の変数宣言
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    #-------------------------------------------------------
    try:
        if request.method == 'POST':
            #POSTの場合
            """
            POST時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、redirect
            """
            errflg = "0"
            list_seq = request.POST.getlist["kibuJiknInfo"]
            kaitUserComment = request.POST['kaitUserComment']
            kaitUserID = request.session['userID']

            for int_seq in list_seq:
                #--S100-------------------------------------------------------------------------
                #サービス呼び出し
                #shitsmnID = "XXXXXXXXXXXXXXX"
                #int_seq = 1
                #kaitUserID = "SYSTEM000000000000"
                #kaitUserComment = "マカヒキが来ました" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                rqYukJikn = 72
                str_rqYukKign = '3000-12-31 00:00:00'
                datetime_rqYukKign = datetime.strptime(str_rqYukKign, '%Y-%m-%d %H:%M:%S')
                json_S100 = S100_KaitRQTork.main(shitsmnID,int_seq,kaitUserID,kaitUserComment,rqYukJikn,datetime_rqYukKign)
                #個々の値を取得
                #flg_S100 = json_S100["json_CommonInfo"]["errflg"]
                list_msgInfo_S100 = json_S100["json_CommonInfo"]["list_msgInfo"]
                #str_shitsmnID_S100 = json_S100["shitsmnID"]
                #int_seq_S100 = json_S100["int_seq"]
                #int_rqSeq_S100 = json_S100["int_rqSeq"]
                #メッセージ格納
                C030_MessageUtil.setMessageList(request,list_msgInfo_S100)
                #検証用
                #json_kaitRQInfo_S130_S100Kensho = S130_KaitRQShutk.main(str_shitsmnID_S100,int_seq_S100,int_rqSeq_S100)["json_kaitRQInfo"]
                #-------------------------------------------------------------------------------
            flg_return = "1"
            #path_name = "'teachersapp:shitsmnDetail' shitsmnID"
            path_name = 'teachersapp:topPage'

        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
            #--S050-------------------------------------------------------------------------
            #サービス呼び出し
            #shitsmnID = "Q20211029000000001"
            json_S050 = S050_ShitsmnInfoShutk.main(shitsmnID)
            #個々の値を取得
            flg_S050 = json_S050["json_CommonInfo"]["errflg"]
            list_msgInfo_S050 = json_S050["json_CommonInfo"]["list_msgInfo"]
            json_shitsmnInfo_S050 = json_S050["json_shitsmnInfo"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S050)
            #-------------------------------------------------------------------------------
            #戻り値にセット
            flg_return = "0"
            template = 'teachersapp/T060_KaitRQTork.html'
            json_keibaInfo = S006_GetKeibaNews.main(10)
            context = {**context,**{
                                    "json_keibaInfo":json_keibaInfo,
                                    "shitsmnInfo":json_shitsmnInfo_S050
                                    }
                    }
        
        #戻り値用のjsonを作成
        json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
        return json_view
    #==例外処理==========================================================================================
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        raise
    #====================================================================================================

