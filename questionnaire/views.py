# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from questionnaire.forms import ResponseForm
from questionnaire.models import Category, Questionnaire, Question, Answer, Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_questionnaire_list(request):
        obj = {}
        try:
            questionnaires = Questionnaire.objects.filter(is_published=True)
            if not request.user.is_authenticated:
                questionnaires = questionnaires.filter(need_logged_user=False)
            # context["questionnaires"] = questionnaires
            # return context
            for questionnaire in questionnaires:
                r = {}
                id = questionnaire.id
                r["questionnaire_name"] = questionnaire.name
                r["questionnaire_description"] = questionnaire.description
                r["questionnaire_is_published"] = questionnaire.is_published
                r["questionnaire_need_logged_user"] = questionnaire.need_logged_user
                r["questionnaire_display_by_question"] = questionnaire.display_by_question
                obj["id = %s" % id] = r
            return JsonResponse(obj, safe=False)
        except questionnaires:
            questionnaires = None
            return HttpResponse("سوالی برای شما یافت نشد.")


# class QuestionnaireCompleted(TemplateView):
#     template_name = "questionnaire/completed.html"
#     def get_context_data(self, **kwargs):
#         context = {}
#         questionnaire = get_object_or_404(Questionnaire, is_published=True, id=kwargs["id"])
#         context["questionnaire"] = questionnaire
#         return context

class QuestionnaireDetail(View):
    def get(self, request, *args, **kwargs):
        obj = {}
        try:
            questionnaires = Questionnaire.objects.filter(id=kwargs["id"], is_published=True)
            for questionnaire in questionnaires:
                categories = Category.objects.filter(questionnaire=questionnaire)
                for category in categories:
                    questions = Question.objects.filter(category=category)
                    if questions:
                        for question in questions:
                            r = {}
                            try:
                                answer = Answer.objects.get(question=question)
                                r["answer_created"] = answer.created
                                r["answer_updated"] = answer.updated
                                r["answer_body"] = answer.body
                            except:
                                pass
                            id = question.id
                            r["questionnaire_name"] = question.questionnaire.name
                            r["questionnaire_description"] = question.questionnaire.description
                            r["questionnaire_is_published"] = question.questionnaire.is_published
                            r["questionnaire_need_logged_user"] = question.questionnaire.need_logged_user
                            r["questionnaire_display_by_question"] = question.questionnaire.display_by_question
                            r["category_name"] = question.category.name
                            r["category_order"] = question.category.order
                            r["category_description"] = question.category.description
                            r["question_text"] = question.text
                            r["question_order"] = question.order
                            r["question_required"] = question.required
                            r["question_type"] = question.type
                            r["question_choices"] = question.choices
                            obj["%s" % id] = r
            return JsonResponse(obj, safe=False)
        except questionnaire:
            return HttpResponse("سوالی برای شما یافت نشد.")

class QuestionDetail(View):
    model = Question
    def get(self, request, *args, **kwargs):
        try:
            r = {}
            question = Question.objects.get(id=kwargs["id"])
            try:
                answer = Answer.objects.get(question=question)
                r["answer_created"] = answer.created
                r["answer_updated"] = answer.updated
                r["answer_body"] = answer.body
            except:
                pass
            r["questionnaire_name"] = question.questionnaire.name
            r["questionnaire_description"] = question.questionnaire.description
            r["questionnaire_is_published"] = question.questionnaire.is_published
            r["questionnaire_need_logged_user"] = question.questionnaire.need_logged_user
            r["questionnaire_display_by_question"] = question.questionnaire.display_by_question
            r["category_name"] = question.category.name
            r["category_order"] = question.category.order
            r["category_description"] = question.category.description
            r["question_text"] = question.text
            r["question_order"] = question.order
            r["question_required"] = question.required
            r["question_type"] = question.type
            r["question_choices"] = question.choices
            return JsonResponse(r, safe=False)
        except question:
            return HttpResponse("سوال یافت نشد.")


@api_view(['POST'])
def answer_question(request,*args, **kwargs):
    user = request.user
    question = Question.objects.get(id=kwargs["id"])
    response = Response.objects.create(user=user,
                        questionnaire=question.questionnaire,category=question.category)
    body = request.data["body"]
    answer = Answer(question=question,body=body,response=response)
    answer.save()
    r = {}
    r["questionnaire_name"] = question.questionnaire.name
    r["questionnaire_description"] = question.questionnaire.description
    r["questionnaire_is_published"] = question.questionnaire.is_published
    r["questionnaire_need_logged_user"] = question.questionnaire.need_logged_user
    r["questionnaire_display_by_question"] = question.questionnaire.display_by_question
    r["category_name"] = question.category.name
    r["category_order"] = question.category.order
    r["category_description"] = question.category.description
    r["question_text"] = question.text
    r["question_order"] = question.order
    r["question_required"] = question.required
    r["question_type"] = question.type
    r["question_choices"] = question.choices
    r["answer_created"] = answer.created
    r["answer_updated"] = answer.updated
    r["answer_body"] = answer.body
    return JsonResponse(r, safe=False)



