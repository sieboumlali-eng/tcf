import os
import sys
import django
from django.db import connection

# Add project root to path
sys.path.append('/home/imad/Documents/Gift/exams')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def reset_db():
    print("Dropping database tables...")
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS revision_questionorale CASCADE;")
        cursor.execute("DROP TABLE IF EXISTS revision_examorale CASCADE;")
    print("Done. Tables dropped.")

if __name__ == "__main__":
    reset_db()
