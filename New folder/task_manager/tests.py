from django.test import TestCase
from .models import Task
from .ai_engine import predict_duration

class TaskAIIntegrationTest(TestCase):
    def test_ml_prediction_logic(self):
        # Test if complexity 3 returns a valid float prediction
        prediction = predict_duration(3)
        self.assertIsInstance(prediction, float)
        self.assertGreater(prediction, 0)

    def test_task_creation(self):
        # Test if SQL saving works
        task = Task.objects.create(title="Test Task", complexity=2)
        self.assertEqual(task.title, "Test Task")