from django.shortcuts import render
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.conf import settings
import json

# Create your views here.
def write_to_cache(request):
    key = "hahaha"
    value = "xixixixi"
    cache.set(key,json.dumps(value),settings.NEVER_REDIS_TIMEOUT)
    return render(request,'redishtml.html')

def read_from_cache(request):
    key = "hahaha"
    value = cache.get(key)
    return render(request,'redishtml.html',{"show":value})


def a(request):
    print("@@@@@@@@@@@wang@@@@@@")
    return render(request,'redishtml.html')