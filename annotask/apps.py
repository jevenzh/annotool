from django.apps import AppConfig
from django.contrib.staticfiles import storage
from django.contrib.staticfiles.apps import StaticFilesConfig


class AnnotaskConfig(AppConfig):
    name = 'annotask'


class AnnotaskStaticFilesConfig(StaticFilesConfig):
    ignore_patterns = ['CVS', '*.edf', '*.json']  # your custom ignore list


class AnnotaskStaticFilesStorage(storage.StaticFilesStorage):
    def __init__(self, *args, **kwargs):
        kwargs['file_permissions_mode'] = 0o640
        kwargs['directory_permissions_mode'] = 0o640
        super().__init__(*args, **kwargs)