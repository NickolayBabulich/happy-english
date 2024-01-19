from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Test, Question


class IndexView(generic.ListView):
    model = Course
    template_name = "self_study_app/index.html"


class ModuleDetailView(generic.DetailView):
    model = Module
    template_name = "self_study_app/detail.html"


class CourseListView(generic.DetailView):
    model = Course
    template_name = 'self_study_app/course_test.html'


class TestListView(generic.ListView):
    model = Test
    template_name = 'self_study_app/course_test.html'
    context_object_name = 'tests'

    def get_queryset(self):
        # Получаем Course из URL-параметра
        course_pk = self.kwargs.get('course_pk')
        # Проверяем, что существует курс с указанным индексом
        course = get_object_or_404(Course, pk=course_pk)
        # Возвращаем тесты для данного курса
        queryset = Test.objects.filter(course=course)
        for i in queryset:
            print(i.pk)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем информацию о курсе в контекст
        context['course'] = get_object_or_404(Course, pk=self.kwargs.get('course_pk'))
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print(request.POST)
            for test in self.get_queryset():
                questions = Question.objects.filter(test_id=test.pk)
                score = 0
                wrong = 0
                correct = 0
                total = 0
                for q in questions:
                    total += 1
                    print(request.POST.get(q.question))
                    print(q.answer)
                    print()
                    if q.answer == request.POST.get(q.question):
                        score += 10
                        correct += 1
                    else:
                        wrong += 1
                percent = score / (total * 10) * 100
                if percent >= 80:
                    result = 'Вы отлично справились с тестом, удачи в дальнейшем изучение английского языка!'
                elif 60 <= percent < 80:
                    result = 'Вы хорошо справились с тестом, но вам необходимо повторить пройденный материал!'
                elif 40 <= percent < 60:
                    result = ('Вы удовлетворительно справились с тестом, думаем, что вам стоит '
                              'повторить материал еще, подготовиться получше и у вас все получится!')
                else:
                    result = ('Вы не справились с тестом, не отчаивайтесь, больше практики, '
                              'повторений и у вас все получится! Мы в вас верим!')
                context = {
                    'score': score,
                    'time': request.POST.get('timer'),
                    'correct': correct,
                    'wrong': wrong,
                    'percent': percent,
                    'total': total,
                    'result': result
                }
                return render(request, 'self_study_app/results.html', context)
            else:
                questions = Question.objects.all()
                context = {
                    'questions': questions
                }
                return render(request, 'self_study_app/course_test.html', context)
