from .NLP import NLP
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import cess_esp
from openai import OpenAI
import os


class NLP_nltk_openai(NLP):
    def __init__(self):
        nltk.download('cess_esp')
        nltk.download('punkt')
        print("Se ha creado una instancia de NLP_nltk_openai")

    def tokenize_sentences(self, text_to_analyze):
        sentences = sent_tokenize(text_to_analyze)
        return sentences

    def tag_sentences_with_pos(self, tokenized_sentences):
        unigramTagger = self.get_tagger()
        tagged_sentences = [
            unigramTagger.tag(nltk.word_tokenize(sentence))
            for sentence in tokenized_sentences
        ]
        return tagged_sentences

    def tagged_sentences_to_string(self, tagged_sentences):
        tagged_sentences_strings = []
        for tagged_sentence in tagged_sentences:
            sentence_string = " ".join([f"{word}/{tag}" for word, tag in tagged_sentence])
            tagged_sentences_strings.append(sentence_string)
        return "\n".join(tagged_sentences_strings)

    def anlyze_text_with_gpt(self, pos_tagged_sentences):
        prompt = self.tagged_sentences_to_string(pos_tagged_sentences)
        openai_key = os.environ.get('OPENAI_API_KEY')
        client = OpenAI(api_key=openai_key)
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "Analiza la oración que el usuario proporcionará con etiquetas POS en términos de su estructura gramatical. El análisis debe estar adaptado al nivel A1 en español mexicano, identificando posibles errores sintácticos o semánticos. Proporciona una explicación sencilla en español, como si estuvieras enseñando a un estudiante de este nivel. El resultado hazlo en JSON",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        response = completion.choices[0].message.content

        return response

    def get_tagger(self, default_tagger="None"):
               
        patterns = [
            (r".*é$", "v"),  # verbo pasado
            (r".*ó$", "v"),  # verbo pasado
            (r".*rán$", "v"),  # verbo pasado
            (r".*ando$", "v"),  # gerundio
            (r".*iendo$", "v"),  # gerundio
            (r".*endo$", "v"),  # gerundio
            (r".*osa$", "a"),  # adjetivo
            (r".*oso$", "a"),  # adjetivo
            (r".*o$", "n"),  # noun masculine singular
            (r".*os$", "n"),  # noun masculine plural
            (r".*a$", "n"),  # noun femenine singular
            (r".*as$", "n"),  # noun femenine plural
        ]

        default = nltk.DefaultTagger(default_tagger)

        sentencesTagged = []
        for (
            sentence
        ) in (
            cess_esp.tagged_sents()
        ):  # obtenemos de las etiquetas solo la primera letra
            sentencesTagged.append([(word, tag) for (word, tag) in sentence])

        regexTagger = nltk.RegexpTagger(patterns, backoff=default)
        unigramTagger = nltk.UnigramTagger(sentencesTagged, backoff=regexTagger)

        return unigramTagger


# # Main for testing
# if __name__ == "__main__":
#     nltk.download('cess_esp')
#     nltk.download('universal_tagset')
#     nlp = NLP_nltk_openai()
#     text = "El gato come pescado."
#     tokenized_sentences = nlp.tokenize_sentences(text)
#     print(tokenized_sentences)
#     tagged_sentences = nlp.tag_sentences_with_pos(tokenized_sentences)
#     print(tagged_sentences)
