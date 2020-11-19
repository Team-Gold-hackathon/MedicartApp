from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def products(request):
#     products=Product.objects.all()
#     return render(request, 'check/products.html',{'products':products})

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def customer(request, pk):
#     customer=Customer.objects.get(id=pk)
#     orders = customer.order_set.all()
#     order_count = orders.count()
#     context = {'customer':customer, 'orders':orders, 'order_count':order_count}
#     return render(request, 'check/customer.html', context)