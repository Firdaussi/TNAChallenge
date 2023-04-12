
import requests
from http import HTTPStatus
from django.core.management.base import BaseCommand, CommandError
from challenge.models import TNARecord
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = "Fetch data from TNA API and store in database"
    urlbase = 'http://discovery.nationalarchives.gov.uk/API/records/v1/details/'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='The id of the TNA record')

    def handle(self, *args, **kwargs):
        id = kwargs['id']

        url = self.urlbase + id

        response = requests.get(url)

        if response.status_code == HTTPStatus.NO_CONTENT:
            self.stdout.write(f"I'm sorry - I didn't find anything for id [{id}]")

        elif response.status_code == HTTPStatus.OK:
            data = response.json()
            title       = data.get('title')
            citable     = data.get('citableReference')
            description = data.get('scopeContent', {}).get('description')

            tnarec = TNARecord(tna_id=id, title=title, description=description, citable=citable)

            try:
                tnarec.save(force_insert=True)
            except IntegrityError:
                self.stdout.write(f"The record with id [{id}] already exists in the database")

        else:
            self.stdout.write("Unexpected response {response.data_code}")
        