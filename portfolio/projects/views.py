from django.shortcuts import render
from projects.models import Project
# from usps import USPSApi, Address
#
#
# def check_address(address_info):
#     address = Address(
#         name='Tobin Brown',
#         address_1='1234 Test Ave.',
#         city='Test',
#         state='NE',
#         zipcode='55555'
#     )
#     usps = USPSApi('293PETIT2689', test=True)
#     validation = usps.validate_address(address)
#     print(validation.result)

# Create your views here.

# def project_list(request):
#     return render(request, 'projects/index.html')

def all_projects(request):
    # query the database to return all project objects
    projects = Project.objects.all()
    # print(projects)
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})
