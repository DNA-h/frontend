# -*- coding: utf-8 -*-

from django.contrib import admin

from questionnaire.models import Answer, Category, Question, Response, Questionnaire

from .actions import make_published


class QuestionInline(admin.TabularInline):
    model = Question
    raw_id_fields = ('category',)
    ordering = ("order", "category")
    extra = 1
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "need_logged_user", "template")
    list_filter = ("is_published", "need_logged_user")
    inlines = [CategoryInline, QuestionInline]
    actions = [make_published]


class AnswerBaseInline(admin.StackedInline):
    raw_id_fields = ('question',)
    # fields = ("question", "body")
    # readonly_fields = ("question",)
    extra = 0
    model = Answer
class ResponseAdmin(admin.ModelAdmin):
    raw_id_fields = ('questionnaire', 'user', "category")
    list_display = ("questionnaire", "user","created","interview_uuid")
    list_filter = ("questionnaire", "created")
    date_hierarchy = "created"
    inlines = [AnswerBaseInline]
    # specifies the order as well as which fields to act on
    # readonly_fields = ("questionnaire", "created", "updated", "interview_uuid", "user")
    # readonly_fields = ( "created", "updated", "interview_uuid",)



class AnswerAdmin(admin.ModelAdmin):
    raw_id_fields = ('question',)
    fields = ("question","_question_text", "body")
    readonly_fields = ("_question_text",)
    def _question_text(self, obj):
        return obj.question.text


class QuestionAdmin(admin.ModelAdmin):
    raw_id_fields = ('questionnaire',"category")
    fields = ("questionnaire","category","text","order", "required","type", "choices")
    # readonly_fields = ("_question_text",)


class CategoryAdmin(admin.ModelAdmin):
    raw_id_fields = ('questionnaire',)
    fields = ("name","questionnaire","order","description")



# admin.site.register(Question, QuestionInline)
# admin.site.register(Category, CategoryInline)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
