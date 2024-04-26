<div align="center">
  <img src='./data/pictures/Banner Elas Project.gif'>
  <br> 
</div>

<div align="center">

## Proyecto Data-BI/ Machine Learning: Reconocimiento de Emociones 🤖
</div>

<div align = "center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-FDEE21?style=flat-square&logo=apachespark&logoColor=black)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
</div>


### Descripcion 🤖
El proyecto de Reconocimiento de Emociones fue pensado para variadas utilidades; en este caso lo planteamos en el Aula teniendo como objetivo principal analizar y comprender el estado emocional de los estudiantes durante una clase específica, y conocer como se relaciona éste estado emocional con la comprensión de lo enseñado y los resultados finales en las calificaciones. Pudiendo ser un modelo de Machine Learning que ayude a mejorar el proceso de apredizaje. 
Para lograr esto, se propone grabar las interacciones en el aula y extraer datos relevantes sobre las emociones expresadas por los estudiantes.

### Objetivos 🤖
* Grabar sesiones de clase para capturar la interacción y las expresiones emocionales de los estudiantes.
* Analizar los datos recopilados para identificar patrones de emociones dentro del aula.
* Utilizar técnicas de análisis de datos para comprender cómo las emociones afectan el rendimiento y la participación de los estudiantes.
* Proponer recomendaciones o intervenciones basadas en los hallazgos para mejorar el ambiente emocional y el aprendizaje en el aula.

### Estructura del proyecto 🤖
* data: Contiene los datos utilizados en el proyecto.
    * imagenes: Imágenes utilizadas para el reconocimiento de emociones.
    * pruebas: Contiene videos de las clases grabadas y los resultados del análisis. 
        * reconocidos: Imágenes reconocidas por el modelo.
        * emociones: Imágenes clasificadas por emociones.
    * resultados: Resultados del análisis de datos.
* modelos: Contiene los modelos entrenados utilizados en el proyecto.
* src: Contiene los archivos fuente del proyecto.
    * Archivos .py para la captura de imágenes, entrenamiento del modelo y pruebas.

### Instalacion y uso 🤖
1. Clona este repositorio en tu maquina local
```
git clone https://github.com/tu-usuario/s14-26-ft-data-bi.git
```
2. Crea tu entorno virtual
```
python3 -m venv env
```
3. Activa el entorno virtual
    * En wimdows
    ```
    venv\Scripts\activate
    ```
    * En macOS y Linux
    ```
    source venv/bin/activate
    ```
4. Instala las dependencias del proyecto
```
pip install -r requirements.txt
```
5. Crea la carpeta pruebas en el directorio data, en esta carpeta subiras todos los videos
```
mkdir pruebas
```
6. Dentro de la carpeta pruebas crearas la carpeta emociones y reconocidos que seran donde se guardaran las imagenes que se necesitan para entrenar el modelo a partir de los videos
```
mkdir emociones
```
```
mkdir reconocidos
```

### Proceso de Creación 🤖
Se utilizaron diferentes videos y datos para entrenar al modelo, comenzando por un dataset de Kaggle con imagenes de emociones que puedes encontrarlo en el siguiente enlace [Link](https://www.kaggle.com/datasets/debanga/facial-expression-recognition-challenge) <br>
Una vez creado el modelo con la librería Open CV, se utilizó el framework Flet para la creación de una interfaz amigable y fácil de utilizar por el usuario en una escuela por ejemplo; tratando los archivos como locales a fin de lograr mantener privacidad en los datos. Aqui una demostración de su funcionamiento.

<div align = "center">
  
[![Alt text](https://img.youtube.com/vi/zhYxQvsIOms/0.jpg)](https://www.youtube.com/watch?v=zhYxQvsIOms)
 
<br>
</div>

Para el análisis de los datos de emociones recolectados por el Modelo, hemos utilizado el servicio en la nube de Azure, con variadas herramientas. Si bien, en una aplicación real debería poder utilizarse sólo Azure Storage y Azure Synapse Analytics. Hemos aprovechado la instancia de proyecto para probar herramientas como Azure Data Factory, Databricks, Apache Spark con lenguaje Pyspark para alhunas consultas y transformaciónes en los datos a finde llegar a Azure Synapse para su conexión e ingesta de datos a travès de Power Bi
<div align = "center">
  
<img src='data/proceso_deploy/ELAS Projects Diagrama.jpeg'>
</div>

En la carpeta data/proceso_deploy pueden verse imágenes de cada paso en el proceso y de las consultas realizadas para la transformación e ingesta de datos, aquí el [Enlace](data/proceso_deploy) <br>


<div align="center">
  <img src='data/proceso_deploy/AzureDataFactory.JPG'>
  <br> 
</div>

<div align="center">
  <img src='data/proceso_deploy/Pyspark.JPG'>
  <br> 
</div>

### Contribución 🤖
¡Se agradecen las contribuciones! Si deseas colaborar en el proyecto, por favor sigue estos pasos:

1. Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
2. Realiza tus cambios y haz commit de ellos (git commit -am 'Añade nueva característica').
3. Haz push de tu rama (git push origin feature/nueva-caracteristica).
4. Abre un Pull Request y describe tus cambios detalladamente.


### Contacto 🤖

| Integrantes | Rol | Contacto
|------------|------------|------------|
| [Jimena Fioni](https://github.com/JimeFioni) | ![Data Analyst](https://img.shields.io/badge/Data%20Analyst-black?style=for-the-badge&color=%23fdfd96) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JimeFioni) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jimena-fioni/)
| [Jorge Henriquez Novoa](https://github.com/jorgea-hn) | ![ML Engineer](https://img.shields.io/badge/ML%20Engineer-black?style=for-the-badge&color=%2384b6f4) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jorgea-hn) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jorge-henriquez-novoa/)
| [Hernán Hernández](github.com/hernandroz) | ![Data Engineer](https://img.shields.io/badge/Data%20Engineer-black?style=for-the-badge&color=%2384b6f4) | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](github.com/hernandroz) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](http://linkedin.com/in/hernandroz)



