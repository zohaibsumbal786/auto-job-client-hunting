import requests
import json
import config
from datetime import datetime

class LeadFinder:
    def __init__(self):
        self.hunter_api_key = config.HUNTER_API_KEY
        self.leads = []
    
    def find_leads(self, service_type, limit=10):
        """Find potential leads for a specific service"""
        service = config.SERVICES.get(service_type)
        if not service:
            return []
        
        leads = []
        
        # Method 1: Use Hunter.io to find companies
        if self.hunter_api_key:
            leads.extend(self._find_via_hunter(service, limit))
        
        # Method 2: Search LinkedIn (requires manual setup)
        # leads.extend(self._find_via_linkedin(service, limit))
        
        # Method 3: Reddit/Twitter mentions (requires API setup)
        # leads.extend(self._find_via_social(service, limit))
        
        return leads[:limit]
    
    def _find_via_hunter(self, service, limit):
        """Find leads using Hunter.io API"""
        leads = []
        keywords = service['keywords'][:3]  # Use top 3 keywords
        
        for keyword in keywords:
            try:
                # Hunter.io domain search
                url = f"https://api.hunter.io/v2/domain-search"
                params = {
                    'domain': keyword,  # This is simplified - you'd search by industry
                    'api_key': self.hunter_api_key,
                    'limit': limit // len(keywords)
                }
                
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    # Process results
                    for email_data in data.get('data', {}).get('emails', []):
                        leads.append({
                            'email': email_data.get('value'),
                            'company': data.get('data', {}).get('organization'),
                            'name': email_data.get('first_name', '') + ' ' + email_data.get('last_name', ''),
                            'source': 'hunter.io',
                            'service_match': service['name']
                        })
            except Exception as e:
                print(f"Hunter.io search failed for {keyword}: {e}")
        
        return leads
    
    def _find_via_linkedin(self, service, limit):
        """Find leads via LinkedIn (requires LinkedIn API access)"""
        # This requires LinkedIn Developer Account and OAuth
        # Placeholder for LinkedIn integration
        leads = []
        print("LinkedIn integration requires API setup")
        return leads
    
    def _find_via_social(self, service, limit):
        """Find leads from social media mentions"""
        # Placeholder for Twitter/Reddit API integration
        leads = []
        print("Social media integration requires API setup")
        return leads
    
    def get_sample_leads(self):
        """Generate sample leads for testing"""
        return [
            {
                'email': 'contact@example-startup.com',
                'company': 'Example Startup',
                'name': 'John Doe',
                'industry': 'Technology',
                'source': 'sample',
                'service_match': 'Web Development'
            },
            {
                'email': 'info@sample-business.com',
                'company': 'Sample Business',
                'name': 'Jane Smith',
                'industry': 'E-commerce',
                'source': 'sample',
                'service_match': 'AI Solutions'
            }
        ]
