"""
ビュークラス
A999_SampleAction
エラーフラグ：0(正常終了),1(業務エラー),2(システムエラー)

flg_return：0(render),1(redirect)

flg_return==0の時、「template」「context」必須
flg_return==1の時、「path_name」必須

"""

import datetime
from django.urls import reverse
from . import S999_SampleService
from . import (C010_Const,C030_MessageUtil,
                S020_ShitsmnInfoTork,
                S030_ShitsmnInfoKoshn,
                S040_ShitsmnInfoSakj,
                S050_ShitsmnInfoShutk,
                S060_ShitsmnListShutk_Shinchk,
                S070_ShitsmnListShutk_Jokn,
                S080_HashTagSuggestShutk,
                S090_KaigiJiknListShutk,
                S095_RQYukJiknListShutk,
                S100_KaitRQTork,
                S120_KaitRQSakj,
                S130_KaitRQShutk,
                S140_KaitRQListShutk,
                S150_UserInfoTork,
                S160_UserInfoKoshn,
                S170_UserInfoSakj,
                S180_UserInfoShutk,
                S185_UserInfoShutk_SysLogin,
                S900_HanyoMstShutk,
                S905_SaibnMstShtk
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
            tuple_shitsmnIchirn_S999 = json_S999["tuple_shitsmnIchirn"]
            #メッセージがある場合はセットする
            C030_MessageUtil.setMessageList(request,list_msgInfo_S999)
            #--S020-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnTitle = "菊花賞の勝ち馬を教えてください"
            shitsmnNaiyo = "3000mの3歳馬なので分かりません。"
            shitsmnUserID = "tsunesanbk"
            list_hashTag = ["菊花賞","福永祐一"]
            list_kaigikibujikn = [{"KAISHNCHJ":"2021-10-23 13:00:00","SHURYNCHJ":"2021-10-23 13:30:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-23 18:00:00","SHURYNCHJ":"2021-10-23 18:00:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-24 13:00:00","SHURYNCHJ":"2021-10-24 13:30:00","KAIGIJIKN":30}
                                ]
            json_S020 = S020_ShitsmnInfoTork.main(shitsmnTitle,shitsmnNaiyo,shitsmnUserID,list_hashTag,list_kaigikibujikn)
            #個々の値を取得
            flg_S020 = json_S020["json_CommonInfo"]["errflg"]
            list_msgInfo_S020 = json_S020["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S020 = json_S020["str_shitsmnID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S020)
            #検証用
            json_shitsmnInfo_S050_S020Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S020)["json_shitsmnInfo"]
            #-------------------------------------------------------------------------------
            #--S030-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnID = "Q20211017000000036"
            shitsmnTitle = "マカヒキは強いですか？"
            shitsmnNaiyo = "ニエル賞の勝ち馬が弱いわけありません。"
            shitsmnUserID = ""
            kaigiID = ""
            updUserID = "tsunesanbk"
            list_hashTag = ["凱旋門賞","ニエル賞","クリストフ"]
            list_kaigikibujikn = [{"KAISHNCHJ":"2021-10-23 13:00:00","SHURYNCHJ":"2021-10-23 13:30:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-23 18:00:00","SHURYNCHJ":"2021-10-23 18:00:00","KAIGIJIKN":30},
                                    {"KAISHNCHJ":"2021-10-24 13:00:00","SHURYNCHJ":"2021-10-24 13:30:00","KAIGIJIKN":30}
                                ]
            json_S030 = S030_ShitsmnInfoKoshn.main(shitsmnID,shitsmnTitle,shitsmnNaiyo,shitsmnUserID,kaigiID,list_hashTag,list_kaigikibujikn,updUserID,"0")
            #個々の値を取得
            flg_S030 = json_S030["json_CommonInfo"]["errflg"]
            list_msgInfo_S030 = json_S030["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S030 = json_S030["str_shitsmnID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S030)
            #検証用
            json_shitsmnInfo_S050_S030Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S030)["json_shitsmnInfo"]
            #-------------------------------------------------------------------------------
            #--S040-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnID = "Q20211017000000034"
            updUserID = "tsunesanbk"
            json_S040 = S040_ShitsmnInfoSakj.main(shitsmnID,updUserID)
            #個々の値を取得
            flg_S040 = json_S040["json_CommonInfo"]["errflg"]
            list_msgInfo_S040 = json_S040["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S040 = json_S040["str_shitsmnID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S040)
            #検証用
            json_shitsmnInfo_S050_S040Kensho = S050_ShitsmnInfoShutk.main(str_shitsmnID_S040)["json_shitsmnInfo"]
            #-------------------------------------------------------------------------------
            #--S050-------------------------------------------------------------------------
            #サービス呼び出し
            json_S050 = S050_ShitsmnInfoShutk.main("Q20210920000000001")
            #個々の値を取得
            flg_S050 = json_S050["json_CommonInfo"]["errflg"]
            list_msgInfo_S050 = json_S050["json_CommonInfo"]["list_msgInfo"]
            json_shitsmnInfo_S050 = json_S050["json_shitsmnInfo"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S050)
            #-------------------------------------------------------------------------------
            #--S060-------------------------------------------------------------------------
            #サービス呼び出し
            json_S060 = S060_ShitsmnListShutk_Shinchk.main()
            #個々の値を取得
            flg_S060 = json_S060["json_CommonInfo"]["errflg"]
            list_msgInfo_S060 = json_S060["json_CommonInfo"]["list_msgInfo"]
            tuple_T100_shitsmnList_shinchk_S060 = json_S060["tuple_T100_shitsmnList_shinchk"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S060)
            #-------------------------------------------------------------------------------
            #--S070-------------------------------------------------------------------------
            #サービス呼び出し
            keyWord = "マカヒキ"
            list_hashTag = ["競馬","マカヒキ"]
            date_From = "2021-10-15 21:00:00"
            date_To = "2021-10-17 21:00:00"
            selfQ_userID = ""
            selfRQ_userID = "tsunesanBK"
            json_S070 = S070_ShitsmnListShutk_Jokn.main(keyWord,list_hashTag,date_From,date_To,selfQ_userID, selfRQ_userID)
            #個々の値を取得
            flg_S070 = json_S070["json_CommonInfo"]["errflg"]
            list_msgInfo_S070 = json_S070["json_CommonInfo"]["list_msgInfo"]
            tuple_T100_shitsmnList_jokn_S070 = json_S070["tuple_T100_shitsmnList_jokn"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S070)
            #-------------------------------------------------------------------------------
            #--S080-------------------------------------------------------------------------
            #サービス呼び出し
            keyword = "天皇賞"
            json_S080 = S080_HashTagSuggestShutk.main(keyword)
            #個々の値を取得
            flg_S080 = json_S080["json_CommonInfo"]["errflg"]
            list_msgInfo_S080 = json_S080["json_CommonInfo"]["list_msgInfo"]
            tuple_hashTag_S080 = json_S080["tuple_hashTag"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S080)
            #-------------------------------------------------------------------------------
            #--S090-------------------------------------------------------------------------
            #サービス呼び出し
            json_S090 = S090_KaigiJiknListShutk.main()
            #個々の値を取得
            flg_S090 = json_S090["json_CommonInfo"]["errflg"]
            list_msgInfo_S090 = json_S090["json_CommonInfo"]["list_msgInfo"]
            tuple_M110_kaigiJiknList_S090 = json_S090["tuple_M110_kaigiJiknList"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S090)
            #-------------------------------------------------------------------------------
            #--S095-------------------------------------------------------------------------
            #サービス呼び出し
            json_S095 = S095_RQYukJiknListShutk.main()
            #個々の値を取得
            flg_S095 = json_S095["json_CommonInfo"]["errflg"]
            list_msgInfo_S095 = json_S095["json_CommonInfo"]["list_msgInfo"]
            tuple_M111_rqYukJiknList_S095 = json_S095["tuple_M111_rqYukJiknList"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S095)
            #-------------------------------------------------------------------------------
            #--S100-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnID = "Q20210920000000001"
            int_seq = 1
            kaitUserID = "SYSTEM000000000000"
            kaitUserComment = "マカヒキが来ました" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            rqYukJikn = 12
            rqYukKign = datetime.datetime.now()
            json_S100 = S100_KaitRQTork.main(shitsmnID,int_seq,kaitUserID,kaitUserComment,rqYukJikn,rqYukKign)
            #個々の値を取得
            flg_S100 = json_S100["json_CommonInfo"]["errflg"]
            list_msgInfo_S100 = json_S100["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S100 = json_S100["shitsmnID"]
            int_seq_S100 = json_S100["int_seq"]
            int_rqSeq_S100 = json_S100["int_rqSeq"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S100)
            #検証用
            json_kaitRQInfo_S130_S100Kensho = S130_KaitRQShutk.main(str_shitsmnID_S100,int_seq_S100,int_rqSeq_S100)["json_kaitRQInfo"]
            #-------------------------------------------------------------------------------
            #--S120-------------------------------------------------------------------------
            #サービス呼び出し
            userID = "SYSTEM000000000000"
            shitsmnID = "Q20210920000000001"
            int_seq = 1
            int_rqSeq = 4
            json_S120 = S120_KaitRQSakj.main(userID,shitsmnID,int_seq,int_rqSeq)
            #個々の値を取得
            flg_S120 = json_S120["json_CommonInfo"]["errflg"]
            list_msgInfo_S120 = json_S120["json_CommonInfo"]["list_msgInfo"]
            str_shitsmnID_S120 = json_S120["shitsmnID"]
            int_seq_S120 = json_S120["int_seq"]
            int_rqSeq_S120 = json_S120["int_rqSeq"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S120)
            json_kaitRQInfo_S130_S120Kensho = S130_KaitRQShutk.main(str_shitsmnID_S120,int_seq_S120,int_rqSeq_S120)["json_kaitRQInfo"]
            #-------------------------------------------------------------------------------
            #--S140-------------------------------------------------------------------------
            #サービス呼び出し
            shitsmnID = "Q20210920000000001"
            int_seq = 1
            json_S140 = S140_KaitRQListShutk.main(shitsmnID,int_seq)
            #個々の値を取得
            flg_S140 = json_S140["json_CommonInfo"]["errflg"]
            list_msgInfo_S140 = json_S140["json_CommonInfo"]["list_msgInfo"]
            tuple_T120_kaitRQList_S140 = json_S140["tuple_kaitRQList"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S140)
            #-------------------------------------------------------------------------------
            #--S150-------------------------------------------------------------------------
            #サービス呼び出し
            userName = "福永祐一"
            mailAddress = "fukunaga.y@jp.jra.com"
            #loginID = "2018derby"
            loginID = "2018derby" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            loginPass = "wagnerian"
            hyoka = 50
            userComment = "シュバルグランが行ったぞ！大胆戦法福永祐一！"
            loginKbn = "0"
            json_S150 = S150_UserInfoTork.main(userName,mailAddress,loginID,loginPass,hyoka,userComment,loginKbn)
            #個々の値を取得
            flg_S150 = json_S150["json_CommonInfo"]["errflg"]
            list_msgInfo_S150 = json_S150["json_CommonInfo"]["list_msgInfo"]
            str_userID_S150 = json_S150["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S150)
            #検証用
            json_shitsmnInfo_S180_S150Kensho = S180_UserInfoShutk.main(str_userID_S150)["json_userInfo"]
            #-------------------------------------------------------------------------------
            #--S160-------------------------------------------------------------------------
            #サービス呼び出し
            userID = "U20211018000000019"
            userName = "横山たけし"
            mailAddress = "yokoyama.t@jp.jra.com"
            loginID = "goldship"
            loginPass = "takaradsuka"
            hyoka = 50
            userComment = "お父さんの思い出"
            json_S160 = S160_UserInfoKoshn.main(userID,userName,mailAddress,loginID,loginPass,hyoka,userComment)
            #個々の値を取得
            flg_S160 = json_S160["json_CommonInfo"]["errflg"]
            list_msgInfo_S160 = json_S160["json_CommonInfo"]["list_msgInfo"]
            str_userID_S150 = json_S160["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S160)
            json_shitsmnInfo_S180_S160Kensho = S180_UserInfoShutk.main(str_userID_S150)["json_userInfo"]
            #-------------------------------------------------------------------------------
            #--S170-------------------------------------------------------------------------
            #サービス呼び出し
            userID = "U20211018000000021"
            json_S170 = S170_UserInfoSakj.main(userID)
            #個々の値を取得
            flg_S160 = json_S170["json_CommonInfo"]["errflg"]
            list_msgInfo_S170 = json_S170["json_CommonInfo"]["list_msgInfo"]
            str_userID_S170 = json_S170["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S170)
            json_shitsmnInfo_S180_S170Kensho = S180_UserInfoShutk.main(str_userID_S170)["json_userInfo"]
            #-------------------------------------------------------------------------------
            #--S180-------------------------------------------------------------------------
            #サービス呼び出し
            userID = "U20211018000000019"
            json_S180 = S180_UserInfoShutk.main(userID)
            #個々の値を取得
            flg_S180 = json_S180["json_CommonInfo"]["errflg"]
            list_msgInfo_S180 = json_S180["json_CommonInfo"]["list_msgInfo"]
            json_userInfo_S180 = json_S180["json_userInfo"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S180)
            #-------------------------------------------------------------------------------
            #--S185-------------------------------------------------------------------------
            #サービス呼び出し
            loginID = "2018derby20211018-205142"
            loginPass = "wagnerian"
            json_S185 = S185_UserInfoShutk_SysLogin.main(loginID,loginPass)
            #個々の値を取得
            flg_S185 = json_S185["json_CommonInfo"]["errflg"]
            list_msgInfo_S185 = json_S185["json_CommonInfo"]["list_msgInfo"]
            str_userID_S185 = json_S185["str_userID"]
            #メッセージ格納
            C030_MessageUtil.setMessageList(request,list_msgInfo_S185)
            #-------------------------------------------------------------------------------
            #--S900-------------------------------------------------------------------------
            json_S900 = S900_HanyoMstShutk.main("SEC0001","01")
            flg_S900 = json_S900["json_CommonInfo"]["errflg"]
            list_msgInfo_S900 = json_S900["json_CommonInfo"]["list_msgInfo"]
            tuple_M101_hanyoMst_S900 = json_S900["tuple_M101_hanyoMst"]
            C030_MessageUtil.setMessageList(request,list_msgInfo_S900)
            #-------------------------------------------------------------------------------
            #--S905-------------------------------------------------------------------------
            tableID = C010_Const.S100["tableID"]
            header = C010_Const.S100["header"]
            json_S905 = S905_SaibnMstShtk.main(tableID,header)
            flg_S905 = json_S905["json_CommonInfo"]["errflg"]
            list_msgInfo_S905 = json_S905["json_CommonInfo"]["list_msgInfo"]
            str_newID_S905 = json_S905["newID"]
            C030_MessageUtil.setMessageList(request,list_msgInfo_S905)
            #-------------------------------------------------------------------------------

            #戻り値にセット
            flg_return = str(int(flg_S999) \
                            + int(flg_S900) \
                            + int(flg_S060) \
                            )
            template = 'teachersapp/T999_Sample.html'
            context = {**context,**{"list_shitsmnIchirn":tuple_shitsmnIchirn_S999,
                                    "json_shitsmnInfo_S050_S020Kensho": json_shitsmnInfo_S050_S020Kensho,
                                    "json_shitsmnInfo_S050_S030Kensho": json_shitsmnInfo_S050_S030Kensho,
                                    "json_shitsmnInfo_S050_S040Kensho": json_shitsmnInfo_S050_S040Kensho,
                                    "json_shitsmnInfo":json_shitsmnInfo_S050,
                                    "tuple_shitsmnList_shinchk":tuple_T100_shitsmnList_shinchk_S060,
                                    "tuple_T100_shitsmnList_jokn":tuple_T100_shitsmnList_jokn_S070,
                                    "tuple_hashTag_S080":tuple_hashTag_S080,
                                    "tuple_M110_kaigiJiknList_S090":tuple_M110_kaigiJiknList_S090,
                                    "tuple_M111_rqYukJiknList_S095":tuple_M111_rqYukJiknList_S095,
                                    "json_kaitRQInfo_S130_S100Kensho":json_kaitRQInfo_S130_S100Kensho,
                                    "json_kaitRQInfo_S130_S120Kensho":json_kaitRQInfo_S130_S120Kensho,
                                    "tuple_T120_kaitRQList_S140":tuple_T120_kaitRQList_S140,
                                    "json_shitsmnInfo_S180_S150Kensho" : json_shitsmnInfo_S180_S150Kensho,
                                    "json_shitsmnInfo_S180_S160Kensho" : json_shitsmnInfo_S180_S160Kensho,
                                    "json_userInfo_S180" : json_userInfo_S180,
                                    "str_userID_S185" : str_userID_S185,
                                    "tuple_hanyoMst":tuple_M101_hanyoMst_S900,
                                    "str_newID":str_newID_S905,
                                    }
                    }
        
        #戻り値用のjsonを作成
        json_view = {'flg_return':flg_return, 'template':template, 'context':context, 'path_name':path_name}
        print("===デバッグ用=============================================================================")
        print("■json_view(V999)")
        print(" flg_return:",json_view['flg_return'])
        print(" template:",json_view['template'])
        print(" path_name:",json_view['path_name'])
        print("=========================================================================================")
        return json_view
    #==例外処理==========================================================================================
    except Exception as e :
        raise
    #====================================================================================================

