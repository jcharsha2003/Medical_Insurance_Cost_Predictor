from django.db import models

# Create your models here.
class Insurance(models.Model):
    MALE= 1
    FEMALE= 0
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    SOUTHEAST = 0
    SOUTHWEST = 1
    NORTHEAST = 2
    NORTHWEST = 3
    REGION_CHOICES =(
        (NORTHWEST,'Northwest'),
        (NORTHEAST,'Northeast'),
        (SOUTHWEST, 'Southwest'),
        (SOUTHEAST, 'Southeast'),
    )
    YES=1
    NO=0
    DIABETES_CHOICES=(
        (YES,'Yes'),
        (NO,'No')
    )
    BLOOD_PRESSURE_PROBLEMS_CHOICES=(
        (YES,'Yes'),
        (NO,'No')
    )
    ANY_TRANSPLANTS_CHOICES=(
        (YES,'Yes'),
        (NO,'No')
    )
    ANY_CHRONIC_DISEASES_CHOICES=(
        (YES,'Yes'),
        (NO,'No')
    )
    KNOWN_ALLERGIES_CHOICES=(
        (YES,'Yes'),
        (NO,'No')


    )
    HISTORY_CHOICES=(
        (YES,'Yes'),
        (NO,'No')
    )
    NMS_CHOICES=(
         (YES,'Yes'),
        (NO,'No')
    )

    age = models.FloatField()
    sex = models.IntegerField(choices=SEX_CHOICES)
    bmi = models.FloatField()
    children = models.FloatField()
    smoker = models.IntegerField(choices=((0,'Smoker'),(1,'non-Smoker')))
    region = models.IntegerField(choices= REGION_CHOICES)
    diabetes=models.IntegerField(choices=DIABETES_CHOICES)
    bPP=models.IntegerField(choices=BLOOD_PRESSURE_PROBLEMS_CHOICES)
    anyTransplants=models.IntegerField(choices=ANY_TRANSPLANTS_CHOICES)
    anyChronicDiseases=models.IntegerField(choices=ANY_CHRONIC_DISEASES_CHOICES,default=NO)
    height=models.FloatField()
    weight=models.FloatField()
    knownAllergies=models.IntegerField(choices=KNOWN_ALLERGIES_CHOICES)
    history=models.IntegerField(choices=HISTORY_CHOICES)
    nms=models.IntegerField(choices=NMS_CHOICES)

###{"age":45,"sex":1,"bmi":20,"children":2,"smoker":1,"region":0,"diabetes":1,"bPP":1,"anyTransplants":1,"anyChronicDiseases":1,"height":166,"weight":60,"knownAllergies":1,"history":1,"nms":1}
###{"age":20,"sex":0,"bmi":19,"children":0,"smoker":0,"region":2,"diabetes":0,"bPP":0,"anyTransplants":0,"anyChronicDiseases":0,"height":168,"weight":53,"knownAllergies":1,"history":0,"nms":0}