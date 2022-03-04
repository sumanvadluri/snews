from rest_framework import serializers

from S_News_app.models import News_model,Full_image_video_model
from rest_framework.status import  HTTP_200_OK

# class News_Serializers(serializers.ModelSerializer):
#     # tittle = serializers.SerializerMethodField('Title')
#     # discription = serializers.SerializerMethodField('Discription')
#     # image = serializers.SerializerMethodField('Image')
#     # catogery = serializers.SerializerMethodField('Category')
#     # date = serializers.SerializerMethodField('News_Date')
#
#     class Meta:
#         model=News_model
#         fields=['Title','Discription','Image','Category','News_Date']








class News_Serializers(serializers.ModelSerializer):
    # code = 200
    # status = True
    # message = 'ok'
    class Meta:
        model=News_model
        fields=['Title','Discription','Image','Category','News_Date','news_resource','Upload_view']



class Category_serilizer(serializers.ModelSerializer):
    class Meta:
        model=News_model
        fields=['Category']


class Full_image_serializer(serializers.ModelSerializer):
    class Meta:
        model=Full_image_video_model
        fields =['Upload_field_type','Image','upload_time']




