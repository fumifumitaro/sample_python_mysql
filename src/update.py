import mysql.connector
import sys

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

    # INSERT文を定義、必ずWHEREを入れて条件をいれること
    insert_sql = '''
        UPDATE members
        SET
          name = "アップデートしてみた"
        WHERE
          name = "にゃんこ"
    '''

    # INSERTすることでデータの追加を行う
    cursor.execute(insert_sql)

    # 追加したデータの確定を行う
    connection.commit()

    # 接続を閉じます。
    cursor.close()

# エラーハンドリング
except Exception as e:
    print(f"Error Occurred: {e}")

# tryでどの場合でも実行される最終的なタスク
finally:
    if connection is not None and connection.is_connected():
        connection.close()
