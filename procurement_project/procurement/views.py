from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProcurementForm
from .models import Procurement

def submit_procurement(request):
    if request.method == 'POST':
        form = ProcurementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Procurement submitted successfully!')
            return redirect('procurement_list')
    else:
        form = ProcurementForm()

    return render(request, 'procurement/submit_procurement.html', {'form': form})

def procurement_list(request):
    procurements = Procurement.objects.filter(branch='Branch A')  # Filter by branch dynamically if needed
    return render(request, 'procurement/procurement_list.html', {'procurements': procurements})

def approval_list(request):
    procurements = Procurement.objects.filter(status='Pending')
    return render(request, 'procurement/approval_list.html', {'procurements': procurements})

def approve_procurement(request, pk):
    procurement = Procurement.objects.get(pk=pk)
    procurement.status = 'Approved'
    procurement.save()
    return redirect('approval_list')