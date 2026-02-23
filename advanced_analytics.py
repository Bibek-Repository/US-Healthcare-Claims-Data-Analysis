from sqlalchemy import create_engine
import pandas as pd
from pg_connection import engine 
from transform import members, claims

# Window Functions
#ROW_NUMBER() – Latest Claim Per Patient
# use case: Get most recent claim of each patient.
query1 = """
SELECT *
FROM (
SELECT 
"MemberID",
"ClaimID",
"ClaimAmount",
"ClaimDate",
ROW_NUMBER() OVER (
PARTITION BY "MemberID" 
ORDER BY "ClaimDate" DESC) AS row_num 
FROM claims
) sub
WHERE row_num = 1;
"""
df = pd.read_sql(query1, engine)
df.to_csv("./visualizations/latest_claim_per_patient.csv", index=False)
#  Gives latest claim per patient
#  Useful for patient activity analysis


# RANK() – Rank Patients by Total Cost
# Use case: Find highest spending patients.
query2 = """
SELECT 
"MemberID",
SUM("ClaimAmount") AS total_spent,
RANK() OVER (
ORDER BY SUM("ClaimAmount") DESC
) AS spending_rank
FROM claims
GROUP BY "MemberID";
"""
# Identifies top cost drivers
# Good for segmentation
df = pd.read_sql(query2, engine)
df.to_csv("./visualizations/highest_spending_patient.csv", index=False)


# SUM() OVER() – Running Total (Trend)
# Use case: Monthly cumulative cost trend.
query3 = """
SELECT
DATE_TRUNC('month', "ClaimDate") AS year_month,
SUM("ClaimAmount") AS monthly_cost,
SUM(SUM("ClaimAmount")) OVER (
    ORDER BY DATE_TRUNC('month', "ClaimDate")
) AS cumulative_cost
FROM claims
GROUP BY DATE_TRUNC('month', "ClaimDate")
ORDER BY year_month;
"""
# Perfect for line charts in dashboard
df = pd.read_sql(query3, engine)
df.to_csv("./visualizations/cummulative_cost_trend.csv", index=False)



# Segment High-Cost Members
# High-cost member = Total spending > 90th percentile
# Find 90th Percentile
query4= """
SELECT 
PERCENTILE_CONT(0.9) 
WITHIN GROUP (ORDER BY total_spent) AS percentile_90
FROM (
SELECT 'MemberID', SUM("ClaimAmount") AS total_spent
FROM claims
GROUP BY "MemberID"
) sub;
"""
df = pd.read_sql(query4, engine)
df.to_csv("./visualizations/percentile calculation.csv", index=False)


query5 = """
WITH patient_spending AS (
  SELECT
    c."MemberID",
    m."Age" AS age,
    m."Gender" AS gender,
    m."Income" AS income,
    SUM(c."ClaimAmount") AS total_spent
  FROM claims c
  JOIN members m
    ON c."MemberID" = m."MemberID"
  GROUP BY c."MemberID", m."Age", m."Gender", m."Income"
),
threshold AS (
  SELECT
    PERCENTILE_CONT(0.9)
    WITHIN GROUP (ORDER BY total_spent) AS p90
  FROM patient_spending
)
SELECT *
FROM patient_spending
WHERE total_spent > (SELECT p90 FROM threshold);
"""
# Identifies high-risk/high-cost patients
# Important for healthcare cost optimization
df = pd.read_sql(query5, engine)
df.to_csv("./visualizations/segment_high_cost_members.csv", index=False)



# Demographic Segmentation
# cost by Gender
query6 = """
SELECT 
    m."Gender" AS gender,
    COUNT(DISTINCT c."MemberID") AS total_patients,
    SUM(c."ClaimAmount") AS total_cost,
    AVG(c."ClaimAmount") AS avg_claim
FROM claims c
JOIN members m
    ON c."MemberID" = m."MemberID"
GROUP BY m."Gender"
ORDER BY m."Gender";
"""

df_gender = pd.read_sql(query6, engine)
df_gender.to_csv("./visualizations/cost_by_gender.csv", index=False)


# Cost by Age Group (joined with members)
query7 = """
SELECT 
    CASE 
        WHEN m."Age" < 25 THEN 'Under 25'
        WHEN m."Age" BETWEEN 25 AND 40 THEN '25-40'
        WHEN m."Age" BETWEEN 41 AND 60 THEN '41-60'
        ELSE '60+'
    END AS age_group,
    SUM(c."ClaimAmount") AS total_cost,
    COUNT(DISTINCT c."MemberID") AS patients
FROM claims c
JOIN members m
    ON c."MemberID" = m."MemberID" 
GROUP BY age_group
ORDER BY total_cost DESC;
"""
df = pd.read_sql(query7, engine)
df.to_csv("./visualizations/cost_by_age.csv", index=False)


# Trend Calculations
# Monthly Growth Rate
query8 = """
WITH monthly_cost AS (
    SELECT
        TO_CHAR("ClaimDate", 'YYYY-MM') AS year_month,
        SUM("ClaimAmount") AS total_cost
    FROM claims
    GROUP BY TO_CHAR("ClaimDate", 'YYYY-MM')
)
SELECT
    year_month,
    total_cost,
    LAG(total_cost) OVER (ORDER BY year_month) AS previous_month,
    ROUND(
        ((total_cost - LAG(total_cost) OVER (ORDER BY year_month)) * 100.0
        / LAG(total_cost) OVER (ORDER BY year_month))::numeric
    , 2) AS growth_percentage
FROM monthly_cost
ORDER BY year_month;
"""
df = pd.read_sql(query8, engine)
df.to_csv("./visualizations/monthly_trend.csv", index=False)
