from django.contrib import admin
from .models import NeighbourHood,User,Business,Post,Profile

admin.site.register(NeighbourHood)
admin.site.register(User)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Profile)