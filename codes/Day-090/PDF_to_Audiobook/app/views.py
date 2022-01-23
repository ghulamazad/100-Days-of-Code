from django.shortcuts import render
from app.pdfToAudio import PDFToAudio
import io


def home(request):
    if request.method == 'POST' and request.FILES['pdf']:
        lang = request.POST.get('lang')
        pdf = request.FILES['pdf'].read()
        filename = str(request.FILES['pdf']).split('.')[0]
        # if pdf available
        if pdf:
            audio_filename = PDFToAudio().pdf_to_audio(
                file=io.BytesIO(pdf), lang=PDFToAudio.ENGLISH, filename=filename)
            context = {
                "status": True,
                "audio_file": audio_filename

            }
            return render(request, 'index.html', context)

    return render(request, 'index.html')
