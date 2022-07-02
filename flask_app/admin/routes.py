
from . import admin
from flask import render_template, redirect


@admin.admin_bp.route('/')
def index():
    return {'admin':'admin'}