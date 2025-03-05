from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Parvam, Story

# View to list all parvams
def parvam_list(request):
    parvams = Parvam.objects.all()
    return render(request, 'stories/parvam_list.html', {'parvams': parvams})

# View to list all stories in a specific parvam
def story_list(request, parvam_id):
    parvam = get_object_or_404(Parvam, id=parvam_id)
    stories = parvam.stories.all()  # Access related stories using related_name
    return render(request, 'stories/story_list.html', {'parvam': parvam, 'stories': stories})

# View to display a single story in detail
def story_detail(request, story_slug):
    story = get_object_or_404(Story, slug=story_slug)
    return render(request, 'stories/story_detail.html', {'story': story})

def like_story(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    story.likes += 1  # Assuming you have a `likes` field in your Story model
    story.save()
    return JsonResponse({"likes": story.likes})