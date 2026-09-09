from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProductsForm
from main.models import Product


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
