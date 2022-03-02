from django.shortcuts import render
from django.http import JsonResponse
from .models import Cities
from django.db.models import Q
from django.forms.models import model_to_dict


def index(request):
    return render(request, 'app/index.html')


def search_city(request):
    value = request.POST.get('city')
    q_list = Q()
    print(value)
    for word in str(value).split():
        q_list |= Q(city__icontains=word)
    data = Cities.objects.filter(q_list).first()
    print(data)
    return JsonResponse({'city': model_to_dict(data)}, status=200)
