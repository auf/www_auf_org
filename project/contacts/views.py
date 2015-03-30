# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail

from auf.django.references.models import Region

from .forms import ContacteForm
from .models import Contacte

def contact(request):

    if request.POST:
	form = ContacteForm(request.POST)
	if form.is_valid():
	    data = form.data
	    try:
		email_bureau = Contacte.objects.filter(bureau=Region.objects.filter(id=data['bureau']))[0].email
		send_mail(data['sujet'],data['message'],data['email'],[email_bureau]) 
	    except:
		pass
	    return render_to_response ('contactes.html',{'form':form,'msg_envoie':'Votre message a ete envoyer !'},context_instance = RequestContext(request))
	else:
	    return render_to_response ('contactes.html',{'form':form},context_instance = RequestContext(request))
    form = ContacteForm()
    return render_to_response ('contactes.html',{'form':form},context_instance = RequestContext(request))
