#!/usr/bin/env python3
"""
Test run of the Client Hunter Bot (without sending real emails)
"""

import config
from lead_finder import LeadFinder
from proposal_generator import ProposalGenerator
from database import LeadDatabase

def test_run():
    print("="*60)
    print("🤖 AI CLIENT HUNTER BOT - TEST RUN")
    print("="*60)
    print(f"\n📋 Company: {config.COMPANY_NAME}")
    print(f"🌐 Website: {config.WEBSITE}")
    print(f"📧 Contact Email: {config.YOUR_EMAIL}")
    print(f"📱 Phone: {config.YOUR_CONTACT_NUMBER}")
    
    print("\n" + "="*60)
    print("SERVICES OFFERED")
    print("="*60)
    for key, service in config.SERVICES.items():
        print(f"\n✅ {service['name']}")
        print(f"   Description: {service['description']}")
        print(f"   Keywords: {', '.join(service['keywords'][:3])}")
    
    # Initialize components
    lead_finder = LeadFinder()
    proposal_gen = ProposalGenerator()
    database = LeadDatabase()
    
    print("\n" + "="*60)
    print("FINDING SAMPLE LEADS")
    print("="*60)
    
    # Get sample leads
    leads = lead_finder.get_sample_leads()
    print(f"\n✅ Found {len(leads)} sample leads:")
    for i, lead in enumerate(leads, 1):
        print(f"\n{i}. {lead['company']}")
        print(f"   Contact: {lead['name']}")
        print(f"   Email: {lead['email']}")
        print(f"   Industry: {lead['industry']}")
        print(f"   Service Match: {lead['service_match']}")
    
    print("\n" + "="*60)
    print("GENERATING PROPOSALS")
    print("="*60)
    
    # Generate proposals for each lead
    for i, lead in enumerate(leads, 1):
        print(f"\n{'='*60}")
        print(f"PROPOSAL #{i} - {lead['company']}")
        print('='*60)
        
        # Determine service type
        service_type = 'web_development' if 'Web' in lead['service_match'] else 'ai'
        
        # Generate proposal
        proposal = proposal_gen.generate_proposal(lead, service_type)
        email_body = proposal_gen.create_email_body(proposal, lead)
        
        # Create subject
        subject = f"Partnership Opportunity: {lead['service_match']} for {lead['company']}"
        
        print(f"\n📧 TO: {lead['email']}")
        print(f"📋 SUBJECT: {subject}")
        print(f"\n📝 EMAIL BODY:")
        print("-" * 60)
        print(email_body)
        print("-" * 60)
        
        # Add to database
        if not database.is_already_contacted(lead['email']):
            database.add_lead(lead, status='pending')
            print(f"\n✅ Lead added to database")
        else:
            print(f"\n⏭️  Lead already in database")
    
    # Show statistics
    print("\n" + "="*60)
    print("DATABASE STATISTICS")
    print("="*60)
    stats = database.get_stats()
    print(f"\n📊 Pending leads: {stats['pending']}")
    print(f"📊 Contacted leads: {stats['contacted']}")
    print(f"📊 Responded leads: {stats['responded']}")
    
    print("\n" + "="*60)
    print("TEST RUN COMPLETED")
    print("="*60)
    print("\n✅ The bot is working correctly!")
    print("\n📝 TO SEND REAL EMAILS:")
    print("1. Edit .env file with your real credentials:")
    print("   - YOUR_EMAIL (your Gmail address)")
    print("   - EMAIL_PASSWORD (Gmail App Password)")
    print("   - YOUR_CONTACT_NUMBER (your phone)")
    print("   - NOTIFICATION_EMAIL (where to receive alerts)")
    print("\n2. For Gmail App Password:")
    print("   - Go to: https://myaccount.google.com/apppasswords")
    print("   - Enable 2-Factor Authentication first")
    print("   - Generate an App Password")
    print("   - Use that password in .env")
    print("\n3. Run: python main.py")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    test_run()
