import sqlite3

def start(components={}):
    connection = sqlite3.connect(":memory:", check_same_thread = False)
    print('DB component started!')
    connection.cursor().execute('create table report(name TEXT, id NUMBER)')
    return connection

def create_email(components={}):
    db = components['db']
    cursor = db.cursor()
    try:
        cursor.execute("insert into report(name, id) values('teste', 1)")
        db.commit()
    except Exception as e:
        print(e)

    return cursor.execute('select * from report').fetchall()