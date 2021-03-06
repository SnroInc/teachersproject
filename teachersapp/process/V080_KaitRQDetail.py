"""
ビュークラス
V080_KaitRQDetail
質問作成ページ用View
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)
flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

import datetime
from django.urls import reverse
from . import (C010_Const,C030_MessageUtil,
                S006_GetKeibaNews,
                S130_KaitRQShutk,
)

def main(request,shitsmnID,int_seq,int_rqSeq):
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
            """
            errflg = "0"
            #更新ボタンの場合
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            #サービスのパラメータをリクエストから取得する--------------------------------------
            userID = "U20211018000000012"
            userName = request.POST['userName']
            mailAddress = request.POST['mailAddress']
            loginID = request.POST['loginID']
            loginPass = request.POST['loginPass']
            loginPass_conf = request.POST['loginPass_conf']
            hyoka = 0
            userComment = "よろしくお願いします。"
            #loginKbn =  "0"
            #サービスのパラメータをリクエストから取得する--------------------------------------
            #--S150-------------------------------------------------------------------------
            json_S160 = S160_UserInfoKoshn.main(userID,userName,mailAddress,loginID,loginPass,hyoka,userComment)
            #個々の値を取得
            flg_S160 = json_S160["json_CommonInfo"]["errflg"]
            list_msgInfo_S160 = json_S160["json_CommonInfo"]["list_msgInfo"]
            str_userID_S160 = json_S160["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S160)
            #-------------------------------------------------------------------------------
            """
            flg_return = "1"
            path_name = C010_Const.APP_NAME_DEFAULT + ':topPage'
        else:
            #POST以外の場合
            """
            POST以外時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、render
            """
            #サービスのパラメータをリクエストから取得する--------------------------------------
            #マイページを表示する場合
            userID = request.session['userID']
            #相手のプロフィールを表示する場合
            #未実装
            #サービスのパラメータをリクエストから取得する--------------------------------------
            #--S130-------------------------------------------------------------------------
            #サービス呼び出し
            json_S130 = S130_KaitRQShutk.main(shitsmnID,int_seq,int_rqSeq)
            #個々の値を取得
            flg_S130 = json_S130["json_CommonInfo"]["errflg"]
            list_msgInfo_S130 = json_S130["json_CommonInfo"]["list_msgInfo"]
            json_kaitRQInfo_S130 = json_S130["json_kaitRQInfo"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S130)
            #-------------------------------------------------------------------------------

            
            #戻り値にセット
            flg_return = "0"
            template = C010_Const.APP_NAME_DEFAULT + '/T080_KaitRQDetail.html'
            json_keibaInfo = S006_GetKeibaNews.main(10)
            context = {**context,**{
                                    "json_kaitRQInfo_S130":json_kaitRQInfo_S130,
                                    "json_keibaInfo":json_keibaInfo,
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

