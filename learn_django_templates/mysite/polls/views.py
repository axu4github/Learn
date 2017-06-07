from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def all(request):
    questions = Question.objects.all().values()
    r = []
    for q in questions:
        tmp = {
            'id': q['id'],
            'question_text': q['question_text'],
            'pub_date': q['pub_date'],
        }
        r.append(tmp)

    return JsonResponse(r, safe=False)


def get(request):
    r = []
    try:
        q = Question.objects.get(pk=request.GET['qid'])
        r.append({
            'id': q.id,
            'question_text': q.question_text,
            'pub_date': q.pub_date,
        })
    except Exception as e:
        pass

    return JsonResponse(r, safe=False)


def list(request):
    return render(request, 'polls/list.html')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


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
