footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 19
# All radios started with [Euler](https://en.wikipedia.org/wiki/Leonhard_Euler)

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l19_radios.md)

---

$$ e^{ix} = cos(x)  + i sin(x)$$

$$ e^{-ix} = cos(-x) - i sin(-x) = cos(x) - i sin(x) $$

![right fit](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Sine_cosine_plot.svg/800px-Sine_cosine_plot.svg.png)

---

[.column]

$$ e^{ix} = cos(x)  + i sin(x)$$

$$ e^{-ix} = cos(-x) - i sin(-x) = cos(x) - i sin(x) $$


[.column]
$$ cos(x) = e^{ix} - i sin(x)$$

$$ -i sin(x) = e^{-ix} - cos(x)$$

$$ cos(x) = e^{ix} + e^{-ix} - cos(x)$$

$$  cos(x) = \frac{e^{ix} + e^{-ix}}{2}$$

---

$$ cos(x) \times cos(y) = \frac{e^{ix} + e^{-ix}}{2} \times \frac{e^{iy}
+e^{-iy}}{2} $$

$$ \rightarrow \frac{1}{4}\left[ e^{ix}e^{iy} + e^{-ix}e^{iy} + e^{ix}e^{-iy} + e^{-ix}e^{-iy}\right]$$

$$ \rightarrow \frac{1}{4}\left[e^{i(x+y)} + e^{-i(x-y)} + e^{i(x-y)} + e^{-i (x + y)}\right]$$

$$ \rightarrow \frac{1}{2}\left[\frac{e^{i(x+y)}+ e^{-i (x +y)}}{2} + \frac{e^{i(x-y)} + e^{-i (x-y)}}{2}\right]$$

$$\Rightarrow cos(x) \times cos(y) =\frac{1}{2}\left[cos(x+y) + cos(x-y)\right]$$ 

---

![inline original](https://upload.wikimedia.org/wikipedia/commons/9/92/Phase_shifter_using_IQ_modulator.gif)

---

An ideal square wave is an infinite sum of odd harmonics

$$ x(t) = \frac{4}{\pi}\sum_{k=1}^{\infty}\frac{sin(2\pi(2k - 1)ft)}{2k-1} $$

![right fit](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Fourier_series_for_square_wave.gif/350px-Fourier_series_for_square_wave.gif)

---

[Complex Signal Processing is Not
Complex](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1333231) 

![inline fit](../media/l19/complex.png)




---
#[fit] Thanks!




