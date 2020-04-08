from django.contrib.auth.models import User


class EmailAuth:
    """Authenticate a user by an exact match on the email and password"""

    def authenticate(self, username=None, password=None):
        """
        Get an instance the User using the email to log in instead of
        username.
        """

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user

            return None
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """
        Used by the Django authentiation system to retrieve an user instance
        """
        
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None