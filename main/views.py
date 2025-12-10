from django.shortcuts import render
from user.models import Request
from django.contrib.auth.decorators import login_required

def index(request):
    # Показываем все заявки на главной странице, отсортированные по дате создания
    all_requests = Request.objects.all().order_by('-created_at')
    
    # Если пользователь авторизован, также показываем его заявки отдельно
    user_requests = None
    if request.user.is_authenticated:
        user_requests = Request.objects.filter(user=request.user).order_by('-created_at')[:4]

    return render(request, 'main/index.html', {
        'all_requests': all_requests,
        'user_requests': user_requests
    })
