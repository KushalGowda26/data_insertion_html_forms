from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def insert_topic(request):
  if request.method=="POST":
    tn=request.POST['topic']
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('Topic insertion done')
  return render(request, 'insert_topic.html')

def insert_webpage(request):
  topics=Topic.objects.all()
  d={'topic':topics}
  if request.method=="POST":
    topic=request.POST['topic']
    name=request.POST['name']
    url=request.POST['url']
    T=Topic.objects.get_or_create(topic_name=topic)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T, name=name, url=url)[0]
    W.save()
    return HttpResponse('Webpage insertion done')
  return render(request, 'insert_webpage.html',d)


def insert_records(request):
  topics=Topic.objects.all()
  web=Webpage.objects.all()
  d={'Web':web, 'topic':topics}
  if request.method=="POST":
    topic=request.POST['topic']
    name=request.POST['name']
    date=request.POST['date']
    url=request.POST['url']
    T=Topic.objects.get_or_create(topic_name=topic)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T, name=name, url=url)[0]
    W.save()
    A=AccessRecords.objects.get_or_create(name=W, date=date)[0]
    A.save()
    return HttpResponse('Record insertion done')
  return render(request, 'insert_records.html',d)


def topic_details(request):
  
  topics=Topic.objects.all()
  d={'topic':topics}
  if request.method=="POST":
    topic=request.POST['topic']
    T=Topic.objects.get_or_create(topic_name=topic)[0]
    T.save()
  return render(request, 'topic_details.html',d)

    