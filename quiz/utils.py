def calculate_results(questions, answers):
    correct_answers = 0
    for question in questions:
        if set(answers.getlist('answers')) == set(question.answers.filter(is_correct=True).values_list('id', flat=True)):
            correct_answers += 1
    total_questions = len(questions)
    percentage = (correct_answers / total_questions) * 100
    return {'correct_answers': correct_answers, 'total_questions': total_questions, 'percentage': percentage}
