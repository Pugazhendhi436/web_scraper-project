import smtplib

from config import (
    EMAIL,
    PASSWORD,
    RECEIVER,
    SMTP_SERVER,
    SMTP_PORT
)

from email.mime.text import MIMEText

# Set up variables
smtp_server = SMTP_SERVER  # Change to your provider
port = SMTP_PORT  # For starttls
sender_email = EMAIL
password = PASSWORD  # NOT your regular password
def send_email(book):
  

    # Create message
    msg = MIMEText(f"Book Name : {book['Title']}\nPrice : {book['Price']}\n\nBuy Now!")
    msg["Subject"] = "Price Alert"
    msg["From"] = sender_email
    msg["To"] = RECEIVER

    server = None

    try:
        # Connect and secure the connection
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Upgrade connection to secure TLS

        # Login and send
        server.login(sender_email, password)
        server.sendmail(sender_email, msg["To"], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if server is not None:
            server.quit()
#     if not EMAIL or not PASSWORD or not RECEIVER:
#         raise RuntimeError(
#             "Email settings are incomplete. Set GMAIL_EMAIL, GMAIL_APP_PASSWORD, and GMAIL_RECEIVER environment variables."
#         )

#     subject = "Price Alert"

#     body = f"""
# Book Name : {book['Title']}

# Price : {book['Price']}

# Buy Now!
# """

#     message = f"Subject:{subject}\n\n{body}"

#     server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

#     try:
#         server.starttls()
#         server.login(EMAIL, PASSWORD)
#         server.sendmail(EMAIL, RECEIVER, message)
#         print("Email Sent")
#     except smtplib.SMTPAuthenticationError as exc:
#         raise RuntimeError(
#             "Gmail authentication failed. Use a Google App Password for the Gmail account, not your normal account password."
#         ) from exc
#     finally:
#         server.quit()