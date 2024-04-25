from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'testsets', views.TestSetViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)

urlpatterns = [
    path('take-test/<int:test_set_id>/', views.take_test, name='take_test'),
]

urlpatterns += router.urls
