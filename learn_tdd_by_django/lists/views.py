from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from lists.models import Item, List

# home_page = None


@csrf_exempt
def home_page(request):
    return render(request, 'home.html')


@csrf_exempt
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_})


@csrf_exempt
def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))


@csrf_exempt
def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
