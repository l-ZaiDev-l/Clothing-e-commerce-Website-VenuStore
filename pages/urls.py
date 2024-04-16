from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path("update_item/", views.updateItem, name="update_item"),
    path("payment/", views.payment, name="payment"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("product/<int:product_id>/", views.product_page, name="product_page"),
]
