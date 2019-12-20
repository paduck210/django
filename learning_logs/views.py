# Similar with Controller in Rails
# Bring and sorting a data from models
# Send the data to template(show in Rails)

from django.shortcuts import render
from .models import Topic
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('text')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    try:
        next_topic = topic.get_next_by_date_added()
    except Topic.DoesNotExist:
        next_topic = None
    try:
        previous_topic = topic.get_previous_by_date_added()
    except Topic.DoesNotExist:
        previous_topic = None

    context = {'topic': topic, 'entries': entries, 'next_topic': next_topic, 'previous_topic': previous_topic}
    return render(request, 'learning_logs/topic.html', context)


