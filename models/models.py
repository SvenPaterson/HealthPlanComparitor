"""
Usage Scenario Model
Represents expected healthcare usage for a year
"""

class UsageScenario:
    """Represents expected medical usage for a year"""
    
    def __init__(self, name: str, description: str = ""):
        """
        Initialize a usage scenario
        
        Args:
            name: Name of the scenario (e.g., "Healthy Year")
            description: Optional description of the scenario
        """
        self.name = name
        self.description = description
        
        # Medical visits
        self.visits = {
            'primary_care': 0,
            'specialist': 0,
            'urgent_care': 0,
            'emergency_room': 0,
            'preventive_care': 0,  # Usually free
        }
        
        # Prescriptions (number of fills per year)
        self.prescriptions = {
            'generic': 0,
            'brand': 0,
        }
        
        # Tests and procedures
        self.tests = {
            'lab_work': 0,     # Blood tests, etc.
            'imaging': 0,      # X-rays, MRI, etc.
            'procedures': 0,   # Minor procedures
        }
        
        # Typical costs (what provider charges before insurance)
        self.typical_costs = {
            'primary_care': 150,
            'specialist': 300,
            'urgent_care': 200,
            'emergency_room': 2000,
            'preventive_care': 200,
            'lab_work': 100,
            'imaging': 500,
            'procedures': 1000,
            'generic_drug': 20,
            'brand_drug': 200,
        }
        
    def __str__(self):
        """String representation"""
        return f"{self.name}: {self.description}" if self.description else self.name
    
    def total_visits(self):
        """Total number of medical visits"""
        return sum(self.visits.values())
    
    def total_medical_cost_before_insurance(self):
        """Calculate total medical costs before insurance"""
        total = 0
        
        # Add visit costs
        for visit_type, count in self.visits.items():
            total += count * self.typical_costs.get(visit_type, 0)
        
        # Add prescription costs
        total += self.prescriptions['generic'] * self.typical_costs['generic_drug']
        total += self.prescriptions['brand'] * self.typical_costs['brand_drug']
        
        # Add test/procedure costs
        for test_type, count in self.tests.items():
            total += count * self.typical_costs.get(test_type, 0)
        
        return total