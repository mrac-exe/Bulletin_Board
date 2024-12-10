from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, TemplateView, ListView
from django_filters import FilterSet

from board.models import Reply, Announce, Author
from users.models import User


class PostFilter(FilterSet):
    class Meta:
        model = Reply
        fields = [
            'announce'
        ]

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['announce'].queryset = Announce.objects.filter(author__user_id=kwargs['request'])


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'users/invalid_code.html')
            return redirect('/')


class ProfileView(LoginRequiredMixin, ListView):
    model = Reply
    template_name = 'users/profile.html'
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = Reply.objects.filter(announce__author__user_id=self.request.user.id)
        self.filterset = PostFilter(self.request.GET, queryset, request=self.request.user.id)
        if self.request.GET:
            return self.filterset.qs
        return Reply.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
