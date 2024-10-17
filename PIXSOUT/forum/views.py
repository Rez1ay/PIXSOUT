from django.shortcuts import render
from .models import Theme, Publication


def forum(request):
    forum_themes = Theme.objects.all()
    data = {'forum_themes': forum_themes}

    return render(request, 'forum/forum.html', context=data)
