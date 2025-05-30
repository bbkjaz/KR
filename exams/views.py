from django.shortcuts import render
from .models import ikexam

def exam_list(request):
    exams = ikexam.objects.filter(is_public=True)
    
    context = {
        'exams': exams,
        'fio': 'Квашнина Ирина Александровна',
        'group': '231-365'
    }
    return render(request, 'exams/exam_list.html', context)