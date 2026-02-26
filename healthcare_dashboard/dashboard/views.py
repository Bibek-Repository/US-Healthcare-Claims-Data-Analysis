from django.conf import settings
import pandas as pd
from django.shortcuts import render

def index(request):

    data_path = settings.BASE_DIR.parent / "visualizations"

    claims_per_member = pd.read_csv(data_path / 'claims_per_member.csv')
    cost_by_age = pd.read_csv(data_path / 'cost_by_age.csv')
    cost_by_gender = pd.read_csv(data_path / 'cost_by_gender.csv')
    cost_per_month = pd.read_csv(data_path / 'cost_per_month.csv')
    cumulative_cost = pd.read_csv(data_path / 'cummulative_cost_trend.csv')
    highest_spending = pd.read_csv(data_path / 'highest_spending_patient.csv')
    top_services = pd.read_csv(data_path / 'top_ten_service.csv')

    context = {
        "total_claims": len(claims_per_member),
        "total_cost": cost_per_month["total_monthly_cost"].sum(),
        "top_patient": highest_spending.iloc[0].to_dict(),
        "top_services": top_services.to_dict(orient='records'),
        "cost_by_gender": cost_by_gender.to_dict(orient='records'),
        "cost_by_age": cost_by_age.to_dict(orient='records'),
        "monthly_cost": cost_per_month.to_dict(orient='records'),
    }

    return render(request, "dashboard/index.html", context)


