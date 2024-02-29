from .NLP import NLP
from .text_preprocessing.pos_tagger.POS_tagger_nltk import POSTaggerNltk
from .text_preprocessing.tokenizer.Tokenizer_nltk import TokenizerNltk
from .token_processor.GrammarAnalyzerOpenai import GrammarAnalyzerOpenai


class NLPNltkOpenai(NLP):
    def __init__(self):
        self.tokenizer = TokenizerNltk()
        self.pos_tagger = POSTaggerNltk()
        self.grammar = GrammarAnalyzerOpenai()
        pass

    def tokenize_sentences(self, text_to_analyze: str) -> list:
        tokenized_sentences = self.tokenizer.tokenize_text_by_sentences(text_to_analyze)
        return tokenized_sentences

    def tag_sentences_with_pos(self, tokenized_sentences: list) -> list:
        tagged_sentences = self.pos_tagger.tag_sentences_with_pos(tokenized_sentences)
        return tagged_sentences

    def analyze_grammar(self, pos_tagged_sentences: list) -> str:
        grammatical_analysis = self.grammar.analyze_grammar(pos_tagged_sentences)
        return grammatical_analysis
