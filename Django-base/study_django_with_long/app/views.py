# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
import random


def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)

def random_people(request):
    p = ['Chicken', 'Cow', 'Dog', 'Duck', 'Pig']
    name = random.choice(p)
    html = f"<html><body>Tien Anh is {name}.</body></html>"
    return HttpResponse(html)

def random_game(request):
    people = ['Hien', 'Nang Anh', 'Tien Anh']
    animal = ['Chicken', 'Cow', 'Dog', 'Duck', 'Pig']
    name1 = random.choice(people)
    name2 = random.choice(animal)
    
    html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Random People</title>
        </head>
        <body style="background-color: #f0f0f0; text-align: center;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
                <h1 style="color: #333;">Random Person and Animal</h1>
                <p style="color: #666; font-size: 18px;">{name1} is {name2}🥲 time.</p>
            </div>
        </body>
        </html>
    """
    return HttpResponse(html)