from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from things.models import Thing
from things.forms import ThingForm, ContactForm
from django.core.validators import validate_email
from django.core.mail import EmailMessage
import json

class CreateThingAjax(View):
    Thing = Thing
    def post(self, request):
        response_data = {}
        title = request.POST.get('title')
        description = request.POST.get('description')
        author_email = request.POST.get('author_email')
        if (title == None or description == None or author_email == None or validate_email(author_email)):
            response_data['error'] = 'Incorrectly Filled'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        
        response_data['error'] = 'none'
        thing = self.Thing(title=title, description=description, author_email=author_email)
        thing.save()
        
        email_title = 'Link to edit your item'
        email_body = request.META['HTTP_HOST'] + '/edit/' + thing.slug
        
        email = EmailMessage(email_title, email_body, to=[thing.author_email])
        email.send()
        
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    
class EditThingAjax(View):
    Thing = Thing
    def post(self, request):
        slug = request.POST.get('slug')
        thing = get_object_or_404(self.Thing, slug=slug)
        response_data = {}
        title = request.POST.get('title')
        description = request.POST.get('description')
    
        if (title == None or description == None):
            response_data['error'] = 'Incorrectly Filled'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        
        response_data['error'] = 'none'
        thing.title = title
        thing.description = description
        thing.save()
        
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    
class ContactAuthorAjax(View):
    Thing = Thing
    def post(self, request):
        response_data = {}
        id = request.POST.get('id')
        thing = get_object_or_404(self.Thing, id=id)
        
        to_email = [thing.author_email]
        from_ = request.POST.get('from_')
        title = request.POST.get('title')
        body = request.POST.get('body') + '\n\n From: ' + from_
        if (title == None or body == None or from_ == None or validate_email(from_)):
            response_data['error'] = "Invalid Form"
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        email = EmailMessage(title, body, to=to_email)
        email.send()
        response_data['error'] = 'none'
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    
