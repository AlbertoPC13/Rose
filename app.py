from flask import Flask
from grammatical_analysis.grammatical_analysis_controller import grammatical_analysis_api

app = Flask(__name__)

# Registrar el blueprint del controlador gramatical_analysis
app.register_blueprint(grammatical_analysis_api, url_prefix='/grammatical_analysis')

if __name__ == '__main__':
    app.run(debug=True)