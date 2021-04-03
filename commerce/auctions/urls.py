from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing", views.create_listing, name= "listing"),
    path("product/<int:product_id>/<int:user_id>", views.product, name="product"),
    path("CloseBid/<int:product_id>", views.product, name = "CloseBid")
]
