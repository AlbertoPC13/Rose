from grammatical_analysis.natural_language_processing_tools.NLP_nltk_openai import NLP_nltk_openai

class GrammaticalAnalysisService:
    def __init__(self):
        print("Se ha creado una instancia de MiClase")

    def analyze_text_grammatically(self,text_to_analyze):
        nlp = NLP_nltk_openai()
        tokenized_sentences = nlp.tokenize_sentences(text_to_analyze)
        pos_tagged_sentences = nlp.tag_sentences_with_pos(tokenized_sentences)
        analyzed_text = nlp.anlyze_text_with_gpt(pos_tagged_sentences)
        return analyzed_text