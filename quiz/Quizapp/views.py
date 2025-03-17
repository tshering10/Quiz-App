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

        #  display the score
        total_questions = len(correct_answers)
        result_message = f"You scored {score} out of {total_questions}"

        return render(request, 'Quizapp/basics.html', {'result': result_message})

    # If it's a GET request, render the quiz page
    return render(request, 'Quizapp/basics.html')

def intermediate_view(request):
     if request.method == 'POST':

        correct_answers = {
            
            'q1': 'The code defines a function that adds 2 to the given number.',
            'q2': '10',
            'q3': 'def add_numbers(a, b): return a + b',
            'q4': '3',
            'q5': 'It is used to define default values for function arguments.',
            'q6': 'None of the above',
            'q7': 'None of the above',
            'q8': '100',
            'q9': '5',
            'q10': 'True',
        }
        print(request.POST)
        score = 0

        for question, correct_answer in correct_answers.items():
            selected_answer = request.POST.get(question)
            if selected_answer == correct_answer:
                score += 1

        total_questions = len(correct_answers)
        result_message = f"You scored {score} out of {total_questions}"

        return render(request, 'Quizapp/intermediate.html', {'result': result_message})
     return render(request, 'Quizapp/intermediate.html')

def advanced_view(request):
    if request.method == 'POST':
        correct_answers = {
            
            'q1': 'It allows a method to be accessed like an attribute, without explicitly calling it.',
            'q2': '0 1 2',
            'q3': 'def gen(): yield value',
            'q4': '[1, 2, 3, 1, 2, 3]',
            'q5': 'It is called when a new object is created.',
            'q6': '*args is for variable-length positional arguments, and **kwargs is for variable-length keyword arguments.',
            'q7': 'A `staticmethod` does not require a reference to the instance or class, while a `classmethod` requires a reference to the class.',
            'q8': 'A class that is used to create other classes.',
            'q9': 'It is used to open files in a clean and efficient manner.',
            'q10': '[10, 2, 3]',
        }
        print(request.POST)
        score = 0
        for question, correct_answer in correct_answers.items():
            selected_answer = request.POST.get(question)
            if selected_answer == correct_answer:
                score += 1

        total_questions = len(correct_answers)
        result_message = f"You scored {score} out of {total_questions}"

        return render(request, 'Quizapp/advanced.html', {'result': result_message})
    return render(request, 'Quizapp/advanced.html')

