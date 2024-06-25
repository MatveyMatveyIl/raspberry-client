from django.core.management.base import BaseCommand

from app.internal.daemon.daemons import Daemons


class Command(BaseCommand):
    def handle(self, *args, **options):
        daemons = Daemons()
        daemons.start_daemons()
