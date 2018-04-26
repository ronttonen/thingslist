from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from things.models import Thing
from things.forms import ThingForm, ContactForm, EditThingForm
from django.core.validators import validate_email
from django.core.mail import EmailMessage
import json


class HomeView(View):
    Thing = Thing
    
    def get(self, request):
        things = self.Thing.objects.all().order_by('-last_edited')
        
        return render(template_name='home.html',request=self.request, context={'things' : things})
    
   

class CreateThing(View):
    Thing = Thing
    ThingForm = ThingForm
    def get(self, request):
        form = self.ThingForm
        return render(template_name="create_thing.html", request=self.request, context={'form':form})
          
       

class ThingView(View):
    Thing = Thing
    
    def get(self, request, id):
        thing = get_object_or_404(self.Thing, id=id)
        return render(template_name="thing.html", request=self.request, context={'thing': thing})
   
class EditThing(View):
    Thing = Thing
    EditThingForm = EditThingForm
    def get(self, request, slug):
        thing = get_object_or_404(self.Thing, slug=slug)
        form = self.EditThingForm
        return render(template_name='edit_thing.html', request=self.request, context={'thing': thing, 'form':form})
    
    def post(self, request, slug):
        slug = request.POST.get('slug')
        self.Thing.objects.filter(slug=slug).delete()
        
        return redirect('/')

    
class ContactAuthor(View):
    Thing = Thing
    ContactForm = ContactForm
    def get(self, request, id):
        thing = get_object_or_404(self.Thing, id = id)
        form = self.ContactForm
        
        return render(template_name='contact_author.html', request=self.request, context={'thing': thing, 'form':form})
    
    
