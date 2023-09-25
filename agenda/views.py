from datetime import date
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from agenda.models import Evento


#from  agenda.models import eventos

# Create your views here.

def listar_eventos(request):
    #return HttpResponse("Olá Mundo!")
    eventos = Evento.objects.filter(data__gte=date.today())
    return render(request=request, 
                  context={"eventos": eventos}, 
                  template_name="agenda/listar_evento.html"
                  )


def exibir_evento(request, id):
    #evento = eventos[1]
    evento = get_object_or_404(Evento,id=id)
    #evento = Evento.objects.get(id=id)
    #template = loader.get_template("agenda/exibir_evento.html")
    #rendered_template = template.render(context={"evento": evento}, request=request)
    #return HttpResponse(rendered_template)
    return render(request=request, context={"evento": evento}, template_name="agenda/exibir_evento.html")


def participar_evento(request):
    evento_id = request.POST.get("evento_id")  
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()
    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))