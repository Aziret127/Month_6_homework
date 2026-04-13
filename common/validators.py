from datetime import date
from rest_framework.exceptions import ValidationError

def validate_age(birthday):
    if not birthday:
        raise ValidationError("Дата рождения неуказана.")
    
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    if age < 18:
        raise ValidationError("Пользователь должен быть старше 18 лет.")
    
    if age < 0:
        raise ValidationError("Дата рождения не может быть в будущем.")
    return age