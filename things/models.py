from django.db import models
from things.utils.utils import generate_token

class Thing(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author_email = models.CharField(max_length=255)
    last_edited = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_token()
        super(Thing, self).save()
    
    def __str__(self):
        return self.title