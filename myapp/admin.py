from django.contrib import admin
from .models import Feature
from .models import CommunityMessage
from .models import ContactMessage
# Register your models here.


admin.site.register(Feature)
admin.site.register(CommunityMessage)
admin.site.register(ContactMessage)