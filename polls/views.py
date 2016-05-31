from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import Answer
from .models import Personaje
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("Hola!")


def respondePreguntas(request):
    listadoDePreguntas = Question.objects.order_by('?')[:5]
    template = loader.get_template('polls/index.html')

    context = {
        'listadoDePreguntas': listadoDePreguntas,
    }
    return render(request,'polls/index.html',context)


def voteBoard(request):
    if(request.method == 'POST'):
        usuarioIngresado = request.POST['nombreDeUsuario']
        Personaje(nombre=usuarioIngresado).save()

    return HttpResponse(usuarioIngresado)
