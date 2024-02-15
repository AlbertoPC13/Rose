from flask import Blueprint, jsonify
from .grammatical_analysis_service import GrammaticalAnalysisService

grammatical_analysis_api = Blueprint('grammatical_analysis_api', __name__)

@grammatical_analysis_api.route('/<text>', methods=['GET'])
def analyze_grammar(text):
    service = GrammaticalAnalysisService()
    result = service.analyze_text_grammatically(text)
    return jsonify(result), 200