from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    emp=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(emp,safe=False)

# https://www.youtube.com/watch?v=DNFTUtZf1Zc      29:18
# https://github.com/LearnCodeWithDurgesh/companyapi/blob/main/companyapi/views.py