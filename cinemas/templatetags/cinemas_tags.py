from django import template
from cinemas.models import *

register = template.Library() #Бібліотека для Реєстрації власних тегів
"""
@register.simple_tag(name='getcats')  # Один з типів тега - simple_tag - простий тег, повертає змінні.
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)
"""
menu = [{'title': "Статистика", 'url': 'baners', 'icon': 'nav-icon fas fa-chart-pie', 'list': []},
        {'title': "Банера", 'url': 'home', 'icon': 'nav-icon far fa-image', 'list': []},
        {'title': "Фільми", 'url': 'baners', 'icon': 'fa-sharp fa-solid fa-film', 'list': ['Додати фільм']},
        {'title': "Кінотеатри", 'url': 'baners', 'icon': 'fa-solid fa-user',
         'list': ['Додати кінотеатр', 'Додати зал']},
        {'title': "Новини", 'url': 'baners', 'icon': 'fa-solid fa-newspaper', 'list': ['Додати новину']},
        {'title': "Акції", 'url': 'baners', 'icon': 'fa-regular fa-star', 'list': ['Додати акцію']},
        {'title': "Сторінки", 'url': 'baners', 'icon': 'fa-solid fa-table-list',
         'list': ['Головна сторінка', "О кінотеатрі"]},
        {'title': "Користувачі", 'url': 'baners', 'icon': 'fa-solid fa-user',
         'list': ['Редагувати користувача']},
        {'title': "Розссилка", 'url': 'baners', 'icon': 'fa-solid fa-envelopes-bulk',
         'list': ['Вибрати користувача']},
        ]
@register.inclusion_tag('cinemas/left_menu.html', name='left_menu')  # Тег, що містить фрагмент html коду
def show_left_menu():
    return {"menu": menu}
