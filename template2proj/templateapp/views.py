from django.shortcuts import render
import datetime
def time_wish(request):
    dt=datetime.datetime.now()
    my_dict={'insert_date':dt}
    return render(request,'templateapp/timewish.html',context=my_dict)

def template_view(request):
    dt=datetime.datetime.now()
    name='Mahesh'
    rollno=101
    marks=100
    my_dict={'date':dt,'name':name,'rollno':rollno,'marks':marks}
    return render(request,'templateapp/results.html',my_dict)

def wish_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg ='Hello Guest !!!! Very Very Good '
    if h<12 :
        msg +='Morning!!!'
    elif h<16 :
        msg +='AfterNoon!!!'
    elif h<21 :
        msg +='Evening!!!'
    else:
        msg ='Hello Guest !!!! Very Very Good Night!!!'
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'templateapp/wish.html',context=my_dict)

def dynamic_view(request):
    dt = datetime.datetime.now()
    dt_dct = {
        'dyn_dat' : dt,
        'wish' : 'Good-Evening',
        'sno': 1569,
        'sname' : 'Naidu',
        'smarks' : 96
    }
    return render(request,'templateapp/dynamicpage.html',context=dt_dct)