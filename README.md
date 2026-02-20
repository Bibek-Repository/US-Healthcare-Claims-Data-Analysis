# Healthcare Data Exploration Project

## Overview
This project involves downloading and exploring healthcare datasets to prepare the environment for further analysis. The focus is on understanding dataset structure, handling missing values, and identifying duplicates.

## Datasets
Enhanced Health Insurance Claims Dataset (Kaggle)

Downloaded from:
https://www.kaggle.com/datasets/leandrenash/enhanced-health-insurance-claims-dataset

This dataset contains enhanced claims records with additional features for deeper analysis.

## Tools & Environment
The following tools are required to set up the environment:

- **Programming & Analysis**
  - Python
  - Pandas
  - Jupyter Notebook / VS Code
- **Databases**
  - SQL (PostgreSQL)
- **Visualization**
  - Tableau 

## Steps

1. **Datasets**
   - Download zip file from https://www.kaggle.com/datasets/leandrenash/enhanced-health-insurance-claims-dataset

2. **Tools**
   - Python and required packages (`pandas`, `numpy`, etc.).
   - Jupyter Notebook and VS Code for coding.
   - PostgreSQL for database exploration.
   - Tableau for visualization.

3. **Explore Datasets**
   - Inspect columns and data types.
        -Columns like ClaimID, PatientID, ProviderID → identifiers, not categorical features
        -Columns like PatientGender, ClaimStatus, PatientMaritalStatus, PatientEmploymentStatus, ProviderSpecialty, ClaimType, ClaimSubmissionMethod → categorical features
        -Columns like DiagnosisCode or ProcedureCode → often categorical too, because they are codes
        -Columns like ClaimDate → datetime (convert later if needed)
   - Check for missing values and duplicates.
   - Take initial notes on dataset characteristics and quality.

4. **Outcomes**
    4500 rows * 17 columns
    Column names: ClaimID', 'PatientID', 'ProviderID', 'ClaimAmount', 'ClaimDate',
       'DiagnosisCode', 'ProcedureCode', 'PatientAge', 'PatientGender',
       'ProviderSpecialty', 'ClaimStatus', 'PatientIncome',
       'PatientMaritalStatus', 'PatientEmploymentStatus', 'ProviderLocation',
       'ClaimType', 'ClaimSubmissionMethod'
    nulls: 0
                                        ClaimAmount	        PatientAge	        PatientIncome
                                count	4500.000000	        4500.000000	        4500.000000
                                mean	5014.203867	        49.838444	        84384.284084
                                std	    2866.291066	        28.790471	        37085.908878
                                min	    100.120000	        0.000000	        20006.870000
                                25%	    2509.072500	        25.000000	        52791.905000
                                50%	    5053.765000	        50.500000	        84061.205000
                                75%	    7462.452500	        75.000000	        115768.417500
                                max	    9997.200000	        99.000000	        149957.520000

    correlation matrix:
                                    ClaimAmount  PatientAge  PatientIncome
                    ClaimAmount       1.000000    0.009515       0.019128
                    PatientAge        0.009515    1.000000       0.017400
                    PatientIncome     0.019128    0.017400       1.000000

    Outliers:
                            ClaimAmount - Number of outliers: 0
                            PatientAge - Number of outliers: 0
                            PatientIncome - Number of outliers: 0

## Deliverable
- Fully prepared environment.
- Initial dataset exploration notes including:
  - Number of columns and rows
  - Data types
  - Missing values
  - Duplicates
  - Any preliminary observations

## Strategy Decision Framework

            Situation:	               What to Do
            <5% missing:	            Drop rows
            Important numeric column:	Fill with median
            Categorical column:	      Fill with mode
            Many missing:	            Investigate before dropping

The dataframe under inspection has no duplicates.

Missing Value Treatment

Filled ClaimAmount with median
Filled PatientGender with mode

Duplicates Removed

X rows removed

Standardization

Gender standardized to M/F
Dates converted to datetime

Feature Engineering

Created YearMonth
Created Member-Month metrics
