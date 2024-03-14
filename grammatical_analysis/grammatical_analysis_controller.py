from flask import Blueprint, jsonify, Response
from .grammatical_analysis_service import GrammaticalAnalysisService
from .natural_language_processing_tools.text_preprocessing.tokenizer.Tokenizer_nltk import TokenizerNltk
from .natural_language_processing_tools.text_preprocessing.pos_tagger.POS_tagger_nltk import POSTaggerNltk
from .natural_language_processing_tools.token_processor.GrammarAnalyzerOpenai import GrammarAnalyzerOpenai
from http import HTTPStatus

grammatical_analysis_api = Blueprint('grammatical_analysis_api', __name__)

tokenizer = TokenizerNltk()
pos_tagger = POSTaggerNltk()
grammatical_analyzer = GrammarAnalyzerOpenai()


@grammatical_analysis_api.route('/<text>', methods=['GET'])
def analyze_grammar(text: str) -> tuple[Response, int]:
    service = GrammaticalAnalysisService(tokenizer, pos_tagger, grammatical_analyzer)
    result = service.analyze_text_grammatically(text)
    return jsonify(result), HTTPStatus.OK
