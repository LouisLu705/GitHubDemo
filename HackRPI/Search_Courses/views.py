from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
"""
def get_template(template_name, using=None):
	content = loader.render_to_string(template_name)
	parse = content.split('\n')
	for x in range(len(parse)):
		if 'course=' in parse[x]:
			course = parse[x].split(' ')[3].split('=')[1]
		if 'time=' in parse[x]:
			time = parse[x].split(' ')[3].split('=')[1]
	return(course, time)
	#print(content)

data = get_template('Search_Courses/for_teachers.html')
"""
#input_course = home(request)

#table_data = [{
#	'course_o' : data[0]}, {'time_o' :data[1]
#}]

#print(table_data)
#print(table_data[0])
#print(table_data[1])
"""
context = {
		'course_o':data[0].replace("'", ''),'time_o':data[1].replace("'",'')
	}
"""
#print(context)

#for x in context.values():
#	for y in range(1):
#		print(x[y]['course_o'])
def submit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form)
            context = {'Chemistry 1': '7-9'}
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        context = {
		'Course':course.replace("'", ''),'Time':time.replace("'",'')}
    #return render(request, 'Search_Courses/find_tutors.html', context)
    
def home(request):
	input_course = render(request,'Search_Courses/home.html')
	return input_course

def about(request):
	return render(request, 'Search_Courses/for_teachers.html')

def find_tutors(request):
	return render(request, 'Search_Courses/find_tutors.html') #context)

def for_teachers(request):
	return render(request, 'Search_Courses/for_teachers.html')
