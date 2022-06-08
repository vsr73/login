from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def signup(request):
    if request.method=='POST':
        x=request.POST.get("fname")
        y=request.POST.get("lname")
        z=request.POST.get("mobielnum")
        w=request.POST.get("mail")
        t=request.POST.get("addrs")
        p=request.POST.get("pswrd")
        q=request.POST.get("cnfrm_pswrd")
        if p==q:
            try:
                mems=details(fname=x,lname=y,mobile_num=z,address=t,password=p,mail=w)
                mems.save()
                messages.info(request,"login to view details,account created successfully")
                return redirect('/')

            except :
                messages.error(request,'error try again')
                return redirect('/signup')
        else:
            messages.error(request,'password doesnt match')
            return redirect('/signup')


    else:
        return render(request,"testapp/home.html")
def login(request):
    if request.method=='POST':
        email_temp=request.POST.get('mail')
        pswrd_temp=request.POST.get("pswrd")
        try:
            user=details.objects.get(mail=email_temp,password=pswrd_temp)
            flag=2
        except:
            flag=0
        if flag ==2:
            dict={'check':user}
            return render(request,'testapp/success.html',dict)
        else:
            return render(request,'testapp/invalid.html')
    else:
        return render(request,'testapp/login.html')



def mainpage(request):
    return render(request,'testapp/mainpage.html')


def logout(request):
    messages.info(request,"logged out successfully")
    return redirect('/login')
def test(request):
    return redirect('/')
def edit(request,pk):
    user=details.objects.get(mail=pk)
    if request.method == 'POST':
        user.fname=request.POST.get("fname")
        user.lname=request.POST.get("lname")
        user.mobile_num=request.POST.get("mobielnum")
        user.mail=request.POST.get("mail")
        user.address=request.POST.get("addrs")
       
    
        user.save()
        dict={'check':user}
        messages.info(request,'details updated successfully')
        return render(request,'testapp/success.html',dict)
        '''except:
            messages.info(request,'error try again')'''
    else:
        return render(request,'testapp/updateform.html',{'user':user})


    '''  if user:
            messages.error(request,"email already exists try a new mail")
            return redirect('/signup')
        el'''
def delete(request,pk):
    user=details.objects.get(mail=pk)
    user.delete()
    messages.info(request,'deleted successfully')
    return render(request,'testapp/mainpage.html')