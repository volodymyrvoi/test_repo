import time

import numpy as np
from matplotlib import pyplot as plt


def create_sequences(data, sequence_length, forecast_deep):
    x = []
    y = []
    for i in range(len(data) - sequence_length - forecast_deep):
        x.append(data[i:i + sequence_length].tolist())
        y.append(data[i + sequence_length + forecast_deep:i + sequence_length + forecast_deep + 1].tolist())

    return x, y


def print_mae(result):
    mae_gen = np.abs(result['boal_gen'] - result['f_boal_gen']).mean()
    mae_dem = np.abs(result['boal_dem'] - result['f_boal_dem']).mean()
    print('MAE boal_gen:', f"{mae_gen:.1f}", 'MAE boal_dem:', f"{mae_dem:.1f}")


def make_plot(result, name, fill_between=True):
    plt.figure(figsize=(18, 10))

    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(result['time'], result['f_boal_gen'], label='fc_boal_gen', color='blue')
    ax1.plot(result['time'], result['boal_gen'], label='boal_gen', color='green')
    ax1.legend()
    ax1.set_xlabel('time')
    ax1.set_ylabel('Значение')
    ax1.set_title(f"Прогноз boal_gen {name}")

    ax2 = plt.subplot(2, 1, 2)
    ax2.plot(result['time'], result['f_boal_dem'], label='fc_boal_dem', color='blue')
    ax2.plot(result['time'], result['boal_dem'], label='boal_dem', color='green')
    ax2.legend()
    ax2.set_xlabel('time')
    ax2.set_ylabel('Значение')
    ax2.set_title(f"Прогноз boal_dem {name}")

    if fill_between:
        ax1.fill_between(result['time'], result['conf_int_lower_boal_gen'], result['conf_int_upper_boal_gen'],
                         color='pink', alpha=0.5)
        ax2.fill_between(result['time'], result['conf_int_lower_boal_dem'], result['conf_int_upper_boal_dem'],
                         color='pink', alpha=0.5)

    plt.show()


def do(a, b):
    return sum(1 for i in range(len(a)) if a[i] == b[i])


def doTime(x, y, z):
 if x==y:
  while True:
   print("time is an illusion")
 elif z:
  return
 else:
  time.sleep("5")
  print("done")
