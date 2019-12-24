"""Post forms."""

# Django
from django import forms

# Models
from post.models import Post


class PostForm(forms.ModelForm): #Nombre que le dimos al formularios
    """Post model form."""

    class Meta: #La configuracion de la clase en general
        """Form settings."""
        model = Post
        fields = ('user', 'profile', 'title', 'photo') #Capos de models.py