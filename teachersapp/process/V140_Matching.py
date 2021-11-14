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
from . import (C010_Const, C030_MessageUtil, C050_StringUtil,
               S050_ShitsmnInfoShutk,
               S130_KaitRQShutk,
               S240_CreateKaigi,
               S280_GetKaigiPath,
               S910_TableItemCounter,
               )


def main(request):
    # --View共通----------------------------------------------
    # 戻り値用の変数宣言
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    # -------------------------------------------------------
    try:
        if request.method == 'POST':
            # POSTの場合
            """
            POST時の処理を書く。
            パターンに応じてflg_returnの値を設定する。
            bottunパターンによって処理を分けたりもするかも。
            例は、redirect
            """
            errflg = "0"
            # サービスのパラメータをリクエストから取得する--------------------------------------
            shitsmnID = request.POST['shitsmnID']
            int_seq = request.POST['int_seq']
            int_rqSeq = request.POST['int_rqSeq']
            loginUserID = request.session['userID']
            # サービスのパラメータをリクエストから取得する--------------------------------------

            # ビジネスエラーじゃないから不要。DBにunique属性持たせているため、システムエラーになって回避できる
            # (画面上で、マッチング済みの場合は「この人に教えてもらう」ボタンを非表示にする前提)
            # ==チェック処理=============================================================================================
            # DBに同じロ質問IDが登録されていないかのチェック--------------------------------------------------------------------
            # json_S185 = S910_TableItemCounter.main(
            #     "T130_KAIGI", "SHITSMN_ID", shitsmnID, "0")
            # #errflg_S185 = json_S185["json_CommonInfo"]["errflg"]
            # list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            # # メッセージ格納
            # # C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            # counter_loginID = json_S185["counter"]
            # if counter_loginID > 0:
            #     errflg = "1"
            #     # 「すでに回答リクエストを受諾しています。」
            #     C030_MessageUtil.setMessage(
            #         request, "E0007", ())
            # DBに同じロ質問IDが登録されていないかのチェック--------------------------------------------------------------------
            # ==チェック処理=============================================================================================

            # --S050-------------------------------------------------------------------------
            # サービス呼び出し
            json_S050 = S050_ShitsmnInfoShutk.main(shitsmnID)
            # 個々の値を取得
            flg_S050 = json_S050["json_CommonInfo"]["errflg"]
            list_msgInfo_S050 = json_S050["json_CommonInfo"]["list_msgInfo"]
            json_shitsmnDetail = json_S050["json_shitsmnInfo"]
            # メッセージ格納
            C030_MessageUtil.setMessageList(request, list_msgInfo_S050)
            # --S050-------------------------------------------------------------------------
            # --S130-------------------------------------------------------------------------
            # サービス呼び出し
            json_S130 = S130_KaitRQShutk.main(shitsmnID, int_seq, int_rqSeq)
            # 個々の値を取得
            flg_S130 = json_S130["json_CommonInfo"]["errflg"]
            list_msgInfo_S130 = json_S130["json_CommonInfo"]["list_msgInfo"]
            json_kaitRQInfo_S130 = json_S130["json_kaitRQInfo"]
            # メッセージ格納
            C030_MessageUtil.setMessageList(request, list_msgInfo_S130)
            # -------------------------------------------------------------------------------
            # --S280-------------------------------------------------------------------------
            # 会議パスを取得する
            json_S280 = S280_GetKaigiPath.main()
            # 個々の値を取得
            #flg_S150 = json_S150["json_CommonInfo"]["errflg"]
            list_msgInfo_S280 = json_S280["json_CommonInfo"]["list_msgInfo"]
            kaigiPath = json_S280["kaigiPath"]
            # メッセージ格納
            C030_MessageUtil.setMessageList(request, list_msgInfo_S280)
            # -------------------------------------------------------------------------------
            # --S240(引数準備)----------------------------------------------------------------
            shitsmnUserID = json_shitsmnDetail['SHITSMN_USERID']
            kaitUserID = json_kaitRQInfo_S130['KAIT_USERID']
            strDateTime = None
            endDateTime = None
            kaigiTime = None
            if int_seq == 1:
                strDateTime = json_S050['KAISHNCHJ01']
                endDateTime = json_S050['SHURYNCHJ01']
                kaigiTime = json_S050['KAIGIJIKN01']
            elif int_seq == 2:
                strDateTime = json_S050['KAISHNCHJ02']
                endDateTime = json_S050['SHURYNCHJ02']
                kaigiTime = json_S050['KAIGIJIKN02']
            elif int_seq == 3:
                strDateTime = json_S050['KAISHNCHJ03']
                endDateTime = json_S050['SHURYNCHJ03']
                kaigiTime = json_S050['KAIGIJIKN03']
            # --S240-------------------------------------------------------------------------
            # サービス呼び出し
            json_S240 = S240_CreateKaigi.main(
                kaigiPath, shitsmnUserID, kaitUserID, shitsmnID, int_seq, strDateTime, endDateTime, kaigiTime, loginUserID)
            # 個々の値を取得
            #flg_S240 = json_S240["json_CommonInfo"]["errflg"]
            list_msgInfo_S240 = json_S240["json_CommonInfo"]["list_msgInfo"]
            #str_kaigiID_S240 = json_S240["str_kaigiID"]
            # メッセージ格納
            C030_MessageUtil.setMessageList(request, list_msgInfo_S240)
            # -------------------------------------------------------------------------------
            flg_return = "1"
            path_name = C010_Const.PATH_NAME_SUCCESS
        else:
            # POST以外の場合
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
            # 戻り値にセット
            flg_return = "0"
            template = C010_Const.APP_NAME_DEFAULT + '/T100_SignUp.html'
            #list_newsInfo = S006_GetKeibaNews.main(10)
            context = {**context, **{
                # "list_newsInfo":list_newsInfo,
            }
            }

        # 戻り値用のjsonを作成
        json_view = {'flg_return': flg_return, 'template': template,
                     'context': context, 'path_name': path_name}
        return json_view
    # ==例外処理==========================================================================================
    except Exception as e:
        # システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        raise
    # ====================================================================================================
