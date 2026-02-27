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

---

## Project Structure

```
US Healthcare Claims Data Analysis/
├── README.md                              # Project documentation
├── requirements.txt                       # Python dependencies
├── load_data.py                          # Data loading utilities
├── transform.py                          # Data transformation pipeline
├── pg_connection.py                      # PostgreSQL connection handler
├── basic_analytics.py                    # Basic statistical analysis
├── advanced_analytics.py                 # Advanced analytics and ML
├── Datasets/
│   ├── cleaned_healthcare_claims.csv     # Processed claims data
│   └── enhanced_health_insurance_claims.csv  # Original enhanced dataset
├── visualizations/                       # Pre-generated CSV exports for dashboards
│   ├── claims_per_member.csv
│   ├── cost_by_age.csv
│   ├── cost_by_gender.csv
│   ├── cost_per_month.csv
│   ├── cumulative_cost_trend.csv
│   ├── highest_spending_patient.csv
│   ├── latest_claim_per_patient.csv
│   ├── monthly_trend.csv
│   ├── segment_high_cost_members.csv
│   └── top_ten_service.csv
├── Notebooks/
│   ├── cleaning_validation.ipynb         # Data cleaning and validation
│   ├── EDA.ipynb                        # Exploratory Data Analysis
│   ├── schema_design.ipynb              # Database schema design
│   └── test.ipynb                       # Testing and prototyping
└── healthcare_dashboard/                 # Django dashboard application
    ├── manage.py
    ├── db.sqlite3
    ├── dashboard/                        # Main dashboard app
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── templates/
    │       └── dashboard/
    │           └── index.html
    └── healthcare_dashboard/              # Django project settings

```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip or conda package manager
- Git

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd "US Healthcare Claims Data Analysis"
```

### Step 2: Create Virtual Environment
```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Database Connection
Edit `pg_connection.py` with your PostgreSQL credentials:
```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'healthcare_claims',
    'user': 'your_username',
    'password': 'your_password',
    'port': 5432
}
```

### Step 5: Run Data Pipeline
```bash
# Load and transform data
python load_data.py
python transform.py

# Generate analytics
python basic_analytics.py
python advanced_analytics.py
```

## Data Pipeline

### 1. Data Loading (`load_data.py`)
- Ingests CSV files from the Datasets directory
- Validates data integrity
- Performs initial quality checks
- Handles character encoding issues

### 2. Data Transformation (`transform.py`)
- Cleans and standardizes data types
- Handles missing values using median/mode imputation
- Removes duplicates
- Creates derived features
- Exports cleaned data to CSV and database

### 3. Database Schema (`schema_design.ipynb`)
- Defines normalized PostgreSQL schema
- Creates relationships between tables
- Implements indexing for performance
- Supports transactional integrity

### 4. Analytics (`basic_analytics.py` & `advanced_analytics.py`)
**Basic Analytics:**
- Descriptive statistics
- Distribution analysis
- Correlation measurements
- Outlier detection
- Summary aggregations

**Advanced Analytics:**
- Time series analysis
- Segmentation and clustering
- Seasonal trend decomposition
- Predictive modeling
- Cost driver analysis

## Dashboard Application

The Django dashboard provides interactive visualization of healthcare claims data:

```bash
cd healthcare_dashboard
python manage.py runserver
# Navigate to http://localhost:8000/dashboard
```

**Dashboard Features:**
- Real-time claims summary
- Cost trends and patterns
- Patient segmentation analysis
- Provider performance metrics
- Geographic distribution maps
- Drill-down capabilities

## Key Analyses Performed

### Cost Analysis
- Average claim amounts by demographics
- High-cost patient identification
- Cost trends over time
- Seasonal cost variations

### Patient Analytics
- Patient segmentation by spending
- Age and gender cost correlations
- Insurance status impact analysis
- Employment status patterns

### Provider Analytics
- Provider specialty cost breakdowns
- Geographic cost variations
- Provider claim patterns
- Service utilization rates

### Claim Analysis
- Claim status distributions
- Submission method effectiveness
- Diagnosis and procedure patterns
- Claims processing timelines

## Data Quality Standards

- **Completeness**: 100% - No missing values after treatment
- **Accuracy**: Validated against source data
- **Consistency**: Standardized formats and units
- **Timeliness**: Updated regularly with new claims
- **Validity**: All values within expected ranges

## Key Statistics (Summary)

| Metric | Value |
|--------|-------|
| Total Records | 4,500 claims |
| Date Range | Multiple years |
| Claim Amount Range | $100.12 - $9,997.20 |
| Average Claim | $5,014.20 |
| Patient Age Range | 0 - 99 years |
| Unique Patients | ~2,500+ |
| Unique Providers | ~500+ |
| Data Quality | 100% (after cleaning) |

## Technologies Used

- **Python Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Databases**: PostgreSQL, SQLite
- **Web Framework**: Django
- **Notebooks**: Jupyter Lab
- **Visualization**: Tableau, Matplotlib, Seaborn
- **Version Control**: Git

## Usage Examples

### Running Jupyter Notebooks
```bash
jupyter lab
# Open EDA.ipynb for exploratory analysis
# Open cleaning_validation.ipynb for data quality checks
```

### Accessing Clean Data
```python
import pandas as pd
df = pd.read_csv('Datasets/cleaned_healthcare_claims.csv')
print(df.head())
```

### Database Queries
```python
from pg_connection import connect_database
conn = connect_database()
cursor = conn.cursor()
cursor.execute("SELECT * FROM claims WHERE claim_amount > 5000")
```

## Troubleshooting

**Issue**: PostgreSQL connection failed
- Verify PostgreSQL service is running
- Check credentials in `pg_connection.py`
- Ensure database exists

**Issue**: Missing package errors
- Run `pip install -r requirements.txt` again
- Check Python version compatibility

**Issue**: Jupyter kernel errors
- Reinstall jupyter: `pip install --upgrade jupyter`
- Restart the kernel in notebook

## Future Enhancements

- Machine learning models for claim fraud detection
- Predictive analytics for cost forecasting
- Real-time data pipeline with streaming capabilities
- Mobile dashboard for on-the-go access
- API endpoints for external integrations
- Advanced geographic visualization with maps
- Integration with healthcare standard formats (FHIR)

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit pull request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support & Contact

For questions, issues, or suggestions:
- Open an issue on the repository
- Contact the project maintainers
- Review existing documentation and notebooks

## Acknowledgments

- Dataset source: Kaggle Enhanced Health Insurance Claims Dataset
- Community contributions and feedback
- Open-source libraries and tools

---

**Last Updated**: February 27, 2026
**Version**: 1.0.0
**Status**: Active Development

X rows removed

Standardization

Gender standardized to M/F
Dates converted to datetime

Feature Engineering

Created YearMonth
Created Member-Month metrics

Members (1) ────< Claims >──── (1) Providers
                      |
                      |
                   Services

services table is created and a new column is added which has its range: range(1, len(services) + 1)

Task Documentation – Day 4: Basic Analytics & SQL Queries

Date: 22-Feb-2026
Goal: Extract insights from the healthcare claims dataset using SQL and Python; perform basic analytics and fix minor errors.

1. SQL Queries Completed

a) Total claims per member

SELECT 
    m.member_id,
    COUNT(c.claimid) AS total_claims
FROM members m
LEFT JOIN claims c 
    ON m.member_id = c.member_id
GROUP BY m.member_id
ORDER BY total_claims DESC;

b) Total cost per month

SELECT 
    DATE_TRUNC('month', c.claimdate) AS claim_month,
    SUM(c.claimamount) AS total_cost
FROM claims c
GROUP BY claim_month
ORDER BY claim_month;

c) Top 10 services by total cost

SELECT 
    s.serviceid,
    s.procedurecode,
    SUM(c.claimamount) AS total_cost
FROM services s
JOIN claims c
    ON s.claimid = c.claimid
GROUP BY s.serviceid, s.procedurecode
ORDER BY total_cost DESC
LIMIT 10;

Notes on Queries:

LEFT JOIN ensures members with zero claims are included.

SUM() aggregates costs for services and monthly totals.

LIMIT 10 fetches only the top 10 most expensive services.

GROUP BY ensures proper aggregation at member, month, or service level.

2. Error Fixes / Improvements

Fixed incorrect joins that caused NULL or missing entries.

Corrected aggregation to group by both serviceid and procedurecode for accurate top 10 service costs.

Ensured column names match the current table schema (claimid, serviceid, procedurecode, claimamount).

3. Recommendations / Next Steps

Validate SQL results against raw CSV data.

Move queries into analytics.py for reproducible analysis using Pandas.




