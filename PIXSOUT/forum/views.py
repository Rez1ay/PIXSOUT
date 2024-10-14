from django.shortcuts import render


def forum(request):
    forum_themes = [
        {'title': 'Новости', 'user': 'kaziyar', 'message': 'Мы релизнулись!', 'time': '6 дней назад'},
        {'title': 'Техподдержка', 'user': 'duboooon', 'message': 'у меня игра крашается хелп', 'time': '2 дня назад'}
    ]
    data = {'forum_themes': forum_themes}

    return render(request, 'forum/forum.html', context=data)
