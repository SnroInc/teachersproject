from django.urls import path

from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'teachersapp'
urlpatterns = [
    #main
    path('', views.v010_TopPage, name='topPage'),
    path('login/', views.v020_LoginView, name='login'),
    path('logout/', views.v025_Logout, name='logout'),
    path('shitsmnsaksi/', views.v030_ShitsmnSaksiView, name='shitsmnsaksi'),
    path('shitsmnDetail/<str:shitsmnID>/', views.v050_ShitsmnDetailView, name='shitsmnDetail'),
    path('shitsmnDetail/<str:shitsmnID>/kaitRQTork/', views.v060_KaitRQTorkView, name='kaitRQTork'),
    path('shitsmnDetail/<str:shitsmnID>/kaitRQList/', views.v070_KaitRQListView, name='kaitRQList'),
    path('shitsmnDetail/<str:shitsmnID>/kaitRQDetail/<int:int_seq>/<int:int_rqSeq>/', views.v080_KaitRQDetailView, name='kaitRQDetail'),
    path('signUp/', views.v100_SignUpView, name='signUp'),
    path('profile/', views.v110_ProfileView, name='profile'),
    path('myPage/', views.v115_MyPageView, name='myPage'),
    path('userKoshn/', views.v120_UserKoshn, name='userKoshn'),
    path('success/', views.v910_SuccessView, name='success'),
    path('systemError/', views.v999_SystemError, name='systemError'),
    #Sample
    path('Sample/', views.v999_sampleMethod, name='sample_path1'),
    path('Sample2/', views.v999_sampleMethod2, name='sample_path2'),
    path('test01/', views.test01, name='test01'),
] + static (settings.STATIC_URL, document_root=settings.STATIC_ROOT)
