from django.contrib import admin
from .models import Feedback
from .models import Items
from .models import Clients
from .models import Orders


admin.site.register(Feedback)
# Register your models here.
admin.site.register(Items)
admin.site.register(Clients)
admin.site.register(Orders)
