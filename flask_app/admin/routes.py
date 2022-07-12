
from . import admin_bp
from flask import render_template, redirect


@admin_bp.route('/')
def index():
    return {'admin':'admin'}