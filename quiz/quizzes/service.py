from rest_framework import viewsets,mixins,views

from .serializers import *
from .models import *
from rest_framework.response import Response





class QuizService(mixins.ListModelMixin,viewsets.GenericViewSet):

    def get_queryset(self):
        # params = self.request.query_params
        queryset= response.objects
        return queryset
    
    def filter_queryset(self, queryset):
        # params = self.request.query_params
       
        return queryset
    
    def get_serializer_class(self):
        return quizserializer
    
   

class responseService(views.APIView):

    def get(self, request, format=None):
        print('am i isnide')
        queryset= response.objects.all()
        qs={}
        scre=0
        print(queryset)
        for val in queryset:
            print(val.question,val.answer.question ,val.answer.correct)
            
            if val.question == val.answer.question and val.answer.correct:
                print(val.answer.correct)
                try:
                    scre=scre+1
                    qs[val.attemptee.user.username] = scre
                except:
                    pass
                
        return Response(
        qs
        )

