from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.translation import gettext as _ 

@api_view()
def hello_world(request):
    message = _("This is my first Django API")
    return Response({"message": message})