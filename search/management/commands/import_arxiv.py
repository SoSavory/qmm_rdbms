from django.core.management.base import BaseCommand

import xml.etree.ElementTree as ET
from django.db import models
from search.models import *

class Command(BaseCommand):
    def handle(self, **options):

        tree = ET.parse('search/xml_imports/arXivCM_17071705.xml')
        # tree = ET.parse('test.xml')
        root = tree.getroot()
        # print(root.tag)

        list_records = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')

        for record in list_records.iter('{http://www.openarchives.org/OAI/2.0/}record'):

            header = record.find('{http://www.openarchives.org/OAI/2.0/}header')
            arxiv_id = header.find('{http://www.openarchives.org/OAI/2.0/}identifier').text

            metadata = record.find('{http://www.openarchives.org/OAI/2.0/}metadata')
            arxiv_raw = metadata.find('{http://arxiv.org/OAI/arXivRaw/}arXivRaw')

            title = arxiv_raw.find('{http://arxiv.org/OAI/arXivRaw/}title').text
            authors = arxiv_raw.find('{http://arxiv.org/OAI/arXivRaw/}authors').text
            abstract = arxiv_raw.find('{http://arxiv.org/OAI/arXivRaw/}abstract').text

            arxiv_xml = ArxivXML(arxiv_id=arxiv_id, title=title, authors=authors, abstract=abstract)
            arxiv_xml.save()
