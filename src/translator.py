import deepl
import os
from dotenv import load_dotenv

load_dotenv()

translator = deepl.Translator(os.getenv("DEEPL_API_KEY"))

def translate(text):

    try:
        result = translator.translate_text(
            text,
            source_lang="JA",
            target_lang="EN-US"
        )
        return result.text

    except:
        return text
