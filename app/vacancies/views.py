from flask import Blueprint, render_template
from app.vacancies.dao.vacancies_dao import VacanciesDAO


vacancies_blueprint = Blueprint("vacancies_blueprint", __name__, template_folder="templates", url_prefix='/vacancies')
vacancies_dao = VacanciesDAO("./data/vacancies.json")


@vacancies_blueprint.route('/')
def page_vacancies():
    vacancies = vacancies_dao.get_all()
    return render_template('vacancies_all.html', vacancies=vacancies)


@vacancies_blueprint.route('/<int:pk>')
def page_vacancy(pk):
    vacancy = vacancies_dao.get_by_pk(pk)
    return render_template('vacancy.html', vacancy=vacancy)
