from flair.data import Sentence
from flair.models import SequenceTagger
import nltk
import re
import truecase
import spacy

nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)
nltk.download('maxent_ne_chunker', quiet=True)
nltk.download('words', quiet=True)

spacy.cli.download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")
tagger = SequenceTagger.load("flair/ner-english")


dicti = {}

def spacy_ano(string: str):
    """
    named entity recognition with spacy
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by spacy
    """
    text = nlp(string)
    for X in text.ents:
        # print(X.text, X.label_)
        dicti[X.text.lower()] = X.label_


def nltk_ano(string: str):
    """
    named entity recognition with nltk
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by nltk
    """
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(string))):
        if hasattr(chunk, 'label'):
            # print(chunk.label(), ' '.join(c[0] for c in chunk))
            label = chunk.label()
            lex = " ".join(c[0] for c in chunk)
            dicti[lex.lower()] = label


def flair_ano(string: str):
    """
    named entity recognition with flair
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by flair
    """
    sentence = Sentence(string)
    tagger.predict(sentence)
    for entity in sentence.get_spans('ner'):
        dicti[entity.text.lower()] = entity.get_label("ner").value

def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

def read_company_thesaurus(thesaurus : str):
    """
    fuction to construct dictionary with company names
    :param thesaurus: path to thesaurus file with company names
    :return: dictionary
    """
    temp_dict = {}
    with open(thesaurus) as thesaurus_file:
        for line in thesaurus_file.readlines():
            dicti[line.replace('\n', '').lower()]="COMP"


def main_ano(string: str, thesaurus: str):
    """
    main function for initialising named entity recognition
    :param string: string used to extract the named entities
    :param thesaurus: path to company names
    :return: dictionary with all NEs
    """

    read_company_thesaurus(thesaurus)

    m = re.search(r'\w+$', string)
    if m is not None:
        string = string+"."

    string = truecase.get_true_case(string)
    string_variance = [string]
    for sent in string_variance:
        spacy_ano(sent)
        nltk_ano(sent)
        flair_ano(sent)

    lowerstring = string.lower()

    for key in dicti:
        lowerstring = lowerstring.replace(key, dicti[key])
    return lowerstring
