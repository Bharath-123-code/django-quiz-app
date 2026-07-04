from django.shortcuts import render, redirect
from .models import Question, HighScore
import random

def home(request):
    if request.method == "POST":
        score = 0
        review_data = []
        player_name = request.POST.get('player_name', 'Anonymous')
        
        # We need to reconstruct the questions that were shown
        question_ids_str = request.POST.get('question_ids', '')
        if question_ids_str:
            question_ids = [q_id.strip() for q_id in question_ids_str.split(',') if q_id.strip()]
            for q_id in question_ids:
                try:
                    question = Question.objects.get(id=q_id)
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
                except Question.DoesNotExist:
                    continue
        else:
            # Fallback to old behavior if question_ids is missing
            for key, value in request.POST.items():
                if key.startswith('question_'):
                    q_id = key.split('_')[1]
                    try:
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
                    except Question.DoesNotExist:
                        continue

        # Save to Leaderboard
        HighScore.objects.create(player_name=player_name, score=score)
        leaderboard = HighScore.objects.all()[:10]

        return render(request, 'result.html', {
            'score': score,
            'total': len(review_data),
            'review_data': review_data,
            'leaderboard': leaderboard
        })

    # Get all questions and select 15 random ones
    all_questions = list(Question.objects.all())
    if len(all_questions) >= 15:
        questions = random.sample(all_questions, 15)
    else:
        questions = all_questions  # If fewer than 15 questions, use all available
    return render(request, 'home.html', {
        'questions': questions
    })

from django.http import JsonResponse
from django.db import connection
import os

def debug_deploy(request):
    info = {
        'DATABASE_URL_PRESENT': 'DATABASE_URL' in os.environ,
        'DATABASE_URL_VALUE': os.environ.get('DATABASE_URL', '')[:30] + '...' if 'DATABASE_URL' in os.environ else None,
        'DEBUG': os.environ.get('DEBUG'),
        'RENDER': os.environ.get('RENDER'),
        'DB_SETTINGS': {
            'ENGINE': connection.settings_dict.get('ENGINE'),
            'NAME': connection.settings_dict.get('NAME'),
            'HOST': connection.settings_dict.get('HOST'),
            'PORT': connection.settings_dict.get('PORT'),
            'USER': connection.settings_dict.get('USER'),
        }
    }
    try:
        from quiz.models import Question, HighScore
        info['QUESTION_COUNT'] = Question.objects.count()
        info['HIGHSCORE_COUNT'] = HighScore.objects.count()
        info['CONNECTION_OK'] = True
    except Exception as e:
        import traceback
        info['CONNECTION_OK'] = False
        info['ERROR'] = str(e)
        info['TRACEBACK'] = traceback.format_exc()
        
    return JsonResponse(info)