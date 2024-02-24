from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    text = """
        <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    return HttpResponse(text)


def about(request):
    text = """
        Имя: <b>Иван</b><br>
Отчество: <b>Петрович</b><br>
Фамилия: <b>Иванов</b><br>
телефон: <b>8-923-600-01-02</b><br>
email: <b>vasya@mail.ru</b>
"""
    return HttpResponse(text)


def out_item(request, id):
    for item in items:
        if item['id'] == id:
            text = f"""<i>Товар</i> <b>{item['name']}</b>
            <br>
            <i>Колличество товара</i>
            <b>{item['quantity']}</b>"""
            break
        text = f'<b>Товар с id={id} не найден</b>'
    return HttpResponse(text)


def out_all_items(request):
    pass
