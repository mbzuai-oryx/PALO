

def get_chatgpt_prompt_to_arabic(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Modern Standard Arabic translator. Please provide the translation of the provided English text into Modern Standard Arabic, ensuring to respect the right-to-left writing system of Arabic. Make sure all Nunnation is appropriately reflected in the translated text along with correct punctuation. Only output the Modern Standard Arabic translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to arabic: <{english_str}>. "
                "Only output the Arabic translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_chinese(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Chinese translator. Please provide the Chinese translation of the provided English text. Only output the Chinese translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to Chinese: <{english_str}>. "
                "Only output the Chinese translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_spanish(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Spanish translator. Please provide the Spanish translation of the provided English text. Only output the Spanish translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to Spanish: <{english_str}>. "
                "Only output the Spanish translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_hindi(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Hindi translator. Please provide the Hindi translation of the provided English text. Only output the Hindi translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to Hindi: <{english_str}>. "
                "Only output the Hindi translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_french(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to French translator. Please provide the French translation of the provided English text. Only output the French translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to French: <{english_str}>. "
                "Only output the French translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_german(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to German translator. Please provide the German translation of the provided English text. Only output the German translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to German: <{english_str}>. "
                "Only output the German translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_russian(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Russian translator. Please provide the Russian translation of the provided English text. Only output the Russian translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to Russian: <{english_str}>. "
                "Only output the Russian translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_urdu(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Urdu translator. Please provide the Urdu translation of the provided English text. Only output the Urdu translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to Urdu: <{english_str}>. "
                "Only output the Urdu translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_bengali(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Bengali translator. Please provide the Bengali translation of the provided English text. Only output the Bengali translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to Bengali: <{english_str}>. "
                "Only output the Bengali translation. Do not output anything else."
        }
    ]
    return messages


def get_chatgpt_prompt_japanese(english_str):
    messages = [
        {
            "role": "system",
            "content":
                "You are an English to Japanese translator. Please provide the Japanese translation of the provided English text. Only output the Japanese translation."
        },
        {
            "role": "user",
            "content":
                f"Translate the English phrase/word enclosed in <> to Japanese: <{english_str}>. "
                "Only output the Japanese translation. Do not output anything else."
        }
    ]
    return messages
