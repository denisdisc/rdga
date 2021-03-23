from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from webapp.events.models import Events


class AddEventForm(FlaskForm):
    url = StringField('Ссылка на главную страницу события', validators=[DataRequired()], render_kw={"class": "form-control"})
    category = SelectField('Выбрать раздел', choices=[('Beginner', 'Новичковый'), ('ProTour', 'Профессиональный')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить',render_kw={"class":"btn btn-primary"})

    def validate_event(self, url):
        event_count = Events.query.filter_by(url=url.data).count()
        if user_count > 0:
            raise ValidationError('Событие уже записано в базу данных')
