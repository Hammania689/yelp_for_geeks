from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from users.models import Review, Profile, User
from django.http import Http404

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = {
        'reviews': Review.objects.all()
    }
    return render(request, "guts/index.html", context)

class ReviewListView(ListView):
    model = Review
    template_name = 'guts/index.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'reviews'
    ordering = ['-date_posted']

class ReviewDetailView(DetailView):
    model = Review

class ReviewCreateView(CreateView):
    model = Review
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.author:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        Review = self.get_object()
        if self.request.user == Review.author:
            return True
        return False

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'

    def get_object(self):
        # return get_object_or_404(Profile, user__username=self.kwargs['username'])
        return get_object_or_404(User, username=self.kwargs.get('username'))

    # I know pk=username is not correct. I am not sure what to put pk=?

    # I was able to get the writers other posts using the code below. I did not have to show this code for this question. But just to show you that the pk above has to be username. Or Else the code below won't work(I guess)
    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['review_list'] = Review.objects.filter(user__username__iexact=self.kwargs.get('username'))
        return context