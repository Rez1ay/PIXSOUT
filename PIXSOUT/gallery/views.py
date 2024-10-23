from django.shortcuts import render
from .models import Screenshot


def gallery(request):
    screenshots = Screenshot.objects.all()
    data = {'screenshots': screenshots}
    return render(request, 'gallery/gallery.html', context=data)
