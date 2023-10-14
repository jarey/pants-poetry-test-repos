from project_models.models import Greeting
import numpy as np


def test_model():
    Greeting(greet='hi', name='Marcelo')
    a = np.arange(15).reshape(3, 5)
