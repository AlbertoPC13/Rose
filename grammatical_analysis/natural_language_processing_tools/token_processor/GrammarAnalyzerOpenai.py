from grammatical_analysis.natural_language_processing_tools.token_processor.GrammarAnalyzer import GrammarAnalyzer
from openai import OpenAI
import os


def tagged_sentences_to_string(tagged_sentences: list) -> str:
    tagged_sentences_strings = []
    for tagged_sentence in tagged_sentences:
        sentence_string = " ".join([f"{word}/{tag}" for word, tag in tagged_sentence])
        tagged_sentences_strings.append(sentence_string)
    return "\n".join(tagged_sentences_strings)


class GrammarAnalyzerOpenai(GrammarAnalyzer):
    def __init__(self):
        openai_key = os.environ.get('OPENAI_API_KEY')
        self.client = OpenAI(api_key=openai_key)

    def analyze_grammar(self, pos_tagged_sentences: list) -> str:
        text_to_analyze = tagged_sentences_to_string(pos_tagged_sentences)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Analiza la oración que el usuario proporcionará con etiquetas POS en términos de su estructura gramatical. El análisis debe estar adaptado al nivel A1 en español mexicano, identificando posibles errores sintácticos o semánticos. Proporciona una explicación sencilla en español, como si estuvieras enseñando a un estudiante de este nivel. El resultado hazlo en JSON",
                },
                {
                    "role": "user",
                    "content": text_to_analyze,
                },
            ],
        )

        response = completion.choices[0].message.content

        return response

    @staticmethod
    def tagged_sentences_to_string(tagged_sentences):
        tagged_sentences_strings = []
        for tagged_sentence in tagged_sentences:
            sentence_string = " ".join([f"{word}/{tag}" for word, tag in tagged_sentence])
            tagged_sentences_strings.append(sentence_string)
        return "\n".join(tagged_sentences_strings)
