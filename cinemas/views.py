from django.shortcuts import render

menu = [{'title': "Статистика",'url':'baners', 'icon':'nav-icon fas fa-chart-pie', 'list': []},
        {'title': "Банера",'url':'baners', 'icon':'nav-icon far fa-image', 'list': []},
        {'title': "Фільми",'url':'baners', 'icon':'fa-sharp fa-solid fa-film', 'list': ['Додати фільм']},
        {'title': "Кінотеатри",'url':'baners', 'icon':'fa-solid fa-user', 'list': ['Додати кінотеатр', 'Додати зал']},
        {'title': "Новини",'url':'baners', 'icon':'fa-solid fa-newspaper', 'list': ['Додати новину']},
        {'title': "Акції",'url':'baners', 'icon':'fa-regular fa-star', 'list': ['Додати акцію']},
        {'title': "Сторінки",'url':'baners', 'icon':'fa-solid fa-table-list', 'list': ['Головна сторінка',"О кінотеатрі"]},
        {'title': "Користувачі",'url':'baners', 'icon':'fa-solid fa-user', 'list': ['Редагувати користувача']},
        {'title': "Розссилка",'url':'baners', 'icon':'fa-solid fa-envelopes-bulk', 'list': ['Вибрати користувача']},

        ]


def index(request):
    context = {
        'menu': menu,
        'title': "ADMIN Панель",
    }
    return render(request, 'cinemas/index.html', context=context)

def baners(request):
    context = {
        'menu': menu,
        'title': "Baners",
    }
    return render(request, 'cinemas/index.html', context=context)





