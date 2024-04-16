from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
import json
from .models import *

def index(request):
    customer = None  # Initialize customer with None
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    products = Product.objects.all()
    context = {"products": products, "cartItems": cartItems, 'customer': customer}
    return render(request, "pages/index.html", context)




def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]
    context = {"items": items, "order": order, "cartItems": cartItems}
    return render(request, "pages/cart.html", context)



def product_page(request, product_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
        cartItems = order["get_cart_items"]

    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product, "cartItems": cartItems}
    return render(request, "pages/product_page.html", context)


def payment(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}
    context = {"items": items, "order": order}
    return render(request, "pages/payment.html", context)



def updateItem(request):
    print("updateItem view called")

    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("Action:", action)
    print("Product:", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = orderItem.quantity + 1
    elif action == "remove":
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    response_data = {
        'newQuantity': orderItem.quantity,
    }
    print(response_data)
    return JsonResponse(response_data)

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with the URL name of your home page
        else:
            error_message = 'Invalid username or password'
            return render(request, 'pages/login.html', {'error_message': error_message})
    else:
        return render(request, 'pages/login.html')
    
def logout_view(request):
    logout(request)
    return redirect("index")

def signup(request):
    if request.method == 'POST':
        # Get the form data
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        
        # Create a corresponding customer
        customer = Customer(user=user, name=username, email=email)
        customer.save()
        
        # Log in the user
        login(request, user)
        
        # Redirect to a success page or any other desired page
        return redirect('index')
    
    # Render the sign-up form
    return render(request, 'pages/signup.html')
