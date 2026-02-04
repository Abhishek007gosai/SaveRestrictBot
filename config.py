"""
Save Restricted Content Bot Configuration

Developed by: LastPerson07Xcantarella
Telegram: @cantarellabots X @THEUPDATEDGUYS

Please retain this credit if you use or modify this project.
"""

import os


# ==============================
# Telegram Bot Credentials
# ==============================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = 29245477
API_HASH = "0abc83883262245c90ca337b7a0375c4"


# ==============================
# Admin Configuration
# ==============================

# Add admin user IDs separated by commas in environment variables
ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "8226767954").split(",") if admin]


# ==============================
# Database Configuration
# ==============================

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = "marin"


# ==============================
# Logging Configuration
# ==============================

# Replace with your Telegram log channel ID (example: -1001234567890)
LOG_CHANNEL = -1002456565415


# ==============================
# Error Handling
# ==============================

# Set to True to send error messages to users
ERROR_MESSAGE = os.environ.get("ERROR_MESSAGE", "True").lower() == "true"
