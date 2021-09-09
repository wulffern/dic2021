footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 5
# MOSFET's

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l5_mosfets.md)

---

| Week | Book                    | Monday                                                                    | Book                    | Friday                               |
|------|-------------------------|---------------------------------------------------------------------------|-------------------------|--------------------------------------|
| 34   |                         | Introduction, what are we going to do in this course. Why do you need it? | WH 1 , WH 15            | Manufacturing of integrated circuits |
| 35   | CJM 1.1                 | pn Junctions                                                              | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                   |
| 36   | CJM 1.2 WH 1.3, 2.1-2.4 | **Mosfet transistors**                                                        | CJM 1.3 - 1.6           | Modeling and passive devices         |
| 37   |                         | Guest Lecture - Sony                                                      | CJM 3.1, 3.5, 3.6       | Current mirrors                      |
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
# Goal for today

[.column]
- Low frequency model
- High frequency model
- Subthreshold operation
- Velocity saturation

[.column]

- Other effects
  - DIBL
  - WPE
  - Stress
  - Gate current
  - Breakdown effects
  
---

#[fit] Low frequency model

---


## $$ g_{m} = \frac{\partial I_{DS}}{\partial V_{GS}}\ $$

## $$ g_{ds} = \frac{1}{r_{ds}}  = \frac{\partial I_{DS}}{\partial V_{DS}}\ $$


![right fit](../media/small_signal.pdf)

---
## Transconductance ($$ g_m $$)
[.column]

Define $$ \ell = \mu_n C_{ox} \frac{W}{L} $$ and $$ V_{eff} = V_{GS} - V_{tn} $$ 

 $$ I_{D} = \frac{1}{2} \ell (V_{eff})^2$$ and $$ V_{eff} = \sqrt{\frac{2I_{D}}{\ell}} $$ and $$ \ell = \frac{2I_D}{V_{eff}^2} $$

 $$ g_m = \frac{ \partial I_{DS}} {\partial V_{GS}} = \ell V_{eff} = \sqrt{2 \ell I_{D}} $$
 
 $$  g_m = \ell V_{eff} = 2 \frac{I_D}{V_{eff}^2} V_{eff} = \frac{2 I_D}{V_{eff}} $$

[.column]
---

Define $$ \ell = \mu_n C_{ox} \frac{W}{L} $$ and $$ V_{eff} = V_{GS} - V_{tn} $$ 

 $$ I_D = \frac{1}{2} \ell V_{eff}^2[1 + \lambda V_{DS} - \lambda V_{eff})] $$ 

 $$\frac{1}{r_{ds}} = g_{ds} = \frac{ \partial I_D}{\partial V_{DS} }  = \lambda \frac{1}{2} \ell V_{eff}^2$$
 
 Assume channel length modulation is not there, then 
 
 $$I_D = \frac{1}{2} \ell V_{eff}^2 $$ which means $$\frac{1}{r_{ds}} = g_{ds} \approx \lambda I_D $$

---

# Intrinsic gain

Define intrinsic gain as  

 $$ A = \left|\frac{v_{out}}{v_{in}}\right| =  g_m r_{ds} = \frac{g_m}{g_{ds}}  $$

 $$ A  =  \frac{2 I_D}{V_{eff}} \times \frac{1}{ \lambda I_D } = \frac{2}{\lambda V_{eff}}  $$

![right fit](../media/vgaini.pdf)



<sub>vgaini = Gate Source Voltage = $$V_{eff} + V_{tn} $$ </sub>

---


#[fit] Body Effect

---

# Bulk voltage

| Param | Voltage [V]|
| :---:| :---:|
| V<sub>GS</sub> | 0.5 |
| V<sub>DS</sub> | 1.0 |
| V<sub>S</sub> | 0 |
| V<sub>B</sub> | -1.0 to 0.3 |

![right fit](../media/vbulk.pdf)

---

![inline 110%](../media/l5/bulk.pdf)

---

[.column]

$$ V_{tn} = V_{tn0} + \gamma \left(\sqrt{ V_{SB} + | 2 \phi_F |} - \sqrt{| 2 \phi_F |}  \right) $$

$$ V_{tn} = V_{tn0} + \gamma \sqrt{|2 \phi_F|} \left(\sqrt{ \frac{V_{SB}}{| 2 \phi_F |} + 1 } - 1 \right) $$

$$ \gamma = \frac{ \sqrt{ 2 q N_A K_{si} \epsilon_0}}{C_{ox}}$$  $$ \Phi_F = V_T ln\left(\frac{N_A}{n_i}\right) $$

[.column]

$$ V_{SB} = 0, V_{tn} = V_{tn0}$$

$$ V_{SB} > 0, V_{tn} > V_{tn0}$$

$$ V_{SB} < 0, V_{tn} < V_{tn0}$$

---

![original fit](../media/l5/bulk_fw_bulk.pdf)

---

![original fit](../media/l5/bulk_fw.pdf)

---

![original fit](../media/small_signal_w_gs.pdf)

---

#[fit] High frequency model

---


![inline fit](../media/l5/hfmodel.pdf) 

---

![inline fit](../media/l5/caps.pdf)

---
# $$C_{gs} $$ and $$C_{gd}$$

[.column]

$$
C_{gs} =
\begin{cases}
WLC_{ox} & \text{if }V_{DS} = 0 \\[15pt]
\frac{2}{3}WLC_{ox} & \text{if }V_{DS} > V_{eff} \\[15pt]
\end{cases}
$$

[.column]

$$ C_{gd} = C_{ox} W L_{ov} $$

---

# $$C_{sb}$$ and $$C_{db}$$

Both are depletion capacitances, ref lecture 3

[.column]
$$ C_{sb} = (A_s + A_{ch}) C_{js} $$

$$ C_{js} = \frac{C_{j0}}{\sqrt{1 + \frac{V_{SB}}{\Phi_0}}} $$

$$\Phi_0 = V_T ln\left(\frac{N_A N_D}{n_i^2}\right)$$

[.column]

$$ C_{db} = A_d C_{jd} $$

$$ C_{js} = \frac{C_{j0}}{\sqrt{1 + \frac{V_{DB}}{\Phi_0}}} $$

---

### Be careful with $$ C_{gd} $$ (blame Miller)

[.column]

<sub> You will derive Miller theorem in the future (p 169) </sub>

If $$ Y(s) = 1/sC $$ then 
 $$Y_1(s) = 1/sC_{in} $$ and $$Y_2(s) = 1/sC_{out}$$ where
 $$ C_{in} = (1 + A) C $$, $$ C_{out} = (1 + \frac{1}{2})C $$
 
 $$ C_{1} = C_{gd} g_{m} r_{ds} $$

**$$C_{gd}$$ can appear to be 10 to 100 times larger!**

 if gain from input to output is large 


[.column]

![inline fit](../media/l5/miller.pdf)

---

#[fit] Weak inversion 
# <sub> or subthreshold </sub>

---

If $$ V_{eff} < 0 $$ diffusion currents dominate.

 $$ I_{D} = I_{D0} \frac{W}{L} e^{V_eff / n V_T} $$, where
 
 $$ V_T = kT/q $$, $$n = (C_{ox} + C_{j0})/C_{ox}$$
 
 $$ I_{D0} = (n - 1) \mu_n C_{ox} V_T^2 $$

 $$ g_m = \frac{I_D}{nV_T} $$

![right fit](../media/weakinv.pdf)

---
# $$ g_m/I_D $$ <sub> or "bang for the buck" </sub>

 Subthreshold:  
 
 $$ \frac{g_m}{I_D} = \frac{1}{nV_T} \approx 25.6 \text{ [S/A] @ 300 K} $$ 

 Strong inversion:  
 
 $$ \frac{g_m}{I_D} = \frac{2}{V_{eff}}$$ 

![right fit](../media/l5/vgmid.pdf)

---

#[fit] Velocity saturation

---

[.column]

Electron speed limit in silicon

 $$ v \approx  10^7 cm/s $$

 $$ v = \mu_n E = \mu_n \frac{dV}{dx} $$
 
 $$ \mu_n \approx 100 \text{ to  } 600 \text{  } cm^2/Vs $$ in nanoscale CMOS
 
[.column]
 
![right fit](l5_velocity.pdf)

---

[.column]

## Square law model

 $$ Q(x) = C_{ox}\left[V_{eff} - V(x)\right] $$ 
 
 $$ v = \mu_n E = \mu_n \frac{dV}{dx} $$ 
 
 $$ \ell = \mu_n C_{ox} \frac{W}{L} $$

 $$ I_{D} = W Q(x) v  = \ell L \left[ V_{eff} - V(x)\right] \frac{dV}{dx} $$

 $$ I_{D} dx = \ell L \left[ V_{eff} - V(x)\right] dV $$

[.column]

 $$ I_{D} \int_0^L{dx}  = \ell L \int_0^{V_{DS}}{\left[ V_{eff} - V(x)\right] dV} $$

 $$ I_{D} \left[x\right]_0^L = \ell L \left[V_{eff}V - \frac{1}{2}V^2\right]_0^{V_{DS}} $$

 $$ I_{D} L = \ell L \left[V_{eff}V_{DS} - \frac{1}{2} V_{DS}^2\right] $$

 $$ @ V_{DS} = V_{eff} \Rightarrow I_{D} = \frac{1}{2} \ell V_{eff}^2 $$

---

 
[.column]
 
## Mobility Degredation

Multiple effects degrade mobility

- Velocity saturation
- Vertical fields reduce channel depth => more charge-carrier scattering

 $$ \ell = \mu_n C_{ox} \frac{W}{L} $$

[.column]
 

 $$ \mu_{n\_eff} = \frac{\mu_n}{([1 + (\theta V_{eff})^m])^{1/m}} $$

 $$ I_{D} = \frac{1}{2} \ell V_{eff}^2 \frac{1}{([1 + (\theta V_{eff})^m])^{1/m}} $$

From square law
$$ g_{m} = \frac{\partial I_{D}}{\partial V_{GS}} =   \ell V_{eff} $$

With mobility degredation
$$ g_{m(mob-deg)} = \frac{\ell}{2 \theta} $$

---

#[fit] What about holes (PMOS)

---

[.column]

In PMOS holes are the charge-carrier.

 $$ \mu_p < \mu_n $$

In intrinsic silicon:
 $$ \mu_n  \leq 1400 [cm^2/Vs] = 0.14 [m^2/Vs] $$
 $$ \mu_p  \leq 450 [cm^2/Vs] = 0.045 [m^2/Vs] $$
 
 $$ \mu_n \approx 3\mu_p $$

[.column]

 $$ v_{n\_max} \approx 2.3 \times 10^5 [m/s] $$
 $$ v_{p\_max} \approx 1.6 \times 10^5 [m/s] $$


 **Doping ($$N_A \text{or} N_D$$) reduces $$\mu $$** 

---

![left 200%](../media/l5/fig_inv.pdf)

## Assume we want same current in strong inversion and active region 

## What should $$\frac{W_p}{W_n}$$ be?

---


#[fit] OTHER

---

# As we make transistors smaller, we find new effects that matter, and that must be modelled.

### <sub> which is an opportunity for engineers to come up with cool names </sub>

---

![original fit](../media/l5/aicdn_front.png)

[https://ieeexplore.ieee.org/document/5247174](https://ieeexplore.ieee.org/document/5247174 )

---

![original fit](../media/l5/aicdn.pdf)

---

#[fit] Drain induced barrier lowering (DIBL)

---

![original fit](../media/l5/dibl.pdf)


---

#[fit] Well Proximity Effect (WPE)

---

![original fit](../media/l5/wpe.pdf)


---

#[fit] Stress effects 

---

| Stress | PMOS | NMOS |
| :--: | :--: | :---:|
| Stretch Fz | Good | Good |
| Compress Fy | OK | Good |
| Compress Fx | Good | Bad |

## What can change stress?

![right fit](../media/l5/stress.pdf)

---


#[fit] Gate current

---

![original fit](../media/l5/gateleakage.pdf)

---

![original fit](https://patentimages.storage.googleapis.com/9d/08/77/b6842f1e219aba/imgf0001.png)

---

#[fit] Hot carrier injection

---

![original 80%](../media/l5/hci.pdf)

---

#[fit] Channel initiated secondary-electron (CHISEL)

---

![original 80%](../media/l5/chisel.pdf)

---

#[fit] Analog Design Recommendations

---

# Unit size transistors for analog design

 $$ W/L \in[4, 6, 10] $$, but should have space for two contacts
 
Use parallell transistors for larger W/L

Amplifiers $$ L = 1.2 \times L_{min} $$

Current mirrors $$ L = 4 \times L_{min} $$

Choose sizes that have been used by foundry for measurement to match SPICE model

---

# Unit transistor layout

Use 2 fingers (parallel transistors)

Never rotate transistors

Make sure bulk is close

![right fit](../media/l5/2fingunit.pdf)

---

#[fit] Thanks!

---


