from django.test import TestCase

from .models import QuizType
from quizapp.api.v1.serializers import QuizTypeSerializer

class TestQuizType(TestCase):
    def setUp(self):
        self.quiz_type = QuizType.objects.create(name='Test quiz type')

    def test_data(self):
        serializer = QuizTypeSerializer(self.quiz_type).data

        assert serializer['id'] == self.quiz_type.id