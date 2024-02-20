from abc import ABCMeta, abstractmethod


class NLP(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_sentences(self, sentences):
        pass

    @abstractmethod
    def tag_sentences_with_pos(self, tokenized_sentences):
        pass

    @abstractmethod
    def analyze_grammar(self, pos_tagged_sentences):
        pass
