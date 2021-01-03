from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView
from django.urls import reverse

from . models import Possession, CarOwner

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


class CarOwnerCreate(CreateView):
    model = CarOwner
    template_name = 'project_first_app/create.html'
    fields = ['name', 'last_name', 'date_of_birth']

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))
