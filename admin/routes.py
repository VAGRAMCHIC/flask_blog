
from . import admin
from flask import render_template, redirect


@admin.route('/')
def index():
    return render_template('admin_panel.html', title='Admin')