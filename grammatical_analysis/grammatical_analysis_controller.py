from flask import Blueprint, jsonify, Response, request
from .grammatical_analysis_service import GrammaticalAnalysisService
from .natural_language_processing_tools.text_preprocessing.pos_tagger.tagger_file.TaggerFile import TaggerFile
from .natural_language_processing_tools.text_preprocessing.tokenizer.sentence.SentenceTokenizerNltk import SentenceTokenizerNltk
from .natural_language_processing_tools.text_preprocessing.tokenizer.word.WordTokenizerNltk import WordTokenizerNltk
from .natural_language_processing_tools.text_preprocessing.pos_tagger.POS_tagger_nltk import POSTaggerNltk
from .natural_language_processing_tools.token_processor.GrammarAnalyzerOpenai import GrammarAnalyzerOpenai
from http import HTTPStatus

grammatical_analysis_api = Blueprint('grammatical_analysis_api', __name__)
trained_tagger_from_file = TaggerFile.load_tagger('grammatical_analysis/natural_language_processing_tools'
                                                  '/text_preprocessing/pos_tagger/tagger_file/'
                                                  'universal_tagger_default_regex_sents.pkl')
sentence_tokenizer = SentenceTokenizerNltk()
word_tokenizer = WordTokenizerNltk()
pos_tagger = POSTaggerNltk(trained_tagger_from_file)
grammatical_analyzer = GrammarAnalyzerOpenai()


@grammatical_analysis_api.route('', methods=['POST'])
def analyze_grammar() -> tuple[Response, int]:
    if request.is_json:
        data = request.get_json()
        text = data.get('text')
        if text:
            service = GrammaticalAnalysisService(sentence_tokenizer, word_tokenizer, pos_tagger, grammatical_analyzer)
            result = service.analyze_text_grammatically(text)
            return jsonify(result), HTTPStatus.OK
        else:
            return jsonify(
                {'error': 'The "text" field is required on the body of the request'}), HTTPStatus.BAD_REQUEST
    else:
        return jsonify({'error': 'The request must be on JSON format'}), HTTPStatus.BAD_REQUEST
