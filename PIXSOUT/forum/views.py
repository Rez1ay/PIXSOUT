from django.shortcuts import render
from .models import Theme, Publication
from .forms import AddPublicationForm


def forum(request):
    forum_themes = []
    for t in Theme.objects.all():
        last_publication = Publication.objects.filter(theme=t).last()
        last_publication.text = last_publication.text[:120] + '...'
        forum_themes.append((t, last_publication))
    data = {'forum_themes': forum_themes}

    return render(request, 'forum/forum.html', context=data)


def theme(request, theme_name):
    current_theme = Theme.objects.get(name=theme_name)
    publications = Publication.objects.filter(theme=current_theme)

    if request.method == 'POST':
        form = AddPublicationForm(request.POST)
        if form.is_valid():
            new_publication = form.save(commit=False)
            new_publication.theme = current_theme
            new_publication.author = request.user
            new_publication.save()

    form = AddPublicationForm()
    data = {'publications': publications, 'form': form}

    return render(request, 'forum/theme.html', data)
