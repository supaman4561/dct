# Discrete Cosine Transform

## 原理

### フーリエ変換

時間と周波数領域の相互変換。  
時間領域で見てよくわからない信号でも、周波数領域で見ると性質がわかる場合がある。

**フーリエ変換**

<div style="text-align:center">
<img src="https://latex.codecogs.com/gif.latex?X(\omega) = \int_{-\infty}^{+\infty} x(t)e^{-i \omega t}dt" />
</div>

**フーリエ逆変換**

<div style="text-align:center">
<img src="https://latex.codecogs.com/gif.latex?x(t) = \int_{-\infty}^{+\infty} X(\omega)e^{+i \omega t}d\omega
" />
</div>

###　離散フーリエ変換

フーリエ変換を離散化して、デジタルなフーリエ変換を行う方法。

* DCT(Discrete Cosine Transform)
* FFT(Fast Fourier Transform) **DCTの高速版！**

**離散フーリエ変換**

k : 周波数  
n : 離散的な時間  
とする。

<div style="text-align:center">
<img src="https://latex.codecogs.com/gif.latex?X_{k}=\sum_{n=0}^{N-1}x_{n}e^{\frac{-2\pi ikn}{N}}" />
</div>
<br>
<div style="text-align:center">
<img src="https://latex.codecogs.com/gif.latex?x_{n}=\frac{1}{N}\sum_{k=0}^{N-1}X_{k}e^{\frac{+2\pi ikn}{N}}" />
</div>
