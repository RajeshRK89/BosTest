from rest_framework import routers
from django.conf.urls import url, include
# from django.urls import path

router = routers.SimpleRouter()

from .service import *

router.register(r'quiz', QuizService, 'quiz')
# router.register(r'score',responseService.as_view())

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'score',responseService.as_view())
]