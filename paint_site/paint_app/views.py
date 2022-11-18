from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View

from paint_app.forms import ColorPickerForm


# Create your views here.
class ColorPickerView(View):
    def get(self, request):
        """Present the color picker form and color the user"""
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 255,
            'green': 255,
            'blue': 255,
        }

        return render(request, 'paint.html', context=context)