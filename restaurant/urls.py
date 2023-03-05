from django.urls import path, include
from . import views

urlpatterns = [
    # static page
    path('', views.index, name='index'),   

    # api

    # show menuitems
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),

    # bookings
    path('api/book/', views.BookingView.as_view()),
    path('api/book/<int:pk>', views.SingleBookingView.as_view()),

    # user managements
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]