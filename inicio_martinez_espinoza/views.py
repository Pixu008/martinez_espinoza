from django.shortcuts import render

# Diccionario centralizado con los temas y sus imágenes
TEMAS_DATA = [
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

def index(request):
    """Vista principal que lista los dos temas en la raíz (/)"""
    return render(request, 'inicio_martinez_espinoza/inicio.html', {'temas': TEMAS_DATA})

def detalle_tema(request, tema_id):
    """Vista que redirige y muestra los detalles y el carrusel de imágenes de un tema específico"""
    tema = next((t for t in TEMAS_DATA if t['id'] == tema_id), None)
    
    if not tema:
        from django.http import Http404
        raise Http404("Tema no encontrado")
        
    return render(request, 'inicio_martinez_espinoza/detalle.html', {'tema': tema})