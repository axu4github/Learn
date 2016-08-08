from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from lists.models import Item

# home_page = None


@csrf_exempt
def home_page(request):
    return render(request, 'home.html')


@csrf_exempt
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


@csrf_exempt
def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
