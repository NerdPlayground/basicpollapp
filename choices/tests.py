from django.test import TestCase
from choices.models import Choice
from questions.models import Question

class ChoiceModel(TestCase):
    def test_objest_representation(self):
        question= Question.objects.create(
            title="Question",
            body="This is a question"
        )
        choice= Choice.objects.create(
            question=question,
            body="This is a choice",
        )

        self.assertEquals(choice.__str__(),choice.body)