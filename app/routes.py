from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/labels")
def labels():
    return render_template("label_maker.html")


@bp.route("/color-code")
def color_code():
    return render_template("color_code.html")
