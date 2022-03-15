from django.shortcuts import render
from django.views import View


class ViewMainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vaccina_page/index.html')