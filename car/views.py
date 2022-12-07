from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Car
from django.urls import reverse_lazy
# Create your views here.
class CarListView(ListView):
    template_name = 'car/car_ListView.html'
    model = Car

class CarDetailView(DetailView):
    template_name = 'car/car_DetailView.html'
    model = Car

class CarCreateView(CreateView):
    template_name = 'car/car_CreateView.html'
    model = Car
    fields = ['name','purchaser','description','model','images']

class CarUpdateView(UpdateView):
    template_name = 'car/car_UpdateView.html'
    model = Car
    fields = ['name','purchaser','description','model','images']

class CarDeleteView(DeleteView):
    template_name = 'car/car_DeleteView.html'
    model = Car
    success_url = reverse_lazy('car_listview')

