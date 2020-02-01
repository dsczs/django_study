from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("hello app")


def t1(request):
    from app.models import Question
    from django.utils import timezone
    from django.utils.timezone import utc
    import datetime
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    print(request.GET)

    q = Question()
    # add
    q.question_test = 'a'
    q.pub_date = now
    q.save()

    # del
    # update
    # selete
    return HttpResponse("t1 app")
