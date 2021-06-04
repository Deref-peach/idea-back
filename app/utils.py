from app.core.config import settings
from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP


def send_email(
    email_to: str,
    subject: str = "",
    template_path: str = "",
    environment = None,
):
    if environment is None:
        environment = {}

    email_from = settings.EMAIL
    message = MIMEMultipart()
    loader = FileSystemLoader(settings.TEMPLATES_DIR)
    env = Environment(loader=loader)
    template = env.get_template(template_path)
    msg = template.render(**environment)

    message['Subject'] = subject
    message['From'] = email_from
    message['To'] = email_to
    message.attach(MIMEText(msg, "html"))
    msgBody = message.as_string()

    server = SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    server.starttls()
    server.login(email_from, settings.EMAIL_PASSWORD)
    server.sendmail(email_from, email_to, msgBody)

    server.quit()

def send_new_account_email(email_to: str, username: str, link: str):
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    send_email(
        email_to=email_to,
        subject=subject,
        template_path='new_account.html',
        environment={
            "project_name": project_name,
            "username": username,
            "email": email_to,
            "link": link,
        },
    )

def send_del_account_email(email_to: str, username: str, link: str):
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Delete account for user {username}"
    send_email(
        email_to=email_to,
        subject=subject,
        template_path='del_account.html',
        environment={
            "project_name": project_name,
            "username": username,
            "email": email_to,
            "link": link,
        },
    )

def get_current_user():
    pass

def update_cls(dct: dict, cls):
    cls.__dict__.update(dct)
