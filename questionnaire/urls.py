from django.conf.urls import url
from questionnaire.views import QuestionnaireDetail,\
    get_questionnaire_list, QuestionDetail, answer_question

urlpatterns = [
    url(r"^(?P<id>\d+)/", QuestionnaireDetail.as_view(), name="questionnaire-detail"),
    url(r"^$", get_questionnaire_list),
    url(r"^q/(?P<id>\d+)/", answer_question),
    url(r"^q/(?P<id>\d+)/", QuestionDetail.as_view(), name="question-detail"),
]
