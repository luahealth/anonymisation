import en_core_web_lg
import re
from flair.data import Sentence
from flair.models import SequenceTagger
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nlp = en_core_web_lg.load()
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
        dicti[X.text] = X.label_


def nltk_ano(string: str):
    """
    named entity recognition with nltk
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by nltk
    """
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(string))):
        if hasattr(chunk, 'label'):
            label = chunk.label()
            lex = " ".join(c[0] for c in chunk)
            dicti[lex] = label


def flair_ano(string: str):
    """
    named entity recognition with flair
    :param string: string used to extract the named entities
    :return: populating dictionary with NEs extracted by flair
    """
    sentence = Sentence(string)
    tagger.predict(sentence)
    for entity in sentence.get_spans('ner'):
        dicti[entity.text] = entity.get_label("ner").value


def main_ano(string: str):
    """
    main function for initialising named entity recognition
    :param string: string used to extract the named entities
    :return: dictionary with all NEs
    """
    string_variance = [string, string.upper(), string.lower()]

    for sent in string_variance:
        spacy_ano(sent)
        nltk_ano(sent)
        flair_ano(sent)

    for key in dicti:
        compiled = re.compile(re.escape(key), re.IGNORECASE)
        string = compiled.sub(dicti[key], string)

    return string
