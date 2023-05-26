from flask import Blueprint

main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route('/')
def page_index():
    return f"Головна сторінка"
