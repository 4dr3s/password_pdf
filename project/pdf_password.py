import PyPDF2

def proteger_pdf(archivo_entrada, archivo_salida, clave):
    with open(archivo_entrada, 'rb') as entrada:
        lectura = PyPDF2.PdfReader(entrada)
        escribir = PyPDF2.PdfWriter()
        
        for num_pag in range (len(lectura.pages)):
            pagina = lectura.pages[num_pag]
            escribir.add_page(pagina)
            
        escribir.encrypt(clave)
        
        with open(archivo_salida, 'wb') as salida:
            escribir.write(salida)
            
archivo_entrada = 'project/Cambio De Paralelo.pdf'
archivo_salida = './Protegido.pdf'
clave = 'password'

proteger_pdf(archivo_entrada, archivo_salida, clave)