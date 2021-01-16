import sqlite3
import numpy as np
import io

CREATE_ANALYZE_RESULTS_TABLE = "CREATE TABLE IF NOT EXISTS analyze_results (userid TEXT," \
                               "twitter_user_name TEXT," \
                               "amount_tweets INTEGER," \
                               "avg REAL," \
                               "model_name TEXT," \
                               "analyze_result_arr array);"
GET_ALL_RESULTS = "SELECT * FROM analyze_results;"
GET_RESULTS_BY_ID = "SELECT * FROM analyze_results WHERE userid=?;"
INSERT_ANALYZE_RESULTS = "INSERT INTO analyze_results (userid,twitter_user_name,amount_tweets,avg,model_name,analyze_result_arr)" \
                         " VALUES (?,?,?,?,?,?);"
GET_ALL_MODEL_NAME="SELECT model_name FROM analyze_results;"

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())


def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)



def connect():
    return sqlite3.connect("analyze_results.db", detect_types=sqlite3.PARSE_DECLTYPES)


def create_table(connection):
    with connection:
        connection.execute(CREATE_ANALYZE_RESULTS_TABLE)

def get_all_results(connection):
    with connection:
        sqlite3.register_converter("array", convert_array)
        return connection.execute(GET_ALL_RESULTS).fetchall()

def get_results_by_id(connection,userid):
    with connection:
        sqlite3.register_converter("array", convert_array)
        return connection.execute(GET_RESULTS_BY_ID,(userid,)).fetchall()

def add_results(connection,user_id, twitter_user_name, amount_tweets,avg,model_name,analyze_result_arr):
    with connection:
        sqlite3.register_adapter(np.ndarray, adapt_array)
        connection.execute(INSERT_ANALYZE_RESULTS,(user_id, twitter_user_name, amount_tweets,avg,model_name,analyze_result_arr, ))

def get_model_name(connection):
    with connection:
        return connection.execute(GET_ALL_MODEL_NAME).fetchall()

