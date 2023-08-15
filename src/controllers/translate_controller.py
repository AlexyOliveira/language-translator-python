from flask import Blueprint, render_template, request
from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        exemple_text = "O que deseja traduzir"
        exemple_translated = "Tradução"
        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate=exemple_text,
            translated=exemple_translated,
        )
    if request.method == "POST":
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        text = request.form.get("text-to-translate")
        translated_text = GoogleTranslator(
            source="auto", target=translate_to
        ).translate(text)

        return render_template(
            "index.html",
            languages=LanguageModel.list_dicts(),
            text_to_translate=text,
            translated=translated_text,
            translate_from=translate_from,
            translate_to=translate_to,
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    text = request.form.get("text-to-translate")
    translated_text = GoogleTranslator(
        source="auto", target=translate_to or "en"
    ).translate(text)

    return render_template(
        "index.html",
        languages=LanguageModel.list_dicts(),
        text_to_translate=translated_text,
        translated=text,
        translate_from=translate_to or "en",
        translate_to=translate_from or "pt",
    )
