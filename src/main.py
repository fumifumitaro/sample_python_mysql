import mysql.connector
import sys

if len(sys.argv) > 1:
    id: int = sys.argv[1]
else:
    print('IDを指定してください。')
    exit()

connection = mysql.connector.connect(
    host='mysql',
    user='user',
    passwd='password',
    db='db'
)

try:
    cursor = connection.cursor()

    # 該当IDのデータを引っ張る
    select_sql = "SELECT * FROM members WHERE id = " + str(id)
    cursor.execute(select_sql)

    # 子テーブルに該当IDと連動するレコードを設定して下記のサンプルを子テーブルのfoodに置き換えたい
    morning = 'サンプル'

    member = cursor.fetchone()
    print(f'{member[1]}は朝食に{morning}を食べました。')

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if connection is not None and connection.is_connected():
        connection.close()
