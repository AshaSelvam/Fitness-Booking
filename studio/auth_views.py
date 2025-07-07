from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exits'},status=400)
            user = User.objects.create_user(username=username, password= password)
            return JsonResponse({'message': 'User registered sucessfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)},status=400)
    return JsonResponse({'error':'Only POST allowed'},status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']

            user= authenticate(request,username= username,password= password)
            if user is not None:
                login(request,user)
                return  JsonResponse({'message':'Login successful'})
            else:
                return JsonResponse({'error':'invalid username or password'},status= 401)
        except Exception as e:
            return JsonResponse({'error': str(e)},status=400)
    return JsonResponse({'error':'Only POST allowed'},status=405)




