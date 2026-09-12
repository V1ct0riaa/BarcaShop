from django.core import serializers
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProductsForm
from main.models import Product

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):
    form = UserCreationForm()

    # Check if a request method is POST
    if request.method == "POST":
        form = UserCreationForm(request.POST) # make a form from existing library
        if form.is_valid():
            form.save() #save form
            messages.success(request, "Your account has been created! You are now able to log in")
            return redirect("main:login")
    context = {"form": form} # Put form into context and pass it into register.html
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST) # make a form from existing library

        if form.is_valid():
            user = form.get_user() # Get the user data
            login(request, user) # Log the user in
            return redirect("main:show_main") # Redirect to homepage
    else:
        form = AuthenticationForm(request)

    context = {"form": form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:login")

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()  # take all Product object from db
    context = {
        "app_name": "BarcaShop",
        "name": "Natanael Pascal",
        "product_list": product_list,
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect(
            "main:show_main"
        )  # searches for a path name in /main where name=show_main

    context = {"form": form}
    return render(request, "create_product.html", context)


def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {"product": product}

    return render(request, "product_detail.html", context)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)

def show_json_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        json_data = serializers.serialize("json", product_item)
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)
