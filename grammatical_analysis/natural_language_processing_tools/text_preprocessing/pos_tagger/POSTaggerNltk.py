import nltk
from .POSTagger import POSTagger


class POSTaggerNltk(POSTagger):

    def __init__(self, tagger: nltk.UnigramTagger):
        self.tagger = tagger

    def tag_sentences_with_pos(self, tokenized_sentences: list[list[str]]) -> list[list[tuple[str, str]]]:
        tagged_sentences = [
            self.tagger.tag(sentence)
            for sentence in tokenized_sentences
        ]

        return tagged_sentences
