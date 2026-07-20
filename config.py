import os

# Website URL
URL = "https://books.toscrape.com/"

# Price Alert
PRICE_LIMIT = 30

# Email Configuration
# Set these in your terminal before running the script:
#   $env:GMAIL_EMAIL="your@gmail.com"
#   $env:GMAIL_APP_PASSWORD="your-16-char-app-password"
#   $env:GMAIL_RECEIVER="recipient@gmail.com"
EMAIL = os.getenv("supremekingzh@gmail.com", "")
PASSWORD = os.getenv("dxjo awxz isjy mxvp", "")
RECEIVER = os.getenv("may28avph@gmail.com", "")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587