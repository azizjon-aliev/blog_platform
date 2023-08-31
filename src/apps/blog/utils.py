from django.utils.html import format_html


def display_image(obj, width: float, height: float):
    default_image_url = '/static/blog/img/default_image.png'

    if obj.image:
        return format_html(f"<img src={obj.image.url} width={width} height={height} />")
    return format_html(f"<img src={default_image_url} width={width} height={height} />")