from nltk import UnigramTagger

from .POSTagger import POSTagger
import nltk
from nltk.corpus import cess_esp


def get_tagger() -> UnigramTagger:
    patterns = [
        (r".*é$", "VBD"),  # past verb
        (r".*ó$", "VBD"),  # past verb
        (r".*rán$", "VBD"),  # past verb
        (r".*ando$", "VBG"),  # gerund
        (r".*iendo$", "VBG"),  # gerund
        (r".*endo$", "VBG"),  # gerund
        (r".*osa$", "ADJ"),  # adjective
        (r".*oso$", "ADJ"),  # adjective
        (r".*o$", "NOUN"),  # noun masculine singular
        (r".*os$", "NOUN"),  # noun masculine plural
        (r".*a$", "NOUN"),  # noun feminine singular
        (r".*as$", "NOUN"),  # noun feminine plural
    ]

    default_tagger = "NOUN"
    default = nltk.DefaultTagger(default_tagger)

    sentences_tagged = []
    for sentence in cess_esp.tagged_sents(tagset='universal_tagset'):
        sentences_tagged.append([(word, tag) for (word, tag) in sentence])

    regex_tagger = nltk.RegexpTagger(patterns, backoff=default)
    unigram_tagger = nltk.UnigramTagger(sentences_tagged, backoff=regex_tagger)

    return unigram_tagger


class POSTaggerNltk(POSTagger):
    def __init__(self):
        nltk.download('cess_esp')
        nltk.download('universal_tagset')
    
    def tag_sentences_with_pos(self, tokenized_sentences: list) -> list:
        unigram_tagger = get_tagger()
        tagged_sentences = [
            unigram_tagger.tag(nltk.word_tokenize(sentence))
            for sentence in tokenized_sentences
        ]
        return tagged_sentences
