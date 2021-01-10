import sqlite3


CREATE_USER_TABLE="CREATE TABLE IF NOT EXISTS users (userid TEXT PRIMARY KEY,password INTEGER,permission INTEGER);"
GET_ALL_USERS="SELECT * FROM users;"
GET_USER_BY_ID="SELECT * FROM users WHERE userid=?;"
INSERT_USER="INSERT INTO users (userid,password,permission) VALUES (?,?,?);"


def connect():
    return sqlite3.connect('user.db', detect_types=sqlite3.PARSE_DECLTYPES)

def create_table(connection):
    with connection:
        connection.execute(CREATE_USER_TABLE)

def get_all_users(connection):
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()

def get_user_by_id(connection,userid):
    with connection:
        return connection.execute(GET_USER_BY_ID,(userid,)).fetchall()

def add_user(connection,userid,password,permission):
    with connection:
        connection.execute(INSERT_USER,(userid,password,permission,))



# def main():
#
#
#     user_id ='barak'
#     password=123
#     permission=0
#
#     con = connect()
#     create_table(con)
#
#     add_user(con,user_id,password,permission)
#     an2=get_all_users(con)
#     print(an2)
#
#
#
#
# if __name__ == "__main__":
#     main()

