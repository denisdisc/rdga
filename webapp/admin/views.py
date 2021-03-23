from flask import Blueprint, Flask, render_template, flash, redirect, session, url_for

from webapp.user.decorators import admin_required
from webapp.events.models import Events
from webapp.admin.forms import AddEventForm
from webapp.event import event_data
from webapp.db import db


blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/add-event')
@admin_required
def admin_index():
    form = AddEventForm()
    title = "Добавить событие на сайт"
    return render_template('admin/index.html', page_title=title, form=form)

@blueprint.route('/process-add-event', methods=['POST'])
@admin_required
def process_add_event():
    form = AddEventForm()
    if form.validate_on_submit():
        url = form.url.data
        category = form.category.data
        event = Events.query.filter(Events.url==url).count()
        if not event:
            print('Парсим и возвращаем данные')
            event_data(url, category)
            title = "Подтвердите добавление события"
            add_event = Events.query.filter(Events.url==url)
            return render_template('admin/add_event.html', page_title=title, events=add_event) #добавить параметры для отрисовки события
        else:
            print('Эвент уже внесен. Вернуть данные')
            title = "Подтвердите добавление события"
            add_event = Events.query.filter(Events.url==url)
            flash('Эвент уже внесен в базу данных')
            return render_template('admin/add_event.html', page_title=title, events=add_event) #добавить параметры для отрисовки события
    flash('Пожалуйста, исправьте ошибки в форме')
    return redirect(url_for('admin.admin_index'))
