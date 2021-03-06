from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView
from nashr.settings import PROFILE_KEY, PAYTAB_API_SERVERKEY, API_ENDPOINT
import json
import requests
from django.contrib import messages





from services.models import (
    TranslateService,
    RequestDesignService,
    Vouchers,
    PaidVoucher
)
from services.forms import (
    TrnaslateServiceForm
)
from designs.forms import (
    TakeDesignForm
)
from designs.models import (
    TakeDesign
)


def AllVouchers(request):
    vouchers = Vouchers.objects.filter(user = request.user.pk , is_paid = False)
    return render(request , 'services/all_vouchers.html' , context={"vouchers":vouchers})
        
     
def PayVoucher(request , pk):
    try:
        voucher = Vouchers.objects.get(pk=pk)
        paid =  PaidVoucher(voucher = voucher)
        paid.save()
        payload = {
            "profile_id": PROFILE_KEY,
            "tran_type": "sale",
            "tran_class": "ecom",
            "cart_description": f"{voucher.description}",
            "cart_id": "50",
            "cart_currency": "sar",
            "cart_amount": int(voucher.amount),
            "callback": "https://naashr.co",
            "return": "https://naashr.co/"
        }
        headers = {
            "authorization": PAYTAB_API_SERVERKEY,
            "Content-Type": 'application/json; charset=utf-8'
        }
        r = requests.post(API_ENDPOINT, data=json.dumps(payload), headers=headers)
        data = json.dumps(r.json())
        content = json.loads(data)
        voucher.is_paid = True
        voucher.save()
        return redirect(content['redirect_url'])
    except:
        messages.error(request,
                             "حدث خطأ ")
        return redirect('all-vouchers')
    

        
        
    

   

class RequestTranslateServiceView(CreateView):
    model = TranslateService
    form_class = TrnaslateServiceForm
    template_name = 'services/design_service.html'

    def get_success_url(self):
        return reverse('home-page')


class RequestDesignServiceView(View):
    def get(self, request):
        return render(request, 'services/translate_service.html')

    def post(self, request):
        book_size = request.POST.get('book_sizes')
        book_title = request.POST.get('book_title')
        author_name = request.POST.get('author_name')
        translator_name = request.POST.get('translator_name')
        scientific_rank = request.POST.get('scientific_rank')
        version_number = request.POST.get('version_number')
        house_logo = request.POST.get('house_logo')
        author_name_tail = request.POST.get('author_name_tail')
        translator_name_tail = request.POST.get('translator_name_tail')
        scientific_rank_tail = request.POST.get('scientific_rank_tail')
        part_number = request.POST.get('part_number')
        version_number_tail = request.POST.get('version_number_tail')
        about_book = request.POST.get('about_book')
        isbn = request.POST.get('isbn')
        house_information = request.POST.get('house_information')
        email = request.POST.get('email')
        notes = request.POST.get('notes')

        file = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        design_request = RequestDesignService(book_size=book_size, title_book=book_title, author_name=author_name,
                                              translator_name=translator_name, scientific_rank=scientific_rank,
                                              version_number=version_number, house_logo=house_logo,
                                              author_name_tail=author_name_tail,
                                              translator_name_tail=translator_name_tail,
                                              scientific_rank_tail=scientific_rank_tail, part_number=part_number,
                                              version_number_tail=version_number_tail, about_book=about_book,
                                              isbn_number=isbn, images=file,
                                              house_info=house_information, communication=email, note=notes
                                              )
        design_request.save()
        return redirect('home-page')


class AllServicesForDesignView(View):
    def get(self, request):
        requests = RequestDesignService.objects.filter(is_shown_designer=True)
        paginator = Paginator(requests, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'dashboard/all_designs.html', context={"designs": page_obj})


class RequestServiceDetails(DetailView):
    model = RequestDesignService
    template_name = 'designs/design_detail.html'


class CreateTakeDesignRequest(CreateView):
    model = TakeDesign
    form_class = TakeDesignForm
    template_name = 'designs/TakeDesign.html'

    def form_valid(self, form):
        take_Design = form.save(commit=True)
        take_Design.user = self.request.user
        take_Design.save
        return super(CreateTakeDesignRequest, self).form_valid(form)

    def get_success_url(self):
        return reverse('dashboard')
