'''
Introduction to Python Programming (aka Programmierkurs I, aka Python I)
Software Assignment WS 2016/17
'''

import copy
import re
import string
from math import log

from stemming.porter2 import stem


class SearchEngine:
    def __init__(self, collectionName, create):
        '''
        Initialize the search engine, i.e. create or read in index. If
        create=True, the search index should be created and written to
        files. If create=False, the search index should be read from
        the files. The collectionName points to the filename of the
        document collection (without the .xml at the end). Hence, you
        can read the documents from <collectionName>.xml, and should
        write / read the idf index to / from <collectionName>.idf, and
        the tf index to / from <collectionName>.tf respectively. All
        of these files must reside in the same folder as THIS file. If
        your program does not adhere to this "interface
        specification", we will subtract some points as it will be
        impossible for us to test your program automatically!
        '''
        self.idf = {}
        self.tf = {}
        filename = '.'.join([collectionName, 'xml'])

        if create:
            print('Creating indices from file...')
            with open(filename, 'r') as toRead:
                dicts = []
                current_dict = {}
                isDateline = False
                for line in toRead:
                    if re.match('<.*>', line):
                        if re.match('<.*DATELINE>', line):
                            isDateline = True
                        else:
                            m = re.search('<DOC id="(.*)" type=".*".*>', line)
                            if m:
                                current_dict = {'id': m.group(1), 'words': {}}
                            elif re.match('</DOC>', line):
                                dicts.append(current_dict)
                            isDateline = False
                    else:
                        if not isDateline:
                            for word in line.split(' '):
                                # Strip punctuation from string:
                                # http://stackoverflow.com/questions/23175809/typeerror-translate-takes-one-argument-2-given-python
                                stemmed = self.stemmer(word)
                                if stemmed != '':
                                    if stemmed not in current_dict['words']:
                                        current_dict['words'][stemmed] = 0
                                    current_dict['words'][stemmed] += 1
                self.dicts = dicts

            self.idf = self.computeIdf(self.dicts)
            self.writeIdf(collectionName)

            self.tf = self.computeTf(self.dicts)
            self.writeTf(collectionName)
            print('Done.')
        else:
            print('Reading index from file...')
            self.readIdfFromFile(collectionName)
            self.readTfFromFile(collectionName)
            print('Done.')
        self.tf_idf = self.computeTfIdf(self.tf, self.idf)

    def stemmer(self, word):
        return stem(word.lower().translate(str.maketrans('', '', string.punctuation)).strip())

    def computeIdf(self, dicts):
        """
        Calculates the inverse document frequencies of a list of dictionaries.
        :param dicts: list of dictionaries where each has a dict 'words' where key = <WORD> and value = <WORD_FREQ>.
        :return: single dictionary with one calculated idf value per word.
        """
        num_docs = len(dicts)
        tokens = {}
        for current in dicts:
            for word in current['words']:
                if word not in tokens:
                    tokens[word] = 0
                tokens[word] += 1
        for token in tokens:
            tokens[token] = log(num_docs / tokens[token])
        return tokens

    def writeIdf(self, collectionName):
        with open('.'.join([collectionName, 'idf']), 'w') as idf_write:
            for key, value in sorted(self.idf.items()):
                idf_write.write('\t'.join([key, str(value)]) + '\n')

    def readIdfFromFile(self, collectionName):
        idf = {}
        with open('.'.join([collectionName, 'idf']), 'r') as idf_read:
            for line in idf_read:
                result = line.strip().split('\t')
                idf[result[0]] = float(result[1])
        self.idf = idf

    def computeTf(self, dicts):
        """
        Calculates the term frequencies per dictionary of a list of dictionaries.
        :param dicts: list of dictionaries where each has a dict 'words' where key = <WORD> and value = <WORD_FREQ>.
        :return: list of dictionaries with their calculated tf value per word.
        """
        terms = copy.deepcopy(dicts)
        for doc in terms:
            max_occurences = max(doc['words'].values())

            for word in doc['words']:
                doc['words'][word] = doc['words'][word] / max_occurences
        return terms

    def writeTf(self, collectionName):
        with open('.'.join([collectionName, 'tf']), 'w') as tf_write:
            for doc in self.tf:
                for key, value in sorted(doc['words'].items()):
                    tf_write.write('\t'.join([doc['id'], key, str(value)]) + '\n')

    def readTfFromFile(self, collectionName):
        tf = []
        current_dict = {}
        with open('.'.join([collectionName, 'tf']), 'r') as tf_read:
            for line in tf_read:
                id, word, value = line.strip().split('\t')
                exists = False
                for doc in reversed(tf):
                    if doc['id'] == id:
                        exists = True
                        current_dict = doc
                        break
                if exists:
                    current_dict['words'][word] = float(value)
                else:
                    current_dict = {'id': id, 'words': {word: float(value)}}
                    tf.append(current_dict)
        self.tf = tf

    def computeTfIdf(self, tf, idf):
        """
        Multiplies each dictionary in tf with idf and returns as a new list of dictionaries.
        :param tf: list of dictionaries where each has a dict 'words' where key = <WORD> and value = <TF_VALUE>.
        :param idf: dictionary where key = <WORD> and value = <IDF_VALUE>.
        :return: list of dictionaries the same structure as param tf, where each key's tf value is multiplied
            by its idf value. Products resulting in 0 are removed, as 0 is the same as not being present in the
            dictionary for cosine similarity.
        """
        tf_idf = copy.deepcopy(tf)
        for doc in tf_idf:
            toDelete = []
            for word in doc['words']:
                result = 0
                if word in idf:
                    result = doc['words'][word] * idf[word]
                if result == 0:
                    toDelete.append(word)
                else:
                    doc['words'][word] = doc['words'][word] * idf[word]
            for item in toDelete:
                del doc['words'][item]
        return tf_idf

    def convertListToQueryDoc(self, terms):
        query_dict = {}
        for word in terms:
            stemmed = self.stemmer(word)
            if stemmed != '':
                if stemmed not in query_dict:
                    query_dict[stemmed] = 0
                query_dict[stemmed] += 1
        return [{'id': 'query', 'words': query_dict}]

    def computeQueryVectorDoc(self, query_doc):
        tf_query = self.computeTf(query_doc)
        tfIdf_query = self.computeTfIdf(tf_query, self.idf)
        return tfIdf_query

    def norm(self, input_dict):
        """
        Returns the square root of the sum of the squares of the values in the input dictionary.
        :param input_dict: dictionary where key = <WORD> and value = <FLOAT>
        :return: single number of the calculated norm
        """
        result = 0
        for word in input_dict:
            result += input_dict[word] ** 2
        return result ** 0.5

    def executeQuery(self, queryTerms):
        '''
        Input to this function: List of query terms

        Returns the 10 highest ranked documents together with their
        tf.idf-sum scores, sorted score. For instance,

        [('NYT_ENG_19950101.0001', 0.07237004260325626),
         ('NYT_ENG_19950101.0022', 0.013039249597972629), ...]

        May be less than 10 documents if there aren't as many documents
        that contain the terms.
        '''
        query_doc = self.convertListToQueryDoc(queryTerms)
        tfIdf_query = self.computeQueryVectorDoc(query_doc)
        query_norm = self.norm(tfIdf_query[0]['words'])

        scores = []
        for doc in self.tf_idf:
            numerator = 0
            for key in tfIdf_query[0]['words']:
                if key in doc['words']:
                    numerator += tfIdf_query[0]['words'][key] * doc['words'][key]
            denominator = self.norm(doc['words']) * query_norm
            if denominator != 0 and numerator != 0:
                scores.append((doc['id'], numerator / denominator))

        top_ten = []
        for pair in reversed(sorted(scores, key=lambda x: x[1])):
            if len(top_ten) == 10:
                break
            top_ten.append(pair)
        return top_ten

    def executeQueryConsole(self):
        '''
        When calling this, the interactive console should be started,
        ask for queries and display the search results, until the user
        simply hits enter.
        '''

        user_input = None
        while user_input != '':
            user_input = input('Please enter query, terms separated by whitespace: ')
            tokens = user_input.split(' ')

            noWhitespace = False
            for token in tokens:
                if token != '':
                    noWhitespace = True
                    break

            if noWhitespace:
                result = self.executeQuery(tokens)
            else:
                result = []
            if user_input == '':
                print('Goodbye!')
            elif len(result) == 0:
                print('Sorry, I didn’t find any documents for this term.')
            else:
                print('I found the following documents:')
                for pair in result:
                    print(pair[0], str(pair[1]).join(['(', ')']))


if __name__ == '__main__':
    '''
    write your code here:
    * load index / start search engine
    * start the loop asking for query terms
    * program should quit if users enters no term and simply hits enter
    '''
    # Example for how we might test your program:
    # Should also work with nyt199501 !
    searchEngine = SearchEngine("nytsmall", create=False)
    # print(searchEngine.executeQuery(['hurricane', 'philadelphia']))
    searchEngine.executeQueryConsole()
