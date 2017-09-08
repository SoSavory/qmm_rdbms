from adaptor.fields import *
from adaptor.model import XMLModel
import xml.etree.ElementTree
from .models import *


def importArxivXML():
    class ArxivXMLImporter(ArxivXML):
        root = XMLRootField(path="record")
        arxiv_id = XMLCharField(path="header/identifier")
        title = XMLCharField(path="metadata/arXivRaw/title")
        authors = XMLCharField(path="metadata/arXivRaw/authors")
        abstract = XMLTextField(path="metadata/arXivRaw/abstract")

    xml = xml.etree.ElementTree.parse('test.xml')
    ArxivXMLImporter.import_data(xml)
