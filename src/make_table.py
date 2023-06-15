import MySQLdb

connection = MySQLdb.connect(
    host='mysql',
    user='user',
    passwd='password',
    db='db'
)

try:
    cursor = connection.cursor()
    create_members_sql = '''
        CREATE TABLE members (
          id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(50) NULL
        )'''
    cursor.execute(create_members_sql)

    create_mornings_sql = '''
        CREATE TABLE mornings (
          id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
          member_id INT NOT NULL,
          food VARCHAR(50) NULL
        )'''
    cursor.execute(create_mornings_sql)

    insert_sql = '''
        INSERT INTO members (
          name
        ) VALUES (
          '子猫ちゃん'
        )
    '''
    cursor.execute(insert_sql)
    connection.commit()

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    connection.close()
