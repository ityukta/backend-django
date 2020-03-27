from django.shortcuts import render


from .models import *

# Create your views here.


def indexView(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST, args, kwargs)
    return render(request, 'html/login.html')


def registrationUserView(request, *args, **kwargs):
    if request.method == 'POST':
        data = dict(list(request.POST.items())[1:])
        print(data)
        name = data['username']
        email_id = data['email_id']
        password = data['password']
        department = data['department']
        faculty_type = data['type']
        try:
            ft_query = Type(type_description=faculty_type)
            ft_query.save()
            query = Faculty(name=name, email_id=email_id, password=password,
                            department=department)
            query.save()
            query.faculty_type.add(ft_query)
            a = Faculty.objects.get(name=name)
        except e:
            print(e)

        finally:
            pass

        # if a.name:
        #     context = {
        #         'status_code': 201,
        #         'status message': 'Created'
        #     }
        # else:
        #     context = {
        #         'status_code': 500,
        #         'status message': 'Invalid'
        #     }
        return render(request, '../../html.login.html')

        # Validate Error

    return render(request, 'html/register1.html')
