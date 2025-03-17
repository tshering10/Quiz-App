from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    return render(request, 'Quizapp/home.html')

@login_required
def dashboard(request):
    return render(request, 'Quizapp/dashboard.html')

def basic_view(request):
    if request.method == 'POST':
        # Correct answers for the questions
        correct_answers = {
            'q1': 'def function_name:',
            'q2': 'List',
            'q3': '8',
            'q4': 'except',
            'q5': 'len()',
            'q6': 'Instance of the class',
            'q7': 'setter',
            'q8': 'append()',
            'q9': 'Skip the rest of the current iteration',
            'q10': 'import module_name',
        }
        print(request.POST)
        score = 0

        # Check each question answer
        for question, correct_answer in correct_answers.items():
            selected_answer = request.POST.get(question)
            if selected_answer == correct_answer:
                score += 1

        # Calculate the percentage or simply display the score
        total_questions = len(correct_answers)
        result_message = f"You scored {score} out of {total_questions}"
        print(f" CComparing '{selected_answer}' to '{correct_answer}'")  # Debugging line


        return render(request, 'Quizapp/basics.html', {'result': result_message})

    # If it's a GET request, render the quiz page
    return render(request, 'Quizapp/basics.html')

def intermediate_view(request):
    return render(request, 'Quizapp/intermediate.html')

def advanced_view(request):
    return render(request, 'Quizapp/advanced.html')

