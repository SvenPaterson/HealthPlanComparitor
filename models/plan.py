"""
Healthcare Plan Model
Represents a health insurance plan with all its parameters
"""

class HealthcarePlan:
    """Represents a health insurance plan"""
    
    def __init__(self, name: str, plan_type: str = "PPO"):
        """
        Initialize a healthcare plan
        
        Args:
            name: Display name for the plan
            plan_type: Type of plan (PPO, HDHP, HMO, etc.)
        """
        self.name = name
        self.plan_type = plan_type
        
        # Monthly costs
        self.monthly_premium = 0.0
        self.annual_employer_contribution = 0.0  # Annual lump sum
        
        # Annual limits
        self.deductible = 0.0
        self.out_of_pocket_max = 0.0
        
        # Cost sharing
        self.coinsurance_rate = 0.0  # Percentage you pay after deductible
        
        # Copays (mainly for PPO)
        self.copays = {
            'primary_care': 0,
            'specialist': 0,
            'urgent_care': 0,
            'emergency_room': 0,
            'generic_drug': 0,
            'brand_drug': 0,
        }
        
        # HSA settings (mainly for HDHP)
        self.hsa_eligible = False
        self.employer_hsa_contribution = 0.0  # Annual
        self.current_year_hsa_limit = 8550  # 2025 family limit
        
        # HSA strategy - treating as investment, not using for current expenses
        self.use_hsa_for_expenses = False  # Key assumption!
        
    def __str__(self):
        """String representation of the plan"""
        return f"{self.name} ({self.plan_type})"
    
    def annual_premium_cost(self):
        """Calculate annual premium cost after employer contribution"""
        annual_premium = self.monthly_premium * 12
        return annual_premium - self.annual_employer_contribution
    
    def employee_hsa_contribution(self):
        """Calculate employee HSA contribution (assumes maxing out)"""
        if not self.hsa_eligible:
            return 0.0
        
        # Employee contributes the difference to reach the limit
        return self.current_year_hsa_limit - self.employer_hsa_contribution
    
    def total_hsa_contributions(self):
        """Calculate total HSA contributions (employer + employee)"""
        if not self.hsa_eligible:
            return 0.0
        
        return self.current_year_hsa_limit
    
    def hsa_balance_end_of_year(self):
        """
        Calculate HSA balance at end of year
        Since we're not using HSA for expenses, this equals total contributions
        """
        if not self.hsa_eligible:
            return 0.0
        
        return self.total_hsa_contributions()