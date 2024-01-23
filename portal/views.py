from typing import Any
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service, Post, CustomUser
import logging
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import InquiryForm, ServiceCreateForm, PostCreateForm
from member.models import UserDetailBusiness

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    model = Service
    paginate_by = 8
    template_name = "index.html"

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            Services = Service.objects.filter(name__icontains=query)
        else:
            Services = Service.objects.all().order_by('-created_at')
        return Services
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        is_business_account = {'is_business_account': str(self.request.user.pk) in [str(i)[0] for i in UserDetailBusiness.objects.all()]}
        category_dict = {'category_dict':{'space':'空間', 
                                          'stuff':'モノ', 
                                          'transportation':'移動', 
                                          'skill':'スキル'}}
        context.update(is_business_account)
        context.update(category_dict)
        return context
    
class SearchResultView(generic.ListView):
    model = Service
    paginate_by = 8
    template_name = "index.html"

class InquiryView(generic.TemplateView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('portal:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry set by{}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

# class ServiceListView(generic.ListView):
#     model = Service
#     template_name = "service_list.html"

class ServiceDetailView(generic.ListView):
    model = Post, Service
    template_name = "service_detail.html"
    paginate_by = 8
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        service_name = {"service_name": Service.objects.get(id=self.request.path.strip("/")).name}
        service_overview = {"service_overview": Service.objects.get(id=self.request.path.strip("/")).overview}
        service_image = {"service_image": Service.objects.get(id=self.request.path.strip("/")).image}
        context.update(service_name)
        context.update(service_overview)
        context.update(service_image)
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('query')
        id = self.request.path.strip("/")
        if query:
            Posts = Post.objects.filter(title__icontains=query, service_id = id).order_by('-created_at')
        else:
            Posts = Post.objects.filter(service_id=id).order_by('-created_at')
        return Posts
    
class ServiceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Service
    template_name = 'service_create.html'
    form_class = ServiceCreateForm
    success_url = reverse_lazy('portal:index')

    def form_valid(self, form):
        qryset =  form.save(commit=False)
        qryset.company=self.request.user
        qryset.save()
        print(qryset)
        return super().form_valid(form)

class ServiceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Service
    template_name = 'service_update.html'
    form_class = ServiceCreateForm
    def get_success_url(self):
        return reverse_lazy('portal:Service_detail',kwargs={'pk': self.kwargs['pk']})
    def form_valid(self, form):
        messages.success(self.request, '内容を更新しました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"内容の更新に失敗しました。")
        return super().form_invalid(form)

class ServiceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Service
    template_name = 'service_delete.html'
    success_url = reverse_lazy('portal:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "サービスを削除しました。")
        # ここに'media'を削除する処理を書く
        return super().delete(request, *args, **kwargs)

# class PostListView(generic.ListView):
#     model = Post
#     template_name = "post_list.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        is_self_post = {"is_self_post": Post.objects.get(pk=self.kwargs['pk']).user == self.request.user}
        context.update(is_self_post)
        return context

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostCreateForm
    # slugをpkからkwにしたら遷移先を作成したサービスの詳細画面に書き換える
    success_url = reverse_lazy('portal:index')

    def form_valid(self, form):
        qryset =  form.save(commit=False)
        # qryset.service=Service.objects.get(pe=self.kwargs['pk'])
        qryset.user=self.request.user
        qryset.save()
        print(qryset)
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostCreateForm
    def get_success_url(self):
        return reverse_lazy('portal:post_detail',kwargs={'pk': self.kwargs['pk']})
    def form_valid(self, form):
        messages.success(self.request, '内容を更新しました。')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request, '内容の更新に失敗しました。')
        return super().form_invalid(form)

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # slugをpkからkwにしたら遷移先を作成したサービスの詳細画面に書き換える
    success_url = reverse_lazy('portal:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "サービスを削除しました。")
        # ここに'media'を削除する処理を書く
        return super().delete(request, *args, **kwargs)
    
class Post_FinishView(generic.TemplateView):
    template_name = "post_finish.html"