from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
from things.models import Thing
from things.forms import ThingForm, ContactForm, EditThingForm
from django.core.validators import validate_email
from django.core.mail import EmailMessage
import json

class CreateThingAjax(View):
    Thing = Thing
    ThingForm = ThingForm
    def post(self, request):
        form = self.ThingForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        response_data = {}
        title = request.POST.get('title')
        description = request.POST.get('description')
        author_email = request.POST.get('author_email')
        if validate_email(author_email):
            return HttpResponseBadRequest()
        
        thing = self.Thing(title=title, description=description, author_email=author_email)
        thing.save()
        
        response_data['edit'] = 'false'
        
        email_title = 'Link to edit your item'
        email_body = request.META['HTTP_HOST'] + '/edit/' + thing.slug
        
        email = EmailMessage(email_title, email_body, to=[thing.author_email])
        email.send()
        
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    
class EditThingAjax(View):
    Thing = Thing
    EditThingForm = EditThingForm
    def post(self, request):
        form = self.EditThingForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        
        slug = request.POST.get('slug')
        thing = get_object_or_404(self.Thing, slug=slug)
        response_data = {}
        title = request.POST.get('title')
        description = request.POST.get('description')
        thing.title = title
        thing.description = description
        thing.save()
        response_data['edit'] = 'true'
        
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    
class ContactAuthorAjax(View):
    Thing = Thing
    ContactForm = ContactForm
    def post(self, request):
        form = self.ContactForm(request.POST)
        response_data = {}
        if not form.is_valid():
            return HttpResponseBadRequest()
        
        id = request.POST.get('id')
        thing = get_object_or_404(self.Thing, id=id)
        to_email = [thing.author_email]
        from_ = request.POST.get('from_')
        title = request.POST.get('title')
        body = request.POST.get('body') + '\n\n From: ' + from_
        if validate_email(from_):
            return HttpResponseBadRequest()
        
        response_data['edit'] = 'false'
        
        email = EmailMessage(title, body, to=to_email)
        email.send()
       
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    
