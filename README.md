
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
  
pdf_exporter.from_template('test.html', 'out.pdf',{
	'id': 1, 
	'object': object
},request)  
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
