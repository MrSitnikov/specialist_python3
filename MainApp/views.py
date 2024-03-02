from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
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
    # text = """
    #     <h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    # return HttpResponse(text)
    data_name = {'name': 'Петров Иван Иваныч',
                 'email': 'may_mail@ya.ru'}
    return render(request, 'index.html',data_name)


def about(request):
    text = """
        Имя: <b>Иван</b><br>
        Отчество: <b>Петрович</b><br>
        Фамилия: <b>Иванов</b><br>
        телефон: <b>8-923-600-01-02</b><br>
        email: <b>vasya@mail.ru</b>
        """
    return HttpResponse(text)


def out_item(request, item_id):
    for item in items:
        if item['id'] == item_id:
            print(item)
            return render(request, 'item.html', item)
    return render(request, 'item.html', {"item": False, 'id': item_id})
    #     if item['id'] == id:
    #         text = f"""<i>Товар</i> <b>{item['name']}</b>
    #         <br>
    #         <i>Колличество товара</i>
    #         <b>{item['quantity']}</b><br>
    #         <a href="/items"><i>Назад к списку товаров</i></a>
    #         """
    #         return HttpResponse(text)
    #     text = f'<b>Товар с id={id} не найден</b>'
    #     return HttpResponseNotFound(text)


def out_all_items(request):
    # out = []
    # for item in items:
    #     out.append(f"""<b>id:</b> <a href="/item/{item['id']}">{item['id']}</a>
    #                <b>товар:</b> {item['name']}
    #                <b>кол-во:</b> {item['quantity']}<br>""")
    # return HttpResponse("\n".join(out))
    return render(request, 'items.html', {'items_dic':items})
