from django.contrib import admin
from tutorialpost.models import Post,Opencv,AVR,Forum, TutorialModel, TopicsModel

# Register your models here.

admin.site.register(Post)
admin.site.register(Opencv)
admin.site.register(AVR)
admin.site.register(Forum)
admin.site.register(TutorialModel)
admin.site.register(TopicsModel)
