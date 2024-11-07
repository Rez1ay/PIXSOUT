from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from .models import Theme, Publication
from .forms import AddPublicationForm


class ThemesList(ListView):
    template_name = 'forum/forum.html'
    context_object_name = 'forum_themes'

    def get_queryset(self):
        forum_themes = []
        for t in Theme.objects.all():
            last_publication = Publication.objects.filter(theme=t).last()
            last_publication.text = last_publication.text[:120] + '...'
            forum_themes.append((t, last_publication))
        return forum_themes


class PublicationsList(FormMixin, ListView):
    model = Publication
    template_name = 'forum/theme.html'
    context_object_name = 'publications'
    form_class = AddPublicationForm

    def get_success_url(self, **kwargs):
        return f'/forum/{self.kwargs["theme_name"]}'

    def get_queryset(self):
        return Publication.objects.filter(theme__name=self.kwargs['theme_name'])

    def post(self, request, **kwargs):
        form = self.get_form()
        current_theme = Theme.objects.get(name=kwargs['theme_name'])
        if form.is_valid():
            new_publication = form.save(commit=False)
            new_publication.theme = current_theme
            new_publication.author = request.user
            form.save()
            return self.form_valid(form)
