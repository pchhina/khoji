from django.contrib import admin
from .models import Passion, Goal, PassionComment, GoalComment

# Register your models here.
admin.site.register(Passion)
admin.site.register(Goal)
admin.site.register(PassionComment)
admin.site.register(GoalComment)
