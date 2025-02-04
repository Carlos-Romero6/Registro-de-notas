def isCualitativa(instance, definitiva):
    for i in instance:
        if i.notas.materia.cualitativa  == 1:
            if 18 <= getattr(i, definitiva) <= 20:
                setattr(i, definitiva, 'A')
            elif 15 <= getattr(i, definitiva) <= 17:
                setattr(i, definitiva, 'B')
            elif 12 <= getattr(i, definitiva) <= 14:
                setattr(i, definitiva, 'C')
            else: 
                setattr(i, definitiva, 'D')