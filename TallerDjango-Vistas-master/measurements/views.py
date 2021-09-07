from django.shortcuts import render

import json
# Create your views here.


from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_one_measurement
from .logic.logic_measurements import del_one_measurement
from .logic.logic_measurements import mod_one_measurement
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')

def get_measurement(request, id):
    measurement = get_one_measurement(id)
    unique_measurement = serializers.serialize('json', [measurement,])
    return HttpResponse(unique_measurement, content_type='application/json')

def del_measurement(request, id):
    measurement = del_one_measurement(id)
    measurement_deleted = serializers.serialize('json', [measurement,])
    return HttpResponse(measurement_deleted, content_type='application/json')

def mod_measurement(request, id, entry):
    measurement = mod_one_measurement(id, entry)
    measurement_modified = serializers.serialize('json', [measurement,])
    return HttpResponse(measurement_modified, content_type='application/json')


    

