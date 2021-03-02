from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TickerForm(FlaskForm):
    ticker = StringField('Ticker',
                          validators=[DataRequired()])
    submit = SubmitField('Search')

class CryptoForm(FlaskForm):
    crypto = SelectField(u'Crypto', choices=['BTCUSDT','ETHUSDT'], validators=[DataRequired()])
    submit = SubmitField('Search')