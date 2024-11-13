from django.shortcuts import render
from django.shortcuts import render
from .models import ProblemaAmbiental

# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})
def about(request):
    return render(request, 'about.html')
def acerca(request):
    return render(request, 'acerca.html')

def index4(request):
    return render(request, 'index4.html')



from django.shortcuts import render, redirect
from django.http import HttpRequest

questions = [
    {"question": "¿Cuál es la principal causa del cambio climático?", "options": ["El uso de bolsas de papel", "La deforestación", "La producción de energía a partir de fuentes renovables", "El reciclaje de plástico"], "correct": "La deforestación"},
    {"question": "¿Qué gas es conocido por contribuir al efecto invernadero?", "options": ["Oxígeno", "Dióxido de carbono", "Helio", "Nitrógeno"], "correct": "Dióxido de carbono"},
    {"question": "¿Cuál es la forma más efectiva de reducir la cantidad de residuos?", "options": ["Comprar más productos desechables", "Usar productos de un solo uso", "Reutilizar y reciclar", "Quemar basura"], "correct": "Reutilizar y reciclar"},
    {"question": "¿Qué tipo de energía se considera más limpia y sostenible?", "options": ["Energía solar", "Energía nuclear", "Energía a base de carbón", "Energía derivada del petróleo"], "correct": "Energía solar"},
    {"question": "¿Cuál es uno de los principales contaminantes del agua?", "options": ["Agua destilada", "Productos químicos agrícolas", "Agua de lluvia", "Aire puro"], "correct": "Productos químicos agrícolas"},
    {"question": "¿Qué práctica ayuda a conservar el agua?", "options": ["Dejar el grifo abierto mientras se cepilla los dientes", "Tomar duchas largas", "Recolectar agua de lluvia", "Lavar el coche con manguera sin cuidado"], "correct": "Recolectar agua de lluvia"},
    {"question": "¿Cuál es un efecto negativo de la contaminación del aire?", "options": ["Mejora la salud respiratoria", "Aumenta la biodiversidad", "Provoca enfermedades respiratorias", "Reduce el calentamiento global"], "correct": "Provoca enfermedades respiratorias"},
    {"question": "¿Qué se puede hacer para ayudar a proteger la vida silvestre?", "options": ["Comprar productos hechos con especies en peligro", "Destruir hábitats naturales", "Apoyar reservas naturales y parques nacionales", "Ignorar las leyes de protección ambiental"], "correct": "Apoyar reservas naturales y parques nacionales"},
    {"question": "¿Qué tipo de transporte es más amigable con el medio ambiente?", "options": ["Coches eléctricos", "Automóviles a gasolina", "Aviones comerciales", "Motocicletas"], "correct": "Coches eléctricos"},
    {"question": "¿Cuál es una buena manera de reducir el uso del plástico?", "options": ["Usar botellas desechables", "Llevar bolsas reutilizables al hacer compras", "Comprar productos envueltos en plástico", "Usar pajitas desechables"], "correct": "Llevar bolsas reutilizables al hacer compras"}
]



def quiz_view(request: HttpRequest):
    if 'question_index' not in request.session:
        request.session['question_index'] = 0
        request.session['correct_answers'] = 0

    index = request.session['question_index']
    total_questions = len(questions)
    
    if index >= len(questions):
        return render(request, 'juego_terminado.html', {'correct_answers': request.session['correct_answers']})

    question = questions[index]
    return render(request, 'juego.html', {'question': question, 'index': index + 1, 'total_questions':total_questions})


def answer_view(request: HttpRequest):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        index = request.session['question_index']
        if questions[index]["correct"] == selected_option:
            request.session['correct_answers'] += 1

        request.session['question_index'] += 1
        return redirect('quiz')
    return redirect('quiz')

# Nueva vista para reiniciar el juego
def reiniciar_view(request: HttpRequest):
    # Restablece el índice y el contador de respuestas correctas
    request.session['question_index'] = 0
    request.session['correct_answers'] = 0
    return redirect('quiz')
