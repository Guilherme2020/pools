from django.shortcuts import render
from django.http import HttpResponse
from pools.models import Question
# Create your views here.



def index(request):
    todas_questoes = {'question':Question.objects.all()}

    return render(request,'index.html', todas_questoes )
    # return  todas_questoes
def question_id(request,question_id):
    question = Question.objects.get(id=question_id)
    questao_id = { 'question_id': Question.objects.get(id=question_id), 'choice':question.choise_set.all()}

    return render(request, 'question.html',questao_id)