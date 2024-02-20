from abc import ABCMeta, abstractmethod


class POSTagger(metaclass=ABCMeta):
    @abstractmethod
    def tag_sentences_with_pos(self, tokenized_sentences: list) -> list:
        pass
