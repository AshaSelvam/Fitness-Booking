from django.http import JsonResponse
from .models import FitnessClass

def get_classes(request):
    if request.methos == 'GET':
        classes = FitnessClass.objects.all()
        data = [
            {
                'id': cls.id,
                'name': cls.name,
                'start_time': cls.start_time,
                'end_time': cls.end_time,
                'capacity': cls.capacity

            }
            for cls in classes
        ]
        return JsonResponse(data, safe=False)

# Create your views here.
