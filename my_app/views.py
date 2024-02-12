from django.shortcuts import render, redirect
from .models import Scheduler, personalCV, Education, Work, Skils
import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def Home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender= request.POST.get('gender')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        summary = request.POST.get('summary')
        institute = request.POST.get('institute')
        graduation_date = request.POST.get('graduation_date')
        workplace = request.POST.get('workplace')
        start_date = request.POST.get('start_date')
        skill_name= request.POST.get('skill_name')
        skill_detail = request.POST.get('skill_detail')

        if image:
            cvNew = personalCV.objects.create(name = name, dob= dob, gender= gender, image=image, address=address, summary=summary)
            cvNew.save()
            eduNew = Education.objects.create(institute=institute,graduation_date =graduation_date)
            eduNew.save()
            workNew = Work.objects.create(workplace=workplace,start_date=start_date)
            workNew.save()
            skillNew = Skils.objects.create(skill_name=skill_name,skill_detail=skill_detail)
            skillNew.save()
            return redirect('cv')
        else:
            cvNew = personalCV.objects.create(name = name, dob= dob, gender= gender, address=address, summary=summary)
            cvNew.save()
            eduNew = Education.objects.create(institute=institute,graduation_date =graduation_date)
            eduNew.save()
            workNew = Work.objects.create(workplace=workplace,start_date=start_date)
            workNew.save()
            skillNew = Skils.objects.create(skill_name=skill_name,skill_detail=skill_detail)
            skillNew.save()
            return redirect('cv')

    return render(request, "app_temp/index.html")


def cv(request):
    cvs = personalCV.objects.all()
    education = Education.objects.all()
    work = Work.objects.all()
    skills = Skils.objects.all()
    return render (request, "app_temp/cv.html", locals())

# Add education, work and skills
def addEdu(request):
    institute = request.POST.get('institute')
    graduation_date = request.POST.get('graduation_date')
    if institute:
        eduNew = Education.objects.create(institute=institute,graduation_date =graduation_date)
        eduNew.save()
        return redirect('cv')

    return render (request, "app_temp/education.html")

def addWork(request):
    workplace = request.POST.get('workplace')
    start_date = request.POST.get('start_date')
    if workplace:
        workNew = Work.objects.create(workplace=workplace,start_date=start_date)
        workNew.save()
        return redirect('cv')

    return render (request, "app_temp/work.html")

def addSkill(request):
    skill_name= request.POST.get('skill_name')
    skill_detail = request.POST.get('skill_detail')
    if skill_name:
        skillNew = Skils.objects.create(skill_name=skill_name,skill_detail=skill_detail)
        skillNew.save()
        return redirect('cv')
    return render (request, "app_temp/skill.html")





# PDF 
def pdfCv(request):
    cvs = personalCV.objects.all()
    education = Education.objects.all()
    work = Work.objects.all()
    skills = Skils.objects.all()

    template_path = 'app_temp/pdfcv.html'
    # context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename="cv.pdf"' 
    #attachment;
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(locals())

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # link_callback=link_callback
    # if error then show some funny view

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def new_cv(request, id):
    p = personalCV.objects.get(id=id)
    pe = personalCV.objects.all()
    ed = Education.objects.all()
    wr = Work.objects.all()
    sk =Skils.objects.all()
    if p.name:
        pe.delete()
        ed.delete()
        wr.delete()
        sk.delete()
        if p.image != 'def.jpg':
            os.remove(p.image.path)
    return redirect('home')

def scheduler(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        task_date = request.POST.get('task_date')
        task_time = request.POST.get('task_time')
        taskNew = Scheduler.objects.create(task=task, task_date=task_date,task_time=task_time )
        taskNew.save()
    
    scheduler = Scheduler.objects.all()
        
    return render(request, "app_temp/scheduler.html",locals())


def delete_task(request, id):
    p = Scheduler.objects.get(id=id)
    if p.task:
        p.delete()

    return redirect('scheduler')