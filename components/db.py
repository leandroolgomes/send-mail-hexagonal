import sqlite3

def start(components={}):
    connection = sqlite3.connect(":memory:", check_same_thread = False)
    print('DB component started!')
    connection.cursor().execute('create table report(name TEXT, id NUMBER)')
    return connection