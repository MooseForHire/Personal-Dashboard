from django.shortcuts import render


posts = [
    {
        'author' : 'Caleb',
        'title' : 'First post',
        'content' : 'Content of my first post',
        'date_posted' : 'October 2021'
    },
    {
        'author' : 'Bob',
        'title' : 'Second post',
        'content' : 'Content of my second post',
        'date_posted' : 'October 1 2021'
    }
]




#Function to handle the traffic from the homepage to our dashboard
def home(request):

    #Return the home.html template
    #Still returns an http response still.
    return render(request, 'dash/home.html')

#About guyaki view
def about(request):
    return render(request,'dash/about.html', {'title' : ':D'} )


def mydash(request):

    context = {
    'posts': posts
}
    return render(request,'dash/mydash.html', context)


