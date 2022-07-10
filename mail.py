#!/usr/bin/env python3

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import getpass
import smtplib
import ssl
import config


def load_companies_info():
    with open(config.COMPANIES_CSV) as file:
        reader = csv.DictReader(file)
        return list(reader)


def send_emails(email_address, password, companies, attachment_filename):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(config.HOST, config.PORT, context=context) as smtp:
        smtp.login(email_address, password)

        for company in companies:
            print(f'Sending email to {company["Email"]}')

            msg = MIMEMultipart()

            msg['Subject'] = config.EMAIL_SUBJECT.format(company_name=company['Company'])
            msg['From'] = email_address
            msg['To'] = company['Email']

            msg.attach(MIMEText(config.EMAIL_CONTENT.format(name=company['Name'])))

            with open(attachment_filename, 'rb') as file:
                attachment = MIMEApplication(file.read())

            attachment.add_header('content-disposition', 'attachment', filename=attachment_filename.name)
            msg.attach(attachment)

            smtp.send_message(msg)


def main():
    companies = load_companies_info()

    email_address = input('Email address: ')
    password = getpass.getpass()

    send_emails(email_address, password, companies, config.ATTACHMENT_FILENAME)


if __name__ == '__main__':
    main()
