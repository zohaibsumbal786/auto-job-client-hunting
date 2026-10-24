import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config
from datetime import datetime

class EmailSender:
    def __init__(self):
        self.smtp_server = config.SMTP_SERVER
        self.smtp_port = config.SMTP_PORT
        self.email = config.YOUR_EMAIL
        self.password = config.EMAIL_PASSWORD
    
    def send_proposal(self, to_email, subject, body, lead_info):
        """Send proposal email to potential client"""
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = f"{config.YOUR_NAME} <{self.email}>"
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Create plain text version
            text_part = MIMEText(body, 'plain')
            msg.attach(text_part)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            
            print(f"✅ Proposal sent to {to_email}")
            
            # Send notification to yourself
            self.send_notification(lead_info, to_email)
            
            return True
        except Exception as e:
            print(f"❌ Failed to send email to {to_email}: {e}")
            return False
    
    def send_notification(self, lead_info, sent_to):
        """Send notification to yourself about new lead contact"""
        try:
            subject = f"🎯 New Lead Contacted: {lead_info.get('company', 'Unknown')}"
            body = f"""
New lead has been contacted!

Company: {lead_info.get('company', 'N/A')}
Contact: {lead_info.get('name', 'N/A')}
Email: {sent_to}
Service: {lead_info.get('service_match', 'N/A')}
Source: {lead_info.get('source', 'N/A')}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Wait for their response or follow up in 3-5 days.

---
Client Hunter Bot
"""
            
            msg = MIMEText(body, 'plain')
            msg['From'] = self.email
            msg['To'] = config.NOTIFICATION_EMAIL
            msg['Subject'] = subject
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email, self.password)
                server.send_message(msg)
            
            print(f"📧 Notification sent to {config.NOTIFICATION_EMAIL}")
        except Exception as e:
            print(f"Failed to send notification: {e}")
    
    def test_connection(self):
        """Test email configuration"""
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.quit()
            print("✅ Email configuration is working!")
            return True
        except Exception as e:
            print(f"❌ Email configuration error: {e}")
            print(f"Email: {self.email}")
            print(f"Password length: {len(self.password) if self.password else 0}")
            return False
