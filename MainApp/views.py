from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from MainApp.models import Item
# Create your views here.

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]
items = Item.objects.all()


def home(request):
    data_name = {'name': 'Иван Петров Иваныч',
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
    #get_data = Item.objects.get(pk=item_id) # MainApp.models.Item.DoesNotExist
    get_id  = Item.objects.filter(id=item_id) #list
    if not get_id:
        context = {'item_id': item_id}
        return render(request, 'item.html', context)
    context = {'item': get_id}
    return render(request, 'item.html', context)


def out_all_items(request):
    items = Item.objects.all()
    return render(request, 'items.html', {'items_dic':items})
