from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404  # redirectとget_object_or_404をインポート
from .models import Product
from .forms import ProductForm
from django.db.models import Q

def product_list(request):
    query = request.GET.get('q')
    category_filter = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    sort_by = request.GET.get('sort_by', 'name')

    product_list = Product.objects.all()

    if query:
        product_list = product_list.filter(name__icontains=query)

    if category_filter:
        product_list = product_list.filter(category=category_filter)

    if min_price:
        product_list = product_list.filter(price__gte=min_price)

    if max_price:
        product_list = product_list.filter(price__lte=max_price)

    product_list = product_list.order_by(sort_by)

    paginator = Paginator(product_list, 6)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    # 背景色をテンプレート用に付加
    for product in products:
        product.background_color_code = product.get_background_color_code()

    categories = Product.objects.values_list('category', flat=True).distinct()

    return render(request, 'products/main.html', {
        'products': products,
        'categories': categories,
        'query': query,
        'category_filter': category_filter,
        'min_price': min_price,
        'max_price': max_price,
        'sort_by': sort_by,
    })


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)  # get_object_or_404を使う
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return redirect('product_list')

def product_form(request, pk=None):
    # pkが指定されていれば編集、指定されていなければ新規作成
    product = get_object_or_404(Product, pk=pk) if pk else None
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'is_edit': bool(product)  # テンプレートで「編集」か「新規作成」かを判別するためのフラグ
    }
    return render(request, 'products/add.html', context)
