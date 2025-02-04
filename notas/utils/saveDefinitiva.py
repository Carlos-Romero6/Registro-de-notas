from .calculoDefinitiva import calcularDefinitiva
def saveDefinitiva(instance):
        print("saveOK")
        instance.definitiva = calcularDefinitiva(instance)
        