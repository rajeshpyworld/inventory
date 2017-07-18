from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from .forms import TransactionForm
from .models import Transaction


@login_required
def transaction_list(request):
    today_sales_info = Transaction.get_today_sales_info()
    transactionlist = Transaction.objects.all().select_related('product', 'sales_person', 'customer')
    paginator = Paginator(transactionlist, 10)
    page = request.GET.get('page')
    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)
    return render(request, 'transactions/transactions.html',
                  {'transactions': transactions, 'today_sales_info': today_sales_info})


@login_required
def transaction_add(request):
    if not request.user.is_salesperson:
        raise Http404

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if not form.is_valid():
            return render(request, 'transactions/transaction_add.html',
                          {'form': form})
        else:
            transactions = form.save(commit=False)
            transactions.save()
            messages.success(request, "Successfully Added")
            return redirect('transactions:transaction_list')

    else:
        context = {
            "title": 'Add Product',
            "form": TransactionForm(),
        }
        return render(request, 'transactions/transaction_add.html', context)
