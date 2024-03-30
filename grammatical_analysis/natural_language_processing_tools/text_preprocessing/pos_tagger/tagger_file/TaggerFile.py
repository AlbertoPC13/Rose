from pickle import dump, load


class TaggerFile:
    @staticmethod
    def save_tagger(tagger, archivo):
        with open(archivo, 'wb') as file:
            dump(tagger, file, -1)

    @staticmethod
    def load_tagger(archivo):
        with open(archivo, 'rb') as file:
            tagger = load(file)
        return tagger
