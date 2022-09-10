from math import ceil
from django.shortcuts import render, redirect
from main.models import *
from datetime import datetime


# Create your views here.

def indexHandler(request):
    categories = Category.objects.all()

    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

        wish_list = WishItem.objects.filter(session_id=user_session_id)
        wish_len = len(wish_list)
        compare_list = CompareItem.objects.filter(session_id=user_session_id)
        compare_len = len(compare_list)

    photos = Product.objects.filter(is_main=True)[:3]
    all_product = Product.objects.all()
    ver_photos = Product.objects.filter(is_ver_photo=True)[:4]
    gor_photos = Product.objects.filter(is_gor_photo=True)[:4]
    is_new = Product.objects.filter(is_new=True)[:6]
    sponsor = Sponsors.objects.all()
    about = AboutUs.objects.all()
    team = Worker.objects.all()

    return render(request, 'index.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'photos': photos,
        'all_product': all_product,
        'is_new': is_new,
        'ver_photos': ver_photos,
        'gor_photos': gor_photos,
        'sponsor': sponsor,
        'wish_len': wish_len,
        'compare_len': compare_len,
        'about': about,
        'team': team,
    })


def catalogHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

        wish_list = WishItem.objects.filter(session_id=user_session_id)
        wish_len = len(wish_list)
        compare_list = CompareItem.objects.filter(session_id=user_session_id)
        compare_len = len(compare_list)

    about = AboutUs.objects.all()
    search_value = request.GET.get('q', '')
    if search_value:
        products = Product.objects.filter(title__contains=search_value)
    else:
        products = Product.objects.all()

    return render(request, 'catalog.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
        'about': about,
        'products': products,
        'search_value': search_value,
    })


def aboutHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

        wish_list = WishItem.objects.filter(session_id=user_session_id)
        wish_len = len(wish_list)
        compare_list = CompareItem.objects.filter(session_id=user_session_id)
        compare_len = len(compare_list)

    about = AboutUs.objects.all()
    team = Worker.objects.all()

    return render(request, 'about.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
        'about': about,
        'team': team,
    })


def feedbackHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

        wish_list = WishItem.objects.filter(session_id=user_session_id)
        wish_len = len(wish_list)
        compare_list = CompareItem.objects.filter(session_id=user_session_id)
        compare_len = len(compare_list)

    about = AboutUs.objects.all()

    return render(request, 'feedback.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
    })


def catalogItemHandler(request, catalog_id):
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

        wish_list = WishItem.objects.filter(session_id=user_session_id)
        wish_len = len(wish_list)
        compare_list = CompareItem.objects.filter(session_id=user_session_id)
        compare_len = len(compare_list)

    active_category = Category.objects.get(id=catalog_id)

    categories = Category.objects.all()
    products = Product.objects.filter(category__id=catalog_id)
    brands = CategoryBrand.objects.filter(category__id=catalog_id)
    sizes = Size.objects.filter(category__id=catalog_id)

    active_brands = request.GET.getlist('active_brand', [])
    active_brands = [int(i) for i in active_brands]

    active_grams = request.GET.getlist('active_gram', [])
    active_grams = [int(i) for i in active_grams]

    price = request.GET.get('price', None)
    price_start = None
    price_stop = None

    if price and len(price.split('-')) == 2:
        price_start = int(price.split('-')[0])
        price_stop = int(price.split('-')[1])

    if active_brands:
        new_products = []
        for p in products:
            if p.brand and p.brand.id in active_brands:
                new_products.append(p)
        products = new_products

    if active_grams:
        new_products = []
        for p in products:
            if p.size and p.size.id in active_grams:
                new_products.append(p)
        products = new_products

    if price_start and price_stop:
        new_products = []
        for p in products:
            if p.price >= price_start and p.price <= price_stop:
                new_products.append(p)
        products = new_products

    limit = request.GET.get('limit', 2)
    current_page = int(request.GET.get('page', 1))
    total = len(products)
    pages_count = ceil(total / limit)
    pages = range(1, pages_count + 1)
    stop = current_page * limit
    start = stop - limit
    prev_page = current_page - 1
    next_page = None
    if current_page < pages_count:
        next_page = current_page + 1

    about = AboutUs.objects.all()

    return render(request, 'catalog.html', {
        'categories': categories,
        'products': products[start:stop],
        'brands': brands,
        'active_category': active_category,
        'active_brands': active_brands,
        'active_grams': active_grams,
        'sizes': sizes,
        'pages': pages,
        'current_page': current_page,
        'prev_page': prev_page,
        'next_page': next_page,
        'start': start,
        'stop': stop,
        'total': total,
        'pages_count': pages_count,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
        'about': about,
    })


def productHandler(request, product_id):
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

        wish_list = WishItem.objects.filter(session_id=user_session_id)
        wish_len = len(wish_list)
        compare_list = CompareItem.objects.filter(session_id=user_session_id)
        compare_len = len(compare_list)

    categories = Category.objects.all()
    active_product = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(category__id=active_product.category.id)
    about = AboutUs.objects.all()

    return render(request, 'product.html', {
        'categories': categories,
        'active_product': active_product,
        'related_products': related_products,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
        'about': about,
    })


def cartHandler(request):
    categories = Category.objects.all()

    if not request.session.session_key:
        request.session.create()
    user_session_id = request.session.session_key

    open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
    new_cart = None
    if open_carts:
        new_cart = open_carts[0]
        wish_list = WishItem.objects.filter(session_id=user_session_id)
        wish_len = len(wish_list)
        compare_list = CompareItem.objects.filter(session_id=user_session_id)
        compare_len = len(compare_list)
    else:
        new_cart = Cart()
        new_cart.session_id = user_session_id
        new_cart.save()

    if request.POST:
        return_url = request.POST.get('return_url', '')
        action = request.POST.get('action', '')

        if action == 'add_to_cart':
            product_id = int(request.POST.get('product_id', 0))
            amount = float(request.POST.get('amount', 0))

            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0).filter(product__id=product_id)

            if cart_items:
                new_cart_item = cart_items[0]
                new_cart_item.amount = new_cart_item.amount + amount
                new_cart_item.all_price = new_cart_item.price * new_cart_item.amount
                new_cart_item.save()
            else:
                new_cart_item = CartItem()
                new_cart_item.product_id = product_id
                new_cart_item.cart_id = new_cart.id
                new_cart_item.amount = amount
                new_cart_item.price = new_cart_item.product.price
                new_cart_item.all_price = new_cart_item.price * new_cart_item.amount
                new_cart_item.save()

        if action == 'remove_from_cart':
            product_id = int(request.POST.get('product_id', 0))
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0).filter(product__id=product_id)
            for ci in cart_items:
                ci.delete()

        if action == 'clear_cart':
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
            for ci in cart_items:
                ci.delete()

        if action == 'checkout':
            new_cart.first_name = request.POST.get('first_name', '')
            new_cart.last_name = request.POST.get('last_name', '')
            new_cart.country = request.POST.get('country', '')
            new_cart.city = request.POST.get('city', '')
            new_cart.address = request.POST.get('address', '')
            new_cart.zip_code = request.POST.get('zip_code', '')
            new_cart.email = request.POST.get('email', '')
            new_cart.phone = request.POST.get('phone', '')
            new_cart.comment = request.POST.get('comment', '')
            new_cart.created_at = datetime.now()
            new_cart.status = 1
            new_cart.save()

        if action == 'accepted':
            order_id = int(request.POST.get('order_id', 0))
            if request.user.is_authenticated:
                main_order = Cart.objects.get(id=order_id)
                if main_order:
                    main_order.status = 2
                    main_order.save()

        if action == 'add_to_compare_list':
            product_id = int(request.POST.get('product_id', 0))
            compare_item = CompareItem.objects.filter(product__id=product_id).filter(session_id=user_session_id)
            if compare_item:
                pass
            else:
                compare_item = CompareItem()
                compare_item.session_id = user_session_id
                compare_item.product_id = product_id
                compare_item.save()

        if action == 'add_to_wish_list':
            product_id = int(request.POST.get('product_id', 0))
            wish_item = WishItem.objects.filter(product__id=product_id).filter(session_id=user_session_id)
            if wish_item:
                pass
            else:
                wish_item = WishItem()
                wish_item.session_id = user_session_id
                wish_item.product_id = product_id
                wish_item.save()

        if action == 'remove_from_compare_list':
            product_id = int(request.POST.get('product_id', 0))
            compare_items = CompareItem.objects.filter(product__id=product_id).filter(session_id=user_session_id)
            if compare_items:
                for com in compare_items:
                    com.delete()

        if action == 'remove_from_wish_list':
            product_id = int(request.POST.get('product_id', 0))
            wish_items = WishItem.objects.filter(product__id=product_id).filter(session_id=user_session_id)
            if wish_items:
                for com in wish_items:
                    com.delete()

        if action in ['add_to_cart', 'remove_from_cart']:
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
            all_price = 0
            all_amount = 0
            all_orig_price = 0
            if cart_items:
                for ci in cart_items:
                    all_amount += ci.amount
                    all_orig_price += ci.amount * ci.price

            new_cart.orig_price = all_orig_price
            all_price = all_orig_price * (100 - new_cart.discount_int) / 100
            new_cart.amount = all_amount
            new_cart.orig_price = all_orig_price
            new_cart.price = all_price
            new_cart.save()

        if return_url:
            return redirect(return_url)

    cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)
    about = AboutUs.objects.all()

    return render(request, 'cart.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
        'about': about,
    })


def checkoutHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

    wish_list = WishItem.objects.filter(session_id=user_session_id)
    wish_len = len(wish_list)
    compare_list = CompareItem.objects.filter(session_id=user_session_id)
    compare_len = len(compare_list)

    about = AboutUs.objects.all()

    return render(request, 'checkout.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
    })


def checkoutSuccessHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

    wish_list = WishItem.objects.filter(session_id=user_session_id)
    wish_len = len(wish_list)
    compare_list = CompareItem.objects.filter(session_id=user_session_id)
    compare_len = len(compare_list)
    about = AboutUs.objects.all()

    return render(request, 'checkout_success.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_len': wish_len,
        'compare_len': compare_len,
    })


def ordersHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    confirmed_orders = []

    if request.user.is_authenticated:
        confirmed_orders = Cart.objects.filter(status__gte=1)
    about = AboutUs.objects.all()

    return render(request, 'orders.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'confirmed_orders': confirmed_orders,
    })


def ordersItemHandler(request, order_id):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []

    order_items = []
    main_order = None

    if request.user.is_authenticated:
        order_items = CartItem.objects.filter(cart__id=order_id)
        main_order = Cart.objects.get(id=order_id)
    about = AboutUs.objects.all()

    return render(request, 'order_item.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'order_items': order_items,
        'main_order': main_order,
    })


def compareHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    compare_list = []

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

    compare_list = CompareItem.objects.filter(session_id=user_session_id)
    wish_list = WishItem.objects.filter(session_id=user_session_id)
    wish_len = len(wish_list)
    compare_len = len(compare_list)
    about = AboutUs.objects.all()

    return render(request, 'compare.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'compare_list': compare_list,
        'wish_len': wish_len,
        'compare_len': compare_len,
    })


def wishHandler(request):
    categories = Category.objects.all()
    new_cart = None
    cart_items = []
    wish_list = []

    user_session_id = request.session.session_key
    if user_session_id:
        open_carts = Cart.objects.filter(session_id=user_session_id).filter(status=0)
        if open_carts:
            new_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=new_cart.id).filter(status=0)

    wish_list = WishItem.objects.filter(session_id=user_session_id)
    wish_len = len(wish_list)
    compare_list = CompareItem.objects.filter(session_id=user_session_id)
    compare_len = len(compare_list)
    about = AboutUs.objects.all()

    return render(request, 'wishlist.html', {
        'categories': categories,
        'new_cart': new_cart,
        'cart_items': cart_items,
        'wish_list': wish_list,
        'wish_len': wish_len,
        'compare_len': compare_len,
    })