---
title: lectures/l4_mosfets
output:
  slidy_presentation:
    footer: "Copyright (c) 2023, Carsten Wulff"
    fig_width: 800
---







## TFE4152 - Lecture 4
## MOSFET's

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l4_mosfets.md)

---

## Goal for today
- Symbols
- Current characteristics
- Operating regions
- The square-law model
- Channel length modulation
- The small signal model (low frequency)
- Bulk Effect

---

## Metal-Oxide-Semiconductor (MOS) Transistors 



NMOS conduct for positive gate-to-source voltage

![](/aic2023/assets/fig_nmos.svg)



PMOS conduct for negative gate-to-source voltage

![](/aic2023/assets/fig_pmos.svg)

---

![](/aic2023/assets/3dcross.svg)

---

## Drain Source Current ($$I_{DS}$$)

### dicex/sim/spice/NCHIO

---
## Large signal model

## $$I_{DS} = f(V_{GS},V_{DS},...)$$

![](/aic2023/assets/large_signal.svg)

---

##  Gate Source Voltage ($$V_{GS}$$)

---




**<sub>dicex/sim/spice/vgate.cir:</sub>**

```

.include ../../../lib/SUN_TRIO_GF130N.spi
.include ../../../models/ptm_130.spi

vdrain  D  0  dc  1
vgate   G  0  dc  0.5

vbulk   B  0  dc  0
vcur    S  0  dc  0

X1 D G S B NCHIO

.dc vgate 0 1.8 0.01

.plot I(vcur)

```




**<sub>dicex/lib/SUN\_TRIO\_GF13N.spi:</sub>**

```
.SUBCKT NCHIO D G S B
M1   D   G   S   B  nmos   w=1.08u    l=0.6u
.ENDS
```

**<sub>dicex/models/ptm_130.spi</sub>**

```
.model  nmos  nmos  level = 21
+version = 4.0          binunit = 1            paramchk= 1            mobmod  = 0
+capmod  = 2            igcmod  = 1            igbmod  = 1            geomod  = 1
+diomod  = 1            rdsmod  = 0            rbodymod= 1            rgatemod= 1
+permod  = 1            acnqsmod= 0            trnqsmod= 0

+tnom    = 27           toxe    = 2.25e-9      toxp    = 1.6e-9       toxm    = 2.25e-9
+dtox    = 0.65e-9      epsrox  = 3.9          wint    = 5e-009       lint    = 10.5e-009
...(about 60 more lines)

```

---

## Gate-source voltage

| Param | Voltage [V]|
| :---:| :---:|
| V<sub>GS</sub> | 0 to 1.8 |
| V<sub>DS</sub> | 1.0 |
| V<sub>S</sub> | 0 |
| V<sub>B</sub> | 0 |

$$i(vcur) = I_{DS} $$

![](/aic2023/assets/vgate.svg)

---
## Inversion level

Define $$ V_{eff} \equiv V_{GS} - V_{tn} $$, where $$V_{tn}$$ is the "threshold voltage" 

| V<sub>eff</sub>  | Inversion level |
| :---:  | :---: |
| < 0  | weak inversion or subthreshold |
|  0    | moderate inversion |
| > 100 mV | strong inversion| 

![](/aic2023/assets/vgate.svg)

---

## Weak inversion
 
The drain current is low, but not zero, when $$ V_{eff} << 0$$

$$
I_{DS} \approx I_{D0} \frac{W}{L} e^{V_{eff}/n V_{T}} \text{  if } V_{DS} > 3 V_{T} 
$$

$$
n \approx 1.5
$$

![](/aic2023/assets/vgate.svg)

---
## Moderate inversion

Stay away from moderate inversion for analog design.

If you can't, then trust the model

![](/aic2023/assets/vgate.svg)

---

## Strong inversion
 
$$
I_{DS} = \mu_n C_{ox} \frac{W}{L} 
\begin{cases}
V_{eff} V_{DS} & \text{if }V_{DS} << V_{eff} \\[15pt]
V_{eff} V_{DS} - V_{DS}^2/2
& \text{if }  V_{DS} < V_{eff}  \\[15pt]
\frac{1}{2} V_{eff}^2
& \text{if }  V_{DS} > V_{eff} \\[15pt]
\end{cases}
$$

![](/aic2023/assets/vgate.svg)

---

![](/aic2023/assets/accumulated.svg)

---


![](/aic2023/assets/depleted.svg)

---

![](/aic2023/assets/weakinv.svg)

---

![](/aic2023/assets/inversion.svg)

---

## The threshold voltage ($$ V_{tn} $$) is defined as $$ p_p = n_{ch} $$ 

---

##  Gate Source Capacitance ($$C_{GS}$$)

---
## $$C_{GS} \text{ for }  V_{DS} = 0, V_{S} = 0 $$ 

![](/aic2023/assets/vgatec.svg)

In strong inversion

$$ 
C_{GS} = W L C_{ox} 
$$

where 

$$
C_{ox} = \frac{K_{ox} \epsilon_0}{t_{ox}}
$$

$$
Q_{ch} = W L C_{ox} V_{eff}
$$

[^1]: $$vgatec = V_{GS} $$

---

##  Drain Source Voltage ($$V_{DS}$$)

---

## Drain-source voltage

| Param | Voltage [V]|
| :---:| :---:|
| V<sub>GS</sub> | 0.5 |
| V<sub>DS</sub> | 0 to 1.8 |
| V<sub>S</sub> | 0 |
| V<sub>B</sub> | 0 |

$$i(vcur) = I_{DS} $$

![](/aic2023/assets/vdrain.svg)

---

## Strong inversion
 
$$
I_{DS} = \mu_n C_{ox} \frac{W}{L} 
\begin{cases}
V_{eff} V_{DS} & \text{if }V_{DS} << V_{eff} \\[15pt]
V_{eff} V_{DS} - V_{DS}^2/2
& \text{if }  V_{DS} < V_{eff}  \\[15pt]
\frac{1}{2} V_{eff}^2
& \text{if }  V_{DS} > V_{eff} \\[15pt]
\end{cases}
$$

![](/aic2023/assets/vdrain.svg)

---

![](/aic2023/assets/vds_l_veff.svg)

---

![](/aic2023/assets/vds_veff.svg)

---

![](/aic2023/assets/vds_h_veff.svg)

---

![](/aic2023/assets/drain_close.svg)

---

![](/aic2023/assets/strong_deriv.svg)

---

##  Head simulation

---
![](/aic2023/assets/l4_ex1.svg)

![](/aic2023/assets/vgate.svg)

---


##  Channel length modulation

---

![](/aic2023/assets/drain_close.svg)

---

$$
I_{DS} = \mu_n C_{ox} \frac{W}{L} 
\begin{cases}
V_{eff} V_{DS} & \text{if }V_{DS} << V_{eff} \\[15pt]
V_{eff} V_{DS} - V_{DS}^2/2
& \text{if }  V_{DS} < V_{eff}  \\[15pt]
\frac{1}{2} V_{eff}^2[1 + \lambda(V_{DS} - V_{eff})]
& \text{if }  V_{DS} > V_{eff} \\[15pt]
\end{cases}
$$

$$ \lambda = \frac{k_{ds}}{2L\sqrt{V_{DS} - V_{eff} + \Phi_0}} $$, where $$ k_{ds} =
\sqrt{\frac{2K_s \epsilon_0}{q N_A}} $$

---
##  Thanks!