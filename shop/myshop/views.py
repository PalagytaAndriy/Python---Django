from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Portfolio
from django.contrib import messages
import imaplib
import email.message
from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import *
from django.shortcuts import render
from django.http import HttpResponse



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })

def portfolio_list(request):
    portfolio_photo = Portfolio.objects.all()
    return render(request, 'portfolio.html',
                  {
                      'portfolio_photo': portfolio_photo
                  })




def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    return render(request, 'detail.html', {'product': product, 'cart_product_form': cart_product_form})


def about_us(request):
    return render(request, "about_us.html")
def shop(request):
    return render(request, "shop.html")
def zamovnuku(request):
    return render(request, "zamovnuku.html")
def zakaz(request):
    return render(request, "zakaz.html")
def hero(request):
    return render(request, "hero.html")
def order(request):
    return render(request, "order_modal.html")


def order_l(request):
    if request.method == "POST":
        name = request.POST.get('name')
        s_name = request.POST.get('s_name')
        phone = request.POST.get('phone')
        e_email = request.POST.get('e_email')

        # Налаштування з'єднання з сервером
        mail = imaplib.IMAP4_SSL('imap.ukr.net')
        mail.login('made_by_mama@ukr.net', 'VykYqvJiV1CksdiG')

        # Створення повідомлення
        msg = email.message.EmailMessage()
        msg['From'] = 'Покупець'
        msg['To'] = 'made_by_mama@ukr.net'
        msg['Subject'] = 'Нове замовлення!'

        body = f'Нове замовлення:\n\n' \
               f'Покупець: {name} {s_name}\n' \
               f'Телефон: {phone}\n\n' \
               f'Email: {e_email}\n\n'


        body += 'Товари:\n'
        cart = Cart(request)
        for item in cart:
            body += f'{item["product"]} - {item["quantity"]}шт - по - {item["price"]} грн\n'

        body += f'\nВсього на суму: {cart.get_total_price()}'

        msg.set_content(body)
        mail.append('INBOX', None, None, msg.as_bytes())
        mail.logout()

    return render(request, "erder_accepted.html")

