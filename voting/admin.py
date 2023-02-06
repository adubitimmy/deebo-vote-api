from django.contrib import admin
from .models import Candidates, Vote, RequestForm

# Register your models here.
admin.site.register([Candidates,Vote,RequestForm])
