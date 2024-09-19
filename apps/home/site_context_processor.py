from apps.home.models import MainSettings


def main_data(request):
    data = MainSettings.objects.last()
    return {'data':data}