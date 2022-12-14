from django.views.generic import View
from KevinApp.libs.base_render import render_to_response

class Base(View):
    TEMPLATE = 'dashboard/base.html'

    def get(self, request):
        return render_to_response(request, self.TEMPLATE)