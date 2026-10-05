from django.shortcuts import render

def index(request):
    # Diccionario con los dos temas requeridos, sus descripciones e imágenes
    temas = [
        {
            'id': 1,
            'nombre': 'Ciberseguridad en Redes',
            'descripcion': 'Importancia de la protección de datos, cortafuegos y el análisis de vulnerabilidades en infraestructuras modernas.',
            'imagenes': [
                'inicio_martinez_espinoza/images/tema1_img1.jpg',
                'inicio_martinez_espinoza/images/tema1_img2.jpg'
            ]
        },
        {
            'id': 2,
            'nombre': 'Desarrollo Web con Django',
            'descripcion': 'Construcción de aplicaciones robustas utilizando patrones MVT, ORM y control de versiones con Git.',
            'imagenes': [
                'inicio_martinez_espinoza/images/tema2_img1.jpg',
                'inicio_martinez_espinoza/images/tema2_img2.jpg'
            ]
        }
    ]
    
    return render(request, 'inicio_martinez_espinoza/inicio.html', {'temas': temas})