import mysql.connector

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

    # SELECT文を実行
    select_sql = "SELECT * FROM members WHERE name = 'にゃんこ'"

    # SQLを以下で実行します
    cursor.execute(select_sql)

    # 実行の結果を一つだけ取得します。
    record = cursor.fetchone()

    print(record)

    # 接続を閉じます。
    cursor.close()

# エラーハンドリング
except Exception as e:
    print(f"Error Occurred: {e}")

# tryでどの場合でも実行される最終的なタスク
finally:
    if connection is not None and connection.is_connected():
        connection.close()
