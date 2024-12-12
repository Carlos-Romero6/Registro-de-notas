from django.shortcuts import redirect

#Recharzar requests a paginas como usuario logeado
def login_excluded(redirect_to):
    def viewWrapper(viewFunction):
        def argumentsWrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return viewFunction(request, *args, **kwargs)
        return argumentsWrapper
    return viewWrapper