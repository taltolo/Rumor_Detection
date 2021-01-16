import io
import sqlite3



CREATE_HYPERPARAMETERS_TABLE="CREATE TABLE IF NOT EXISTS hyperparameters (model_name TEXT PRIMARY KEY," \
                             "filters_number INTEGER," \
                             "optimizer TEXT," \
                             "epochs INTEGER," \
                             "batch_size INTEGER);"
GET_ALL_HYPERPARAMETERS="SELECT * FROM hyperparameters;"
GET_HYPERPARAMETERS_BY_MODEL="SELECT * FROM hyperparameters WHERE model_name=?;"
INSERT_HYPERPARAMETERS="INSERT INTO hyperparameters (model_name,filters_number,optimizer,epochs,batch_size) VALUES (?,?,?,?,?);"
GET_ALL_MODEL_NAME="SELECT model_name FROM hyperparameters;"
DELETE_BY_NAME_MODEL="DELETE FROM hyperparameters WHERE model_name=?"
DELETE_TABLE = "DROP TABLE hyperparameters"



def connect():
    return sqlite3.connect('hyperparameters.db', detect_types=sqlite3.PARSE_DECLTYPES)

def create_table(connection):
    with connection:
        connection.execute(CREATE_HYPERPARAMETERS_TABLE)

def get_all_hyperparameters(connection):
    with connection:
        return connection.execute(GET_ALL_HYPERPARAMETERS).fetchall()

def get_hyperparameters_by_model(connection,model_name):
    with connection:
        return connection.execute(GET_HYPERPARAMETERS_BY_MODEL,(model_name,)).fetchall()

def add_hyperparameters(connection,model_name,filters_number,optimizer,epochs,batch_size):
    with connection:
        connection.execute(INSERT_HYPERPARAMETERS,(model_name,filters_number,optimizer,epochs,batch_size,))

def get_model_name(connection):
    with connection:
        return connection.execute(GET_ALL_MODEL_NAME).fetchall()

def delete_model_by_model_name(connection,model_name):
    with connection:
        connection.execute(DELETE_BY_NAME_MODEL,(model_name,))

