import os
import django

# 1. Configurar el entorno de Django para ejecutar scripts independientes
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User

def create_initial_users():
    # Variables para el usuario con Staff / Administrador
    staff_name = os.getenv('STAFF_NAME', 'AdminStaff')
    staff_email = os.getenv('STAFF_EMAIL', 'staff@example.com')
    staff_pass = os.getenv('STAFF_PASSWORD', 'staff123')

    # Variables para el usuario Normal (sin Staff)
    user_name = os.getenv('USER_NAME', 'UsuarioNormal')
    user_email = os.getenv('USER_EMAIL', 'user@example.com')
    user_pass = os.getenv('USER_PASSWORD', 'user123')

    # 1. Crear el usuario con Staff (is_staff=True / Superusuario)
    if not User.objects.filter(username=staff_name).exists():
        print(f"Creando usuario Staff/Admin: {staff_name}...")
        User.objects.create_superuser(
            username=staff_name,
            email=staff_email,
            password=staff_pass
        )
        print("Usuario Staff creado exitosamente.")
    else:
        print(f"El usuario Staff '{staff_name}' ya existe.")

    # 2. Crear el usuario Normal (is_staff=False)
    if not User.objects.filter(username=user_name).exists():
        print(f"Creando usuario normal (is_staff=False): {user_name}...")
        User.objects.create_user(
            username=user_name,
            email=user_email,
            password=user_pass,
            is_staff=False,
            is_superuser=False
        )
        print("Usuario normal creado exitosamente.")
    else:
        print(f"El usuario normal '{user_name}' ya existe.")

if __name__ == '__main__':
    create_initial_users()