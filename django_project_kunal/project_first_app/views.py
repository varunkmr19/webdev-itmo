from project_first_app.forms import CarForm
from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from . models import Car, Possession, CarOwner

# Create your views here.


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
        possessions = Possession.objects.filter(owner=owner).all()
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")

    return render(request, 'project_first_app/owner.html', {
        'owner': owner,
        'possessions': possessions
    })


def car_detail(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404('Car does not exist')

    return render(request, 'project_first_app/car.html', {
        'car': car
    })


class CarOwnerCreate(CreateView):
    model = CarOwner
    template_name = 'project_first_app/create.html'
    fields = ['name', 'last_name', 'date_of_birth']

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class AddCar(CreateView):
    model = Car
    template_name = 'project_first_app/add_car.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse('car_detail', args=(self.object.id,))


class UpdateCar(UpdateView):
    model = Car
    template_name = 'project_first_app/add_car.html'
    fields = ['marks', 'model', 'number_guest', 'color']

    def get_success_url(self):
        return reverse('car_detail', args=(self.object.id,))
