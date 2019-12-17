import pdfkit
from django.template.loader import render_to_string


def from_template(template_name, output_path, options=None, context=None, request=None, using=None):
    """
    Convert given template or templates to PDF document

    :param template_name: may be a string or a list of strings.
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltopdf global and page options, with or w/o '--'
    :param context: (optional)
    :param request: (optional)
    :param using: (optional)
    """
    html = render_to_string(template_name, context, request, using)
    return pdfkit.from_string(html, output_path, options)


def from_url(url, output_path, options=None):
    """
    Convert file of files from URLs to PDF document

    :param url: URL or list of URLs to be saved
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltopdf global and page options, with or w/o '--'
    """
    return pdfkit.from_url(url, output_path, options)


def from_string(input, output_path, options=None):
    """
    Convert given string or strings to PDF document

    :param input: string with a desired text.
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltopdf options, with or w/o '--'
    """
    return pdfkit.from_string(input, output_path, options)
