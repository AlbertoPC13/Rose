import pytest

from grammatical_analysis.natural_language_processing_tools.text_preprocessing.pos_tagger.POS_tagger_nltk import \
    POSTaggerNltk


class TestPOSTaggerNltk:

    @pytest.fixture
    def pos_tagger_nltk(self):
        return POSTaggerNltk()


    @pytest.mark.pos_tagger_nltk
    def test_tag_sentences_with_pos(self, pos_tagger_nltk):
        # Given
        sentences = ["La princesa juega hoy", "El valiente caballero lucha contra el dragón"]
        # When
        tagged_sentences = pos_tagger_nltk.tag_sentences_with_pos(sentences)
        # Then
        assert isinstance(tagged_sentences, list) and len(tagged_sentences) > 0
        assert isinstance(tagged_sentences[0][0],tuple)