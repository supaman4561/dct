#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time

def dct(x, N):
    # X is spectrum
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            re += x[n]*np.cos(-2*np.pi*k*n/N)
            im += x[n]*np.sin(-2*np.pi*k*n/N)
        X[k] = complex(re, im)
    return X

if __name__ == '__main__':
    N = int(input("サンプリング点数:"))
    t = np.arange(0, N)
    waves = []
    spectrums = []
    # wave 1
    waves.append(np.sin(2*np.pi*t*10/N))
    # wave 2
    waves.append(np.sin(2*np.pi*t/N) + np.sin(2*np.pi*t*10/N))
    # wave 3
    waves.append(np.sin(2*np.pi*t/N) + np.sin(2*np.pi*t*10/N) + np.sin(2*np.pi*t*20/N)/5)

    # Discrete Cosine Transform
    start = time.time()
    for w in waves:
        spectrums.append(np.abs(dct(w, N))**2)
    end = time.time()

    print("実行時間 : " + str(end - start) + "[sec]")

    plt.subplot(121)
    plt.title("waves")
    for i,w in enumerate(waves):
        plt.plot(t, w, label="wave"+str(i), linewidth=len(waves)-i)
    plt.legend()

    plt.subplot(122)
    plt.title("spectrums")
    for i,s in enumerate(spectrums):
        plt.plot(t, s, label="spectrum"+str(i), linewidth=len(spectrums)-i)

    plt.legend()
    plt.show()
