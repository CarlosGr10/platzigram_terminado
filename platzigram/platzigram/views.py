from django.http import HttpResponse

nombres = [{'Nombre':'Carlos',
            'apellido':'Garcia',
            'edad':24
            },

            {'Nombre':'Paco',
            'apellido':'Gonzalez',
            'edad':24
            },

            {'Nombre':'Marck',
            'apellido':'Efron',
            'edad':24
            }
            ]

def lis(request):
    contenido = []
    for i in nombres:
     return HttpResponse(str(i))


 
    








    


