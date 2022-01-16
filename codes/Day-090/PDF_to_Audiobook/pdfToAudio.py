from gtts import gTTS
import PyPDF2
import pdfplumber


class PDFToAudio:
    ENGLISH = 'en'
    HINDI = 'hi'

    def pdf_to_audio(self, pdf_file, lang, dest):
        """
            Convert PDF to audio 
            Return: Name and location of audio file
        """
        file = open(pdf_file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(file)
        pages = pdfReader.numPages
        text = ''
        with pdfplumber.open(file) as pdf:
            for i in range(pages):
                page = pdf.pages[i]
                text += page.extract_text()

        if text:
            tts = gTTS(text, lang=lang)
            tts.save(f'{dest}/audio.mp3')
