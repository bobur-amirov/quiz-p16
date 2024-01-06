from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import QuizTypeSerializer, QuestionSerializer
from ...models import QuizType, Question


@api_view(['GET'])
def hello_world(request):

    data = {'message': 'hello world'}
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def quiz_types(request):
    if request.method == 'GET':
        quiz_types = QuizType.objects.all()
        serializer = QuizTypeSerializer(quiz_types, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = QuizTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def quiz_type_detail(request, pk):

    try:
        quiz_type = QuizType.objects.get(pk=pk)
    except QuizType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuizTypeSerializer(quiz_type)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = QuizTypeSerializer(quiz_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        quiz_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class QuestionListAPIView(APIView):
#     def get(self, request, format=None):
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True, context={'request': self.request})
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


class QuestionListAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # authentication_classes = [TokenAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class QuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = []
    permission_classes = []


