from django.contrib import admin

# Register your models here.

from .models import MeasurementFreq, Place, TypeOfMeasurement, Device, SensorType, Sensor, UpperWarn, LowerWarn, MeasuredValue

#admin.site.register(MeasurementFreq)
#admin.site.register(Place)
#admin.site.register(TypeOfMeasurement)
#admin.site.register(Device)
#admin.site.register(SensorType)
#admin.site.register(Sensor)
admin.site.register(UpperWarn)
admin.site.register(LowerWarn)
#admin.site.register(MeasuredValue)

#sensortypes diplay in admin
class SensorInline(admin.TabularInline):
	model = Sensor

class SensorTypeAdmin(admin.ModelAdmin):
	list_display = ('Name', 'MaxValue', 'MinValue', 'Accuracy')
	inlines = [SensorInline]

admin.site.register(SensorType, SensorTypeAdmin)
	
#sensors display in admin
class SensorAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Description', 'DeviceID', 'TypeID')

admin.site.register(Sensor, SensorAdmin)

#TypeOfMeasurement display in admin
class SensorTypeInline(admin.TabularInline):
    model = SensorType

class TypeOfMeasurementAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Unit')
	inlines = [SensorTypeInline]

admin.site.register(TypeOfMeasurement, TypeOfMeasurementAdmin)

#place display in admin
class PlaceAdmin(admin.ModelAdmin):
	list_display = ('Name', 'Description')

admin.site.register(Place, PlaceAdmin)

from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

#measuredvalues display in admin
class MeasuredValueAdmin(admin.ModelAdmin):
	list_display = ('SensorID', 'Value', 'Date', 'Valid', 'Original')
	list_filter = ('SensorID', 'Valid', 'Original', ('Date', DateTimeRangeFilter))

admin.site.register(MeasuredValue, MeasuredValueAdmin)

#measurementfreq display in admin
class MeasurementFreqAdmin(admin.ModelAdmin):
    list_display = ('Freq',)
    inlines = [SensorTypeInline]
    
admin.site.register(MeasurementFreq, MeasurementFreqAdmin)

#device display in admin
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'PlaceID')
    
admin.site.register(Device, DeviceAdmin)