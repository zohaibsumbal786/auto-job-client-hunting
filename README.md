# AI Client Hunter Bot 🤖

**Automated Lead Generation System for Tech Services & Freelancers**

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Powered-00DFA2?style=for-the-badge)
![Automation](https://img.shields.io/badge/Automation-FF6B35?style=for-the-badge)

</div>

---

## 📋 Overview

**AI Client Hunter Bot** is an intelligent automation tool designed for freelancers and tech service providers. It automatically discovers potential clients, generates personalized proposals using AI, and manages email outreach campaigns—saving hours of manual work daily.

Perfect for:
- Web Developers
- AI/ML Engineers
- Data Scientists
- Software Consultants
- Freelance Tech Professionals

---

## ✨ Key Features

### 🔍 **Intelligent Lead Discovery**
- Automatically scans platforms like Upwork, Freelancer, and other job boards
- Filters opportunities based on your service offerings
- Identifies high-quality leads matching your expertise
- Tracks new postings in real-time

### 📝 **AI-Powered Proposal Generation**
- Generates personalized proposals for each opportunity
- Adapts tone and content based on client requirements
- Includes relevant experience and portfolio links
- Maintains professional formatting

### 📧 **Automated Email Outreach**
- Sends personalized outreach emails automatically
- Manages email templates and customization
- Handles scheduling to avoid spam filters
- Tracks sent emails and delivery status

### 📊 **Lead Management & Tracking**
- SQLite database for storing leads and proposals
- Response tracking and follow-up management
- Lead scoring based on match quality
- Historical data for analytics

### 🔔 **Real-Time Notifications**
- Email alerts for new high-quality opportunities
- Response notifications from potential clients
- Daily summary reports
- Error and status notifications

---

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **SQLite** - Local database for lead management
- **SMTP** - Email sending automation
- **Web Scraping** - Lead discovery (BeautifulSoup/Selenium)
- **Natural Language Processing** - Proposal generation
- **Scheduling** - Automated task execution

---

## 💻 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Email account with SMTP access (Gmail, Outlook, etc.)
- Active accounts on freelancing platforms

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/zohaibsumbal786/auto-job-client-hunting.git
   cd auto-job-client-hunting
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` with your credentials:
   ```env
   # Email Configuration
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   EMAIL_ADDRESS=your.email@gmail.com
   EMAIL_PASSWORD=your_app_password
   
   # Platform Credentials (if needed)
   UPWORK_USERNAME=your_username
   UPWORK_PASSWORD=your_password
   
   # Notification Email
   NOTIFICATION_EMAIL=your.notification@email.com
   
   # Services & Keywords
   SERVICES=Web Development,AI Solutions,Machine Learning,Data Science
   KEYWORDS=python,django,react,machine learning,data analysis
   ```

4. **Configure your profile**
   
   Edit `config.py` to customize:
   - Your name and contact information
   - Service descriptions
   - Portfolio links
   - Pricing ranges
   - Proposal templates

5. **Test email functionality**
   ```bash
   python test_email.py
   ```

6. **Run a test search**
   ```bash
   python test_run.py
   ```

---

## 🔄 Usage

### Running the Bot

**Single execution:**
```bash
python main.py
```

**Automated scheduling (recommended):**

The bot includes a built-in scheduler that runs periodically:

```bash
python scheduler.py
```

This will:
- Check for new opportunities every 30 minutes
- Send proposals to qualified leads
- Track responses and update database
- Send daily summary emails

### Customizing Search Criteria

Edit `config.py` to specify:

```python
SERVICES = [
    "Web Development",
    "AI & Machine Learning",
    "Data Science & Analytics",
    "Mobile App Development"
]

KEYWORDS = [
    "python", "django", "flask", "react",
    "machine learning", "deep learning",
    "data visualization", "API development"
]

EXPERIENCE_LEVEL = "intermediate"  # entry, intermediate, expert
MIN_BUDGET = 500  # Minimum project budget
MAX_PROPOSALS_PER_DAY = 10
```

### Managing Proposals

**View all leads:**
```python
python -c "from database import get_all_leads; print(get_all_leads())"
```

**Check proposal status:**
```python
python -c "from database import get_pending_proposals; print(get_pending_proposals())"
```

---

## 📁 Project Structure

```
auto-job-client-hunting/
│
├── main.py                  # Main entry point
├── lead_finder.py           # Lead discovery logic
├── proposal_generator.py    # AI proposal generation
├── email_sender.py          # Email automation
├── database.py              # Database operations
├── scheduler.py             # Automated scheduling
├── config.py                # Configuration settings
│
├── test_email.py            # Email testing script
├── test_run.py              # Test search functionality
│
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

---

## 🔧 Configuration Details

### Email Settings

**Gmail Users:**
1. Enable 2-factor authentication
2. Generate an [App Password](https://myaccount.google.com/apppasswords)
3. Use the app password in `.env` (not your regular password)

**Outlook/Office365:**
```env
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
```

### Proposal Templates

Customize proposal templates in `proposal_generator.py`:

```python
def generate_proposal(lead_details):
    template = f"""
    Hello {lead_details['client_name']},
    
    I noticed your project: {lead_details['title']}
    
    With {YOUR_EXPERIENCE} years of experience in {YOUR_SERVICES},
    I can help you {PROJECT_SOLUTION}.
    
    My approach:
    1. {STEP_1}
    2. {STEP_2}
    3. {STEP_3}
    
    Portfolio: {YOUR_PORTFOLIO_LINK}
    
    Best regards,
    {YOUR_NAME}
    """
    return template
```

---

## 📊 Database Schema

The SQLite database includes:

**leads** table:
- id (Primary Key)
- title
- description
- client_name
- budget
- posted_date
- platform (Upwork, Freelancer, etc.)
- url
- status (new, contacted, responded, rejected)
- created_at

**proposals** table:
- id (Primary Key)
- lead_id (Foreign Key)
- proposal_text
- sent_at
- response_received
- response_text

---

## 🚀 Advanced Features

### Email Throttling
Prevents spam detection:
```python
MAX_EMAILS_PER_HOUR = 10
DELAY_BETWEEN_EMAILS = 60  # seconds
```

### Response Detection
Automatically detects client responses:
```python
python -c "from email_sender import check_inbox; check_inbox()"
```

### Analytics
Track your success rate:
```python
from database import get_stats
stats = get_stats()
print(f"Total Leads: {stats['total_leads']}")
print(f"Proposals Sent: {stats['proposals_sent']}")
print(f"Response Rate: {stats['response_rate']}%")
```

---

## ⚠️ Important Notes

### Legal & Ethical Considerations

1. **Platform Terms of Service**: Ensure automation complies with platform ToS
2. **Rate Limiting**: Respect platform rate limits and API restrictions
3. **Personalization**: Always review auto-generated proposals before sending
4. **Data Privacy**: Securely store client information
5. **Spam Prevention**: Don't send duplicate or mass emails

### Best Practices

- ✅ Start with manual review mode
- ✅ Gradually increase automation as you refine templates
- ✅ Monitor response rates and adjust strategies
- ✅ Keep proposals genuine and personalized
- ✅ Follow up on promising leads manually

---

## 🔮 Future Enhancements

### Planned Features

1. **AI Improvements**
   - GPT integration for better proposal quality
   - Sentiment analysis for lead prioritization
   - Natural language understanding for client requirements

2. **Platform Expansion**
   - LinkedIn job postings
   - Indeed integration
   - Custom job board scraping

3. **Analytics Dashboard**
   - Web-based dashboard
   - Success rate visualization
   - ROI tracking
   - A/B testing for proposals

4. **CRM Integration**
   - Salesforce integration
   - HubSpot compatibility
   - Calendar scheduling

5. **Multi-Language Support**
   - Proposal generation in multiple languages
   - International platform support

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional platform integrations
- Better AI proposal generation
- UI/dashboard development
- Documentation improvements

---

## 📄 License

This project is for personal and educational use. Please review platform terms of service before deployment.

---

## 👤 Author

**Zohaib Ahmed Khan Sumbal**

- GitHub: [@zohaibsumbal786](https://github.com/zohaibsumbal786)
- LinkedIn: [Connect with me](#)

---

## 🙏 Acknowledgments

- Python community for excellent automation libraries
- Freelancing platforms for opportunities
- AI/ML tools for intelligent proposal generation

---

## 📞 Support

For issues or questions:
1. Check the `.env` configuration
2. Review email credentials and SMTP settings
3. Test with `test_email.py` and `test_run.py`
4. Open an issue on GitHub

---

<div align="center">

### 🎯 Automate your client hunting, focus on delivering great work!

*Built with passion for automation and efficiency*

</div>
