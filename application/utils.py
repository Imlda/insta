from wtforms.validators import ValidationError

from application import login_manager
from application.models import User

def exists_email(form, email):
    # user = User.query.filter_by(email=email.data).first()
    user = User.query.filter_by(username=username).first()
    if user:
        raise ValidationError('Email address is already registered. Please choose a different one.')

#LOGIN MANAGER UTILS
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#END OF LOGIN MANAGER UTILS