import pytest

from grammatical_analysis.natural_language_processing_tools.text_preprocessing.tokenizer.Tokenizer_nltk import \
    TokenizerNltk


class TestTokenizerNltk:

    @pytest.fixture
    def tokenizer_nltk(self):
        return TokenizerNltk()

    @pytest.mark.tokenizer_nltk
    def test_tokenize_text_by_sentences(self, tokenizer_nltk):
        text = "El patito blanco sonrió feliz a su nueva familia, pero su familia no le devolvió la sonrisa. Mamá Pata estaba muy confundida."
        tokenized_sentences = tokenizer_nltk.tokenize_text_by_sentences(text)
        expected_sentences= [
            "El patito blanco sonrió feliz a su nueva familia, pero su familia no le devolvió la sonrisa.",
            "Mamá Pata estaba muy confundida."]
        assert tokenized_sentences == expected_sentences
