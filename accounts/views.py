from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from accounts.forms import UserForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages


class LoginView(View):

    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(
            request,
            'accounts/login.html',
            context=context
        )

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(
                    request,
                    'Usuário não encontrado com esse email.'
                )
                return redirect('/accounts/login/')

            user = authenticate(
                request,
                username=user.username,
                password=password
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    'Login realizado com sucesso!'
                )
                return redirect('/dashboard/')
            else:
                messages.error(
                    request,
                    'Senha incorreta. Tente novamente.'
                )
                return redirect('/accounts/login/')
        else:
            messages.error(
                request,
                'Dados inválidos. Por favor, verifique os campos.'
            )
            return redirect('/accounts/login/')


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login_view')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
                
        if User.objects.filter(email=email).exists():
            messages.error(
                self.request,
                'Este email já está em uso.'
            )
            return self.form_invalid(form)

        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        messages.success(
            self.request,
            'Registrado com Sucesso'
            )
        return super().form_valid(form)

def home(request):
    return render(request, 'accounts/home.html')