from abc import ABCMeta, abstractmethod


class SentenceTokenizer(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_text_by_sentences(self, text: str) -> list[str]:
        pass
