#!/usr/bin/env python3
"""
AI Client Hunter Bot
Finds and contacts potential clients for your services
"""

import config
from lead_finder import LeadFinder
from proposal_generator import ProposalGenerator
from email_sender import EmailSender
from database import LeadDatabase
import time
import random

def main():
    print("🤖 AI Client Hunter Bot Starting...")
    print(f"Company: {config.COMPANY_NAME}")
    print(f"Website: {config.WEBSITE}")
    print(f"Contact: {config.YOUR_EMAIL}\n")
    
    # Initialize components
    lead_finder = LeadFinder()
    proposal_gen = ProposalGenerator()
    email_sender = EmailSender()
    database = LeadDatabase()
    
    # Test email configuration
    print("Testing email configuration...")
    if not email_sender.test_connection():
        print("\n⚠️  Email configuration failed. Please check your .env file.")
        print("Make sure you have:")
        print("1. YOUR_EMAIL set")
        print("2. EMAIL_PASSWORD set (use App Password for Gmail)")
        print("3. SMTP settings correct")
        return
    
    print("\n" + "="*50)
    print("Starting Lead Generation")
    print("="*50 + "\n")
    
    total_sent = 0
    
    # Process each service
    for service_key, service_info in config.SERVICES.items():
        print(f"\n🔍 Finding leads for: {service_info['name']}")
        
        # Find leads (using sample data for now)
        leads = lead_finder.get_sample_leads()
        
        # If you have API keys configured, uncomment this:
        # leads = lead_finder.find_leads(service_key, limit=5)
        
        if not leads:
            print(f"No leads found for {service_info['name']}")
            continue
        
        print(f"Found {len(leads)} potential leads")
        
        # Process each lead
        for lead in leads:
            # Skip if already contacted
            if database.is_already_contacted(lead['email']):
                print(f"⏭️  Skipping {lead['email']} (already contacted)")
                continue
            
            # Add to database
            database.add_lead(lead, status='pending')
            
            # Generate proposal
            print(f"\n📝 Generating proposal for {lead.get('company', 'Unknown')}")
            proposal = proposal_gen.generate_proposal(lead, service_key)
            email_body = proposal_gen.create_email_body(proposal, lead)
            
            # Create subject line
            subject = f"Partnership Opportunity: {service_info['name']} for {lead.get('company', 'Your Business')}"
            
            # Send email
            print(f"📤 Sending proposal to {lead['email']}")
            if email_sender.send_proposal(lead['email'], subject, email_body, lead):
                database.mark_contacted(lead['email'])
                total_sent += 1
                
                # Rate limiting - wait between emails
                wait_time = random.randint(30, 60)
                print(f"⏳ Waiting {wait_time} seconds before next email...")
                time.sleep(wait_time)
            
            # Daily limit check
            if total_sent >= config.MAX_LEADS_PER_DAY:
                print(f"\n⚠️  Daily limit reached ({config.MAX_LEADS_PER_DAY} emails)")
                break
        
        if total_sent >= config.MAX_LEADS_PER_DAY:
            break
    
    # Show statistics
    print("\n" + "="*50)
    print("Campaign Summary")
    print("="*50)
    stats = database.get_stats()
    print(f"📊 Emails sent today: {total_sent}")
    print(f"📊 Total contacted: {stats['contacted']}")
    print(f"📊 Pending leads: {stats['pending']}")
    print(f"📊 Responses received: {stats['responded']}")
    print("\n✅ Bot execution completed!")
    print(f"Check your email ({config.NOTIFICATION_EMAIL}) for notifications.\n")

if __name__ == "__main__":
    main()
