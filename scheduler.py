#!/usr/bin/env python3
"""
Scheduler for running the bot automatically
"""

import schedule
import time
from main import main

def run_bot():
    """Run the bot"""
    print("\n" + "="*60)
    print("🤖 Scheduled Bot Run Starting")
    print("="*60 + "\n")
    main()

# Schedule the bot to run daily at 9 AM
schedule.every().day.at("09:00").do(run_bot)

# Or run every 6 hours
# schedule.every(6).hours.do(run_bot)

print("🤖 Client Hunter Bot Scheduler Started")
print("📅 Bot will run daily at 9:00 AM")
print("Press Ctrl+C to stop\n")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
