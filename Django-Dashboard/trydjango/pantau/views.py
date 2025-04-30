from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import MonitoringData
import json

@csrf_exempt
def dashboard(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            MonitoringData.objects.create(
                suhu=data.get('suhu', ''),
                kelembaban=data.get('kelembaban', ''),
                co2=data.get('co2', ''),
                gas_lpg=data.get('gas_lpg', ''),
                gas_alkohol=data.get('gas_alkohol', ''),
                cahaya=data.get('cahaya', ''),
                jumlah_orang=data.get('jumlah_orang', 0),
                kebisingan=data.get('kebisingan', ''),
                tegangan=data.get('tegangan', ''),
                arus=data.get('arus', ''),
                daya=data.get('daya', '')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:  # method == GET
        latest = MonitoringData.objects.last()
        chart_co2 = list(MonitoringData.objects.values_list('co2', flat=True).order_by('-id')[:5])

        if latest:
            context = {
                'suhu': f"{latest.suhu} C",
                'kelembaban': f"{latest.kelembaban} %",
                'co2': f"{latest.co2} ppm",
                'gas_lpg': f"{latest.gas_lpg}",
                'gas_alkohol': f"{latest.gas_alkohol}",
                'cahaya': f"{latest.cahaya} lux",
                'jumlah_orang': f"{latest.jumlah_orang}",
                'kebisingan': f"{latest.kebisingan} dB",
                'listrik': {
                    'tegangan': f"{latest.tegangan} volt",
                    'arus': f"{latest.arus} Ampere",
                    'daya': f"{latest.daya} watt",
                },
                'chart_co2': chart_co2  
            }
        else:
            context = {
                'suhu': '-',
                'kelembaban': '-',
                'co2': '-',
                'gas_lpg': '-',
                'gas_alkohol': '-',
                'cahaya': '-',
                'jumlah_orang': '-',
                'kebisingan': '-',
                'listrik': {
                    'tegangan': '-',
                    'arus': '-',
                    'daya': '-',
                },
                'chart_co2': []  
            }
        return render(request, 'dashboard.html', context)

@csrf_exempt
def dashboard_new(request):
    return render(request, 'dashboard_new.html')

@csrf_exempt
def get_latest_data(request):
    latest = MonitoringData.objects.last()
    last_5_data = MonitoringData.objects.all().order_by('-id')[:5] 
    
    chart_co2 = [data.co2 for data in last_5_data] if last_5_data else []

    if latest:
        return JsonResponse({
            'suhu': f"{latest.suhu} C",
            'kelembaban': f"{latest.kelembaban} %",
            'co2': f"{latest.co2} ppm",
            'gas_lpg': f"{latest.gas_lpg}",
            'gas_alkohol': f"{latest.gas_alkohol}",
            'cahaya': f"{latest.cahaya} lux",
            'jumlah_orang': f"{latest.jumlah_orang}",
            'kebisingan': f"{latest.kebisingan} dB",
            'tegangan': f"{latest.tegangan} volt",
            'arus': f"{latest.arus} Ampere",
            'daya': f"{latest.daya} watt",
            'chart_co2': chart_co2,  
        })
    else:
        return JsonResponse({'error': 'No data found'}, status=404)

