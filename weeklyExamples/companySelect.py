from companyConnect import get_conn_params
import pandas as pd
from sqlalchemy import create_engine, text

params = get_conn_params()

# Construct the SQLAlchemy connection URI (string)
engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(**params))

departments = pd.read_sql("select * from departments where Dept = 33;", engine)
sales = pd.read_sql("select * from sales limit 5;", engine)

print(departments)
print(sales)


                       
