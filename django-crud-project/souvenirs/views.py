from django.shortcuts import render
from django.shortcuts import render, redirect  
from souvenirs.forms import BookingForm
from souvenirs.models import BookingRecords
 
def reg(request):  
    if request.method == "POST":  
        form = BookingForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = BookingForm()  
    return render(request,'index.html',{'form':form}) 
 
def records(request):  
    bookings = BookingRecords.objects.all()  
    return render(request,"records.html",{'bookingrecords':bookings})  

def edit(request, id):  
    booking = BookingRecords.objects.get(booking_id=id)  
    return render(request,'edit.html', {'bookingrecords':booking})
  
def update(request, id):  
    booking = BookingRecords.objects.get(booking_id=id)  
    form = BookingForm(request.POST, instance = booking)  
    if form.is_valid():  
        form.save()  
        return redirect("/records")  
    return render(request, 'edit.html', {'form': form, 'bookingrecords': booking})

def destroy(request, id):  
    booking = BookingRecords.objects.get(booking_id=id)  
    booking.delete()  
    return redirect("/records")