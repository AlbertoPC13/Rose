import pytest

from grammatical_analysis.natural_language_processing_tools.text_preprocessing.pos_tagger.POSTaggerNltk import \
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
        sentences = [['El', 'patito', 'blanco', 'sonrió', 'feliz', 'a', 'su', 'nueva', 'familia', ',', 'pero', 'su', 'familia', 'no', 'le', 'devolvió', 'la', 'sonrisa', '.'],
                              ['Mamá', 'Pata', 'estaba', 'muy', 'confundida', '.']]
        # When
        tagged_sentences = pos_tagger_nltk.tag_sentences_with_pos(sentences)
        print(tagged_sentences)
        # Then
        assert isinstance(tagged_sentences, list) and len(tagged_sentences) > 0
        assert isinstance(tagged_sentences[0][0], tuple)
