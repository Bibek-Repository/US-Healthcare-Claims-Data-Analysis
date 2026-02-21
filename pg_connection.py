import pandas as pd
from sqlalchemy import create_engine

# credentials
username = "postgres"
password = "ultra123"
host = "localhost"
port = "5432"
database = "healthcare_db"

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

# # Testing connection
# df = pd.read_sql("SELECT version();", engine)
# print(df)