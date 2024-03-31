from grammatical_analysis.natural_language_processing_tools.token_processor.GrammarAnalyzer import GrammarAnalyzer
from openai import OpenAI
import os


class GrammarAnalyzerOpenai(GrammarAnalyzer):
    def __init__(self):
        openai_key = os.environ.get('OPENAI_API_KEY')
        self.client = OpenAI(api_key=openai_key)
        with (open("grammatical_analysis/natural_language_processing_tools/token_processor/prompt.json", "r")
              as prompt_file):
            self.prompt_json = eval(prompt_file.read())

    def analyze_grammar(self, pos_tagged_sentences: list) -> str:
        text_to_analyze = self.tagged_sentences_to_string(pos_tagged_sentences)
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": self.prompt_json["role"],
                    "content": self.prompt_json["content"]
                }
                ,
                {
                    "role": "user",
                    "content": text_to_analyze,
                }
            ]
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
