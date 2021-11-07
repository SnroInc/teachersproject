"""
共通クラス
C010_Const
共通的な定数を格納する

"""
from django.contrib.messages import constants
import MySQLdb


# Djangoメッセージレベル
DEBUG = constants.DEBUG
INFO = constants.INFO
SUCCESS = constants.SUCCESS
WARNING = constants.WARNING
ERROR = constants.ERROR

# シーケンステーブルID
S010 = {"tableID": "S010_USER_ID", "header": "U"}
S100 = {"tableID": "S100_SHITSMN_ID", "header": "Q"}
S120 = {"tableID": "S130_KAIG_ID", "header": "K"}

# urls.py path_name
APP_NAME_DEFAULT = 'teachersapp'

# 共通画面パス
PATH_NAME_ERR = APP_NAME_DEFAULT + ':systemError'
PATH_NAME_SUCCESS = APP_NAME_DEFAULT + ':success'
