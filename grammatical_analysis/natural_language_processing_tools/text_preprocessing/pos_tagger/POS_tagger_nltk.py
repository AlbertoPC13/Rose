import nltk
from .POSTagger import POSTagger


class POSTaggerNltk(POSTagger):

    def __init__(self, tagger: nltk.UnigramTagger):
        self.tagger = tagger
        nltk.download('cess_esp')
        nltk.download('universal_tagset')

    def tag_sentences_with_pos(self, tokenized_sentences: list) -> list:
        tagged_sentences = [
            self.tagger.tag(nltk.word_tokenize(sentence))
            for sentence in tokenized_sentences
        ]
        return tagged_sentences
