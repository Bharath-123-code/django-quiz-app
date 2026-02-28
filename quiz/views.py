from django.shortcuts import render, redirect
from .models import Question, HighScore

def home(request):
    if request.method == "POST":
        score = 0
        review_data = []
        player_name = request.POST.get('player_name', 'Anonymous')
        
        # We need to reconstruct the questions that were shown
        for key, value in request.POST.items():
            if key.startswith('question_'):
                q_id = key.split('_')[1]
                question = Question.objects.get(id=q_id)
                is_correct = (value == question.correct_answer)
                
                if is_correct:
                    score += 1
                
                review_data.append({
                    'text': question.question_text,
                    'user_choice': value,
                    'correct_answer': question.correct_answer,
                    'is_correct': is_correct
                })

        # Save to Leaderboard
        HighScore.objects.create(player_name=player_name, score=score)
        leaderboard = HighScore.objects.all()[:10]

        return render(request, 'result.html', {
            'score': score,
            'total': len(review_data),
            'review_data': review_data,
            'leaderboard': leaderboard
        })

    questions = Question.objects.order_by('?')[:15]
    return render(request, 'home.html', {'questions': questions})