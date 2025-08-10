import pandas as pd
from sqlalchemy import create_engine
# Load CSV file
df = pd.read_csv('/Users/bollipallipreethichowdary/Downloads/Proj - 1/ETL_Proj_2 /Financial dataset.csv')
print(df)
# /Users/bollipallipreethichowdary/Downloads/Proj - 1/ETL_Proj_2 /Financial dataset.csv
# MySQL connection details
user = 'root'
password = 'Preethi@2810'  # raw password
host = 'localhost'
port = '3306'
database = 'Mysql'  # name of the database you created

# Encode password for safe URL usage
# encoded_password = quote_plus(password)

# Create connection engine
#engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
engine = create_engine("mysql+mysqlconnector://root:Preethi%402810@localhost:3306/Mysql")


# Load data into MySQL (creates a table from the DataFrame)
df.to_sql(name='financial_transactions', con=engine, if_exists='replace', index=False)

#print(" Data loaded successfully!")
