<div align="center">

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Arial&size=30&duration=3000&pause=8000&color=F7F7F7&width=435&lines=Sistema+de+Gesti%C3%B3n+de+Notas)](https://git.io/typing-svg)


### Programa para gestionar notas, matrículas y estudiantes de un liceo.


![Django](https://img.shields.io/badge/Django-5.1.6-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)


</div>

---

## 🧭 Navegación

- [Stack Tecnológico](#️-stack-tecnológico)
- [Instalación y Puesta en Marcha](#-instalación-y-puesta-en-marcha)
- [Licencia](#-licencia)

## 🛠️ Stack Tecnológico

### Backend
* **Lenguaje:** Python 3.11+.
* **Framework:** Django 5.1.x (ORM integrado, panel de administración y sistema de plantillas).
* **Base de Datos:** SQLite.
* **Plantillas:** Django Template Language junto a Bootstrap 5.3.
* **Exportación:** xlwt (genera los reportes en formato `.xls`).
* **Servidor de producción:** Waitress (servidor WSGI estable en Windows).

## 🚀 Instalación y Puesta en Marcha

El proyecto se ejecuta de forma local y utiliza una base de datos SQLite que no requiere configuración externa.

### Requisitos Previos
* **Intérprete de Python 3.11+.** Se verifica con el siguiente comando:

```bash
python --version
```
* **Git**.
* **Librerías utilizadas:** Django y xlwt. Se instalan con los siguientes comandos:

```bash
pip install django
pip install xlwt
```

### Puesta en Marcha

**Paso 1 - Clonar el repositorio:**

```bash
git clone git@github.com:Carlos-Romero6/Registro-de-notas.git
```

**Paso 2 - Ingresar en la carpeta del proyecto:**

```bash
cd Registro-de-notas
```

**Paso 3 - Crear y activar el entorno virtual:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**Paso 4 - Instalar las dependencias:**

```bash
pip install -r requirements.txt
```

**Paso 5 - Aplicar las migraciones:**

```bash
python manage.py migrate
```

**Paso 6 - Crear un superusuario (opcional, para ingresar al panel de administración):**

```bash
python manage.py createsuperuser
```

**Paso 7 - Iniciar el servidor de desarrollo:**

```bash
python manage.py runserver
```

**Paso 8 - Acceder a la aplicación:**
* Aplicación: http://localhost:8000
* Panel de administración: http://localhost:8000/admin

## 📄 Licencia

Todos los derechos reservados.
