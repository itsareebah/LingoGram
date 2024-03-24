# lingua.py
from .generateText import generateText

command_data = {
    "name": "lingua",
    "description": "This tool assists you in improving your English writing and phrasing skills."
}

def execute(tone, text):
    generated_text_res = generateText(text, tone)
    if generated_text_res:
        return generated_text_res['text']  # Assuming generate_text returns a dictionary with a 'text' key
    else:
        return "Sorry could not generate text"

