from django.shortcuts import render, redirect
from .forms import TrainingForm
import time
import random
from time import sleep
from django.http import HttpResponse
from .models import Excercise



def home(request):
    train_type = ''
    train_duration = ''

    submitbutton = request.POST.get("sub")

    form = TrainingForm(request.POST or None)

    if form.is_valid():
        train_type = form.cleaned_data.get("train_type")
        train_duration = form.cleaned_data.get("train_duration")
        request.session['train_type'] = train_type
        request.session['train_duration'] = train_duration

    context= {'form': form, 'train_type': train_type, 
                'train_duration':train_duration,
              'submitbutton': submitbutton}

    return render(request, 'generator/train/type_generator.html', context)
 

def train_generator(request):
    train_duration = request.session['train_duration']
    train_type = request.session['train_type']


    def training_time_scheme(train_duration):
        if train_duration == '15':
            return [4, 5, 3, 3, 0]
                
        elif train_duration == '30':
            return [4, 6, 10, 10, 0]

        elif train_duration == '45':
            return [6, 8, 15, 10, 6]

        else:
            return [6, 10, 20, 14, 8]

    train = training_time_scheme(train_duration)
    [warmup_time, cardio_time, excercises_time, other_time, stretching_time] = train
    request.session['warmup_time'] = warmup_time
    request.session['cardio_time'] = cardio_time
    request.session['excercises_time'] = excercises_time
    request.session['other_time'] = other_time
    request.session['stretching_time'] = stretching_time


    def warmup(warmup_time):
        warmup_list = []
        warmup_exc = Excercise.objects.filter(type_of_excercise='WARMUP')

        for exc in warmup_exc:
            warmup_list.append(exc.name) 

        return warmup_list
  

    def cardio(cardio_time):
        cardio_list = []
        cardio_exc = Excercise.objects.filter(type_of_excercise='CARDIO')
        cardio_time = cardio_time*60
        while cardio_time > 0:
            exc = random.choice(list(cardio_exc))
         
            cardio_time = cardio_time - exc.time
            if cardio_time <0:
                break
            cardio_list.append(exc.name)

        return cardio_list

# CHANGE excercises and karate_exc into Excercise models

    def excercises(excercises_time):  
        excercises_list = []

        abss = {'30 sit ups':1, '50 Lying Floor Leg Raise':2, '50 Crunches':2 }
        legs = {'50 squats':1, '25 half squats with jump':1, '20 (side) leg extension':1}
        arms = {'30 standard pushups':1, '30 pushups narrow':1, '30 pushups wide':1, '30 diamond pushups':1}
        calf = {'Standing calf raise':1}
        backs = {'50 back raising lying':1}
        glutes = {'20 (side) leg raise from front support':1, '20 (side) Lunges':1 }

        if excercises_time == 3:
            body_parts = [abss, legs, arms]
        elif excercises_time == 10:
            body_parts = [abss, legs, arms, calf, backs, glutes, abss, legs, arms, abss]
        elif excercises_time == 15:
            body_parts = [abss, legs, arms, calf, abss, legs, arms, backs, abss, legs, arms, glutes, abss, legs, arms]
        else:
            body_parts = [abss, legs, arms, backs, abss, legs, arms, calf, abss, legs, arms, glutes, abss, legs, arms, backs, abss, legs, arms, abss]

        body_parts_number = 0  

        while excercises_time > 0:
            exc = random.choice(list(body_parts[body_parts_number].keys()))
            exc_value = body_parts[body_parts_number][exc]
            excercises_time = excercises_time - exc_value
            if excercises_time < 0:
                break
            excercises_list.append(exc)

            body_parts_number += 1

        return excercises_list


    def karate_exc(other_time):
        other_list = []

        kihon = {'50 seiken chudan tsuki':1, '40 maygeri':1, '30 gedan barai':1, '30 uchi uke':1, '30 soto uke':1, '30 jodan uke':1}
        kata = {'taikyoku kata sono ichi':2, 'taikyoku kata sono ni':2, 'pinan kata sono ichi':2, 'pinan kata sono ni':2, 'seipai kata':2}

        if other_time == 2:
            karate_parts = [kihon, kihon]
        else:
            karate_parts = [kata, kihon, kihon, kihon, kata, kihon, kihon, kihon, ]

        karate_parts_number = 0 
        while other_time > 0:

            exc = random.choice(list(karate_parts[karate_parts_number].keys()))
            exc_value = karate_parts[karate_parts_number][exc]
            other_time = other_time - exc_value
            if other_time <0:
                break

            other_list.append(exc)
            karate_parts_number += 1
            
        return other_list


    def universal_exc(other_time):
        excercises(other_time)


    cardio_list = cardio(cardio_time)
    warmup_list = warmup(time)
    excercises_list = excercises(excercises_time)
    if train_type == 'KARATE':
        other_list = karate_exc(other_time)
    else:
        other_list = excercises(other_time)
            

    context = {'cardio_time':cardio_time, 'cardio':cardio, 'cardio_list':cardio_list, 
    'warmup':warmup, 'warmup_list':warmup_list, 'warmup_time':warmup_time, 'train_duration':train_duration, 
    'train_type':train_type, 'stretching_time':stretching_time, 'excercises_time':excercises_time, 
    'other_time':other_time, 'excercises_list':excercises_list, 'other_list':other_list, 'other_time':other_time}


    return render(request, 'generator/train/train_generator.html', context)
    #return render(request, 'generator/train/countdown.html', context)
    

# time=60


def countdown(request):
    train_duration = request.session['train_duration']
    warmup_time = request.session['warmup_time']
   #  def counting(time):

   #  t=60
   #  t = int(t)
   # # while t:
   #  mins = int(t) // 60
   #  secs = int(t) % 60
   #  timer = '{:02d}:{:02d}'.format(mins, secs)
    
   #  #time.sleep(1)
   #  #t -= 1

    context = {'train_duration':train_duration, 'warmup_time':warmup_time}

    return render(request, 'generator/train/countdown.html', context)

