# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')

from django.shortcuts import render

questions = [
    {
        'question': 'What is the capital of India?',
        'answer': 'New Delhi'
    },
    {
        'question': 'What is the largest mammal?',
        'answer': 'Blue Whale'
    },
    {
        'question': 'What is the smallest planet?',
        'answer': 'Mercury'
    },
    {
        'question': 'What is the chemical symbol for water?',
        'answer': 'H2O'
    },
    {
        'question':'How many continents are there on Earth?',
        'answer':'7'
    },
    {
        'question':'How many colors are there in a rainbow?',
        'answer':'7'
    },
    {
        'question':'How many states are there in India?',
        'answer':'28'
    },
    {
        'question':'What is the full form of ICC?',
        'answer':'International Cricket Council'
    },
    {
        'question':'what is the full form of ISRO?',
        'answer':'Indian Space Research Organisation'
    },
    {
        'question': 'Who won the 2024 cricket world cup?',
        'answer': 'India'
    }

]

def home(request):
    if request.method == "POST":
        score = 0
        
        for i, q in enumerate(questions):
            user_answer = request.POST.get(f'question{i}')
            
            if user_answer and user_answer.strip().lower() == q['answer'].lower():
                score += 1

        return render(request, 'result.html', {
            'score': score,
            'total': len(questions)
        })

    return render(request, 'home.html', {'questions': questions})

