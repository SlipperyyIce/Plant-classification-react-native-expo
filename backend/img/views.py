from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import base64
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import json

# Create your views here.


def prepare(location):
    
    class_name = ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
    model = keras.models.load_model('./plant.keras')

    img = load_img(location, target_size=(180, 180))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    
    
    return {'probability': 100*np.max(score), 'bird_name': class_name[np.argmax(score)], 'bird_details': "a"}


class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            string = posts_serializer.data['content']
            imgData = base64.b64decode(string)
            filename = "hutiya.jpg"
            with open(filename, 'wb') as fl:
                fl.write(imgData)
            som = prepare("hutiya.jpg")
            #return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
            return Response(som, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
