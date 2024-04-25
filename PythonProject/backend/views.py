from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Core, Boost
from .serializers import CoreSerializer
@api_view(['GET'])
def call_click(request):
    core = Core.objects.get(user=request.user)
    is_levelup = core.click()
    if is_levelup:
        Boost.objects.create(core=core, price=core.level*50, power=core.level*20)
    core.click()
    core.save()

    return Response({'core': CoreSerializer(
        core).data, 'is_levelup': is_levelup})


def index(request):
    coreModel = apps.get_model('backend','Core')
    boostsModel = apps.get_model('backend', 'Boost')
    core = coreModel.objects.get(user=request.user)
    boosts = boostsModel.objects.filter(core=core)
    return render(request, 'index.html', {
        'core': core,
        'boosts': boosts,
    })