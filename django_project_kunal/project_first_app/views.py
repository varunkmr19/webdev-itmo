from django.shortcuts import render
from django.http import Http404

from . models import Possession, CarOwner

# Create your views here.


def detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)
        possessions = Possession.objects.filter(owner=owner).all()
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    except Possession.DoesNotExist:
        raise Http404("Possession does not exist")

    return render(request, 'project_first_app/owner.html', {
        'owner': owner,
        'possessions': possessions
    })
