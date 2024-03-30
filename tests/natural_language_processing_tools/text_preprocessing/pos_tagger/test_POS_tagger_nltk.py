import pytest

from grammatical_analysis.natural_language_processing_tools.text_preprocessing.pos_tagger.POS_tagger_nltk import \
    POSTaggerNltk
from grammatical_analysis.natural_language_processing_tools.text_preprocessing.pos_tagger.tagger_file.TaggerFile import \
    TaggerFile


class TestPOSTaggerNltk:

    @pytest.fixture
    def trained_tagger_from_file(self):
        return TaggerFile.load_tagger('../../../../grammatical_analysis/natural_language_processing_tools'
                                      '/text_preprocessing/pos_tagger/tagger_file'
                                      '/universal_tagger_default_regex_sents.pkl')

    @pytest.fixture
    def pos_tagger_nltk(self, trained_tagger_from_file):
        return POSTaggerNltk(trained_tagger_from_file)

    @pytest.mark.pos_tagger_nltk
    def test_tag_sentences_with_pos(self, pos_tagger_nltk):
        # Given
        sentences = ["La princesa juega hoy", "El valiente caballero lucha contra el dragón"]
        # When
        tagged_sentences = pos_tagger_nltk.tag_sentences_with_pos(sentences)
        # Then
        assert isinstance(tagged_sentences, list) and len(tagged_sentences) > 0
        assert isinstance(tagged_sentences[0][0], tuple)
