from django.conf import settings
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
import json
from .models import Claim
import uuid

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
        # Serialize to JSON strings for proper template rendering
        "cost_by_gender": json.dumps(cost_by_gender.to_dict(orient='records')),
        "cost_by_age": json.dumps(cost_by_age.to_dict(orient='records')),
        "monthly_cost": json.dumps(cost_per_month.to_dict(orient='records')),
    }

    return render(request, "dashboard/index.html", context)


@require_http_methods(["POST"])
def add_claim(request):
    """Handle new claim form submission"""
    try:
        # Get form data
        member_id = request.POST.get('memberID', '').strip()
        claim_amount = request.POST.get('claimAmount', '')
        claim_date = request.POST.get('claimDate', '')
        service_id = request.POST.get('serviceID', '').strip()
        procedure_code = request.POST.get('procedureCode', '').strip()
        description = request.POST.get('description', '').strip()
        
        # Validation
        if not member_id or not claim_amount or not claim_date:
            messages.error(request, "Member ID, Claim Amount, and Claim Date are required fields.")
            return redirect('index')
        
        # Generate unique Claim ID
        claim_id = f"CLM-{uuid.uuid4().hex[:12].upper()}"
        
        # Create and save claim
        claim = Claim.objects.create(
            MemberID=member_id,
            ClaimID=claim_id,
            ClaimAmount=float(claim_amount),
            ClaimDate=claim_date,
            ServiceID=service_id if service_id else None,
            ProcedureCode=procedure_code if procedure_code else None,
            Description=description if description else None
        )
        
        messages.success(request, f"Claim {claim_id} has been successfully added!")
        return redirect('index')
        
    except ValueError as e:
        messages.error(request, f"Invalid input: {str(e)}")
        return redirect('index')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('index')


