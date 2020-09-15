from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        # replace the old usercreationform with our customized
        form = UserRegisterForm(request.POST)  # submition of the form
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username'] get to the fields
            messages.success(request, f'Account Create Now Log In!')
            # this is the name of the home route ['/']
            return redirect('login')
    else:
        form = UserRegisterForm()  # get the register view only and pass the form
    # return the fields
    return render(request, 'users/register.html', {"form": form})
    # if invalid form

# is auth middleware to check if the user is authenticated


@login_required
def profile(request):
    if request.method == 'POST':
        # from the request we stract the
        # keep the instance and the request body
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # current user
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        # from the request we stract and pass in the body if the form the profile of the user
        # this will populate the fields that are required in the form
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    # first argument should be the request
    return render(request, 'users/profile.html', context)


# types of messages
# messages.debug
# messages.info
# messages.success
# messages.error
# messages.warning
