from django.contrib import admin
from .models import TutorflowUsers, AnswersModel, TutorflowModel, Favorites, Feedbacks

# Register your models here.

admin.site.register(TutorflowUsers)
admin.site.register(AnswersModel)
admin.site.register(TutorflowModel)
admin.site.register(Favorites)
admin.site.register(Feedbacks)