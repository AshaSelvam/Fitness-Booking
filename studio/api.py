from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FitnessClass, Booking
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

##GET/class

def list_classes(request):

    classes = FitnessClass.objects.filter(end_time__gte=timezone.now())
    data = []
    for cls in classes:
        data.append({
            'id': cls.id,
            'name': cls.name,
            'start_time': cls.start_time,
            'end_time': cls.end_time,
            'spots_available': cls.spots_available,
        })
    return JsonResponse(data, safe=False)

#POST/book

@csrf_exempt
@login_required(login_url='/login/')

def book_class(request):

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            name = body['name']
            email = body['email']
            class_id = body['fitness_class_id']

            fitness_class = FitnessClass.objects.get(id=class_id)

        #duplicate
            if Booking.objects.filter(email= email, fitness_class= fitness_class).exists():
                return JsonResponse({'error': 'you have already booked this class.'},status=400)

         #check spot
            if fitness_class.spots_available > 0:
                Booking.objects.create(
                    fitness_class=fitness_class,
                    name=name,
                    email=email
                )
                fitness_class.spots_available -= 1
                fitness_class.save()
                return JsonResponse({
                    'message': 'Booking successful',
                    'spots_remaining': fitness_class.spots_available
                })
            else:
                return JsonResponse({'error': 'No Spots Available'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only Post allowed'}, status=405)



