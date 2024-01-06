from django.urls import path

from .views import (
    hello_world,
    quiz_types,
    quiz_type_detail,
    QuestionListAPIView,
    QuestionDetailAPIView
)

urlpatterns = [
    path('', hello_world),
    path('types/', quiz_types),
    path('types/<int:pk>/', quiz_type_detail),
    path('questions/', QuestionListAPIView.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question_deatil')
]
