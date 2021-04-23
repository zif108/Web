from flask_wtf import FlaskForm, validators
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    tag = StringField('Тэг', validators=[DataRequired()])
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')