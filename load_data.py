from pg_connection import engine
import pandas as pd
from transform import members, providers, claims, services

members.to_sql("members", engine, if_exists="append", index=False)
providers.to_sql("providers", engine, if_exists="append", index=False)
claims.to_sql("claims", engine, if_exists="append", index=False)
services.to_sql("services", engine, if_exists="append", index=False)

print("Data loaded successfully!")