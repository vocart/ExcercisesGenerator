from django import forms


TRAINING_TYPES = [
        ('KARATE', 'KARATE'),
        ('STANDARD', 'STANDARD'),
        ('CARDIO', 'CARDIO'),
        ('STRETCHING', 'STRETCHING'),

        ]       

TRAINING_DURATION = [
        ('15', '15'),
        ('30', '30'),
        ('45', '45'),
        ('60', '60'),
        ]   

class TrainingForm(forms.Form):
    train_type = forms.CharField(label='Choose the type of training:', widget=forms.RadioSelect(choices = TRAINING_TYPES))
    train_duration = forms.CharField(label='Choose the duration of training:', widget=forms.RadioSelect(choices = TRAINING_DURATION))
