from django.shortcuts import render
from .models import Theme, Publication
from .forms import AddPublicationForm


def forum(request):
    forum_themes = Theme.objects.all()
    data = {'forum_themes': forum_themes}

    return render(request, 'forum/forum.html', context=data)


def theme(request, theme_name):
    theme_id = Theme.objects.get(name=theme_name).id
    publications = Publication.objects.filter(theme_id=theme_id)

    if request.method == 'POST':
        form = AddPublicationForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddPublicationForm()
    data = {'publications': publications, 'form': form}

    return render(request, 'forum/theme.html', data)
