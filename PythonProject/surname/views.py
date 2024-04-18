from django.shortcuts import render
from django.http import HttpResponse

def surname(request):
    return HttpResponse('Саканцева Валерия Андреевна РИ-220940')

def poem(request):
    return HttpResponse('Не смоют любовь\
                         ни ссоры,\
                         ни версты.\
                         Продумана,\
                         выверена,\
                         проверена.\
                         Подъемля торжественно стих стокоперстый,\
                         клянусь —\
                         люблю\
                         неизменно и верно!')