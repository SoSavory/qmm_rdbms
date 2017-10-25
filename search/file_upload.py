import xml.etree.ElementTree as ET
from django.db import models
from .models import ArxivXML, UserArxivXML, User

def handle_uploaded_arxiv_xml(f, user_id):
    tree = ET.parse(f)
    root = tree.getroot()
    # print(root.tag)


    list_records = root.find('{http://www.openarchives.org/OAI/2.0/}ListRecords')

    for record in list_records.iter('{http://www.openarchives.org/OAI/2.0/}record'):

        header = record.find('{http://www.openarchives.org/OAI/2.0/}header')
        arxiv_id = header.find('{http://www.openarchives.org/OAI/2.0/}identifier').text

        if not ArxivXML.objects.filter(arxiv_id= arxiv_id).exists():

            metadata = record.find('{http://www.openarchives.org/OAI/2.0/}metadata')
            arxiv_raw = metadata.find('{http://arxiv.org/OAI/arXivRaw/}arXivRaw')

            title = arxiv_raw.find('{http://arxiv.org/OAI/arXivRaw/}title').text
            authors = arxiv_raw.find('{http://arxiv.org/OAI/arXivRaw/}authors').text
            abstract = arxiv_raw.find('{http://arxiv.org/OAI/arXivRaw/}abstract').text

            arxiv_xml = ArxivXML(arxiv_id=arxiv_id,
                                 title=title,
                                 authors=authors,
                                 abstract=abstract)
            arxiv_xml.save()

        else:
            arxiv_xml = ArxivXML.objects.filter(arxiv_id= arxiv_id)[0]

        if not UserArxivXML.objects.filter(arxiv_xml = arxiv_xml).filter(user = user_id).exists():
            user_arxiv_xml = UserArxivXML(user__id = user_id, arxiv_xml = arxiv_xml)
            user_arxiv_xml.save()
