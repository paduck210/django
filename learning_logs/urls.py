"""define URL patterns for learning_logs"""
# similar with routes in Rails

from django.urls import path, include
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # Page that show all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single page
    path('topics/<int:topic_id>', views.topic, name='topic'),

]
