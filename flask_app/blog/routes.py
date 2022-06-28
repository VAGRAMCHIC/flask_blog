
from cgitb import text
from . import blog
from flask import render_template, redirect


@blog.route('/')
def index():
    return {'title':'ABOBA', 'text':"Somebody once told me The world is gona roll me Ain't shapest tool in the sheild All star commin and an all star comming", 'pub_date':'yesterday'}
