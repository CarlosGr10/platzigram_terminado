"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous: #Una propiedad del middleware
            if not request.user.is_staff: #Poder entrar en el localhost
                profile = request.user.profile #Una forma de traer los OneToOneField(user), nos trae el objeto profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]: #Redireccionar en caso de que no tenga foto y biografia
                        return redirect('users:update_profile')

        response = self.get_response(request) #En caso de que no se cumple ninguno de los if
        return response