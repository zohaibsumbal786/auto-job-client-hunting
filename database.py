import json
import os
from datetime import datetime

class LeadDatabase:
    def __init__(self, db_file='leads.json'):
        self.db_file = db_file
        self.leads = self._load_database()
    
    def _load_database(self):
        """Load leads from JSON file"""
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {'contacted': [], 'pending': [], 'responded': []}
    
    def _save_database(self):
        """Save leads to JSON file"""
        with open(self.db_file, 'w') as f:
            json.dump(self.leads, f, indent=2)
    
    def add_lead(self, lead, status='pending'):
        """Add new lead to database"""
        lead['added_date'] = datetime.now().isoformat()
        lead['status'] = status
        
        if status not in self.leads:
            self.leads[status] = []
        
        self.leads[status].append(lead)
        self._save_database()
    
    def mark_contacted(self, email):
        """Move lead from pending to contacted"""
        for lead in self.leads.get('pending', []):
            if lead.get('email') == email:
                lead['contacted_date'] = datetime.now().isoformat()
                lead['status'] = 'contacted'
                self.leads['contacted'].append(lead)
                self.leads['pending'].remove(lead)
                self._save_database()
                return True
        return False
    
    def is_already_contacted(self, email):
        """Check if lead was already contacted"""
        for status in ['contacted', 'responded']:
            for lead in self.leads.get(status, []):
                if lead.get('email') == email:
                    return True
        return False
    
    def get_stats(self):
        """Get database statistics"""
        return {
            'pending': len(self.leads.get('pending', [])),
            'contacted': len(self.leads.get('contacted', [])),
            'responded': len(self.leads.get('responded', []))
        }
