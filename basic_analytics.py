from sqlalchemy import create_engine
import pandas as pd
from pg_connection import engine 
from transform import members, claims

try:
    with engine.connect() as conn:
        print("✅ Database connection is active!")
except Exception as e:
    print("❌ Connection failed:", e)

# Total claims per member


query1 = """
SELECT 
m."MemberID",
COUNT(c."ClaimID") AS ClaimAmount
FROM members m
LEFT JOIN claims c 
ON m."MemberID" = c."MemberID"
GROUP BY m."MemberID"
ORDER BY ClaimAmount DESC;
"""

df_claims_per_member = pd.read_sql(query1, engine)
print(df_claims_per_member)


# Total cost per month
query2 = """
SELECT 
DATE_TRUNC('month', "ClaimDate") AS month,
SUM("ClaimAmount") AS total_monthly_cost
FROM claims
GROUP BY DATE_TRUNC('month', "ClaimDate")
ORDER BY month;
"""

df_monthly_cost = pd.read_sql(query2, engine)
print(df_monthly_cost)

# top ten services

query3 = """
SELECT 
s."ServiceID",
s."ProcedureCode",
SUM(c."ClaimAmount") AS total_cost
FROM services s
JOIN claims c
ON s."ClaimID" = c."ClaimID"
GROUP BY s."ServiceID", s."ProcedureCode"
ORDER BY total_cost DESC
LIMIT 10;
"""

df_top_ten_services = pd.read_sql(query3, engine)
print(df_top_ten_services)
