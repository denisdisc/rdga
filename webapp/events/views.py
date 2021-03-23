from flask import Blueprint, Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user

from webapp.events.models import Events

blueprint = Blueprint('event', __name__, url_prefix='/events')
