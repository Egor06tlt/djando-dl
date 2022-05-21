from socket import fromshare
from string import Template
from django.utils.safestring import mark_safe
from django import forms

class PictureWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        html = Template(f"""<img src="$link" style="width: 300px; height: 300px;"/>
                            <input type="file" name={name} accept="{name}/*" id="id_{name}">""")
        return mark_safe(html.substitute(link=value.url))