from random import choice
from string import ascii_letters

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from .forms import ProductForm
from .models import Product

@login_required
def productList(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'products/products.html', {'products': products})


@login_required
def product_add(request):
    if not request.user.is_salesperson:
        raise Http404

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if not form.is_valid():
            return render(request, 'products/products_add.html',
                          {'form': form})
        else:
            product = form.save(commit=False)
            product.save()
            messages.success(request, "Successfully Added")
            return redirect('products:product_list')

    else:
        context = {
            "title": 'Add Product',
            "form": ProductForm(),
        }
        return render(request, 'products/products_add.html', context)


@login_required
def product_update(request, pk=None):
    if not request.user.is_salesperson:
        raise Http404
    instance = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=instance)
        if not form.is_valid():
            return render(request, 'products/products_update.html',
                          {'form': form})
        else:
            product = form.save(commit=False)
            product.save()
            messages.success(request, "Successfully Updated")
            return redirect('products:product_list')

    else:
        context = {
            "title": 'Update Product',
            "form": ProductForm(instance=instance),
        }
        return render(request, 'products/products_update.html', context)

@login_required
def product_delete(request, pk=None):
    if not request.user.is_salesperson:
        raise Http404
    instance = get_object_or_404(Product, pk=pk)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('products:product_list')