from django import forms

class ThingForm(forms.Form):
    title = forms.CharField(label="Title", max_length=55,  widget=forms.TextInput())
    description = forms.CharField(label="Description", max_length=2255,  widget=forms.Textarea(attrs={'class':'materialize-textarea'}))
    author_email =forms.CharField(label='Email',max_length=55, widget=forms.TextInput(attrs={'type':'email','class':'validate'}))
    
class ContactForm(forms.Form):
    title = forms.CharField(label="Title", required=True, max_length=55,  widget=forms.TextInput())
    body = forms.CharField(label="Body", required = True, max_length=2255,  widget=forms.Textarea(attrs={'class':'materialize-textarea'}))
    from_ = forms.CharField(label='From', required=True, max_length=55, widget=forms.TextInput(attrs={'type':'email','class':'validate'}))
    
        