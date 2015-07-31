from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
import traceback
import sys
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext

from models import Post
from forms import PostForm, CommentForm

class HomePageView(TemplateView):
    try:
        template_name = "home/index.html"

        def get_context_data(self, **kwargs):

            context = super(HomePageView, self).get_context_data(**kwargs)
            context['client_list'] = ""

            return context
    except Exception as inst:
        traceback.print_exc(file=sys.stdout)
        raise inst


@user_passes_test(lambda u: u.is_superuser)
def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(post)
    return render_to_response('blog/add_post.html',
                              { 'form': form },
                              context_instance=RequestContext(request))

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        request.session["name"] = comment.name
        request.session["email"] = comment.email
        request.session["website"] = comment.website
        return redirect(request.path)
    form.initial['name'] = request.session.get('name')
    form.initial['email'] = request.session.get('email')
    form.initial['website'] = request.session.get('website')
    return render_to_response('blog/blog_post.html',
                              {
                                  'post': post,
                                  'form': form,
                              },
                              context_instance=RequestContext(request))