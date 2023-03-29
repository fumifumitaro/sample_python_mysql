import mysql.connector
import sys

# ファイル名の後ろにつけている、1という数字を認識する関数が以下のif文ないです。
if len(sys.argv) > 1:
    id: int = sys.argv[1]
else:
    print('IDを指定してください。')
    exit()

# mysql接続用の関数
connection = mysql.connector.connect(
    host='mysql',
    user='user',
    passwd='password',
    db='db'
)

try:
    # mysqlの接続を開始します。
    cursor = connection.cursor()

    # 該当IDのデータを引っ張るためのSELECT文です。 『sql select』などで調べると色々なデータが出てきます。
    select_sql = "SELECT * FROM members WHERE id = " + str(id)
    # SQLを以下で実行します
    cursor.execute(select_sql)
    # 実行の結果を一つだけ取得します。
    member = cursor.fetchone()

    #TODO: 子テーブルに該当IDと連動するレコードを設定して下記のサンプルを子テーブルのfoodに置き換えたい
    morning = 'サンプル'

    print(f'{member[1]}は朝食に{morning}を食べました。')

    # 接続を閉じます。
    cursor.close()

# エラーハンドリング
except Exception as e:
    print(f"Error Occurred: {e}")

# tryでどの場合でも実行される最終的なタスク
finally:
    if connection is not None and connection.is_connected():
        connection.close()
