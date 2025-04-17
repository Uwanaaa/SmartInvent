# import ssl
# from django.core.management.commands.runserver import Command as RunserverCommand

# class Command(RunserverCommand):
#     def inner_run(self, *args, **options):
#         super().inner_run(*args, **options)
#         self.httpd.socket = ssl.wrap_socket(
#             self.httpd.socket,
#             certfile='localhost.pem',
#             keyfile='localhost-key.pem',
#             server_side=True
#         )


from django.core.management import execute_from_command_line
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartinvent.settings')

if __name__ == '__main__':
    execute_from_command_line(['manage.py', 'runsslserver', '--certificate', '/Users/emmanueludofia/cert.pem', '--key', '/Users/emmanueludofia/key.pem'])
