from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import View
from .models import Choice, Question,user
import uuid
#from django.template import loader
# Create your views here.
def index(request):
     # return HttpResponse('hello word')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
  #  return HttpResponse(template.render(context, request))
  
def detail(request, question_id):
  #  return HttpResponse("You're looking at question %s." % question_id)
  '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
  '''
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
'''
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
'''
def xxx(request):
      # return HttpResponse('xxx')
       if request.method=='GET':     
           return render(request,'polls/xxx.html')       
       if request.method=='POST':
           a=request.POST['xxx']
           b=user.objects.create(username=str(uuid.uuid1()), pwd=str(uuid.uuid4()))
           return render(request,'polls/xxx.html')
          # return HttpResponse(request.POST['xxx'])
           
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))