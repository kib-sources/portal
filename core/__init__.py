"""
core

created by pavelmstu in pavelmstu as 5/3/21
Проект portal
"""

__author__ = 'pavelmstu'
__maintainer__ = 'pavelmstu'
__credits__ = ['pavelmstu', ]
__status__ = 'Development'
__version__ = '20210503'


from flask import Blueprint, request, render_template, flash, url_for, redirect, abort, current_app, g
from flask_login import LoginManager, login_user, logout_user, login_required, current_user


app = Blueprint(
    'portal',
    __name__,
    url_prefix='',
    template_folder='../templates',
    static_folder='../static',
)
