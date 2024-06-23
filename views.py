from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    player_choice = request.POST.get('choice')
    result = None
    if player_choice == computer_choice:
        result = 'Tie'
    elif player_choice == 'rock' and computer_choice == 'scissors':
        result = 'You win!'
    elif player_choice == 'paper' and computer_choice == 'rock':
        result = 'You win!'
    elif player_choice == 'scissors' and computer_choice == 'paper':
        result = 'You win!'
    else:
        result = 'You lose.'
    return render(request, 'game/index.html', {'computer_choice': computer_choice, 'player_choice': player_choice, 'result': result})
