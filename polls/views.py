from django.shortcuts import render
from django.http import HttpResponse

from polls.Juego import Juego
from .models import Question
from .models import Answer
from .models import Personaje
from django.template import loader


# Create your views here.

def index(request):
    return HttpResponse("Hola!")


def respondePreguntas(request):
    Juego.setPreguntasTotales(2)
    Juego.ingresarQueryDePreguntas(Question.objects.order_by('?')[:Juego.getPreguntasTotales()])
    context = {
        'listadoDePreguntas': Juego.getQueryDePreguntasSeleccionadas(),
    }
    return render(request, 'polls/index.html', context)


def voteBoard(request):
    context = {
        'listadoDePreguntas': Juego.getQueryDePreguntasSeleccionadas(),
        'listadoDeRespuestas': Answer.objects.order_by('pregunta'),
        'listadoDeUsuarios': Personaje.objects.all()
    }

    if request.method == 'POST':
        usuarioIngresado = request.POST['nombreDeUsuario']
        if not Personaje.objects.filter(nombre=usuarioIngresado).exists():
            Personaje(nombre=usuarioIngresado).save()
           # Respuesta(pregunta=Juego.getQueryDePreguntasSeleccionadas())
            return render(request, 'polls/mainboard.html', context)
            # else:
            #   return HttpResponse("Usted ya se registro, careta!")
    return render(request, 'polls/mainboard.html', context)


def usuarioVota(request):
    if request.method == 'POST':
        votoA = int(request.POST['jugadorA'])
        votoB = int(request.POST['jugadorB'])
        return HttpResponse("Usted voto a Jugador A: %s .. Jugador B: " % (votoA, votoB))
    return HttpResponse("mm error?")
