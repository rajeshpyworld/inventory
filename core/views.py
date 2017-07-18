from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from .forms import SignUpForm, CustomerForm
from .models import CustomUser

User = get_user_model()


def home(request):
    if request.user.is_authenticated():
        return customerList(request)
    else:
        return render(request, 'core/cover.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'core/signup.html',
                          {'form': form})

        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')

    else:
        return render(request, 'core/signup.html',
                      {'form': SignUpForm()})


@login_required
def customerList(request):
    customer_list = CustomUser.customers.filter(is_active=True)
    paginator = Paginator(customer_list, 10)
    page = request.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)
    return render(request, 'core/customers.html', {'customers': customers})


@login_required
def customer_add(request):
    if not request.user.is_salesperson:
        raise Http404

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if not form.is_valid():
            return render(request, 'core/customer_add.html',
                          {'form': form})
        else:
            user = form.save(commit=False)
            user.user_type = 'C'
            user.save()
            messages.success(request, "Successfully Added")
            return redirect('/')

    else:
        context = {
            "title": 'Add Customer',
            "form": CustomerForm(),
        }
        return render(request, 'core/customer_add.html', context)


@login_required
def customer_update(request, pk=None):
    if not request.user.is_salesperson:
        raise Http404
    instance = get_object_or_404(User, pk=pk)
    print(vars(instance))
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=instance)
        if not form.is_valid():
            return render(request, 'core/customer_update.html',
                          {'form': form})
        else:
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Successfully Updated")
            return redirect('/')

    else:
        context = {
            "title": 'Update Customer',
            "form": CustomerForm(instance=instance),
        }
        return render(request, 'core/customer_update.html', context)


@login_required
def customer_delete(request, pk=None):
    if not request.user.is_salesperson:
        raise Http404
    instance = get_object_or_404(User, pk=pk)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect('/')
