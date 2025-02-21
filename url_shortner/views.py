
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect,render
import json
from .models import ShortURL

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def generate_short_url(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            long_url = data.get('long_url')
            description = data.get('description', '')
            is_active = data.get('is_active', True)

            if not long_url:
                return JsonResponse({'error': '請提供有效的網址'}, status=400)

            short_url = ShortURL.objects.create(
                long_url=long_url,
                description=description,
                is_active=is_active
            )

            return JsonResponse({'short_url': f"/{short_url.short_code}/"})
        except json.JSONDecodeError:
            return JsonResponse({'error': '無效的 JSON 格式'}, status=400)

    return JsonResponse({'error': '無效的請求'}, status=400)

def redirect_to_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.long_url)