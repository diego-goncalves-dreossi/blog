from django.shortcuts import render
from .forms import ContatoForm
from django.core.mail import EmailMessage

def contato(request):
    send = False
    form = ContatoForm(request.POST or None)

    if form.is_valid():
        #enviar e-mail
        nome = request.POST.get('nome','')
        email = request.POST.get('email','')
        mensagem = request.POST.get('mensagem','')
        emailM = EmailMessage(
            'Mensagem do blog django',
            'De {} <{}> Escreveu:\n\n{}'.format(nome,email,mensagem),
            'nao-responder@inbox.mailtrap.io',
            ['dididreo@hotmail.com'],
            reply_to=[email]
        )
        try:
            emailM.send()
            send = True
        except Exception as erro:
            print(erro)
            send = False

        
    contexto = {
        'form': form,
        'success':send
    }
    return render(request,'contato.html',contexto)
