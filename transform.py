import pandas as pd


df = pd.read_csv("./Datasets/cleaned_healthcare_claims.csv")
df.head()

# Members Table

members = df[[
    "PatientID",
    "PatientAge",
    "PatientGender",
    "PatientIncome",
    "PatientMaritalStatus",
    "PatientEmploymentStatus",
]]
members = members.drop_duplicates()

members = members.rename(columns={
    "PatientID": "MemberID",
    "PatientAge": "Age",
    "PatientGender": "Gender",
    "PatientIncome": "Income",
    "PatientMaritalStatus": "MaritalStatus",
    "PatientEmploymentStatus": "EmploymentStatus",
})

# Providers Table

providers = df[[
    "ProviderID",
    "ProviderSpecialty",
    "ProviderLocation",
]]
providers = providers.drop_duplicates()

providers = providers.rename(columns={
    "ProviderSpecialty": "Specialty",
    "ProviderLocation": "Location",
})

# Claims Table

claims = df[[
    "ClaimID",
    "PatientID",
    "ProviderID",
    "ClaimAmount",
    "ClaimDate",
    "DiagnosisCode",
    "ClaimStatus",
    "ClaimType",
    "ClaimSubmissionMethod",
]].copy()

claims = claims.rename(columns={
    "PatientID": "MemberID",
    "ClaimSubmissionMethod": "SubmissionMethod",
})

# Date Conversion

claims["ClaimDate"] = pd.to_datetime(claims["ClaimDate"])

# Services Table

services = df[[
    "ClaimID",
    "ProcedureCode",
]].copy()

services["ServiceID"] = range(1, len(services) + 1)

