# this modified views.py is to add the interface component 
# this is to serve the Django application to Gradio

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import gradio as gr
import threading

def greet(name):
    return "Hello " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

@csrf_exempt
def gradio_view(request):
    if request.method == 'POST':
        threading.Thread(target=iface.launch, kwargs={'inline': False, 'share': True}).start()
        return HttpResponse("Gradio interface launched!")
    return HttpResponse("Send a POST request to launch Gradio.")
