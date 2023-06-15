import MySQLdb

connection = MySQLdb.connect(
    host='mysql',
    user='user',
    passwd='password',
    db='db'
)


try:
    cursor = connection.cursor()

    # 以下のままだと動かないので調整が必要
    insert_sql = '''
        INSERT INTO sample_table (
          sample_id,
          sample_name
        ) VALUES (
          0,
          'sample_value'
        )
    '''
    cursor.execute(insert_sql)
    connection.commit()

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    connection.close()
