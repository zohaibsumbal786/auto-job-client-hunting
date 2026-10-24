#!/usr/bin/env python3
"""Test email configuration"""

import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('YOUR_EMAIL')
password = os.getenv('EMAIL_PASSWORD')

print(f"Testing email: {email}")
print(f"Password length: {len(password) if password else 0} characters")
print(f"Password (masked): {'*' * len(password) if password else 'NOT SET'}")

try:
    print("\nConnecting to Gmail SMTP...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)  # Show debug info
    server.starttls()
    print("\nAttempting login...")
    server.login(email, password)
    print("\n✅ SUCCESS! Email configuration is working!")
    server.quit()
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\n📝 TROUBLESHOOTING:")
    print("1. Make sure 2-Factor Authentication is enabled on your Gmail")
    print("2. Generate a new App Password:")
    print("   - Go to: https://myaccount.google.com/apppasswords")
    print("   - Select 'Mail' and your device")
    print("   - Copy the 16-character password (no spaces)")
    print("3. Update EMAIL_PASSWORD in .env file")
    print("4. The password should be 16 characters, no spaces")
