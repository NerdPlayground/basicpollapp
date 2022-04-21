from django.contrib import admin
from questions.models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display= ["id","title","body","created","updated"]
    list_filter= ["updated"]
    search_fields= ["title"]