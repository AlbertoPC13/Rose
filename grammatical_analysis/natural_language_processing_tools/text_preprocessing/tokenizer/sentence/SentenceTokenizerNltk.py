from .SentenceTokenizer import SentenceTokenizer
import nltk
from nltk import sent_tokenize


class SentenceTokenizerNltk(SentenceTokenizer):
    def __init__(self):
        nltk.download('punkt')

    def tokenize_text_by_sentences(self, text: str) -> list[str]:
        tokenized_sentences = sent_tokenize(text)
        return tokenized_sentences
