from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = list(question.choice_set.all().values_list('choice_text', flat=True))
    counts = list(question.choice_set.all().values_list('votes', flat=True))
    return render(request, 'polls/detail.html', {'question': question, 'choices': choices, 'counts':counts})

def results(request):
    return render(request, 'polls/index.html')

def vote(request):

    return render(request, 'polls/index.html')