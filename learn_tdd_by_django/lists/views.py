from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from lists.models import Item

# home_page = None


@csrf_exempt
def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title></html>')

    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html')


@csrf_exempt
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
