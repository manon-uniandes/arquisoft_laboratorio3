from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_one_measurement(id):
    measurement = Measurement.objects.get(pk=id)
    return measurement

def del_one_measurement(id):
    measurement = Measurement.objects.filter(pk=id).delete()
    return measurement

def mod_one_measurement(id, entry):
    measurement = Measurement.objects.select_related().filter(pk=id).update(value=entry)
    return measurement




