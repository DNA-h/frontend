from django.conf.urls import url
from questionnaire.views import ConfirmView, IndexView, QuestionnaireCompleted, QuestionnaireDetail, \
    get_questionnaire_list,get_question_list, get_question_detail
from questionnaire.views import serve_result_csv

urlpatterns = [
    # url(r"^$", IndexView.as_view(), name="questionnaire-list"),
    # url(r"^(?P<id>\d+)/", QuestionnaireDetail.as_view(), name="questionnaire-detail"),
    url(r"^csv/(?P<primary_key>\d+)/", serve_result_csv, name="questionnaire-result"),
    url(r"^(?P<id>\d+)/completed/", QuestionnaireCompleted.as_view(), name="questionnaire-completed"),
    # url(
    #     r"^(?P<id>\d+)-(?P<step>\d+)/",
    #     QuestionnaireDetail.as_view(),
    #     name="questionn               aire-detail-step",
    # ),
    url(r"^confirm/(?P<uuid>\w+)/", ConfirmView.as_view(), name="questionnaire-confirmation"),
    url(r"^$", get_questionnaire_list),
    url(r"^(?P<id>\d+)/", get_question_list),
    url(r"^q/(?P<id>\d+)/", get_question_detail),

]
