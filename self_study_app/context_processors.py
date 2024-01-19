from .models import Course


def navigation(request):
    navigation = Course.objects.all()
    return {'navigation': navigation}
