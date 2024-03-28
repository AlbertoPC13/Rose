from Tokenizer import Tokenizer
import nltk
from nltk import sent_tokenize


class TokenizerNltk(Tokenizer):
    def __init__(self):
        nltk.download('punkt')

    def tokenize_text_by_sentences(self, text: str) -> list:
        tokenized_sentences = sent_tokenize(text)
        return tokenized_sentences
