from django.urls import path
from . import views


urlpatterns = [
    path('', views.parvam_list, name='parvam_list'),  # List all Parvams
    path('parvam/<int:parvam_id>/', views.story_list, name='story_list'),  # List all stories in a Parvam
    path('story/<int:story_id>/', views.story_detail, name='story_detail'),  # Detail of a single story
] 