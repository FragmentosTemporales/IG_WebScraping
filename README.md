# Instagram WebScraping

## 1. Descarga

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/IG_WebScraping.git
```

## 2. Instalación

### Variables de entorno

Al interior de la carpeta debes crear un documento .env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```
NAVEGADOR =

USER_IG=
PW_IG=
```

### Instalación

Para instalar la aplicación debes ejecutar el siguiente código, es necesario que las variables de entorno estén definidas para este punto:

```
$ pip install virtualenv
```

Posteriormente debes crear el entorno:

```
$ python -m venv venv
```

Una vez creado el entorno de trabajo, puedes instalar las librerías requeridas:

```
$ pip install -r requirements.txt
```

## 3. Ejecución

Para ejecutar la aplicación debes ejecutar el archivo main.py:

```
$ python app/main.py
```

Saludos!