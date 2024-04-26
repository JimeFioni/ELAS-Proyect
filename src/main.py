import flet as ft
import shutil
import os
from pathlib import Path
from reconocimiento_emociones import reconocimiento_emociones

import nbconvert
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

def download_csv():
    ruta_origen = "../data/resultados/emociones_clase1.csv"
    try:
        ruta_escritorio = str(Path.home() / "Desktop")
        nombre_archivo = os.path.basename(ruta_origen)
        ruta_destino = os.path.join(ruta_escritorio, nombre_archivo)
        shutil.copy(ruta_origen, ruta_destino)
        print("Archivo CSV generado copiado al escritorio del usuario.")

        return True, ruta_destino
    except Exception as e:
        print("Error al copiar el archivo CSV generado al escritorio:", e)
        return False, None
    
def convert_to_html():
    ruta_origen = "notebooks/analisis.ipynb" 
    try:
        print("Leyendo el notebook...")
        with open(ruta_origen, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)
        
        print("Ejecutando el notebook...")
        executor = ExecutePreprocessor(timeout=600, kernel_name='python3')
        try:
            processed_notebook, _ = executor.preprocess(notebook, {'metadata': {'path': os.path.dirname(ruta_origen)}})
        except Exception as e:
            print("Error al ejecutar el notebook:", e)
            return False, None
        
        print("El notebook se ha ejecutado correctamente.")

        ruta_escritorio = str(Path.home() / "Desktop")
        html_exporter = nbconvert.HTMLExporter()
        (html_body, resources) = html_exporter.from_notebook_node(processed_notebook)
        nombre_archivo_html = os.path.splitext(os.path.basename(ruta_origen))[0] + ".html"
        ruta_destino = os.path.join(ruta_escritorio, nombre_archivo_html)

        with open(ruta_destino, "w", encoding="utf-8") as f:
            f.write(html_body)
        print("Archivo HTML generado y guardado en el escritorio del usuario.")
        return True, ruta_destino
    except Exception as e:
        print("Error al convertir o guardar el archivo HTML:", e)
        return False, None

def upload_video(result):
    if result is not None and result.files is not None:
        if len(result.files) == 1:
            f = result.files[0]
            filename, file_extension = os.path.splitext(f.name)
            if file_extension.lower() in ('.mp4', '.avi', '.mov', '.mkv', '.wmv'):
                destination_path = "../data/pruebas/" + f.name 
                try:
                    shutil.copy(f.path, destination_path)
                    print("Video guardado exitosamente en:", destination_path)
                    
                    duracion_analisis = 60
                    reconocimiento_emociones(destination_path, duracion_analisis)

                except FileNotFoundError:
                    print("Error: No se encontró el archivo o la ruta de destino no es válida.")
                except Exception as ex:
                    print("Error al guardar el video:", str(ex))
            else:
                print("Error: El archivo seleccionado no es un video.")
        else:
            print("Error: Selecciona solo un archivo de video.")
    else:
        print("Error: No se seleccionó ningún archivo.")

def choose_video():
    global file_picker
    print("Abriendo ventana de selección de archivos...")
    file_picker.pick_files(allow_multiple=False)

def main(page: ft.Page):
    page.window_width = 1300
    page.window_height = 700

    global file_picker
    file_picker = ft.FilePicker(on_result=upload_video)

    page.title = "ELAS TECHNOLOGY"
    page.bgcolor = "black"


    page.add(
        ft.Row([
            ft.Container(
                content=ft.Image(src="img/logo.webp", width=200, height=200),
                height=100,
                width=300,
            ),

            ft.Container(
                content=ft.Text("Programa de Reconocimiento de emociones", size=50, font_family="BankGothic Md Bt",
                color="white",
                weight=ft.FontWeight.W_100,
                text_align = "center"),
                width = 900,
                alignment = ft.alignment.center
            )
        ]),

        ft.Row([
            ft.Container(
                content=ft.Image(src="img/emociones.png", width=400, height=400),
                margin = 40),
            ft.Column([
                ft.Container(
                    content=ft.ElevatedButton("Buscar y cargar video", on_click=lambda _: choose_video()),
                    width=500,
                    height=100,
                    padding=30,
                    margin=10),
                ft.Container(
                    content=ft.ElevatedButton("Descargar CSV", on_click=lambda _: download_csv()),
                    width=500,
                    height=100,
                    padding=30,
                    margin=10),
                ft.Container(
                    content=ft.ElevatedButton("Descargar informe", on_click=lambda _: convert_to_html()),
                    width=500,
                    height=100,
                    padding=30,
                    margin=10),
            ]),
            
        ]),

        
        ),
        

    page.overlay.append(file_picker)
    page.update()

ft.app(main)





















