from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

def convert_to_html(text):
    file = util.get_entry(text)
    markdowner = Markdown()
    if file == None:
        return None
    else:
        return markdowner.convert(file) 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, text):
    content = convert_to_html(text)
    if content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": text,
            "content": content
        })
    
def search(request):
    if request.method == "POST": 
        input = request.POST["q"]
        html = convert_to_html(input)
        if html is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": input,
                "content": html
            })
        else:
            entries = util.list_entries()
            files = []
            for entry in entries:
                if input.upper() in entry.upper():
                    files.append(entry) 
            return render(request, "encyclopedia/search.html", {
                "files": files,
            })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        ifTitleExist = util.get_entry(title)
        if ifTitleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "entry page already exist"
            })
        else:
            util.save_entry(title, content)
            html = convert_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                title: title,
                content: html
            })
        
def edit(request):
    if request.method == "POST": 
        title = request.POST["page_title"]
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": entry
        })

def save(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)
        html = convert_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            title: title,
            content: html
        })

def random_page(request):
    entries = util.list_entries()
    random_entry  = random.choice(entries)
    html = convert_to_html(random_entry)
    print(random_entry, html)
    return render(request, "encyclopedia/entry.html", {
            "title": random_entry,
            "content": html
    })