
def create_email(components={}):
    db = components['db']
    cursor = db.cursor()
    try:
        cursor.execute("insert into report(name, id) values('teste', 1)")
        db.commit()
    except Exception as e:
        print(e)

    return cursor.execute('select * from report').fetchall()