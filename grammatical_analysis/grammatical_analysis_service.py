from grammatical_analysis.natural_language_processing_tools.text_preprocessing.tokenizer.Tokenizer import Tokenizer
from grammatical_analysis.natural_language_processing_tools.text_preprocessing.pos_tagger.POSTagger import POSTagger
from grammatical_analysis.natural_language_processing_tools.token_processor.GrammarAnalyzer import GrammarAnalyzer


class GrammaticalAnalysisService:
    def __init__(self, tokenizer: Tokenizer, pos_tagger: POSTagger, grammar_analyzer: GrammarAnalyzer):
        self.tokenizer = tokenizer
        self.pos_tagger = pos_tagger
        self.grammar_analyzer = grammar_analyzer

    def analyze_text_grammatically(self, text_to_analyze: str) -> str:
        tokenized_sentences = self.tokenizer.tokenize_text_by_sentences(text_to_analyze)
        pos_tagged_sentences = self.pos_tagger.tag_sentences_with_pos(tokenized_sentences)
        analyzed_text = self.grammar_analyzer.analyze_grammar(pos_tagged_sentences)
        return analyzed_text
