
from django.shortcuts import render

# Page d'accueil
def home(request):
    context = {
        'nom': 'Molka',
        'formation': 'Développement Web avec Django',
        'connecte': True,
        'cours_list': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript'],
    }

    return render(request, 'myfirstapp/home.html', context)


# Page À propos
def about(request):
    return render(request, 'myfirstapp/about.html')
