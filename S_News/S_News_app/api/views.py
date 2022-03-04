from django.core.serializers import serialize
from django.db.models import Q

from S_News_app.models import News_model,Full_image_video_model
from .serializers import News_Serializers,Category_serilizer,Full_image_serializer
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
import json



class News_view(APIView):
    def get(self,request):
        cat= request.GET['category']

        if cat=='ALL':

            data=reversed(News_model.objects.all())

        else:
            jd = json.loads(cat)
            data = reversed(News_model.objects.filter(Category__in=jd))


        # json_data = serialize('json', data)
        resp=News_Serializers(data,many=True)
        # status_code = status.HTTP_500_INTERNAL_SERVER_ERROR if errors else status.HTTP_200_OK
        if data!=0:

            return JsonResponse({'code': 200, 'status': True, 'message': 'ok', 'data': resp.data})
        else:


            return JsonResponse({'code': 400, 'status': False, 'object': 'invalidata', 'data': resp.data})


class News_Category(APIView):
    def get(self,request):
        data=News_model.objects.order_by().values('Category').distinct()
        
        resp=Category_serilizer(data,many=True)
        if len(data) != 0:

            return JsonResponse({'code': 200, 'status': True, 'message': 'ok', 'data': resp.data})
        else:

            return JsonResponse({'code': 400, 'status': False, 'object': 'invalidata', 'data': resp.data})
class Full_image(APIView):
    def get(self, request):
        data = reversed(Full_image_video_model.objects.all())
        # json_data = serialize('json', data)
        resp = Full_image_serializer(data, many=True)
    # status_code = status.HTTP_500_INTERNAL_SERVER_ERROR if errors else status.HTTP_200_OK
        if data != 0:
            return JsonResponse({'code': 200, 'status': True, 'message': 'ok', 'data': resp.data})
        else:
            return JsonResponse({'code': 400, 'status': False, 'object': 'invalidata', 'data': resp.data})

#
# class News_get(APIView):
#     def get(self,Category):
#         if json.data=="తెలంగాణ":
#             data =News_model.objects.filter(Category='తెలంగాణ')
#             res=News_Serializers(data,many=True)
#             return JsonResponse({'demo': res.data})

# class News_get(APIView):
#     def get(self,request):
#         # request.encoding('utf8')
#
#
#
#
#         cat = request.GET['category']
#         print("data",cat[0])
#         print(type(cat))
#
#         jd = json.loads(cat)
#         # print(jd)
#         # print(type(jd))
#         # print(jd[0])
#
#         data = News_model.objects.filter(Category__in=jd)
#         # print(News_model.objects.filter(Category__in=jd).query)
#         # print(News_model.objects.filter(Category__in=['తెలంగాణ','ఆంధ్రప్రదేశ్']).query)
#         resp = News_Serializers(data, many=True)
#
#         return JsonResponse({'data':resp.data})













