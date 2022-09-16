from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RequestForm(FlaskForm):
    amount = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Submit')
class PayForm(FlaskForm):
    invoice = StringField('Invoice', validators=[DataRequired()])
    submit = SubmitField('Submit')
