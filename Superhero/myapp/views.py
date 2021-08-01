from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse

# Create your views here.
def index(request):
    all_superheros = Superhero.object.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'Superhero/index.html', context)

def detail(request, superhero_id):
    heros = Superhero.objects.get(id=superhero_id)
    context = {
        'hero': hero
    }
    return render(request, 'Superhero/details.html', context)


def creator(request):
    if request.methhod == "POST":
        superheros_names = request.POST.get('superheros_names')
        alter_ego_name = request.POST.get('alter_ego_name')
        prim_ability = request.POST.get('prim_ability')
        second_ability = request.POST.get('second_ability')
        catchphrase = request.POST.get('second_ability')
        new_hero = Superhero(superheros_names=superheros_names, alter_ego_name=alter_ego_name, prim_ability=prim_ability, second_ability=second_ability, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('Superhero:index'))
    else:
        return render(request, 'Superhero/create.html')
def edit(request, superhero_id):
    heros = Superhero.objects.get(id=superhero_id)
    if request.method == "POST":
        heros.superheros_names = request.POST.get('superheros_names')
        heros.alter_ego_name = request.POST.get('alter_ego_name')
        heros.prim_ability = request.POST.get('prim_ability')
        heros.second_ability = request.POST.get('second_ability')
        heros.catchphrase = request.POST.get('second_ability')
        heros.save()
        return render(request, ('Superhero:index'))
        else:
            context = {
                'heros': heros
            }
            return render(request, 'Superhero/edit.html', context)

def delete(request, superhero_id):
    heros = Superhero.objects.get(id=superhero_id)
    heros.delete()
    all_heros = Superhero.objects.all()
    context = {
        'all_heros': all_heros
    }
    return render(request, 'Superhero/index.html', context)
        