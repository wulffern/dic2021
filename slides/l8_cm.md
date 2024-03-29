---
title: lectures/l8_cm
output:
  slidy_presentation:
    footer: "Copyright (c) 2023, Carsten Wulff"
    fig_width: 800
---







## TFE4152 - Lecture 8
## Outside world, variability, and current mirrors

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l8_cm.md)

---

| Week | Book                    | Monday                                                                    | Book                    | Friday                               |
|------|-------------------------|---------------------------------------------------------------------------|-------------------------|--------------------------------------|
| 34   |                         | Introduction, what are we going to do in this course. Why do you need it? | WH 1 , WH 15            | Manufacturing of integrated circuits |
| 35   | CJM 1.1                 | pn Junctions                                                              | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                   |
| 36   | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                                                        | CJM 1.3 - 1.6           | Modeling and passive devices         |
| 37   |                         | Guest Lecture - Sony                                                      | CJM 3.1, 3.5, 3.6       | **Current mirrors**                      |
| 38   | CJM 3.2, 3.3,3.4 3.7    | Amplifiers                                                                | CJM, CJM 2 WH 1.5       | SPICE simulation  and layout         |
| 39   |                         | Verilog                                                                   |                         | Verilog                              |
| 40   | WH 1.4 WH 2.5           | CMOS Logic                                                                | WH 3                    | Speed                                |
| 41   | WH 4                    | Power                                                                     | WH 5                    | Wires                                |
| 42   | WH 6                    | Scaling Reliability and Variability                                       | WH 8                    | Gates                                |
| 43   | WH 9                    | Sequencing                                                                | WH 10                   | Datapaths - Adders                   |
| 44   | WH 10                   | Datapaths - Multipliers, Counters                                         | WH 11                   | Memories                             |
| 45   | WH 12                   | Packaging                                                                 | WH 14                   | Test                                 |
| 46   |                         | Guest lecture - Nordic Semiconductor                                      |                         |                                      |
| 47   | CJM                     | Recap of CJM                                                              | WH                      | Recap of WH                          |

---
## Goal for today

Outside world (ESD, Latchup)

Variability

Current mirrors

---
##  Outside world
---

## Electrostatic Discharge 

If you make an IC, you must consider Electrostatic Discharge (ESD) Protection circuits

![](https://media.wiley.com/product_data/coverImage300/18/04714987/0471498718.jpg)
Standards for testing at [JEDEC](https://www.jedec.org/category/technology-focus-area/esd-electrostatic-discharge-0)

## But I just want a digital input, what do I need?

---

![](/aic2023/assets/esd.svg)

---

##  Input buffer

![](/aic2023/assets/fig_methodology.svg)

---
##  Latch-up

Logic cells close to large NMOS pad drivers are prone to latch-up.

The latch-up process can start with electrons injected into the p-type substrate.

![](/aic2023/assets/fig_inv.svg)

---
## Latch-up

1. Electrons injected into substrate, diffuse around, but will be accelerated by n-well to p-substrate built in voltage. Can end up in n-well
2. PMOS drain can be forward biased by reduced n-well potential. Hole injection into n-well. Holes diffuse around, but will be accelerated by n-well to p-substrate built in voltage. Can end up in p-substrate under NMOS
3. NMOS source pn-junction can be forward biased. Electrons injected into p-substrate. Diffuse around, but will be accelerated by n-well to p-substrate built in voltage.
4. Go to 2 (latch-up)
   
![](/aic2023/assets/scr_eh.svg)

---

![](/aic2023/assets/scr_model.svg)

---

##  Variability

---

##  Provide $$I_2 = 1 \mu A $$ 

Let's use off-chip resistor $$R$$, and pick $$R$$ such that $$I_1 = 1 \mu A $$

Use $$ \frac{W_1}{L_1} = \frac{W_2}{L_2} $$ 

**What makes $$ I_2 \ne 1 \mu A $$?**

![](/aic2023/assets/fig_l8_cmsys.svg)

---

## Voltage variation

## Systematic variations

## Process variations

## Temperature variation

## Random variations

## (Noise)


![](/aic2023/assets/fig_l8_cmsys.svg)

---
##  Voltage variation

 $$I_1 = \frac{V_{DD} - V_{GS1}}{R}$$


If $$V_{DD}$$ changes, then current changes.

**Fix**: Keep $$V_{DD}$$ constant


![](/aic2023/assets/fig_l8_cmsys.svg)

---


## Systematic variations

If $$ V_{DS1} \ne V_{DS2} \rightarrow I_1 \ne I_2 $$

If layout direction of $$ M_1 \ne M_2 \rightarrow I_1 \ne I_2 $$ 

If current direction of $$ M_1 \ne M_2 \rightarrow I_1 \ne I_2 $$

If $$ V_{S1} \ne V_{S2} \rightarrow I_1 \ne I_2 $$

If $$ V_{B1} \ne V_{B2} \rightarrow I_1 \ne I_2 $$

If $$ WPE_{1} \ne WPE_{2} \rightarrow I_1 \ne I_2 $$

If $$ Stress_{1} \ne Stress_{2} \rightarrow I_1 \ne I_2 $$
...

![](/aic2023/assets/fig_l8_cmsys.svg)

---
## Process variations

Assume strong inversion and active **$$ V_{eff} = \sqrt{\frac{2}{\mu_p C_{ox} \frac{W}{L}} I_1} $$**, $$V_{GS} = V_{eff} + V_{tp}$$

 $$ I_1 = \frac{V_{DD} - V_{GS}}{R} =  \frac{V_{DD} - \sqrt{\frac{2}{\mu_p C_{ox} \frac{W}{L}} I_1}  - V_{tp}}{R} $$ 

 $$\mu_p$$, $$C_{ox}$$, $$V_{tp}$$ will all vary from die to die, and wafer lot to wafer lot.

![](/aic2023/assets/fig_l8_cmsys.svg)

---
## Process corners

Common to use 5 corners, or [Monte-Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) process simulation

| Corner | NMOS | PMOS |
| :---: | :---: | :---: | 
| Mtt | Typical | Typical|
| Mss | Slow | Slow|
| Mff | Fast | Fast |
| Msf | Slowish | Fastish |
| Mfs | Fastish | Slowish |


![](/aic2023/assets/fig_l8_cmsys.svg)

---
## Fix process variation

Use calibration: measure error, tune circuit to fix error

For every single chip, measure voltage across known resistor $$R_1$$ and tune $$R_{var}$$ such that we get $$I_1 = 1 \mu A$$

Be careful with multimeters, they have finite input resistance (approximately 1 M$$\Omega$$)

![](/aic2023/assets/fig_l8_cmfixproc.svg)

---

## Temperature variation

Mobility decreases with temperature

Threshold voltage decreases with temperature.

$$ I_D = \frac{1}{2}\mu_n C_{ox} (V_{GS} - V_{tn})^2$$

High $$I_D = $$ fast digital circuits

Low $$I_D = $$ slow digital circuits 

**What is fast? High temperature or low temperature?**

![](/aic2023/assets/fig_l8_cmfixproc.svg)

---
## It depends on $$V_{DD}$$

**Fast corner**
- Mff (high mobility, low threshold voltage) 
- High $$V_{DD}$$ 
- High or low temperature


**Slow corner**
- Mss (low mobility, high threshold voltage)
- Low $$V_{DD}$$ 
- High or low temperature

![](/aic2023/assets/fig_l8_cmfixproc.svg)

---
## How do we fix temperature variation?

Accept it, or don't use this circuit.

If you need stability over temperature, use 7.3.2 and 7.3.4 in CJM
 
![](/aic2023/assets/fig_l8_cmfixproc.svg)

---

##  Random Variation

---





[Mean](https://en.wikipedia.org/wiki/Mean)
$$ \overline{x(t)} = \lim_{T\to\infty} \frac{1}{T}\int^{+T/2}_{-T/2}{ x(t) dt} $$

Mean Square
$$ \overline{x^2(t)} = \lim_{T\to\infty} \frac{1}{T}\int^{+T/2}_{-T/2}{ x^2(t) dt} $$

[Variance](https://en.wikipedia.org/wiki/Variance)
$$ \sigma^2 = \overline{x^2(t)} - \overline{x(t)}^2$$

where $$\sigma$$ is the standard deviation.
If mean is removed, or is zero, then
$$ \sigma^2 = \overline{x^2(t)} $$


Assume two random processes, $$x_1(t)$$ and $$x_2(t)$$ with mean of zero (or removed).
 $$ x_{tot}(t) =  x_1(t) + x_2(t)$$
 $$ x_{tot}^2(t) = x_1^2(t) + x_2^2(t) + 2x_1(t)x_2(t)$$

Variance (assuming mean of zero) 
$$ \sigma^2_{tot} = \lim_{T\to\infty} \frac{1}{T}\int^{+T/2}_{-T/2}{ x_{tot}^2(t) dt} $$
$$ \sigma^2_{tot} = \sigma_1^2 + \sigma_2^2 + \lim_{T\to\infty} \frac{1}{T}\int^{+T/2}_{-T/2}{ 2x_1(t)x_2(t) dt} $$

**Assuming uncorrelated processes (covariance is zero), then
$$ \sigma^2_{tot} = \sigma_1^2 + \sigma_2^2  $$**

---

 $$\ell =  \mu_p C_{ox} \frac{W}{L}$$
 $$ I_D = \frac{1}{2} \ell (V_{GS} - V_{tp})^2$$
 
 Due to doping , length, width, $$C_{ox}$$, $$V_{tp}$$, ... random varation
 
 $$\ell_1 \ne \ell_2$$
 
 $$V_{tp1} \ne V_{tp2} $$

As a result $$ I_1 \ne I_2 $$, but we can make them close.

---
## Pelgrom's[^1] law

Given a random gaussian process parameter $$\Delta P$$ with zero mean, the variance is given by 

$$\sigma^2 (\Delta P) = \frac{A^2_P}{WL} + S_{P}^2 D^2$$

where $$A_P$$ and $$S_P$$ are measured, and $$D$$ is the distance between devices

Assume closely spaced devices ($$ D \approx 0$$) $$ \Rightarrow \sigma^2 (\Delta P) = \frac{A^2_P}{WL} $$


[^1]: M. J. M. Pelgrom, C. J. Duinmaijer, and A. P. G. Welbers, “Matching properties of MOS transistors,” IEEE J. Solid-State Cir- cuits, vol. 24, no. 5, pp. 1433–1440, Oct. 1989.
 
---

## Transistors with same $$V_{GS}$$[^2]

$$\frac{\sigma_{I_D}^2}{I_D^2} = \frac{1}{WL}\left[\left(\frac{gm}{I_D}\right)^2 \sigma_{vt}^2 + \frac{\sigma_{\ell}^2}{\ell}\right] $$

Valid in  weak, moderate and strong inversion


[^2]: Peter Kinget, see CJM

---


$$\frac{\sigma_{I_D}^2}{I_D^2} = \frac{1}{WL}\left[\left(\frac{gm}{I_D}\right)^2 \sigma_{vt}^2 + \frac{\sigma_{\ell}^2}{\ell}\right] $$
$$\frac{\sigma_{I_D}}{I_D} \propto \frac{1}{\sqrt{WL}}$$

Assume $$\frac{\sigma_{I_D}}{I_D} = 10\%$$, We want $$5\%$$, how much do we need to change WL?


$$\frac{\frac{\sigma_{I_D}}{I_D}}{2} \propto \frac{1}{2\sqrt{WL}} =  \frac{1}{\sqrt{4WL}}$$


**We must quadruple the area to half the standard deviation**

$$1 \%$$ would require **100** times the area


![](/aic2023/assets/fig_l8_cmfixproc.svg)

---

## What else can we do?

$$\frac{\sigma_{I_D}^2}{I_D^2} = \frac{1}{WL}\left[\left(\frac{gm}{I_D}\right)^2 \sigma_{vt}^2 + \frac{\sigma_{\ell}^2}{\ell}\right] $$

Strong inversion $$\Rightarrow \frac{gm}{I_D} = \frac{1}{2 V_{eff}} = low$$

Weak inversion $$\Rightarrow \frac{gm}{I_D} = \frac{q}{n k T} \approx 25$$

**Current mirrors achieve best matching in strong inversion**

![](/aic2023/assets/fig_l8_cmfixproc.svg)

---

$$\frac{\sigma_{I_D}^2}{I_D^2} = \frac{1}{WL}\left[\left(\frac{gm}{I_D}\right)^2 \sigma_{vt}^2 + \frac{\sigma_{\ell}^2}{\ell}\right] $$

$$\sigma_{I_D}^2 = \frac{1}{WL}\left[gm^2 \sigma_{vt}^2 + I_D^2\frac{\sigma_{\ell}^2}{\ell}\right] $$

Offset voltage for a differential pair

$$ i_o = i_{o+} - i_{o-} =  g_m v_i = g_m (v_{i+} - v_{i-})$$

$$ \sigma_{v_i}^2 = \frac{\sigma_{I_D}^2}{gm^2} = \frac{1}{WL}\left[\sigma_{vt}^2 + \frac{I_D^2}{gm^2}\frac{\sigma_{\ell}^2}{\ell}\right]  $$

High $$\frac{gm}{I_D}$$ is better (best in weak inversion)

![](/aic2023/assets/fig_diff.svg)

---
## (Transistor Noise) <sub><sub>more in future years </sub></sub>

**Thermal noise**
Random scattering of carriers, generation-recombination in channel? 
$$ PSD_{TH}(f) = \text{Constant}$$


**Popcorn noise**
Carriers get "stuck" in oxide traps (dangling bonds) for a while. Can cause a short-lived (seconds to minutes) shift in threshold voltage
$$ PSD_{GR}(f) \propto \text{Lorentzian shape} \approx \frac{A}{1 + \frac{f^2}{f_0}}$$

**Flicker noise**
Assume there are many sources of popcorn noise at different energy levels and time constants, then the sum of the spectral densities approaches flicker noise.
$$ PSD_{flicker}(f) \propto \frac{1}{f} $$

![](https://upload.wikimedia.org/wikipedia/en/2/2a/Popcorn_noise_graph.png)
---


##  Analog designer = Someone who knows how to deal with variation

---

##  Current Mirrors

---

![](/aic2023/assets/fig_current_mirrors.svg)

---
## Input impedance $$r_{in}$$
## Output impedance $$r_{out}$$
## LF transfer function $$\frac{i_{o}}{i_{i}}$$
## Source degeneration
## Cascode

![](/aic2023/assets/fig_cm.svg)

---
 $$r_{in}$$

![](/aic2023/assets/cm_in.svg)

---
 $$r_{out}$$


![](/aic2023/assets/cm_out.svg)

---
 $$\frac{i_{o}}{i_{i}}$$


![](/aic2023/assets/cm_tf.svg)

---
## Source degeneration

![](/aic2023/assets/fig_cmsf.svg)

What is the operating region of M3 and M4?

What is the operating region of M1 and M2?

---

## Source degeneration - $$ r_{in}$$

M1 and M2 are in linear region, can be simplified to resistors

 $$r_{in} = \frac{1}{g_{m1}}+ R_s$$

![](/aic2023/assets/fig_cmRdeg.svg)

---
## Source degeneration - $$ r_{out} $$


![](/aic2023/assets/cm_sdeg.svg)

$$v_{gs} = -v_{s}$$, $$v_{s} = i_x R_s$$, $$r_{out} = \frac{v_x}{i_x}$$

$$i_x = g_{m2} v_{gs} + \frac{v_x - v_s}{r_{ds2}}$$

$$i_x = -i_x g_{m2} R_s + \frac{v_x - i_x R_s}{r_{ds2}}$$

$$v_x = i_x\left[ r_{ds2} + R_s(g_{m2} r_{ds2} + 1)\right]$$ 

Rearranging

$$ r_{out} =  r_{ds2}[1 + R_s(g_{m1} + g_{ds2})] \approx r_{ds2} [1 + g_{m1}R_s]$$ 


---

## Cascode

From source degeneration (ignoring bulk effect)

$$r_{out} =  r_{ds4}[1 + R_s(g_{m4} + g_{ds4})] $$

$$ R_S = r_{ds2} $$


$$
r_{out} =  r_{ds4}[1 + r_{ds2}(g_{m4} + g_{ds4})] 
$$

$$
r_{out} \approx  r_{ds2}(r_{ds4}g_{m4})
$$

![](/aic2023/assets/fig_cmCascode.svg)

---

![](/aic2023/assets/fig_current_mirrors.svg)

---

## One more thing ....

---

![](/aic2023/assets/cm_gain_boost.svg)

---
<sub>["High speed, high gain OTA in a digital 90nm CMOS technology" Berntsen, Wulff, Ytterdal, Norchip 2005](https://ieeexplore.ieee.org/document/1597006)</sub>


> image ../ip/berntsen.png removed
---

##  Thanks!

---


