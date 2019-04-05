#Import Modules
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import warnings
from Config import pwd, user, host, port, dbname
warnings.filterwarnings('ignore')

##Nish Table
def ebitda_multiple_full():
    # setup pymysql and connect to local MySQL workbench
    pymysql.install_as_MySQLdb()
    string = f"mysql://{user}:{pwd}@{host}/{dbname}"
    engine = create_engine(string)
    # Establish a connection to the local DB
    conn = engine.connect()
    ebita_multiple = pd.read_sql('select * FROM ebitda_multiple;', con=conn)
    ebita_multiple.dropna(inplace=True)
    ebita_multiple = ebita_multiple.to_dict(orient="record")

    return(ebita_multiple)

##Laylas table
def eps_multiple_full():
    # setup pymysql and connect to local MySQL workbench
    pymysql.install_as_MySQLdb()
    string = f"mysql://{user}:{pwd}@{host}/{dbname}"
    engine = create_engine(string)
    # Establish a connection to the local DB
    conn = engine.connect()
    eps_multiple = pd.read_sql('select * FROM eps_multiple;', con=conn)
    eps_multiple.dropna(inplace=True)
    eps_multiple = eps_multiple.to_dict(orient="record")

    return(eps_multiple)

##Don Table
def ev_sales_mutiple_full():
    # setup pymysql and connect to local MySQL workbench
    pymysql.install_as_MySQLdb()
    string = f"mysql://{user}:{pwd}@{host}/{dbname}"
    engine = create_engine(string)
    # Establish a connection to the local DB
    conn = engine.connect()
    ev_sales_mutiple = pd.read_sql('select * FROM ev_sales_multiple;', con=conn)
    ev_sales_mutiple = ev_sales_mutiple.to_dict(orient="record")

    return(ev_sales_mutiple)

#
def book_value_to_revenue_multiple_full():
    # setup pymysql and connect to local MySQL workbench
    pymysql.install_as_MySQLdb()
    string = f"mysql://{user}:{pwd}@{host}/{dbname}"
    engine = create_engine(string)
    # Establish a connection to the local DB
    conn = engine.connect()
    book_value_to_revenue_multiple = pd.read_sql('select * FROM book_value_to_revenue_multiple;', con=conn)
    book_value_to_revenue_multiple.dropna(inplace=True)
    book_value_to_revenue_multiple = book_value_to_revenue_multiple.to_dict(orient="record")

    return(book_value_to_revenue_multiple)


## top_bottom table
def top_bottom(model,topORbottom):
    # setup pymysql and connect to local MySQL workbench
    pymysql.install_as_MySQLdb()
    string = f"mysql://{user}:{pwd}@{host}/{dbname}"
    engine = create_engine(string)
    # Establish a connection to the local DB
    conn = engine.connect()
    # query = f"'select * from top_bottom_table where model like '{model}' and top_bottom like '{topORbottom}''"
    query = "select * from top_bottom_table where model like '" + model + "' and top_bottom like '" + topORbottom + "';"
    # query = '"' + query + '"'
    print(query)
    # sql = "select * from top_bottom_table where model like '{EBITDA_Multiple}' and top_bottom like '{top_3}';"
    top_bottom = pd.read_sql(str(query.strip('\\')), con=conn)
    top_bottom.drop("index", axis = 1, inplace = True)
    top_bottom = top_bottom.to_dict(orient="record")

    return(top_bottom)


def update_desc(model):
    # setup pymysql and connect to local MySQL workbench
    pymysql.install_as_MySQLdb()
    string = f"mysql://{user}:{pwd}@{host}/{dbname}"
    engine = create_engine(string)
    # Establish a connection to the local DB
    conn = engine.connect()
    print(model)
    # query = f"'select * from top_bottom_table where model like '{model}' and top_bottom like '{topORbottom}''"
    query = "select valuation_description from stock_valuation_descriptions where valuation_model like '" + model + "';"
    # query = '"' + query + '"'
    print(query)
    # sql = "select * from top_bottom_table where model like '{EBITDA_Multiple}' and top_bottom like '{top_3}';"
    updated_desc = pd.read_sql(str(query.strip('\\')), con=conn)
    # updated_desc.drop("index", axis = 1, inplace = True)
    updated_desc = updated_desc.to_dict(orient="record")

    return(updated_desc)
