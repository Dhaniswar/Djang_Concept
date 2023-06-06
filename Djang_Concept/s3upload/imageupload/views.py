import uuid
import os
from rest_framework import status
from django.core.files import File
from rest_framework.response import Response
from rest_framework import parsers, renderers
from rest_framework.generics import GenericAPIView
from imageupload.serializers import ImageSerializer
from imageupload.convert_to_webp_and_thumbnail import convert_to_thumbnail, convert_to_webp




class ImageAPIView(GenericAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ImageSerializer
    def post(self, request):

        image_uuid = uuid.uuid4()

        data = request.data

        image = request.data.get('originalImage')

        convert_to_thumbnail(image, image_uuid)
        convert_to_webp(image, image_uuid)

        if "." in str(image):
            extension = str(image).split(".")[-1]
            image_name = ".".join(str(image).split(".")[:-1])   

        thumbnail_path = os.path.join('media','images',f'{image_name}_{image_uuid}.{extension}')
        webp_path = os.path.join('media','images',f'{image_name}_{image_uuid}.webp')


        thumbnail_file = File(open(thumbnail_path, 'rb'))
        webp_file = File(open(webp_path, 'rb'))

        data['pngImage']  = thumbnail_file
        data['webpImage'] = webp_file

        serializer = ImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)