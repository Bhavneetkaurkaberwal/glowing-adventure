from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question

# /polls/
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# /polls/{question_id}/
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# /polls/{question_id}/results/
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# /polls/{question_id}/vote/
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)