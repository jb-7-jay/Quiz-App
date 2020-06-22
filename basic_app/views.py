from django.shortcuts import render,redirect
from .models import Quiz,Scorrer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request,'index.html')

@login_required()
def quiz(request):
    questions = Quiz.objects.all()
    args = {'questions':questions}
    return render(request,'quiz/quiz.html',args)

score = 0
@login_required()
def answer(request):
    questions = Quiz.objects.all()
    global score
    score = 0
    if request.method == 'POST':     
        
        for question in questions:
            correct_answer = question.answer
            entered_answer = request.POST.get(str(question.id))
            if(entered_answer == correct_answer): 
                score+=1 
                
        # total_score = Scorrer.objects.all()

        user_score = Scorrer()
        user_score.owner =request.user
        user_score.scored = score
        user_score.save()
        messages.success(request, f'Your score is {score},which Added at the Last')
        return redirect('leader')
        # user_score = Scorrer.objects.get(owner=request.user).update(scored=score)
        # user_score.save()
    # else:
    #     score = 0 

    args = {'score':score}
    return render(request,'quiz/leader.html',args)  

def leader(request):
    global score
    
    scores = Scorrer.objects.all()
    args = {'scores':scores}
    return render(request,'quiz/leader.html',args)