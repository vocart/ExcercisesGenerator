from django.db import models


class Excercise(models.Model):
	LIST_OF_TYPES = [
        ('KARATE', 'KARATE'),
        ('STANDARD', 'STANDARD'),
        ('CARDIO', 'CARDIO'),
        ('STRETCHING', 'STRETCHING'),
        ('WARMUP', 'WARMUP'), 
        ]

	LIST_OF_BODY_PARTS = [
        ('HEAD', 'HEAD'),
        ('ARMS', 'ARMS'),
        ('LEGS', 'LEGS'),
        ('ABS', 'ABS'),
        ('BACKS', 'BACKS'),
        ('GLUTES', 'GLUTES'),
        ('MULTI', 'MULTI'),
        ]


	name = models.CharField(max_length=30)
	type_of_excercise = models.CharField(max_length=30, choices = LIST_OF_TYPES, default = 'STANDARD')
	time = models.IntegerField(null=True)
	repeats = models.IntegerField(null=True)
	body_part = models.CharField(max_length=30, choices = LIST_OF_BODY_PARTS, default = 'MULTI')

	def __str__(self):
		return self.name




		