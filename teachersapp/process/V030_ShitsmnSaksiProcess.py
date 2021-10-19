"""
ビュークラス
V030_ShitsmnSaksiProcess
質問作成ページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

import datetime
from django.urls import reverse
from . import S999_SampleService
from . import (C010_Const,C030_MessageUtil,
                S020_ShitsmnInfoTork
)

def main(request):
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
            #サービスの引数をリクエストから取得する
            shitsmnTitle = request.POST['shitsmnTitle']
            shitsmnNaiyo = request.POST['shitsmnNaiyo']
            hashTags = request.POST['hashTags']
            list_hashTag = hashTags.replace(" ","").split("#")
            #--S020-------------------------------------------------------------------------
            #サービス呼び出し
            #shitsmnTitle = "菊花賞の勝ち馬を教えてください"
            #shitsmnNaiyo = "3000mの3歳馬なので分かりません。"
            shitsmnUserID = "SYSTEM000000000000"
            #list_hashTag = ["菊花賞","福永祐一"]
            list_kaigikibujikn = [{"KAISHNCHJ":datetime.datetime.now(),"SHURYNCHJ":datetime.datetime.now(),"KAIGIJIKN":30},
                                    {"KAISHNCHJ":datetime.datetime.now(),"SHURYNCHJ":datetime.datetime.now(),"KAIGIJIKN":30},
                                    {"KAISHNCHJ":datetime.datetime.now(),"SHURYNCHJ":datetime.datetime.now(),"KAIGIJIKN":30}
                                ]
            json_S020 = S020_ShitsmnInfoTork.main(shitsmnTitle,shitsmnNaiyo,shitsmnUserID,list_hashTag,list_kaigikibujikn)
            #個々の値を取得
            flg_S020 = json_S020["json_CommonInfo"]["errflg"]
            list_msgInfo_S020 = json_S020["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S020 = json_S020["str_shitsmnID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S020)
            #検証用
            #json_shitsmnInfo_S050_S020Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S020)["json_shitsmnInfo"]
            #-------------------------------------------------------------------------------
            flg_return = "1"
            path_name = 'teachersapp:topPage'
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
            """
            #サービスを利用する場合は呼び出す
            #--S060-------------------------------------------------------------------------
            #サービス呼び出し
            json_S060 = S060_ShitsmnListShutk_Shinchk.main()
            #個々の値を取得
            flg_S060 = json_S060["json_CommonInfo"]["errflg"]
            list_msgInfo_S060 = json_S060["json_CommonInfo"]["list_msgInfo"]
            list_T100_shitsmnList_shinchk_S060 = json_S060["list_T100_shitsmnList_shinchk"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S060)
            #-------------------------------------------------------------------------------
            """
            #戻り値にセット
            flg_return = "0"
            template = 'teachersapp/T030_ShitsmnSaksi.html'
            context = {**context,**{
                                    #"list_shitsmnList_shinchk":list_T100_shitsmnList_shinchk_S060,
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

