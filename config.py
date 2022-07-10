from pathlib import Path

COMPANIES_CSV = Path('Companies.csv')
VISIBILITY_PLAN_PDF = Path('Comité Informatique et Logiciel.pdf')
EMAIL_SUBJECT = 'Plan de visibilité - {company_name}'
EMAIL_CONTENT = ('Bonjour {first_name} {last_name},\n\n'
                'Voici notre plan de visibilité.\n\n'
                'Éloïse Brosseau\n'
                'VP-Externe, CEGInfo')
HOST = 'zimbra-recovery.step.polymtl.ca'
PORT = 465
