from django.shortcuts import render

def post_list(request):
	return render(request, 'blog/post_list.html', {})

#client request > include app/urls.py into project/urls.py > 
#app/urls.py define html files > views.py renders html and sends to client.