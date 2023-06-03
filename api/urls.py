from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
#companies/{companyId}/employees

# http://127.0.0.1:8000/api/v1/
# http://127.0.0.1:8000/api/v1/companies/
# http://127.0.0.1:8000/api/v1/employees/
# http://127.0.0.1:8000/api/v1/companies/1/
# http://127.0.0.1:8000/api/v1/companies/1/employees/
#

urlpatterns = [    
    path('',include(router.urls))
      
]

