import os

from django.core import management
from django.core.management.base import BaseCommand

from tac.models import PopupContent


class Command(BaseCommand):

    def handle(self, *args, **options):
        if PopupContent.objects.all().count() > 0:
            print('nothing loaded: there is allready content')
            return
        file = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '..',
                '..',
                'fixtures',
                'tac.popupcontent.json',
            )
        )
        if os.path.isfile(file):
            management.call_command('loaddata', file, verbosity=0)
        else:
            print('fixture file missing')
        print('tac initial data imported')
