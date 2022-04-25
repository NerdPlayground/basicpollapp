from django.http import Http404
from django.urls import reverse
from django.test import TestCase
from choices.models import Choice
from questions.views import question
from questions.models import Question

class QuestionModel(TestCase):
    def test_objest_representation(self):
        question= Question.objects.create(
            title= "Choose",
            body= "Friday night out or Netflix and Chill?",
        )
        self.assertEquals(question.__str__(),question.title)

class QuestionAPIView(TestCase):
    def generate_question(self):
        question= Question.objects.create(
            title= "Question",
            body= "This is a Question"
        )
        choices= (
            Choice.objects.create(
                question=question,
                body= "This is the First Choice"
            ),
            Choice.objects.create(
                question=question,
                body= "This is the Second Choice"
            ),
        )
        return question,choices
    
    def test_home_api_view_with_questions(self):
        self.generate_question()
        response= self.client.get(reverse("questions:home"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"questions/home.html")
        self.assertEquals(len(response.context['questions']),1)

    def test_home_api_view_without_questions(self):
        response= self.client.get(reverse("questions:home"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"questions/home.html")
        self.assertEquals(len(response.context['questions']),0)

    def test_question_api_view_question_exists(self):
        question,choices= self.generate_question()
        response= self.client.get(
            reverse(
                "questions:question",
                args=(question.id,)
            )
        )
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"questions/question.html")
        self.assertEquals(len(response.context["choices"]),len(choices))

    def test_question_api_view_question_does_not_exist(self):
        response= self.client.get(
            reverse(
                "questions:question",
                args=("e6c31bc6-36d7-4d9c-a2a5-6ea5725b0a34",)
            )
        )
        self.assertEquals(response.status_code,404)
    
    def test_vote_api_view_user_votes(self):
        question,choices= self.generate_question()
        post_data= {"choice":choices[0].id}
        response= self.client.post(
            reverse(
                "questions:vote",
                args=(question.id,)
            ),
            post_data
        )
        self.assertRedirects(
            response,
            reverse(
                "questions:results",
                args=(question.id,)
            )
        )
    
    def test_vote_api_view_user_does_not_vote(self):
        question,choices= self.generate_question()
        post_data= {}
        response= self.client.post(
            reverse(
                "questions:vote",
                args=(question.id,)
            ),
            post_data
        )
        self.assertRaises((KeyError,Choice.DoesNotExist,))
        self.assertEquals("You didn't select a choice.",response.context["error_message"])
        self.assertTemplateUsed(response,"questions/question.html")
    
    def test_vote_api_view_question_does_not_exist(self):
        post_data= {}
        response= self.client.post(
            reverse(
                "questions:vote",
                args=("e6c31bc6-36d7-4d9c-a2a5-6ea5725b0a34",)
            ),
            post_data
        )
        self.assertRaises(Http404)
    
    def test_results_api_view_question_exists(self):
        question,choices= self.generate_question()
        response= self.client.get(
            reverse(
                "questions:results",
                args=(question.id,)
            )
        )
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"choices/results.html")
    
    def test_results_api_view_question_does_not_exist(self):
        self.client.get(
            reverse(
                "questions:results",
                args=("e6c31bc6-36d7-4d9c-a2a5-6ea5725b0a34",)
            )
        )
        self.assertRaises(Http404)
