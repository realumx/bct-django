from django.shortcuts import redirect, render
from students.models import Student


def home(request):
    departments = [
        'Computer Science',
        'Information Technology',
        'Electronics',
        'Mechanical',
        'Civil',
        'Business Administration',
    ]

    if request.method == 'POST':
        action = request.POST.get('action')
        student_id = request.POST.get('student_id')

        if action in ['create', 'update']:
            submitted_data = {
                'name': request.POST.get('name', '').strip(),
                'roll_number': request.POST.get('roll_number', '').strip(),
                'email': request.POST.get('email', '').strip(),
                'department': request.POST.get('department', '').strip(),
                'year': request.POST.get('year', '').strip(),
            }

            if all(submitted_data.values()):
                if action == 'update' and student_id:
                    Student.objects.filter(id=student_id).update(**submitted_data)
                else:
                    Student.objects.create(**submitted_data)

        if action == 'delete':
            if student_id:
                Student.objects.filter(id=student_id).delete()

        return redirect('home')

    students = Student.objects.all().order_by('-created_at')
    edit_id = request.GET.get('edit')
    edit_student = Student.objects.filter(id=edit_id).first() if edit_id else None

    form_data = {
        'name': edit_student.name if edit_student else '',
        'roll_number': edit_student.roll_number if edit_student else '',
        'email': edit_student.email if edit_student else '',
        'department': edit_student.department if edit_student else '',
        'year': edit_student.year if edit_student else '',
    }

    context = {
        'departments': departments,
        'students': students,
        'edit_student': edit_student,
        'form_data': form_data,
    }
    return render(request, 'home.html', context)
