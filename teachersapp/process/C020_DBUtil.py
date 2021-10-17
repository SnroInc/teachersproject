"""
共通クラス
C020_DBUtil
DB関連の共通メソッドを格納する

■PythonでMySQLに接続する方法【初心者向け】現役エンジニアが解説
https://techacademy.jp/magazine/18691
■MySQL 文字コード確認
https://qiita.com/yukiyoshimura/items/d44a98021608c8f8a52a
■【Python】mysqlclientでutf-8を使う方法
https://gametech.vatchlog.com/2019/05/07/mysqlclient-utf-8/
"""
# MySQLdbのインポート
import MySQLdb


def connectDB():
    # データベースへの接続とカーソルの生成
    #settingsから以ってきたい
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='K@iyo2021',
        db='TEACHERSDB',
        charset='utf8')
    #カーソルを辞書型で取得
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    json_DBConnectInfo = {'con':connection,'cur':cursor}
    return json_DBConnectInfo


def executeSQL(json_DBConnectInfo, sql, args):
    cur = json_DBConnectInfo['cur']
    #クエリを実行
    cur.execute(sql,args)
    # 実行結果を取得する
    result = cur.fetchall()
    return result


def closeDB(json_DBConnectInfo,errflg):
    connection = json_DBConnectInfo['con']
    if errflg == "0":
        # コミット
        connection.commit()
    else:
        # ロールバック
        connection.rollback()
    # 接続を閉じる
    connection.close()
