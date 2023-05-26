from flask import Blueprint, render_template
from app.candidates.dao.candidate_dao import CandidateDAO


candidate_blueprint = Blueprint("candidate_blueprint", __name__, template_folder="templates", url_prefix="/candidates")
candidates_dao = CandidateDAO("./data/candidates.json")

# В'юшка для всіх кандидатів
@candidate_blueprint.route("/")
def page_candidates_all():
    candidates = candidates_dao.get_all()
    return render_template("candidates_index.html", candidates=candidates)


# В'юшка для кандидата по номеру
@candidate_blueprint.route('/<int:pk>')
def page_candidate(pk):
    candidate = candidates_dao.get_by_pk(pk)
    return render_template('candidate_single.html', candidate=candidate)