from main import HealthcarePlan, HealthcareScenario, HealthcarePlanComparison

# Create comparison tool
comparison = HealthcarePlanComparison()

# Create PPO plan
ppo_plan = HealthcarePlan("Premium PPO", "PPO")
ppo_plan.set_parameters(
    monthly_premium=292.90,
    employer_premium_contribution=600,
    annual_deductible=2000,
    annual_oop_max=6500,
    coinsurance_rate=0.10,
    primary_care_copay=25,
    specialist_copay=45,
    urgent_care_copay=25,
    er_copay=300,
    generic_drug_copay=10,
    brand_drug_copay=30,
    hsa_eligible=False
)

# Create HDHP with HSA
hdhp_plan = HealthcarePlan("HDHP with HSA", "HDHP")
hdhp_plan.set_parameters(
    monthly_premium=133.21,
    employer_premium_contribution=300,
    annual_deductible=4000,
    annual_oop_max=8000,
    coinsurance_rate=0.10,
    hsa_eligible=True,
    employer_hsa_contribution=1200,
    employee_hsa_contribution=7350,
    federal_tax_rate=0.22,
    state_tax_rate=0.03
)

# Add plans to comparison
comparison.add_plan(ppo_plan)
comparison.add_plan(hdhp_plan)

# Create usage scenarios
healthy_scenario = HealthcareScenario("Healthy Year")
healthy_scenario.set_usage(
    primary_care_visits=4,
    generic_prescriptions=3,
    preventive_care_visits=2
)

moderate_scenario = HealthcareScenario("Moderate Usage")
moderate_scenario.set_usage(
    primary_care_visits=6,
    specialist_visits=2,
    generic_prescriptions=12,
    lab_tests=4,
    urgent_care_visits=4
)

high_usage_scenario = HealthcareScenario("High Usage")
high_usage_scenario.set_usage(
    primary_care_visits=8,
    specialist_visits=4,
    er_visits=1,
    generic_prescriptions=24,
    brand_prescriptions=12,
    lab_tests=8,
    imaging=2
)

# Add scenarios
comparison.add_scenario(healthy_scenario)
comparison.add_scenario(moderate_scenario)
comparison.add_scenario(high_usage_scenario)

# Generate comparison
print("Healthcare Plan Comparison")
print("=" * 80)
df = comparison.compare_plans()
print(df.to_string(index=False))

# Find breakeven points
print("\n\nBreakeven Analysis")
print("=" * 80)
breakeven = comparison.find_breakeven_points()
for comparison_pair, amount in breakeven.items():
    if isinstance(amount, str):
        print(f"{comparison_pair}: {amount}")
    else:
        print(f"{comparison_pair}: Plans have equal cost at ${amount:,.0f} in medical expenses")

# Generate recommendation for specific expected costs
print("\n\nRecommendation for $5,000 Expected Medical Costs")
print("=" * 80)
print(comparison.generate_recommendation(5000))

# Generate cash flow analysis
print("\n\n")
print(comparison.generate_cash_flow_analysis())

# Plot cost curves
comparison.plot_cost_curves()

# Save configuration
comparison.save_comparison("my_healthcare_comparison.json")