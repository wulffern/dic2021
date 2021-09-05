footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 4
# MOSFET's

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l4_mosfets.md)

---

# Goal for today
- Symbols
- Current characteristics
- Operating regions
- The square-law model
- Channel length modulation
- The small signal model (low frequency)
- Bulk Effect

---

# Metal-Oxide-Semiconductor (MOS) Transistors 

[.column]

NMOS conduct for positive gate-to-source voltage

![inline](../media/fig_nmos.pdf)

[.column]

PMOS conduct for negative gate-to-source voltage

![inline](../media/fig_pmos.pdf)

---

![inline 100%](../media/3dcross.pdf)

---

# Drain Source Current ($$I_{DS}$$)

### dicex/sim/spice/NCHIO

---
# Large signal model

## $$I_{DS} = f(V_{GS},V_{DS},...)$$

![right fit](../media/large_signal.pdf)

---

#[fit] Gate Source Voltage ($$V_{GS}$$)

---

[.column]


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

[.column]


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

# Gate-source voltage

| Param | Voltage [V]|
| :---:| :---:|
| V<sub>GS</sub> | 0 to 1.8 |
| V<sub>DS</sub> | 1.0 |
| V<sub>S</sub> | 0 |
| V<sub>B</sub> | 0 |

$$i(vcur) = I_{DS} $$

![right fit](../media/vgate.pdf)

---
# Inversion level

Define $$ V_{eff} \equiv V_{GS} - V_{tn} $$, where $$V_{tn}$$ is the "threshold voltage" 

| V<sub>eff</sub>  | Inversion level |
| :---:  | :---: |
| < 0  | weak inversion or subthreshold |
|  0    | moderate inversion |
| > 100 mV | strong inversion| 

![right fit](../media/vgate.pdf)

---

# Weak inversion
 
The drain current is low, but not zero, when $$ V_{eff} << 0$$

$$
I_{DS} \approx I_{D0} \frac{W}{L} e^{V_{eff}/n V_{T}} \text{  if } V_{DS} > 3 V_{T} 
$$

$$
n \approx 1.5
$$

![right fit](../media/vgate.pdf)

---
# Moderate inversion

Stay away from moderate inversion for analog design.

If you can't, then trust the model

![right fit](../media/vgate.pdf)

---

# Strong inversion
 
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

![right fit](../media/vgate.pdf)

---

![inline 130%](../media/accumulated.pdf)

---


![inline 130%](../media/depleted.pdf)

---

![inline 130%](../media/weakinv.pdf)

---

![inline 130%](../media/inversion.pdf)

---

# The threshold voltage ($$ V_{tn} $$) is defined as $$ p_p = n_{ch} $$ 

---

#[fit] Gate Source Capacitance ($$C_{GS}$$)

---
# $$C_{GS} \text{ for }  V_{DS} = 0, V_{S} = 0 $$ 

![right fit](../media/vgatec.pdf)

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

#[fit] Drain Source Voltage ($$V_{DS}$$)

---

# Drain-source voltage

| Param | Voltage [V]|
| :---:| :---:|
| V<sub>GS</sub> | 0.5 |
| V<sub>DS</sub> | 0 to 1.8 |
| V<sub>S</sub> | 0 |
| V<sub>B</sub> | 0 |

$$i(vcur) = I_{DS} $$

![right fit](../media/vdrain.pdf)

---

# Strong inversion
 
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

![right fit](../media/vdrain.pdf)

---

![inline 130%](../media/vds_l_veff.pdf)

---

![inline 130%](../media/vds_veff.pdf)

---

![inline 130%](../media/vds_h_veff.pdf)

---

![original 80%](../media/drain_close.pdf)

---

![original 80%](../media/strong_deriv.pdf)

---

#[fit] Head simulation

---
![left fit](../media/l4_ex1.pdf)

![right fit](../media/vgate.pdf)

---


#[fit] Channel length modulation

---

![original 80%](../media/drain_close.pdf)

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
#[fit] Thanks!
