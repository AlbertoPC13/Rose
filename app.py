from flask import Flask
from grammatical_analysis.grammatical_analysis_controller import grammatical_analysis_api
from dotenv import load_dotenv
import os

app = Flask(__name__)

if os.path.exists('.env'):
    load_dotenv()

app.register_blueprint(grammatical_analysis_api, url_prefix='/grammatical_analysis')

if __name__ == '__main__':
    app.run(debug=True)
