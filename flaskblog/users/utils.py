import os
import secrets
from PIL import Image
from flask import url_for
from flaskblog import mail
from flask_mail import Message
from flask import current_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8) # For naming our picture files
    _, f_ext = os.path.splitext(form_picture.filename) # To grab the picture file extension, the 'f_name' is not needed so we changed it to underscore "_"
    picture_filename = random_hex + f_ext # Giving the picture a name with filename + extension
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename) # Choosing how to save the picture
    
    # Used to resize the image to 125x125 before saving it
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_filename


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:

{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore email and no changes will be made 
'''
    mail.send(msg)