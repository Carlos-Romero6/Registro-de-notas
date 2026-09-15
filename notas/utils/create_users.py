from django.contrib.auth.models import User, Group

def crearUsuarios(username, password, staff = None, grupo = None):
    try:
        user = User.objects.create_user(username=username, password=password)
        user.is_staff = staff
        user.save()
        if grupo:
            group, creado = Group.objects.get_or_create(name=grupo)
            if creado:
                user.groups.add(group)
        print(user)
    except Exception as e:
        print(e)


crearUsuarios('Administrador', 'admin', True, 'Administrador')

crearUsuarios('Usuario', 'user', False, 'Usuario')
