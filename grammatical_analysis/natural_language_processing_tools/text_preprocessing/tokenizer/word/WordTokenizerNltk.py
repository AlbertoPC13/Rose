from .WordTokenizer import WordTokenizer
import nltk
from nltk import sent_tokenize


class WordTokenizerNltk(WordTokenizer):
    def __init__(self):
        nltk.download('punkt')

    def tokenize_sentence_by_word(self, sentences: list[str]) -> list[list[str]]:
        tokenized_sentences = [
            nltk.word_tokenize(sentence)
            for sentence in sentences
        ]
        return tokenized_sentences
