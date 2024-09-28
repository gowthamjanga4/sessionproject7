from django.shortcuts import render
from .forms import AddItemsForm


# Create your views here Gowtham.

def add_item_view(request):
    form = AddItemsForm()
    if request.method == 'POST':
        item = request.POST['item']
        quantity = request.POST['quantity']
        request.session[item] = quantity
    return render(request, 'testapp/additems.html', {'form': form})


def display_items_view(request):
    return render(request, 'testapp/displayitems.html')
