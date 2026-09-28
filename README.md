# Reto Gemini API

## Objetivo

Configurar y utilizar la API de Gemini desde Python para realizar tareas de análisis de texto e imagen.
        
## Instalación

### Comprobar Python

```bash
py --version
```

### Instalar dependencias

```bash
py -m pip install google-genai
py -m pip install pillow
```

## Proceso realizado

1. Instalación de Python.
2. Instalación de la librería google-genai.
3. Creación de una API Key de Gemini.
4. Configuración del entorno en Visual Studio Code.
5. Desarrollo de scripts de prueba.
6. Conexión correcta con Gemini.
7. Análisis de sentimientos.
8. Descripción automática de imágenes.

## Archivos

### gemini_texto.py

Comprueba la conexión con Gemini.

Resultado:

```text
Conexión correcta.
```

### sentimientos.py

Analiza distintos textos y clasifica el sentimiento como:

- Positivo
- Negativo
- Neutro

### gemini_imagen.py

Envía una imagen a Gemini y obtiene una descripción automática.

## Ejemplos de resultados

### Análisis de sentimientos

Texto:

```text
Me encanta esta película.
```

Resultado:

```text
Positivo
```

Texto:

```text
Ha sido una experiencia horrible.
```

Resultado:

```text
Negativo
```

Texto:

```text
La película dura dos horas.
```

Resultado:

```text
Neutro
```

### Análisis de imagen

Gemini describió correctamente la imagen proporcionada identificando:

- Un paisaje natural.
- Montañas al fondo.
- Un lago con reflejos.
- Vegetación en primer plano.

## Conclusión

Se ha conseguido configurar correctamente la API de Gemini, realizar llamadas desde Python, analizar texto mediante IA y describir imágenes utilizando modelos multimodales.