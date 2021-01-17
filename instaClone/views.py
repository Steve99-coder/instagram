from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Profile, Follow
from .forms import SignUpForm, UpdateForm, UpdateProfileForm, PostForm, CommentForm

# Create your views here.
@login_required(login_url='login')
def index(request):
    images = Post.objects.all()
    print('loaded images', images)
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    
    return render(request, 'instaClone/index.html', {'images':images, 'form': form, 'users': users})

@login_required(login_url='login')
def profile(request, username):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        user_form = UpdateForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,

    }
    return render(request, 'instaClone/profile.html', params)

@login_required(login_url='login')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.posts.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    print(followers)
    return render(request, 'instaClone/user_profile.html', params)

