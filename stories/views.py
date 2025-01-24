from django.shortcuts import render, get_object_or_404
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
def story_detail(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'stories/story_detail.html', {'story': story})
