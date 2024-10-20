from .models import User
from django.contrib.auth.hashers import check_password

def user_is_valid(user_id,password):
    try:
        data = User.objects.get(user_id=user_id)
        if check_password(password, data.password):
            return True 
        return False
    except User.DoesNotExist:
        return False