from django.shortcuts import render,redirect,HttpResponse
from learnapp.models import Person
from learnapp.forms  import PersonForm
from django.core.mail import send_mail
from django.conf import settings

def login(request):
    return render(request,'login.html')
def Show(request):
    stu=Person.objects.all()
    return render(request,'Show.html',{'stu':stu}) 

def sign(request):
    Pe=PersonForm()
    if request.method=='POST':
        Pe=PersonForm(request.POST)
        email=request.POST['Email']
        ak=Person.objects.all()
        for i in ak:
            if i.Email == email:
                return HttpResponse('Email Already register')
        else:
            Password=request.POST['Password']
            Repassword=request.POST['Repassword']
            if Password==Repassword:
                if Pe.is_valid():
                    Pe.save()
                    return redirect('/login')
                else:
                        pass
            else:
                return HttpResponse('Wrong Password') 
    else:
        pe=PersonForm()
        return render(request,'sign.html',{'Person':Pe})




        

    
def update(request,id):
    stu=Person.objects.get(id=id)
    form=PersonForm(request.POST,instance=stu)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'update.html',{'form':stu})
    
def delete(request,id):
    stu=Person.objects.get(id=id) 
    stu.delete()
    return redirect('/show')

def login(request):
    if request.method=='POST':
        user=request.POST.get('FirstName')
        Password=request.POST.get('Password')
        stu=Person.objects.all()
        if user=='cathy'  and Password=='123':
            return redirect ('/show')
        else:
            for  i in stu:
                if user==i.FirstName and Password==i.Password:
                    stu=Person.objects.get(id=i.id)   
                    return render(request,'user.html',
                    
                    {'i':stu})
            else:
                return HttpResponse ('wrong username/password') 
    return render(request,'login.html')                   

# def email(request):
    # if request.method=='POST':
    #     message=request.POST['message']
    #     email=request.POST['email']
    #     title=request.POST['title']
    #     send_mail(
    #         'Contact Form',
    #         message,
    #         settings.EMAIL_HOST_USER,
    #         [email],
    #         #fail_silently=False 
    #     )
    # return render(request,'email.html')    

  







