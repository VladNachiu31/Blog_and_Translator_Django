from googletrans import Translator


def transalte(text):
    transaltor = Translator()
    translation = transaltor.translate(text=text, dest='de')
    return translation.text
