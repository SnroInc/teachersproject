"""
共通クラス
C050_StringUtil
セッション関連の共通メソッドを格納する

"""

def isNullorSpace(str):
    result = False
    if str == None or str == "":
        result = True
    return result
