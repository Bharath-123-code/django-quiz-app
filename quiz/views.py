from django.shortcuts import render
import random
import threading
from datetime import datetime
from .questions import QUESTIONS

# Thread-safe in-memory leaderboard
LEADERBOARD_LOCK = threading.Lock()
LEADERBOARD = []

def home(request):
    if request.method == "POST":
        score = 0
        review_data = []
        player_name = request.POST.get('player_name', 'Anonymous')
        
        # Reconstruct the questions that were shown using static list index lookup
        question_ids_str = request.POST.get('question_ids', '')
        if question_ids_str:
            question_ids = [int(q_id.strip()) for q_id in question_ids_str.split(',') if q_id.strip()]
            for q_id in question_ids:
                if 0 <= q_id < len(QUESTIONS):
                    question = QUESTIONS[q_id]
                    value = request.POST.get(f'question_{q_id}', '')
                    is_correct = (value == question.correct_answer)
                    
                    if is_correct:
                        score += 1
                    
                    review_data.append({
                        'text': question.question_text,
                        'user_choice': value,
                        'correct_answer': question.correct_answer,
                        'is_correct': is_correct
                    })
        else:
            # Fallback to key scanning if question_ids is missing
            for key, value in request.POST.items():
                if key.startswith('question_'):
                    try:
                        q_id = int(key.split('_')[1])
                        if 0 <= q_id < len(QUESTIONS):
                            question = QUESTIONS[q_id]
                            is_correct = (value == question.correct_answer)
                            if is_correct:
                                score += 1
                            review_data.append({
                                'text': question.question_text,
                                'user_choice': value,
                                'correct_answer': question.correct_answer,
                                'is_correct': is_correct
                            })
                    except ValueError:
                        continue

        # Save to in-memory leaderboard
        new_entry = {
            'player_name': player_name,
            'score': score,
            'date_achieved': datetime.now()
        }
        with LEADERBOARD_LOCK:
            LEADERBOARD.append(new_entry)
            # Sort by score descending, then date_achieved descending
            LEADERBOARD.sort(key=lambda x: (x['score'], x['date_achieved']), reverse=True)
            # Limit global cache size to top 100 entries to prevent memory leak
            if len(LEADERBOARD) > 100:
                LEADERBOARD.pop()
            leaderboard_display = list(LEADERBOARD[:10])

        return render(request, 'result.html', {
            'score': score,
            'total': len(review_data),
            'review_data': review_data,
            'leaderboard': leaderboard_display
        })

    # GET request: select 15 random unique questions from QUESTIONS list
    if len(QUESTIONS) >= 15:
        questions = random.sample(QUESTIONS, 15)
    else:
        questions = QUESTIONS

    # Get the current leaderboard
    with LEADERBOARD_LOCK:
        leaderboard_display = list(LEADERBOARD[:10])

    return render(request, 'home.html', {
        'questions': questions,
        'leaderboard': leaderboard_display
    })