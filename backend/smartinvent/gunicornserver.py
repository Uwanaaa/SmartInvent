from django.core.management import execute_from_command_line
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartinvent.settings')

if __name__ == '__main__':
    execute_from_command_line(['gunicorn', '--certificate', '/Users/emmanueludofia/cert.pem', '--key', '/Users/emmanueludofia/key.pem'])