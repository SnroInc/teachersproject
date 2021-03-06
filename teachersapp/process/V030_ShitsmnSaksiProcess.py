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
from . import (C010_Const, C030_MessageUtil, C050_StringUtil, C070_IntegerUtil, C080_DateUtil,
               S006_GetKeibaNews,
               S020_ShitsmnInfoTork
               )


def main(request):
    # --View共通----------------------------------------------
    # 戻り値用の変数宣言
    flg_return = ""
    template = ''
    context = {}
    path_name = ''
    path_param = ()
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
            # サービスの引数をリクエストから取得する
            shitsmnTitle = request.POST['shitsmnTitle']
            shitsmnNaiyo = request.POST['shitsmnNaiyo']
            hashTags = request.POST['hashTags']
            list_hashTag = hashTags.replace(" ", "").split("#")
            #shitsmnTitle = "菊花賞の勝ち馬を教えてください"
            #shitsmnNaiyo = "3000mの3歳馬なので分かりません。"
            shitsmnUserID = request.session['userID']
            #list_hashTag = ["菊花賞","福永祐一"]
            # 会議終了時間計算

            sTime1 = request.POST['sTime1']
            # 多分直書きしているからstr型だけど、dbから取得するようにすればint型になる
            minutes1 = int(request.POST['duration1'])
            sTime2 = request.POST['sTime2']
            minutes2 = int(request.POST['duration2'])
            sTime3 = request.POST['sTime3']
            minutes3 = int(request.POST['duration3'])
            eTime1 = None
            eTime2 = None
            eTime3 = None
            if(not C050_StringUtil.isEmpty(sTime1)) and (not C070_IntegerUtil.isNull(minutes1)):
                eTime1 = datetime.datetime.strptime(
                    sTime1, '%Y-%m-%dT%H:%M') + datetime.timedelta(minutes=minutes1)
            else:
                sTime1 = None
            if(not C050_StringUtil.isEmpty(sTime2)) and (not C070_IntegerUtil.isNull(minutes2)):
                eTime2 = datetime.datetime.strptime(
                    sTime2, '%Y-%m-%dT%H:%M') + datetime.timedelta(minutes=minutes2)
            else:
                sTime2 = None
            if(not C050_StringUtil.isEmpty(sTime3)) and (not C070_IntegerUtil.isNull(minutes3)):
                eTime3 = datetime.datetime.strptime(
                    sTime3, '%Y-%m-%dT%H:%M') + datetime.timedelta(minutes=minutes3)
            else:
                sTime3 = None

            # ==チェック処理======================================================================
            # 質問タイトルチェック
            if C050_StringUtil.isAllSpace(shitsmnTitle):
                # ここに業務エラー処理を書く
                errflg = "1"
                # 「第一希望の必須チェック」
                C030_MessageUtil.setMessage(
                    request, "E0001", ("質問タイトル",))
            # 会議希望時間（第一希望）チェック
            if C050_StringUtil.isEmpty(sTime1) or C070_IntegerUtil.isNull(minutes1):
                # ここに業務エラー処理を書く
                errflg = "1"
                # 「第一希望の必須チェック」
                C030_MessageUtil.setMessage(
                    request, "E0001", ("会議時間 第一希望",))

            # -------------------------------------------------------------------------------
            # チェックNGの場合、処理を終了して再描画
            if errflg == "1":
                flg_return = "0"
                template = C010_Const.APP_NAME_DEFAULT + '/T030_ShitsmnSaksi.html'
                context = {**context, **{
                    "shitsmnTitle": shitsmnTitle,
                    "hashTags": hashTags,
                    "shitsmnNaiyo": shitsmnNaiyo,
                    "sTime1": sTime1,
                    "sTime2": sTime2,
                    "sTime3": sTime3,
                    "duration1": minutes1,
                    "duration2": minutes2,
                    "duration3": minutes3,
                }
                }
                # 戻り値用のjsonを作成
                json_view = {'flg_return': flg_return, 'template': template,
                             'context': context, 'path_name': path_name, 'path_param': path_param}
                return json_view
            # ==チェック処理======================================================================

            # --S020-------------------------------------------------------------------------
            # サービス呼び出し
            json_S020 = S020_ShitsmnInfoTork.main(
                shitsmnTitle, shitsmnNaiyo, shitsmnUserID, list_hashTag, sTime1, eTime1, minutes1, sTime2, eTime2, minutes2, sTime3, eTime3, minutes3, None)
            # 個々の値を取得
            flg_S020 = json_S020["json_CommonInfo"]["errflg"]
            list_msgInfo_S020 = json_S020["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S020 = json_S020["str_shitsmnID"]
            # メッセージ格納
            C030_MessageUtil.setMessageList(request, list_msgInfo_S020)
            # 検証用
            #json_shitsmnInfo_S050_S020Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S020)["json_shitsmnInfo"]
            # -------------------------------------------------------------------------------
            flg_return = "1"
            path_name = C010_Const.APP_NAME_DEFAULT + ':topPage'
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
            template = C010_Const.APP_NAME_DEFAULT + '/T030_ShitsmnSaksi.html'
            json_keibaInfo = S006_GetKeibaNews.main(10)
            context = {**context, **{
                "json_keibaInfo": json_keibaInfo,
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
