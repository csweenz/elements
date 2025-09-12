# backend/views.py
from django.http import JsonResponse

def element_detail(request, symbol: str):
    # Simple test echo - use cache
    return JsonResponse({"ok": True, "symbol": symbol.upper(), "message": "pong"})
