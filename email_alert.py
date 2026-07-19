import smtplib

from config import (
    EMAIL,
    PASSWORD,
    RECEIVER,
    SMTP_SERVER,
    SMTP_PORT
)


def send_email(book):
    if not EMAIL or not PASSWORD or not RECEIVER:
        raise RuntimeError(
            "Email settings are incomplete. Set GMAIL_EMAIL, GMAIL_APP_PASSWORD, and GMAIL_RECEIVER environment variables."
        )

    subject = "Price Alert"

    body = f"""
Book Name : {book['Title']}

Price : {book['Price']}

Buy Now!
"""

    message = f"Subject:{subject}\n\n{body}"

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    try:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, RECEIVER, message)
        print("Email Sent")
    except smtplib.SMTPAuthenticationError as exc:
        raise RuntimeError(
            "Gmail authentication failed. Use a Google App Password for the Gmail account, not your normal account password."
        ) from exc
    finally:
        server.quit()