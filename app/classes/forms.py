# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField

class ProfileForm(FlaskForm):
    role = SelectField('Role', choices=[("Wannabe Therapist", "Wannabe Therapist"),("Sad One", "Sad One"),("Middle man","Middle man"),("Venter ඞ","Venter ඞ")])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    pronouns = SelectField('Pronouns', choices=[("She/Her", "She/Her"),("He/Him", "He/Him"),("They/Them", "They/Them"),("They/She","They/She"),("They/Him","They/Him")])
    age = IntegerField("Age:")
    submit = SubmitField('Post')

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    rating = SelectField('rating', choices=[("1", "1"),("2", "2"),("3","3"),("4","4"),("5","5")])
    submit = SubmitField('Blog')

class ChatForm(FlaskForm):
    content = StringField('Chat', validators=[DataRequired()])
    reaction = SelectField('Reaction', choices=[(":)", ":)"),("<3", "<3"),("( ͡° ͜ʖ ͡°)","( ͡° ͜ʖ ͡°)"),("¯\_(ツ)_/¯","¯\_(ツ)_/¯"),("ಠ_ಠ","ಠ_ಠ"),("(╯°□°）╯︵ ┻━┻","(╯°□°）╯︵ ┻━┻")])
    submit = SubmitField('Send chat!')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ChatReplyForm(FlaskForm):
    content = TextAreaField('Reply', validators=[DataRequired()])
    submit = SubmitField('Reply')
