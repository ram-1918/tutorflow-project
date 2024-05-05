from django.contrib import admin
from .models import Users, TutorModel, AnswersModel, TutorflowModel, Favorites, Feedbacks

# Register your models here.

admin.site.register(Users)
admin.site.register(TutorModel)
admin.site.register(AnswersModel)
admin.site.register(TutorflowModel)
admin.site.register(Favorites)
admin.site.register(Feedbacks)