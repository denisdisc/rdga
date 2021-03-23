from flask import Blueprint, Flask, render_template, request, flash, redirect, session, url_for

from webapp.utils import get_redirect_target
from webapp.events.models import Events
from webapp.breadcrumb import breadcrumb
from flask_breadcrumbs import default_breadcrumb_root, register_breadcrumb


blueprint = Blueprint('cont', __name__, url_prefix='/')
default_breadcrumb_root(blueprint, '.')

@blueprint.route('/<city_id>')
def city_content(city_id):
    session.pop("city", None)
    session["city"] = city_id
    return redirect(get_redirect_target())

@blueprint.route('/about')
@register_breadcrumb(blueprint, '.about', 'О диск-гольфе')
def about_dg():
    title = "Узнай больше о диск-гольфе"
    return render_template('cont/about.html', page_title=title)

@blueprint.route('/mclass')
@register_breadcrumb(blueprint, '.mclass', 'Мастерклассы')
def mclass():
    title = "Попробуй поиграть в диск-гольф"
    return render_template('cont/mclass.html', page_title=title)

@blueprint.route('/where')
# @breadcrumb('Где поиграть')
@register_breadcrumb(blueprint, '.where', 'Где поиграть')
def where():
    title = "Где можно поиграть в диск-гольфа"
    return render_template('cont/where.html', page_title=title)

@blueprint.route('/beginner/<category_id>')
@register_breadcrumb(blueprint, '.beginner', 'Турниры начального уровня')
def beginner(category_id):
    title = "Попробуй посоревноваться"
    post_event = Events.query.filter(Events.category==category_id).limit(3).all()
    print(post_event)
    return render_template('cont/beginner.html', page_title=title, events=post_event)

@blueprint.route('/protour/<category_id>')
@register_breadcrumb(blueprint, '.protour', 'Профессиональные турниры')
def protour(category_id):
    title = "Зарубись с профессионалами диск-гольфа"
    post_event = Events.query.filter(Events.category==category_id).limit(3).all()
    print(post_event)
    return render_template('cont/protour.html', page_title=title, events=post_event)

@blueprint.route('/world/<category_id>')
@register_breadcrumb(blueprint, '.world', 'Международные турниры')
def world(category_id):
    title = "Стань здездой диск-гольфа"
    post_event = Events.query.filter(Events.category==category_id).limit(3).all()
    print(post_event)
    return render_template('cont/world.html', page_title=title, events=post_event)

@blueprint.route('/sponsorship')
@register_breadcrumb(blueprint, '.sponsorship', 'Спонсировать диск-гольф')
def sponsor():
    title = "Поддержи развитие диск-гольфа"
    return render_template('cont/sponsorship.html', page_title=title)

@blueprint.route('/tobuy')
@register_breadcrumb(blueprint, '.tobuy', 'Где купить')
def tobuy():
    title = "Где купить диски и корзины"
    return render_template('cont/tobuy.html', page_title=title)

@blueprint.route('/corp')
@register_breadcrumb(blueprint, '.corp', 'Корпоративным клиентам')
def corp():
    title = "Провести праздник диск-гольфа"
    return render_template('cont/corp.html', page_title=title)
