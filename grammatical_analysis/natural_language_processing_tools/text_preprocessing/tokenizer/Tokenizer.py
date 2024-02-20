from abc import ABCMeta, abstractmethod


class Tokenizer(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_text_by_sentences(self, text: str) -> list:
        pass
