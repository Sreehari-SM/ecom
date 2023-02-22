from cryptography.fernet import Fernet
import base64
from django.conf import settings

def get_auto_id(model):
    auto_id = 1
    latest_auto_id =  model.objects.all().order_by("-date_added")[:1]
    if latest_auto_id:
        for auto in latest_auto_id:
            auto_id = auto.auto_id + 1
    return auto_id


def encrypt(text):
    text = str(text)
    f = Fernet(settings.ENCRYPT_KEY)
    #input should be in bytes
    encrypted_data = f.encrypt(text.encode('ascii'))
    encrypted_data = base64.urlsafe_b64encode(encrypted_data).decode("ascii") 

    return encrypted_data


def decrypt(text):
    text= base64.urlsafe_b64decode(text)
    f = Fernet(settings.ENCRYPT_KEY)
    decrypted_data = f.decrypt(text).decode("ascii")

    return decrypted_data
