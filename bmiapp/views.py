from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes



def calculatebmi(weight,height):
    length= height/100
    bmi = weight/(length*length)
    return bmi

def calculateBMICategory(bmi):
    if bmi<=18.4:
        return "UnderWeight"
    elif 18.4<bmi<=24.9:
        return "Normal weight"
    elif 25<=bmi<=29.9:
        return "Overweight"
    elif 30<=bmi<=34.9:
        return "Moderately obese"
    elif 35<=bmi<=39.9:
        return "Severely obese"
    else:
        return "Very severely obese"

def calculateHealthRisk(bmi):
    if bmi<=18.4:
        return "Malnutrition risk"
    elif 18.4<bmi<=24.9:
        return "Low risk"
    elif 25<=bmi<=29.9:
        return "Enhanced risk"
    elif 30<=bmi<=34.9:
        return "Medium risk"
    elif 35<=bmi<=39.9:
        return "High risk"
    else:
        return "Very high risk"

@api_view(['POST'])
def data(request):
    data = request.data
    lst=[]
    dictio1 = {}
    overweight_count = 0
    for each in data:
        dictio = {}

        height= float(each['HeightCm'])
        weight= float(each['WeightKg'])

        bmi = calculatebmi(weight,height)
        bmiCategory = calculateBMICategory(bmi)
        bmiHealthRisk = calculateHealthRisk(bmi)

        if bmiCategory == 'Overweight':
            overweight_count = overweight_count+1

        dictio['Gender'] = each['Gender']
        dictio['HeightCm'] = each['HeightCm']
        dictio['WeightKg'] = each['WeightKg']
        dictio['bmi'] = bmi
        dictio['bmiCategory'] = bmiCategory
        dictio['bmiHealthRisk'] = bmiHealthRisk

        lst.append(dictio)

    dictio1['overweight_count'] = overweight_count
    lst.append(dictio1)

    return Response(lst, status=status.HTTP_201_CREATED)