from abc import ABCMeta, abstractmethod


class GrammarAnalyzer(metaclass=ABCMeta):
    @abstractmethod
    def analyze_grammar(self, pos_tagged_sentences: list) -> str:
        pass
