from grammatical_analysis.natural_language_processing_tools.text_preprocessing.tokenizer.sentence.SentenceTokenizer import SentenceTokenizer
from grammatical_analysis.natural_language_processing_tools.text_preprocessing.tokenizer.word.WordTokenizer import WordTokenizer
from grammatical_analysis.natural_language_processing_tools.text_preprocessing.pos_tagger.POSTagger import POSTagger
from grammatical_analysis.natural_language_processing_tools.token_processor.GrammarAnalyzer import GrammarAnalyzer


class GrammaticalAnalysisService:
    def __init__(self,
                 sentence_tokenizer: SentenceTokenizer,
                 word_tokenizer: WordTokenizer,
                 pos_tagger: POSTagger,
                 grammar_analyzer: GrammarAnalyzer):
        self.sentence_tokenizer = sentence_tokenizer
        self.word_tokenizer = word_tokenizer
        self.pos_tagger = pos_tagger
        self.grammar_analyzer = grammar_analyzer

    def analyze_text_grammatically(self, text_to_analyze: str) -> str:
        tokenized_sentences = self.sentence_tokenizer.tokenize_text_by_sentences(text_to_analyze)
        sentences_tokens = self.word_tokenizer.tokenize_sentence_by_word(tokenized_sentences)
        pos_tagged_sentences = self.pos_tagger.tag_sentences_with_pos(sentences_tokens)
        analyzed_text = self.grammar_analyzer.analyze_grammar(pos_tagged_sentences)
        return analyzed_text
