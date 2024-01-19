from django.contrib import admin
from self_study_app.models import Course, Module, Question, Test


class ModuleInline(admin.StackedInline):
    model = Module
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 0


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInLine]
