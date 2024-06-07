from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer
from .forms import DestinationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
import requests

class DestinationCreate(generics.CreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request, *args, **kwargs):
        form = DestinationForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination-list')
        return render(request, 'list.html', {'form': form})

class DestinationList(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request, *args, **kwargs):
        destinations = Destination.objects.all()
        return render(request, 'list.html', {'destinations': destinations})

class DestinationRetrieve(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request, *args, **kwargs):
        destination = get_object_or_404(Destination, pk=kwargs['pk'])
        return render(request, 'detail.html', {'destination': destination})

    def destination_detail(request, id):
        destination = get_object_or_404(Destination, id=id)


        api_key = '41036cda4252d1b9205ddc70812463dd'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'


        complete_url = f"{base_url}q={destination.district},{destination.state}&appid={api_key}&units=metric"


        response = requests.get(complete_url)
        weather_data = response.json()

        if weather_data["cod"] != "404":
            main = weather_data["main"]
            weather = weather_data["weather"][0]
            weather_info = {
                "temperature": main["temp"],
                "pressure": main["pressure"],
                "humidity": main["humidity"],
                "description": weather["description"],
                "icon": weather["icon"]
            }
        else:
            weather_info = None

        context = {
            'destination': destination,
            'weather_info': weather_info,
        }
        return render(request, 'detail.html', context)


class DestinationUpdate(generics.UpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    success_url = reverse_lazy('destination-list')

    def get(self, request, *args, **kwargs):
        destination = get_object_or_404(Destination, pk=kwargs['pk'])
        form = DestinationForm(instance=destination)
        return render(request, 'update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        destination = get_object_or_404(Destination, pk=kwargs['pk'])
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination-list')
        return render(request, 'update.html', {'form': form})

class DestinationDestroy(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def get(self, request, *args, **kwargs):
        destination = get_object_or_404(Destination, pk=kwargs['pk'])
        return render(request, 'delete.html', {'destination': destination})

    def post(self, request, *args, **kwargs):
        destination = get_object_or_404(Destination, pk=kwargs['pk'])
        destination.delete()
        return redirect('list')

