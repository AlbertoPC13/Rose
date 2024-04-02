import pytest

from grammatical_analysis.natural_language_processing_tools.text_preprocessing.tokenizer.word.WordTokenizerNltk import WordTokenizerNltk


class TestWordTokenizerNltk:

    @pytest.fixture
    def word_tokenizer_nltk(self):
        return WordTokenizerNltk()

    @pytest.mark.word_tokenizer_nltk
    def test_tokenize_sentence_by_word(self, word_tokenizer_nltk):
        sentences_tokens = ['El patito blanco sonrió feliz a su nueva familia, pero su familia no le devolvió la sonrisa.', 'Mamá Pata estaba muy confundida.']
        sentences_tokens = word_tokenizer_nltk.tokenize_sentence_by_word(sentences_tokens)
        expected_sentences = [['El', 'patito', 'blanco', 'sonrió', 'feliz', 'a', 'su', 'nueva', 'familia', ',', 'pero', 'su', 'familia', 'no', 'le', 'devolvió', 'la', 'sonrisa', '.'],
                              ['Mamá', 'Pata', 'estaba', 'muy', 'confundida', '.']]
        assert sentences_tokens == expected_sentences
