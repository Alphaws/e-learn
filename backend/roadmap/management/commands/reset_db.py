from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import os
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Reset database in local and seed with initial data'
    def handle(self, *args, **kwargs):
        # delete db.sqlite3
        db_path = "db.sqlite3"
        if os.path.exists(db_path):
            os.remove(db_path)  # Deletes the db.sqlite3 file
            print(f"{db_path} has been deleted.")
        else:
            print(f"{db_path} does not exist.")
            exit(1)
        call_command('makemigrations', interactive=False)
        call_command(
            'migrate',
            interactive=False
        )
        #User.objects.create_superuser('admin', 'admin@example.com', 'pass')
        call_command('createsuperuser', username='alphaws', email='alphaws@gmail.com')
        call_command('seed')
