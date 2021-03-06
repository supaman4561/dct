# Discrete Cosine Transform

## 原理

### フーリエ変換

時間と周波数領域の相互変換。  
時間領域で見てよくわからない信号でも、周波数領域で見ると性質がわかる場合がある。

**フーリエ変換**
$$
X(\omega) = \int_{-\infty}^{+\infty} x(t)e^{-i \omega t}dt
$$

**フーリエ逆変換**　
$$
x(t) = \int_{-\infty}^{+\infty} X(\omega)e^{+i \omega t}d\omega
$$

### 離散フーリエ変換

フーリエ変換を離散化して、デジタルなフーリエ変換を行う方法。

* DCT(Discrete Cosine Transform)
* FFT(Fast Fourier Transform) **DCTの高速版！**

**離散フーリエ変換**

$k$ : 周波数    
$N$ : サンプリング点数
$$
X_{k}=\sum_{n=0}^{N-1}x_{n}e^{\frac{-2\pi ikn}{N}}
$$
$$
x_{n}=\frac{1}{N}\sum_{k=0}^{N-1}X_{k}e^{\frac{+2\pi ikn}{N}}
$$

## 演習 ~DCT~

* DCTを実装し、結果をグラフ表示
* DCTへ以下の波形を与え、それぞれのスペクトルを確認
  1. $\sin(\frac{2\pi t}{N} \cdot 10)$
  2. $\sin(\frac{2\pi t}{N})+\sin(\frac{2\pi t}{N} \cdot 10)$
  3. $\sin(\frac{2\pi t}{N})+\sin(\frac{2\pi t}{N} \cdot 10)+\frac{1}{5} \sin(\frac{2\pi t}{N} \cdot 20)$
* N=128, N=1024, N=2048についてそれぞれ試す
* 計算時間をチェックする

## 演習 ~FFT~

* FFTへ以下の波形を与え、それぞれのスペクトルを確認
  1. $\sin(\frac{2\pi t}{N} \cdot 10)$
  2. $\sin(\frac{2\pi t}{N})+\sin(\frac{2\pi t}{N} \cdot 10)$
  3. $\sin(\frac{2\pi t}{N})+\sin(\frac{2\pi t}{N} \cdot 10)+\frac{1}{5} \sin(\frac{2\pi t}{N} \cdot 20)$
* N=128, N=1024, N=2048についてそれぞれ試す
* DCTとの計算時間の違いを測定(N=2048)
