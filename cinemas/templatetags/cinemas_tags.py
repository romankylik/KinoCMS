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
menu = [{'title': "Статистика", 'url': 'home', 'icon': 'fas fa-chart-pie'},
        {'title': "Банера", 'url': 'baners', 'icon': 'far fa-image'},
        {'title': "Фільми", 'url': 'addfilm', 'icon': 'fa-sharp fa-solid fa-film'},
        {'title': "Кінотеатри", 'url': 'addcinema', 'icon': 'fa-solid fa-user'},
        {'title': "Новини", 'url': 'baners', 'icon': 'fa-solid fa-newspaper'},
        {'title': "Акції", 'url': 'baners', 'icon': 'fa-regular fa-star'},
        {'title': "Сторінки", 'url': 'baners', 'icon': 'fa-solid fa-table-list'},
        {'title': "Користувачі", 'url': 'edit_users', 'icon': 'fa-solid fa-user'},
        {'title': "Розссилка", 'url': 'baners', 'icon': 'fa-solid fa-envelopes-bulk'},
        ]
@register.inclusion_tag('cinemas/left_menu.html', name='left_menu')  # Тег, що містить фрагмент html коду
def show_left_menu():
    return {"menu": menu}
