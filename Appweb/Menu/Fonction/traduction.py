from deep_translator import GoogleTranslator
from langdetect import detect

def translate(description):

    lang = detect(description)

    if lang == 'en':
         return GoogleTranslator(source='en', target='fr').translate(description)
    elif lang == 'fr':
        return GoogleTranslator(source='fr', target='en').translate(description)
    else:
        return GoogleTranslator(source='auto', target='fr').translate(to_translate)

