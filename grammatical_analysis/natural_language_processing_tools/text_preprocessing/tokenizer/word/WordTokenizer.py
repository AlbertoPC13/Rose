from abc import ABCMeta, abstractmethod


class WordTokenizer(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_sentence_by_word(self, text: list[str]) -> list:
        pass
