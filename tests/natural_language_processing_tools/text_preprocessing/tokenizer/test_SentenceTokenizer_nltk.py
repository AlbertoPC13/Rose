import pytest

from grammatical_analysis.natural_language_processing_tools.text_preprocessing.tokenizer.sentence.SentenceTokenizerNltk import \
    SentenceTokenizerNltk


class TestSentenceTokenizerNltk:

    @pytest.fixture
    def sentence_tokenizer_nltk(self):
        return SentenceTokenizerNltk()

    @pytest.mark.word_tokenizer_nltk
    def test_tokenize_text_by_sentences(self, sentence_tokenizer_nltk):
        text = "El patito blanco sonrió feliz a su nueva familia, pero su familia no le devolvió la sonrisa. Mamá Pata estaba muy confundida."
        tokenized_sentences = sentence_tokenizer_nltk.tokenize_text_by_sentences(text)
        expected_sentences = [
            "El patito blanco sonrió feliz a su nueva familia, pero su familia no le devolvió la sonrisa.",
            "Mamá Pata estaba muy confundida."]
        print(tokenized_sentences)
        assert tokenized_sentences == expected_sentences
