from django.shortcuts import render
from .models import studetail
# Create your views here.
def students(request):
    stuname=studetail.objects.all()
    
    #object only create
    # student_filter =studetail.objects.filter(name="jose")
    # print("student_filter",student_filter)

    #print first name in the table
    # student_first = studetail.objects.first()
    # print(" first name", student_first.name)
    
    #print the last name in the table
    # last_student = studetail.objects.last()
    # print("last name", last_student.name)

    #error
    # get_va =studetail.objects.get(name="jose")
    # print("getva", get_va.name)

    #object will create
    # exclude_opt = studetail.objects.exclude(name="jose")
    # print("exclude_opt", exclude_opt)

    #total count of rows
    # count_opt = studetail.objects.count()
    # print("totol count", count_opt)

    #create object and print it in the order of alphabet
    # order_by = studetail.objects.order_by('name')
    # print("order_by", order_by)

    #print the values of the name(all names)
    # val = studetail.objects.values('name')
    # print("val", val)

    #print the values in list format(with name and school values)
    # val_li = studetail.objects.values('name', 'school')
    # print("val_li", val_li)

    #print the distinct values in names
    # dist = studetail.objects.values('name').distinct()
    # print("dist", dist)

    #update the name from suji to sujitha
    # upda = studetail.objects.filter(name="suji").update(name="sujitha")
    # print("update", upda)

    # dele =studetail.objects.filter(name="jose").delete()
    # print("dele", dele)

    #error
    # student_countby_name = studetail.objects.values('name').annotate(student_count=Count('id'))
    # print("annotate", student_countby_name)
    return render(request,'student.html',{'stu1':stuname})


def set_session(request):
    request.session['name'] = 'vvv'
    response = render(request,'stu.html')
    response.set_cookie('accepttoken','12345')
    return response

def get_session(request):
    name = request.session.get('name','kani')
    school = request.COOKIES.get('accepttoken', '12345')
    return render(request,'stu.html', {'name':name, 'school':school})    