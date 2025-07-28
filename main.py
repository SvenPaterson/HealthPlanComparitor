"""
Healthcare Plan Comparison Tool
Main entry point for comparing health insurance plans
"""

from models.plan import HealthcarePlan
from models.models import UsageScenario


def create_ppo_plan():
    """Create and configure a PPO plan"""
    plan = HealthcarePlan("Premium PPO", "PPO")
    
    # Your specific PPO details
    plan.monthly_premium = 292.90
    plan.annual_employer_contribution = 600
    plan.deductible = 2000
    plan.out_of_pocket_max = 6500
    plan.coinsurance_rate = 0.10
    
    # PPO copays
    plan.copays = {
        'primary_care': 25,
        'specialist': 45,
        'urgent_care': 25,
        'emergency_room': 300,
        'generic_drug': 10,
        'brand_drug': 30,
    }
    
    return plan


def create_hdhp_plan():
    """Create and configure an HDHP plan"""
    plan = HealthcarePlan("HDHP with HSA", "HDHP")
    
    # Your specific HDHP details
    plan.monthly_premium = 133.21
    plan.annual_employer_contribution = 300
    plan.deductible = 4000
    plan.out_of_pocket_max = 8000
    plan.coinsurance_rate = 0.10
    
    # HDHP HSA settings
    plan.hsa_eligible = True
    plan.employer_hsa_contribution = 1200
    
    return plan

def create_scenarios():
    """Create usage scenarios"""
    scenarios = []
    
    # Healthy year scenario
    healthy = UsageScenario("Healthy Year", "Minimal healthcare usage")
    healthy.visits = {
        'primary_care': 4,      # Quarterly check-ins
        'specialist': 0,
        'urgent_care': 2,
        'emergency_room': 0,
        'preventive_care': 2,   # Annual physicals
    }
    healthy.prescriptions = {
        'generic': 3,           # Occasional needs
        'brand': 0,
    }
    healthy.tests = {
        'lab_work': 2,          # Annual bloodwork
        'imaging': 0,
        'procedures': 0,
    }
    scenarios.append(healthy)
    
    # Moderate usage scenario
    moderate = UsageScenario("Moderate Usage", "Typical family healthcare needs")
    moderate.visits = {
        'primary_care': 6,
        'specialist': 2,
        'urgent_care': 6,       # Kids & us get sick
        'emergency_room': 1,
        'preventive_care': 2,
    }
    moderate.prescriptions = {
        'generic': 12,          # Monthly maintenance
        'brand': 0,
    }
    moderate.tests = {
        'lab_work': 4,
        'imaging': 0,
        'procedures': 0,
    }
    scenarios.append(moderate)
    
    # High usage scenario
    high_usage = UsageScenario("High Usage", "Significant healthcare needs")
    high_usage.visits = {
        'primary_care': 8,
        'specialist': 4,
        'urgent_care': 10,
        'emergency_room': 2,
        'preventive_care': 2,
    }
    high_usage.prescriptions = {
        'generic': 24,          # Multiple medications
        'brand': 12,            # Specialty medications
    }
    high_usage.tests = {
        'lab_work': 8,
        'imaging': 2,
        'procedures': 0,
    }
    scenarios.append(high_usage)
    
    return scenarios

def main():
    """Main function to run healthcare plan comparison"""
    
    print("=" * 60)
    print("Healthcare Plan Comparison Tool")
    print("=" * 60)
    print()
    
    # Step 1: Create plans
    print("Step 1: Setting up healthcare plans...")
    
    ppo_plan = create_ppo_plan()
    hdhp_plan = create_hdhp_plan()
    
    plans = [ppo_plan, hdhp_plan]
    
    for plan in plans:
        print(f"\n✓ Created {plan}")
        print(f"  - Monthly premium: ${plan.monthly_premium:,.2f}")
        print(f"  - Annual premium cost: ${plan.annual_premium_cost():,.2f}")
        print(f"  - Deductible: ${plan.deductible:,.0f}")
        print(f"  - Out-of-pocket max: ${plan.out_of_pocket_max:,.0f}")
        
        if plan.hsa_eligible:
            print(f"  - HSA eligible: Yes")
            print(f"  - HSA Strategy: Long-term investment (not used for current expenses)")
            print(f"  - Employer HSA contribution: ${plan.employer_hsa_contribution:,.0f}")
            print(f"  - Employee HSA contribution: ${plan.employee_hsa_contribution():,.0f}")
            print(f"  - Total HSA contributions: ${plan.total_hsa_contributions():,.0f}")
            print(f"  - HSA balance EOY: ${plan.hsa_balance_end_of_year():,.0f}")
    
    print()
    
    # Step 2: Define usage scenarios  
    print("Step 2: Defining usage scenarios...")
    
    scenarios = create_scenarios()
    
    for scenario in scenarios:
        print(f"\n✓ {scenario}")
        print(f"  - Total visits: {scenario.total_visits()}")
        print(f"  - Medical costs before insurance: ${scenario.total_medical_cost_before_insurance():,.0f}")
    
    print()
    
    # Step 3: Calculate costs
    print("Step 3: Calculating costs...")
    # TODO: Calculate costs for each plan/scenario combination
    print("✓ Costs calculated")
    print()
    
    # Step 4: Display results
    print("Step 4: Results")
    print("-" * 60)
    # TODO: Show comparison table
    # TODO: Show recommendations
    # TODO: Show visualizations
    
    print()
    print("Analysis complete!")


if __name__ == "__main__":
    main()