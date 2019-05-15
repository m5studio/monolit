from django import template

register = template.Library()


@register.filter(name='bytes_to_mb')
def bytes_to_mb(value):
    from apps.settings.classes.file_utils import FileUtils
    return FileUtils.format_bytes(value)


@register.filter(name='get_file_ext')
def get_file_ext(value):
    from apps.settings.classes.file_processing import FileProcessing
    file = FileProcessing(value)
    return file.getFileExt()
