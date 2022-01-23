from gtts import gTTS
import PyPDF2
import pdfplumber
import os


class PDFToAudio:
    ENGLISH = 'en'
    HINDI = 'hi'

    def pdf_to_audio(self, file, lang, filename='audio'):
        """
            Convert PDF to audio
            Return: Name and location of audio file
        """
        audio_filename = f"{filename}.mp3"
        pdfReader = PyPDF2.PdfFileReader(file)
        pages = pdfReader.numPages
        text = ''
        with pdfplumber.open(file) as pdf:
            for i in range(pages):
                page = pdf.pages[i]
                text += page.extract_text()

        if text:
            tts = gTTS(text, lang=lang)
            tts.save(os.path.join('static', audio_filename))

        return audio_filename
