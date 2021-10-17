"""
ビュークラス
V010_TopPageProcess
トップページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

from django.urls import reverse
from . import S999_SampleService
from . import (C010_Const,C030_MessageUtil,
                S180_HANYOMSTSHTK,
                S060_ShitsmnListShutk_Shinchk
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
            flg_return = "1"
            path_name = 'sample_url2'
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
            #サービスを利用する場合は呼び出す
            json_S999 = S999_SampleService.main()
            #json型から各値を取得する
            flg_S999 = json_S999["json_CommonInfo"]["errflg"]
            list_msgInfo_S999 = json_S999["json_CommonInfo"]["list_msgInfo"]
            list_shitsmnIchirn_S999 = json_S999["list_shitsmnIchirn"]
            #メッセージがある場合はセットする
            C030_MessageUtil.setMessageList(request,list_msgInfo_S999)
            #--S180-------------------------------------------------------------------------
            json_S180 = S180_HANYOMSTSHTK.main("SEC0001","01")
            flg_S180 = json_S180["json_CommonInfo"]["errflg"]
            list_msgInfo_S180 = json_S180["json_CommonInfo"]["list_msgInfo"]
            list_M101_hanyoMst_S180 = json_S180["list_M101_hanyoMst"]
            C030_MessageUtil.setMessageList(request,list_msgInfo_S180)
            #-------------------------------------------------------------------------------
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
            #戻り値にセット
            flg_return = "0"
            template = 'teachersapp/T010_TopPage.html'
            context = {**context,**{"list_shitsmnIchirn":list_shitsmnIchirn_S999,
                                    "list_shitsmnList_shinchk":list_T100_shitsmnList_shinchk_S060,
                                    "list_hanyoMst":list_M101_hanyoMst_S180,
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

