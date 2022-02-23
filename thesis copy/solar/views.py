from cProfile import label
from time import strftime
from MySQLdb import Date
from django.shortcuts import render
import numpy as np

# Create your views here.

from .models import MeasurementFreq, Place, TypeOfMeasurement, Device, SensorType, Sensor, UpperWarn, LowerWarn, MeasuredValue
from django.http import JsonResponse

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_sensors = SensorType.objects.all().count()
    num_instances = Sensor.objects.all().count()
    
    #wattage
    wattage = MeasuredValue.objects.filter(SensorID__exact=5).latest('Date')
    
    #inverter last measurements
    place1 = Place.objects.filter(id__exact=1).first()
    temp1_last_measurement = MeasuredValue.objects.filter(SensorID__exact=1).latest('Date')
    temp2_last_measurement = MeasuredValue.objects.filter(SensorID__exact=4).latest('Date')
    hum_last_measurement = MeasuredValue.objects.filter(SensorID__exact=2).latest('Date')
    press_last_measurement = MeasuredValue.objects.filter(SensorID__exact=3).latest('Date')
    
    #solar panel last measurements
    place2 = Place.objects.filter(id__exact=2).first()
    temp1_last_measurement2 = MeasuredValue.objects.filter(SensorID__exact=6).latest('Date')
    temp2_last_measurement2 = MeasuredValue.objects.filter(SensorID__exact=9).latest('Date')
    hum_last_measurement2 = MeasuredValue.objects.filter(SensorID__exact=7).latest('Date')
    press_last_measurement2 = MeasuredValue.objects.filter(SensorID__exact=8).latest('Date')
    light_last_measurement = MeasuredValue.objects.filter(SensorID__exact=10).latest('Date')
    
    context = {
        'num_sensors': num_sensors,
        'num_instances': num_instances,
        'temp1_last_measurement': temp1_last_measurement,
        'temp2_last_measurement': temp2_last_measurement,
        'hum_last_measurement': hum_last_measurement,
        'press_last_measurement': press_last_measurement,
        'place1': place1,
        'wattage': wattage,
        'temp1_last_measurement2': temp1_last_measurement2,
        'temp2_last_measurement2': temp2_last_measurement2,
        'hum_last_measurement2': hum_last_measurement2,
        'press_last_measurement2': press_last_measurement2,
        'light_last_measurement': light_last_measurement,
        'place2': place2,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from datetime import datetime, timedelta
def power_chart(request):
    date = datetime.today()
    today = date.replace(hour=0, minute=0, second=0, microsecond=0)
    #print(today)
    tomorrow = today + timedelta(1)
    #print(tomorrow)
    
    #sensor_data = MeasuredValue.objects.filter(Date__range=(today,tomorrow))

    queryset = np.array(MeasuredValue.objects.filter(SensorID=5,Date__range=(today,tomorrow)).values('Value','Date'))
    #queryset = MeasuredValue.objects.filter(SensorID=5).values('Value','Date')
    queryset2 = np.array(MeasuredValue.objects.filter(SensorID=4,Date__range=(today,tomorrow)).values('Value','Date'))
    #print(queryset)
    queryset3 = np.array(MeasuredValue.objects.filter(SensorID=1,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset4 = np.array(MeasuredValue.objects.filter(SensorID=2,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset5 = np.array(MeasuredValue.objects.filter(SensorID=3,Date__range=(today,tomorrow)).values('Value','Date'))

    labels1 = []
    data1 = []
    
    c=0
    for entry in queryset:
        if c % 60 == 0 or entry == queryset[len(queryset)-1]:
            labels1.append(entry['Date'].strftime('%Y-%m-%d-%H:%M:%S'))
        else:
            labels1.append('')
        data1.append(entry['Value'])
        c+=1
    
    data2 = []
    
    for entry in queryset2:
        data2.append(entry['Value'])
    
    data3 = []
    
    for entry in queryset3:
        data3.append(entry['Value'])
    
    data4 = []
    
    for entry in queryset4:
        data4.append(entry['Value'])
        
    data5 = []
    
    for entry in queryset5:
        data5.append(entry['Value'])
    
    return JsonResponse(data={
        'labels1': labels1,
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5,
    })

def json_example(request):
    return render(request, 'json_example.html')

def chart_data(request):
    date = datetime.today()
    today = date.replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow = today + timedelta(1)

    queryset = np.array(MeasuredValue.objects.filter(SensorID=5,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset2 = np.array(MeasuredValue.objects.filter(SensorID=4,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset3 = np.array(MeasuredValue.objects.filter(SensorID=1,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset4 = np.array(MeasuredValue.objects.filter(SensorID=2,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset5 = np.array(MeasuredValue.objects.filter(SensorID=3,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset6 = np.array(MeasuredValue.objects.filter(SensorID__exact=6,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset7 = np.array(MeasuredValue.objects.filter(SensorID__exact=9,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset8 = np.array(MeasuredValue.objects.filter(SensorID__exact=7,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset9 = np.array(MeasuredValue.objects.filter(SensorID__exact=8,Date__range=(today,tomorrow)).values('Value','Date'))
    queryset10 = np.array(MeasuredValue.objects.filter(SensorID__exact=10,Date__range=(today,tomorrow)).values('Value','Date'))

    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    data10 = []
    labels1 = []    
    
    for entry in queryset:
        labels1.append(entry['Date'].strftime('%Y-%m-%d-%H:%M:%S'))
        data1.append(entry['Value'])    
    
    for entry in queryset2:
        data2.append(entry['Value'])
        
    for entry in queryset3:
        data3.append(entry['Value'])
        
    for entry in queryset4:
        data4.append(entry['Value'])
        
    for entry in queryset5:
        data5.append(entry['Value'])
        
    for entry in queryset6:
        data6.append(entry['Value'])
        
    for entry in queryset7:
        data7.append(entry['Value'])
        
    for entry in queryset8:
        data8.append(entry['Value'])
        
    for entry in queryset9:
        data9.append(entry['Value'])
        
    for entry in queryset10:
        data10.append(entry['Value'])

    chart = {
        'chart': {'type': 'line', 'height': '60%' },
        'title': {'text': 'Sensor Data'},
        'xAxis': [{
            'categories': labels1,
            'crosshair': 'true',
            'labels' : {
                'step' : 60,
                'rotation' : 90
            }
            
        }],
        'yAxis': [{
                'labels': {
                    'format': '{value} Watt',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[1]'
                    }
                },
                'title': {
                    'text': 'Wattage',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[1]'
                    }
                }
            },
            { 
                'title': {
                'text': 'Temperature',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'labels': {
                    'format': '{value} °C',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'opposite': 'true'
            },
            { 
                'title': {
                'text': 'Humidity',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'labels': {
                    'format': '{value} %',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'opposite': 'true'
            },
            { 
                'title': {
                'text': 'Pressure',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'labels': {
                    'format': '{value} hPa',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'opposite': 'true'
            },
            { 
                'title': {
                'text': 'Light',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'labels': {
                    'format': '{value} lx',
                    'style': {
                        'color': 'Highcharts.getOptions().colors[0]'
                    }
                },
                'opposite': 'true'
            },],
        'series': [{
            'name': 'Watt',
            'yAxis': 0,
            'data': data1
            },
            {
            'name': 'Inverter - Temp1',
            'yAxis': 1,
            'data': data2
            },
            {
            'name': 'Inverter - Temp2',
            'yAxis': 1,
            'data': data3
            },
            {
            'name': 'Inverter - Humidity',
            'yAxis': 2,
            'data': data4
            },
            {
            'name': 'Inverter - Pressure',
            'yAxis': 3,
            'data': data5
            },
            {
            'name': 'Panel - Temp1',
            'yAxis': 1,
            'data': data6
            },
            {
            'name': 'Panel - Temp2',
            'yAxis': 1,
            'data': data7
            },
            {
            'name': 'Panel - Humidity',
            'yAxis': 2,
            'data': data8
            },
            {
            'name': 'Panel - Pressure',
            'yAxis': 3,
            'data': data9
            },
            {
            'name': 'Panel - Light',
            'yAxis': 4,
            'data': data10
            },
        ]
    }

    return JsonResponse(chart)