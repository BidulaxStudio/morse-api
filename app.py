from flask import Flask, request
from morse import text_to_morse, morse_to_text

app = Flask(__name__)


@app.route("/api/", methods=["GET"])
def morse_api():

    """
    :return: Text if 'morse' is filled. Morse if 'text' is filled. Affirmation if 'morse' and 'text' are filled.
    """

    text = request.args.get("text")
    morse = request.args.get("morse")

    if text and morse:
        text = text.upper()
        if text == morse_to_text(morse):
            return "% TEXT IS MORSE"
        else: return "% TEXT IS NOT MORSE"

    if text and not morse:
        text = text.upper()
        return text_to_morse(text)

    if not text and morse:
        return morse_to_text(morse)


if __name__ == '__main__':
    app.run()
