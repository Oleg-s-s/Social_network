from django.shortcuts import render, redirect
from .models import Comment, Profile, Post
from .forms import PostForm, CommentForm
from django.views.generic.edit import DeleteView
from django.core.paginator import Paginator

def dashboard(request, page):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect("/dashboard/1")
    else:
        return redirect ("/")

    followed_posts = Post.objects.filter(
        user__profile__in=request.user.profile.follows.all()
        ).order_by("-created_at")
    paginator = Paginator(followed_posts, per_page=5)
    page_object = paginator.get_page(page)

    return render(request, "network/dashboard.html", {"form": form, "posts": followed_posts, "page_object": page_object})

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        form = PostForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect("/dashboard/1")
        return render(request, "network/profile_list.html", {'profiles': profiles, 'form': form})
    else:return redirect ("/")


def profile(request, pk):
    if request.user.is_authenticated:
        if not hasattr(request.user, 'profile'):
            missing_profile = Profile(user=request.user)
            missing_profile.save()

        profile = Profile.objects.get(pk=pk)

        if request.method == "POST":
            current_user_profile = request.user.profile
            data = request.POST
            action = data.get("follow")
            if action == "follow":
                current_user_profile.follows.add(profile)
            elif action == "unfollow":
                current_user_profile.follows.remove(profile)
            current_user_profile.save()
        return render(request, "network/profile.html", {"profile": profile})
    else:return redirect ("/")

def post(request, post_id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=post_id)
        comments = post.comment_set.order_by('-created_at')
        number_of_likes = post.number_of_likes()
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True
        post_is_liked = liked
        form = CommentForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = Post.objects.get(id=post_id)
                comment.save()
    else:
        return redirect("/")
    return render(request, 'network/post.html', {'post': post, 'comments': comments, 'form': form, 'number_of_likes': number_of_likes, 'post_is_liked': post_is_liked})

class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"
    template_name = "network/post_delete.html"

def commentdelete(request, post_id, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=comment_id)
        if request.method == "POST":
            comment.delete()
    else:
        return redirect("/")
    return redirect("network:post", post_id)

def likepost(request, post_id):
    if request.user.is_authenticated:
        post = Post.objects.get(id=post_id)
        if request.method == "POST":
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
    else:
        return redirect("/")
    return redirect("network:post", post_id)
