from django.shortcuts import render

def post_list(request):
    return render(request, 'team/post_list.html', {})
