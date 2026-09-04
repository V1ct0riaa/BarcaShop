from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' :  "BarcaShop",
        'name': 'Natanael Pascal'
    }

    return render(request, "main.html", context)