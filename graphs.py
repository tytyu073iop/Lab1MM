import numpy as np
import matplotlib.pyplot as plt

def plot_method_analysis(arr, method_name):
    fig, axes = plt.subplots(2, 2, figsize=(18, 5))

    # CDF plot
    axes[0][0].plot(np.sort(arr), np.linspace(0, 1, len(arr)), label='Эмпирическая Ф.Р.')
    axes[0][0].plot(np.sort(arr), np.sort(arr), label='Теоретическая Ф.Р. (равномерное)', linestyle='--')
    axes[0][0].set_title(f'Функция распределения для метода {method_name}')
    axes[0][0].set_xlabel('Значение случайной величины')
    axes[0][0].set_ylabel('Вероятность')
    axes[0][0].legend()

    # Scatter plot
    axes[0][1].scatter(arr[:-1], arr[1:], alpha=0.5)
    axes[0][1].set_title(f'Диаграмма рассеяния для метода {method_name}')
    axes[0][1].set_xlabel('Значение x_i')
    axes[0][1].set_ylabel('Значение x_{i+1}')

    # Histogram plot
    obs_freq, bin_edges, _ = axes[1][0].hist(arr, bins=10, density=False, alpha=0.6, color='b', edgecolor='black', label='Наблюдаемая частота')
    exp_freq = len(arr) / 10
    axes[1][0].axhline(y=exp_freq, color='r', linestyle='--', label='Ожидаемая частота (50.0)')
    axes[1][0].set_title(f'Гистограмма частот для метода {method_name}')
    axes[1][0].set_xlabel('Интервалы')
    axes[1][0].set_ylabel('Количество попаданий (частота)')
    axes[1][0].legend()

    plt.tight_layout()
    plt.show()