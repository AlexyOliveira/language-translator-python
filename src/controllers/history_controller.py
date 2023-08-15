from models.history_model import HistoryModel
from flask import Blueprint, jsonify

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history_list():
    history_entries = HistoryModel.list_as_json()
    return jsonify(history_entries) if history_entries else jsonify([])
