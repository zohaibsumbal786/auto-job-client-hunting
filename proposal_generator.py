from openai import OpenAI
import config

class ProposalGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY) if config.OPENAI_API_KEY else None
    
    def generate_proposal(self, lead_info, service_type):
        """Generate personalized proposal based on lead info and service"""
        service = config.SERVICES.get(service_type, {})
        
        if self.client:
            return self._generate_ai_proposal(lead_info, service)
        else:
            return self._generate_template_proposal(lead_info, service)
    
    def _generate_ai_proposal(self, lead_info, service):
        """Use OpenAI to generate personalized proposal"""
        prompt = f"""
        Write a professional, concise proposal email for the following:
        
        Company: {lead_info.get('company', 'the company')}
        Industry: {lead_info.get('industry', 'their industry')}
        Service: {service.get('name')}
        Service Description: {service.get('description')}
        
        Requirements:
        - Keep it under 150 words
        - Be professional but friendly
        - Highlight specific benefits for their industry
        - Include a clear call to action
        - Don't include subject line or signature
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"AI generation failed: {e}")
            return self._generate_template_proposal(lead_info, service)
    
    def _generate_template_proposal(self, lead_info, service):
        """Fallback template-based proposal"""
        company = lead_info.get('company', 'your company')
        service_name = service.get('name', 'our services')
        
        return f"""Hello,

I noticed {company} and thought our {service_name} services could be valuable for your business.

We specialize in {service.get('description')} and have helped numerous companies achieve their digital transformation goals.

Our expertise includes:
• Custom solutions tailored to your needs
• Cutting-edge technology implementation
• Ongoing support and maintenance

I'd love to discuss how we can help {company} grow. Would you be available for a brief call this week?

Looking forward to connecting!"""
    
    def create_email_body(self, proposal, lead_info):
        """Create complete email with proposal and contact info"""
        return f"""{proposal}

Best regards,
{config.YOUR_NAME}
{config.COMPANY_NAME}

📧 Email: {config.YOUR_EMAIL}
📱 Contact: {config.YOUR_CONTACT_NUMBER}
🌐 Website: {config.WEBSITE}

---
This is a business proposal. If you're not interested, please let me know and I won't contact you again.
"""
