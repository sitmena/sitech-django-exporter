

# Sitech Django Exporter
<br/>

## Installation

Run the [pip](https://pip.pypa.io/en/stable/) command to install the latest version:

```bash
$ pip install git+https://github.com/sitmena/sitech-django-exporter.git
```
<br/>

## PDF Exporter
### # Prerequisites:
To use "PDF Exporter" , you need to install the wkhtmltopdf tools:

-   Debian/Ubuntu:

```bash
$ sudo apt-get install wkhtmltopdf
```

-   macOS:
```bash
$ brew install caskroom/cask/wkhtmltopdf
```

-   Windows and other options: check wkhtmltopdf  [homepage](http://wkhtmltopdf.org/)  for binary installers

### # Usage
```python
from sitech_exporter import pdf_exporter
  
pdf_exporter.from_template('test.html', 'out.pdf', context={
	'id': 1, 
	'object': object
},request=request)  
pdf_exporter.from_url('http://google.com', 'out.pdf')  
pdf_exporter.from_string('Hello!', 'out.pdf')
```

You can pass a list with multiple URLs or templates:

```python
pdf_exporter.from_template(['file1.html', 'file2.html'], 'out.pdf')
pdf_exporter.from_url(['google.com', 'yandex.ru', 'engadget.com'], 'out.pdf')
```
If you wish to further process generated PDF, you can read it to a variable:

```python
# Use False instead of output path to save pdf to a variable
pdf = pdf_exporter.from_template('file1.html', False)

from django.http import HttpResponse
return HttpResponse(pdf, content_type='application/pdf')
```

You can specify all wkhtmltopdf  [options](http://wkhtmltopdf.org/usage/wkhtmltopdf.txt). You can drop '--' in option name. If option without value, use  _None, False_  or  _''_  for dict value:. For repeatable options (incl. allow, cookie, custom-header, post, postfile, run-script, replace) you may use a list or a tuple. With option that need multiple values (e.g. --custom-header Authorization secret) we may use a 2-tuple (see example below).

```python
options = {
        'page-size': 'A4',  
	'encoding': 'UTF-8',  
	'margin-top': '0in',  
	'margin-right': '0in',  
	'margin-bottom': '0in',  
	'margin-left': '0in',  
	'dpi': 300,  
	'no-outline': None
}
pdf_exporter.from_template('test.html', 'out.pdf' options=options)
```
