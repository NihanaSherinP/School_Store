from django.contrib import messages
from django.shortcuts import render

# Create your views here.
# orders/views.py

from django.shortcuts import render, redirect
from .models import Department, Course
from .forms import OrderForm
from django.shortcuts import render, redirect
from .models import Department, Course
from .forms import OrderForm
from django.http import JsonResponse



# def order_page(request):
#
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             # Process the form submission, e.g., save to the database
#             message = "Order Confirmed"
#     else:
#         form = OrderForm()
#
#     return render(request, 'userhome.html', {'form': form, 'message': message if 'message' in locals() else None})
# from django.contrib import messages

# def order_page(request):
#
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             # Process the form submission, e.g., save to the database
#             messages.success(request, 'Order Confirmed')
#         else:
#             messages.error(request, 'Order Failed. Please correct the errors in the form.')
#     else:
#         form = OrderForm()
#
#     return render(request, 'userhome.html', {'form': form})
def order_page(request):
    message = None

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process the form submission, e.g., save to the database
            message = "Order Confirmed"

        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = OrderForm()

    return render(request, 'userhome.html', {'form': form, 'message': message})
def getdata(request):
    department = Department.objects.all()
    course = Course.objects.all()

    return render(request, 'userhome.html', {'department': department, 'course': course})
from django.http import JsonResponse

def getdata(request):
    department = Department.objects.all().values('id', 'name')
    course = Course.objects.all().values('id', 'name')

    data = {'department': list(department), 'course': list(course)}

    return JsonResponse(data, safe=False)
def getcourses(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
        department_id = request.GET.get('department_id')

        # Assuming you have a ForeignKey relationship between Course and Department
        courses = Course.objects.filter(deptid_id=department_id)

        # Convert courses to a list of dictionaries for JsonResponse
        courses_list = [{'id': course.id, 'name': course.name} for course in courses]

        return JsonResponse({'courses': courses_list}, safe=False)

    return JsonResponse({'error': 'Invalid request'}, status=400)