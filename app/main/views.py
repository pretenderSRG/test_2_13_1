from flask import Blueprint

main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route('/')
def page_index():
    return f"<h1>Головна сторінка</h1>" \
           f"<h2><a href='/candidates'>Кандидати</a></h2>" \
           f"<h2><a href='/vacancies'>Вакансії</a></h2>" \
           f""
