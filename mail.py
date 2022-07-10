#!/usr/bin/env python3

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
import csv
import getpass
import smtplib
import ssl
import config


def load_companies_info():
    with open(config.COMPANIES_CSV) as file:
        reader = csv.DictReader(file)
        return list(reader)


def send_emails(email_address, password, companies, filename):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(config.HOST, config.PORT, context=context) as smtp:
        smtp.login(email_address, password)

        for company in companies:
            print(f'Email sent to {company["Email"]}')
            msg = MIMEMultipart()

            msg['Subject'] = config.EMAIL_SUBJECT.format(company_name=company['Company'])
            msg['To'] = company['Email']
            msg['From'] = email_address

            with open(filename, 'rb') as file:
                attachment = MIMEApplication(file.read())

            attachment.add_header('content-disposition', 'attachment', filename=filename.name)
            msg.attach(attachment)

            msg.attach(MIMEText(config.EMAIL_CONTENT.format(first_name=company['First Name'], last_name=company['Last Name'])))

            smtp.send_message(msg)


def main():
    companies_info = load_companies_info()

    email_address = input('Email address: ')
    password = getpass.getpass()
    filename = config.VISIBILITY_PLAN_PDF
    
    send_emails(email_address, password, companies_info, filename)


if __name__ == '__main__':
    main()
