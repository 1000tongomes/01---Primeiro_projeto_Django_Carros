from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm



def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
     cars = Car.objects.filter(model__icontains=search)
 

    return render(
        request,
        'cars.html',
        {'cars':cars},
        )


def new_car_view(request):
  if request.method == 'POST':
    new_car_from = CarModelForm(request.POST, request.FILES)
    if new_car_from.is_valid():
      new_car_from.save()
      return redirect('cars_list')
  else:
    new_car_from = CarModelForm()
  return render(request,'new_car.html',{'new_car_form':new_car_from})