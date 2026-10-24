import os
from dotenv import load_dotenv

load_dotenv()

# Business Configuration
YOUR_EMAIL = os.getenv('YOUR_EMAIL')
YOUR_CONTACT_NUMBER = os.getenv('YOUR_CONTACT_NUMBER')
YOUR_NAME = os.getenv('YOUR_NAME', 'GoatNova Team')
COMPANY_NAME = os.getenv('COMPANY_NAME', 'GoatNova')
WEBSITE = os.getenv('WEBSITE', 'https://goatnova.online')

# Email Configuration
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL', YOUR_EMAIL)

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
LINKEDIN_ACCESS_TOKEN = os.getenv('LINKEDIN_ACCESS_TOKEN')
HUNTER_API_KEY = os.getenv('HUNTER_API_KEY')

# Services Offered
SERVICES = {
    'web_development': {
        'name': 'Web Development',
        'keywords': ['website', 'web app', 'frontend', 'backend', 'full stack', 'e-commerce'],
        'description': 'Custom web applications, responsive websites, and e-commerce solutions'
    },
    'ai': {
        'name': 'AI Solutions',
        'keywords': ['artificial intelligence', 'AI', 'chatbot', 'automation', 'NLP'],
        'description': 'AI-powered solutions, chatbots, and intelligent automation systems'
    },
    'machine_learning': {
        'name': 'Machine Learning',
        'keywords': ['machine learning', 'ML', 'predictive analytics', 'model training'],
        'description': 'Custom ML models, predictive analytics, and data-driven insights'
    },
    'data_science': {
        'name': 'Data Science',
        'keywords': ['data analysis', 'data science', 'analytics', 'visualization', 'insights'],
        'description': 'Data analysis, visualization, and business intelligence solutions'
    }
}

# Lead Search Configuration
SEARCH_PLATFORMS = ['linkedin', 'twitter', 'reddit']
MAX_LEADS_PER_DAY = 20
