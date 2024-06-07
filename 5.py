import numpy as np
from scipy.stats import multivariate_normal
import time

def logpdf_custom(X, m, C):
    D = len(m)
    norm_coeff = -0.5 * D * np.log(2 * np.pi)
    sign, logdet = np.linalg.slogdet(C) # Вычисление знака определителя и логарифма абсолютного значения определителя матрицы C
    if sign != 1:
        return -np.inf
    C_inv = np.linalg.inv(C) # Вычисление обратной матрицы от матрицы С
    diff = X - m
    exponent = -0.5 * np.sum(diff @ C_inv * diff, axis=1)
    return norm_coeff + 0.5 * logdet + exponent


N, D = 1000, 3
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D) # Генерирует случайные значения
C = np.dot(C, C.T) # Обеспечение положительной определенности

start_time = time.time()
logpdf_custom(X, m, C)
custom_duration = time.time() - start_time

start_time = time.time()
multivariate_normal.logpdf(X, m, C)
scipy_duration = time.time() - start_time

print(f"Скорость работы пользовательской функции: {custom_duration:.6f} секунд")
print(f"Скорость работы функции из scipy: {scipy_duration:.6f} секунд")

custom_result = logpdf_custom(X, m, C)
scipy_result = multivariate_normal.logpdf(X, m, C)

print("Максимальное отклонение результатов:", np.max(np.abs(custom_result - scipy_result)))