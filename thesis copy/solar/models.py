from django.db import models
from unixtimestampfield.fields import UnixTimeStampField
from django.utils import timezone

# Create your models here.
class MeasurementFreq(models.Model):
	Freq = models.FloatField()

	def __str__(self):
		return str(self.Freq)

class Place(models.Model):
	Name = models.CharField(max_length = 200)

	def __str__(self):
		return self.Name

	Note = models.CharField(max_length = 200)
	Lat = models.FloatField()
	Lon = models.FloatField()
	Description = models.CharField(max_length = 200)

class TypeOfMeasurement(models.Model):
	Name = models.CharField(max_length = 200)

	def __str__(self):
		return f'{self.Name} {self.Unit}'

	Unit = models.CharField(max_length = 200)

class Device(models.Model):
	Name = models.CharField(max_length = 200)

	def __str__(self):
		return self.Name

	PlaceID = models.ForeignKey('Place', on_delete=models.SET_NULL, null = True)
	Description = models.CharField(max_length = 200)

class SensorType(models.Model):
	Name = models.CharField(max_length = 200)

	def __str__(self):
		return self.Name

	MaxValue = models.FloatField()
	MinValue = models.FloatField()
	Accuracy = models.FloatField()
	MeasurementFreqID = models.ForeignKey('MeasurementFreq', on_delete =models.SET_NULL, null = True)
	TypeOfMeasurementID =  models.ForeignKey('TypeOfMeasurement', on_delete =models.SET_NULL, null = True)

class Sensor(models.Model):
	Name = models.CharField(max_length = 200)

	def __str__(self):
		return self.Name

	Description = models.CharField(max_length = 200)
	TypeID = models.ForeignKey('SensorType', on_delete = models.SET_NULL, null = True)
	DeviceID = models.ForeignKey('Device', on_delete = models.SET_NULL, null = True)

class UpperWarn(models.Model):
	SensorID = models.ForeignKey('Sensor', on_delete = models.SET_NULL, null = True)
	Value = models.IntegerField()
	FromDate = models.DateTimeField()
	ToDate = models.DateTimeField(null = True)


class LowerWarn(models.Model):
    SensorID = models.ForeignKey('Sensor', on_delete = models.SET_NULL, null = True)
    Value = models.IntegerField()
    FromDate = models.DateTimeField()
    ToDate = models.DateTimeField(null = True)

class MeasuredValue(models.Model):
	SensorID = models.ForeignKey('Sensor', on_delete = models.SET_NULL, null = True)
	Date = UnixTimeStampField(auto_now_add=True, default = timezone.now)
	Value = models.FloatField()
	Valid = models.BooleanField(null = True, blank = True)
	Original = models.BooleanField(null = True, blank = True)

	def __str__(self):
		return f'{self.SensorID.Name} - {self.Value} {self.SensorID.TypeID.TypeOfMeasurementID.Unit}'

	def val(self):
		return self.Value
