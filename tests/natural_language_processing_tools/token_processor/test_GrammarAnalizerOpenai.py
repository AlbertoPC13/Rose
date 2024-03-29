import pytest

from grammatical_analysis.natural_language_processing_tools.token_processor.GrammarAnalyzerOpenai import \
    GrammarAnalyzerOpenai
from dotenv import load_dotenv


class TestGrammarAnalyzerOpenai:

    @pytest.fixture
    def grammar_analyzer_openai(self):
        return GrammarAnalyzerOpenai()

    @pytest.fixture(autouse=True)
    def load_env_variables(self):
        load_dotenv()

    @pytest.mark.grammar_analyzer_openai
    def test_tagged_sentences_to_string(self, grammar_analyzer_openai):
        tagged_sentences = [
            [("El", "DET"), ("patito", "NOUN"), ("blanco", "ADJ"), ("sonrió", "VERB"), ("feliz", "ADJ"), ("a", "ADP"),
             ("su", "DET"), ("nueva", "ADJ"), ("familia", "NOUN"), (",", "PUNCT"), ("pero", "CCONJ"), ("su", "DET"),
             ("familia", "NOUN"), ("no", "PART"), ("le", "PRON"), ("devolvió", "VERB"), ("la", "DET"),
             ("sonrisa", "NOUN"), (".", "PUNCT")],
            [("Mamá", "NOUN"), ("Pata", "NOUN"), ("estaba", "AUX"), ("muy", "ADV"), ("confundida", "ADJ"),
             (".", "PUNCT")]
        ]
        response = grammar_analyzer_openai.tagged_sentences_to_string(tagged_sentences)
        expected_response = "El/DET patito/NOUN blanco/ADJ sonrió/VERB feliz/ADJ a/ADP su/DET nueva/ADJ familia/NOUN ,/PUNCT pero/CCONJ su/DET familia/NOUN no/PART le/PRON devolvió/VERB la/DET sonrisa/NOUN ./PUNCT\nMamá/NOUN Pata/NOUN estaba/AUX muy/ADV confundida/ADJ ./PUNCT"
        assert response == expected_response
