from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.


class Sum(View):
    def get(self, request, *args, **kwargs):
        total = 0
        return HttpResponse(str(total))
        # a = self.request.GET.get("a", 0)
        # b = self.request.GET.get("b", 0)
        # a = int(self.request.GET.get("a", 0))
        # b = int(self.request.GET.get("b", 0))
        # return HttpResponse(str(a + b))
