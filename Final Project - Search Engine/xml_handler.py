import string
import xml.sax

from stemming.porter2 import stem


class XmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.dicts = []
        self.current_dict = {}
        self.isDateline = False

    def startElement(self, name, attrs):
        self.isDateline = False
        if name == 'DATELINE':
            self.isDateline = True
        elif name == 'DOC':
            for (k, v) in attrs.items():
                if k == 'id':
                    self.current_dict = {'id': v, 'words': {}}

    def endElement(self, name):
        if name == "DOC":
            self.dicts.append(self.current_dict)

    def characters(self, content):
        # Strip punctuation from string:
        # http://stackoverflow.com/questions/23175809/typeerror-translate-takes-one-argument-2-given-python
        if not self.isDateline:
            for word in content.lower().split(' '):
                word = stem(word.translate(str.maketrans('', '', string.punctuation)).strip())
                if word != '':
                    if word not in self.current_dict['words']:
                        self.current_dict['words'][word] = 0
                    self.current_dict['words'][word] += 1
