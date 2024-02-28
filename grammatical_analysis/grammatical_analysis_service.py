from .natural_language_processing_tools.NLPNltkOpenai import NLPNltkOpenai


class GrammaticalAnalysisService:
    def __init__(self):
        self.nlp = NLPNltkOpenai()

    def analyze_text_grammatically(self, text_to_analyze: str) -> str:
        tokenized_sentences = self.nlp.tokenize_sentences(text_to_analyze)
        pos_tagged_sentences = self.nlp.tag_sentences_with_pos(tokenized_sentences)
        analyzed_text = self.nlp.analyze_grammar(pos_tagged_sentences)
        return analyzed_text
