from gutgin.generators.password import PasswordGenerator

from django.views.generic import TemplateView


class GeneratorsView(TemplateView):
    template_name = "generators.html"
    password_generator = PasswordGenerator()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password'] = next(self.password_generator)
        return context
