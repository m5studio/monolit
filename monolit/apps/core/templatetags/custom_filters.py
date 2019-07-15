from django import template

from apps.core.classes.numbers_formatter import NumbersFormatter

register = template.Library()


@register.filter(name='bytes_to_mb')
def bytes_to_mb(value):
    from apps.core.classes.file_utils import FileUtils
    return FileUtils.format_bytes(value)


@register.filter(name='get_file_ext')
def get_file_ext(value):
    from apps.core.classes.file_processing import FileProcessing
    file = FileProcessing(value)
    return file.getFileExt()


def custom_format_number(value):
    return '{:,}'.format(value).replace(',', ' ').replace('.0', '')

@register.filter(name='format_number')
def format_number(value):
    return custom_format_number( float(value) )


@register.filter(name='round_number')
def round_number(value):
    # return str(round(value, 1)).replace('.0', '')
    return NumbersFormatter.round_num(value, 1, '.0', '')


@register.filter(name='format_and_round_number')
def format_and_round_number(value):
    return custom_format_number(round(value, 0))
