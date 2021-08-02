from django.shortcuts import render,reverse,Http404, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
# from bmi.models import Product
# from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
# #from django.contrib.auth.mixins import LoginRequiredMixin
from bmi.models import Userdata
from bmi.forms import BmiCalculateForm

# # Create your views here.

# def dashboard(request):
#     return render(request, 'dashboard.html')

@login_required(login_url="user:login")
def bmi_list(request):
    bmis = Userdata.objects.filter(user=request.user)
    context = {"bmis": bmis}
    return render(request, 'bmi_list.html',context)

@login_required(login_url="user:login")
def bmi_calculate(request):
    form = BmiCalculateForm(request.POST)
    if form.is_valid():
        user_data = form.save(commit=False)
        user_data.user = request.user
        user_data.save()
        context = {"result": user_data.bmi, "category": user_data.bmi_category, "color": user_data.bmi_color, 'id': user_data.id,  "form": form}
        return render(request,"bmi_calculate.html",context)
    context ={"form":form}
    return render(request,"bmi_calculate.html",context)


@login_required(login_url="user:login")
def bmi_delete(request, *args, **kwargs):
    id = kwargs.get("id", None)
    Userdata.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("bmi:bmi_list"))
    
# # class ProductAddView(LoginRequiredMixin, CreateView):
# #     model = Product
# #     form_class = ProductForm
# #     template_name ="form.html"
        
# #     def get_success_url(self):
# #         return reverse('product:product_list')

# #     def form_valid(self, form):
# #         product = form.save(commit=False)
# #         product.user = self.request.user
# #         return super().form_valid(product)
#     # 
# @login_required(login_url="user:login")
# def product_add(request):
#     form = ProductForm(request.POST or None, request.FILES or None)
#     #context = {"form":form}
#     # if request.POST:
#     #     print(request.POST)
#     if form.is_valid():
#         # print(form.cleaned_data)
#         #user = request.user # Assignment
#         product = form.save(commit=False)
#         product.user = request.user
#         product.save()
#         #form = ProductForm()
#         #return HttpResponseRedirect("/product/product-list")
#         return HttpResponseRedirect(reverse("product:product_list"))
#     context = {"form":form}
#     return render(request, 'form.html',context)

# def product_edit(request,id):
#     product = get_object_or_404(Product, id=id)
#     form = ProductForm(request.POST or None, request.FILES or None, instance=product)
#     if form_is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse("product:product_list"))
#     context = {"form":form}
#     return render(request,"form.html", context)


# def product_delete(request,id):
#     product = get_object_or_404(Product,id=id)
#     product.delete()
#     return HttpResponseRedirect(reverse("product:product_list"))
    