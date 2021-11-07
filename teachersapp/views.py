from django.shortcuts import render,redirect

# Create your views here.

from .process import (
    V999_SampleProcess,
    V010_TopPageProcess,
    V020_LoginProcess,
    V025_Logout,
    V030_ShitsmnSaksiProcess,
    V050_ShitsmnDetailProcess,
    V060_KaitRQTork,
    V070_KaitRQList,
    V080_KaitRQDetail,
    V100_SignUp,
    V110_Profile,
    V115_MyPage,
    V120_UserKoshn
)
from .process import C010_Const,C030_MessageUtil
from .process import S006_GetKeibaNews

PATH_ERR = C010_Const.PATH_NAME_ERR

#トップページ
def v010_TopPage(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V010_TopPageProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#ログインページ
def v020_LoginView(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V020_LoginProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#ログアウト
def v025_Logout(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V025_Logout.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#質問作成
def v030_ShitsmnSaksiView(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V030_ShitsmnSaksiProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#質問詳細
def v050_ShitsmnDetailView(request,shitsmnID):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V050_ShitsmnDetailProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#回答RQ
def v060_KaitRQTorkView(request,shitsmnID):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V060_KaitRQTork.main(request,shitsmnID)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)
      
#回答RQ
def v070_KaitRQListView(request,shitsmnID):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V070_KaitRQList.main(request,shitsmnID)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

def v080_KaitRQDetailView(request,shitsmnID,int_seq,int_rqSeq):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V080_KaitRQDetail.main(request,shitsmnID,int_seq,int_rqSeq)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)

#サインアップ
def v100_SignUpView(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V100_SignUp.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)


#プロフィール
def v110_ProfileView(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V110_Profile.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)


#マイページ
def v115_MyPageView(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V115_MyPage.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)


#ユーザ情報更新
def v120_UserKoshn(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V120_UserKoshn.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)


def v999_SystemError(request):
    template = 'teachersapp/T900_ERR500.html'
    context = {}
    try:
        return render(request, template, context)
    except Exception as e :
        #コンソールにエラーを出力
        C030_MessageUtil.systemErrorCommonMethod()
        return render(request, template, context)

def v910_SuccessView(request):
    template = 'teachersapp/T910_Success.html'
    context = {}
    try:
        return render(request, template, context)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)


#===テストorサンプルメソッド========================================================================
def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')

def v999_sampleMethod(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V999_SampleProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #システムエラー共通処理
        C030_MessageUtil.systemErrorCommonMethod()
        #システムエラー画面に遷移
        return redirect(PATH_ERR)
        

def v999_sampleMethod2(request):
    try:
        #ビュープロセスクラスを呼び出し
        json_view = V999_SampleProcess.main(request)
        #「render」か「redirect」かを判断
        flg_return = json_view["flg_return"]
        if flg_return == "0":
            #「render」の場合
            context = json_view["context"]
            template = json_view["template"]
            return render(request, template, context)
        elif flg_return == "1":
            #「redirect」の場合
            path_name = json_view["path_name"]
            return redirect(path_name)
    except Exception as e :
        #エラーフラグを「2：システムエラー」にする
        errflg = "2"
        #コンソールにエラーを出力
        C030_MessageUtil.systemErrorCommonMethod()
        raise(e)

    #テスト01
def test01(request):
    json_keibaInfo = S006_GetKeibaNews.main(0)
    #メッセージリストを宣言
    template = "teachersapp/T999_test01.html"
    context = {"json_keibaInfo":json_keibaInfo}
    #返却
    return render(request, template, context) 
#====================================================================================================