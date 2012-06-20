from django.conf import settings

def get_settings(context):
    return {'STATIC_URL': settings.STATIC_URL}
