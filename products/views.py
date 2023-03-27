from django.shortcuts import render
from products.forms import RecentProduct

# Create your views here.
def product(request):
    return render(request, 'product/product.html', {})

def details(request):
    if request.method == 'POST':
        frm = RecentProduct(request.POST)
        print(frm.changed_data)
    else:
      frm = RecentProduct(auto_id=True, label_suffix=' :', ) # auto_id is used to add id to the fields in the form
      print("GET request") 


    return render(request, 'product/recent.html', {'form': frm})

