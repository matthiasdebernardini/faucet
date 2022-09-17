from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class RequestForm(FlaskForm):
    amount = StringField('Sats', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PayForm(FlaskForm):
    invoice = StringField('Invoice', validators=[DataRequired()])
    submit = SubmitField('Submit')
