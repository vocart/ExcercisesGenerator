from django.shortcuts import render, redirect
from .forms import TrainingForm


def home(request):

    submitbutton = request.POST.get("sub")
    train_type = ''
    train_duration = ''
    form = TrainingForm(request.POST or None)

    if form.is_valid():
        train_type = form.cleaned_data.get("train_type")
        train_duration = form.cleaned_data.get("train_duration")
        
    context= {'form': form, 'train_type': train_type, 
                'train_duration':train_duration,
              'submitbutton': submitbutton}

    return render(request, 'generator/train/type_generator.html', context)

    




def train_generator(request):
    return render(request, 'generator/train/train_generator.html')
