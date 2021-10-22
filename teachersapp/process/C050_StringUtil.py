"""
共通クラス
C050_StringUtil
セッション関連の共通メソッドを格納する

"""

def isNullCharacter(_str_):
    result = False
    if _str_ == None or _str_ == "":
        result = True
    return result
