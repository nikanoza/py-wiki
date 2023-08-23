from django.shortcuts import render
from markdown2 import Markdown

from . import util

def convert_to_html(text):
    file = util.get_entry(text)
    markdowner = Markdown()
    if file == None:
        return None
    else:
        return markdowner.convert(file) 

def index(request):
    entries = util.list_entries()
    css = util.get_entry("CSS")
    coffee = util.get_entry("coffee")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, text):
    print(text)
    content = convert_to_html(text)
    if content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": text,
            "content": content
        })