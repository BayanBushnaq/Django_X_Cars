from django.urls import path
from .views import CarListView,CarDetailView,CarCreateView,CarUpdateView,CarDeleteView
urlpatterns =[
    path('car/',CarListView.as_view(), name='car_listview'),
    path('car/<int:pk>/',CarDetailView.as_view(), name='car_DetailView'),
    path('car/create/',CarCreateView.as_view(),name = 'car_CreateView'),
    path('car/update/<int:pk>',CarUpdateView.as_view(),name='car_UpdateView'),
    path('car/delete/<int:pk>', CarDeleteView.as_view(),name='car_DeleteView' )
]