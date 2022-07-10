from pathlib import Path

# Email server settings
HOST = 'zimbra-recovery.step.polymtl.ca'
PORT = 465

# CSV containing company names and emails
COMPANIES_CSV = Path('companies.csv')

# Attachment to include in emails
ATTACHMENT_FILENAME = Path('attachment.pdf')

# Email
EMAIL_SUBJECT = 'Plan de visibilité - {company_name}'
EMAIL_CONTENT = (
    'Bonjour {name},\n\n'
    'Voici notre plan de visibilité.\n\n'
    'Éloïse Brosseau\n'
    'VP-Externe, CEGInfo'
)
