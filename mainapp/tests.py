from django.test import TestCase
from decimal import Decimal, ROUND_HALF_UP
# Create your tests here.

n_momentos = 3
definitiva = Decimal((18 + 19 + 20) / n_momentos).quantize(0, ROUND_HALF_UP)
print(definitiva)