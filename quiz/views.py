from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import TestSet, Question, Answer
from .serializers import TestSetSerializer, QuestionSerializer, AnswerSerializer
from .forms import AnswerForm
from .utils import calculate_results


class TestSetViewSet(viewsets.ModelViewSet):
    queryset = TestSet.objects.all()
    serializer_class = TestSetSerializer
    permission_classes = [IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


@login_required
@action(detail=True, methods=['get'])
def take_test(request, test_set_id):
    test_set = get_object_or_404(TestSet, id=test_set_id)
    questions = test_set.questions.all()
    total_questions = questions.count()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answers = form.cleaned_data['answers']
            results = calculate_results(questions, answers)
            return render(request, 'results.html', {'results': results})
    else:
        form = AnswerForm()

    return render(request, 'testing/take_test.html',
                  {'test_set': test_set, 'questions': questions, 'form': form, 'total_questions': total_questions})


from django.shortcuts import render

# Create your views here.
