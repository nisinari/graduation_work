from django.shortcuts import render
from django.views import generic
from .forms import SignUpBusinessForm, SignUpBasicForm
from allauth.account.views import SignupView
from django.contrib import messages

# class SignUpBusinessView(generic.TemplateView):
class SignUpBusinessView(SignupView):
    template_name = 'account/signup_business.html'
    form_class = SignUpBusinessForm
    # redirect_field_name = 'next'
    # view_name = 'signup_business'

    # def form_valid(self,form):
    #     member = form.save(commit=False)
    #     member.user = self.request.user
    #     member.save()
    #     messages.success(self.request,'アカウントを作成しました。')
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SignUpBusinessView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret

class SignUpBasicView(SignupView):
    template_name = 'account/signup.html'
    form_class = SignUpBasicForm
    # redirect_field_name = 'next'
    # view_name = 'signup_basic'

    # def form_valid(self,form):
    #     diary = form.save(commit=False)
    #     diary.user = self.request.user
    #     diary.save()
    #     messages.success(self.request,'アカウントを作成しました。')
    #     return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(SignUpBasicView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret