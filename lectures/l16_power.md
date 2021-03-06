footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 16
# Power and Wires

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l16_power.md)

---

| Week | Book                    | Monday                                                                    | Book                    | Friday                               |
|------|-------------------------|---------------------------------------------------------------------------|-------------------------|--------------------------------------|
| 34   |                         | Introduction, what are we going to do in this course. Why do you need it? | WH 1 , WH 15            | Manufacturing of integrated circuits |
| 35   | CJM 1.1                 | pn Junctions                                                              | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                   |
| 36   | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                                                        | CJM 1.3 - 1.6           | Modeling and passive devices         |
| 37   |                         | Guest Lecture - Sony                                                      | CJM 3.1, 3.5, 3.6       | Current mirrors                      |
| 38   | CJM 3.2, 3.3,3.4 3.7    | Amplifiers                                                                | CJM, CJM 2 WH 1.5       | SPICE simulation                     |
| 39   |                         | Verilog                                                                   |                         | Verilog                              |
| 40   | WH 1.4 WH 2.5           | CMOS Logic                                                                | WH 3                    | Speed                                |
| 41   |                         | Q & A                                                                     | WH 4/WH 5               | **Power/Wires**                      |
| 42   | WH 6                    | Scaling Reliability and Variability                                       | WH 8                    | Gates                                |
| 43   | WH 9                    | Sequencing                                                                | WH 10                   | Datapaths - Adders                   |
| 44   | WH 10                   | Datapaths - Multipliers, Counters                                         | WH 11                   | Memories                             |
| 45   | WH 12                   | Packaging                                                                 | WH 14                   | Test                                 |
| 46   |                         | Guest lecture - Nordic Semiconductor                                      |                         |                                      |
| 47   | CJM                     | Recap of CJM                                                              | WH                      | Recap of WH                          |


---


#[fit] Pick two

![right fit](../media/l16/optimization.pdf)

---

#[fit] Power

---

# What is power?

Instantanious power: $$ P(t) = I(t)V(t)$$

Energy : $$ \int_0^T{P(t)dt} $$  [J]

Average power: $$\frac{1}{T} \int_0^T{P(t)dt} $$ [W or J/s]



---
# Power dissipated in a resistor

 Ohm's Law $$V_R = I_R R$$

 $$P_R = V_R I_R =  I_R^2 R  = \frac{V_R^2}{R} $$

---
# Charging a capacitor to $$V_{DD}$$

 Capacitor differential equation $$ I_C = C\frac{dV}{dt}$$

 $$E_{C}  = \int_0^\infty{I_C V_C dt} = \int_0^\infty{ C \frac{dV}{dt} V_C dt} = \int_0^{V_C}{C V dV} = C\left[\frac{V^2}{2}\right]_0^{V_{DD}} $$

 $$E_{C} = \frac{1}{2} C V_{DD}^2$$

---
# Energy to charge a capacitor to a voltage $$V_{DD}$$

 $$ E_{C} = \frac{1}{2} C V_{DD}^2$$
 
 $$ I_{VDD} = I_C = C \frac{dV}{dt}$$

 $$ E_{VDD} = \int_0^\infty{I_{VDD} V_{DD} dt} = \int_0^\infty{C \frac{dV}{dt} V_{DD} dt} = C V_{DD}\int_0^{V_{DD}}{dV} = C V_{DD}^2$$

 Only half the energy is stored on the capacitor, the rest is dissipated in the PMOS 

---
# Discharging a capacitor to $$0$$

$$ E_{C} = \frac{1}{2} C V_{DD}^2$$

Voltage is pulled to ground, and the power is dissipated in the NMOS

---
# Power consumption of digital circuits

$$E_{VDD} = C V_{DD}^2$$

In a clock distribution network (chain of inverters), every output is charged once per clock cycle

$$P_{VDD} = C V_{DD}^2 f$$

---
# Sources of power dissipation in CMOS logic

$$ P_{total} = P_{dynamic} + P_{static}$$ 

[.column]
**Dynamic power dissipation**

Charging and discharging load capacitances

*short-circut* current, when PMOS and NMOS conduct at the same time

$$P_{dynamic} = P_{switching} + P_{short circuit}$$

[.column]
**Static power dissipation**

Subthreshold leakage in OFF transistors

Gate leakage (tunneling current) through gate dielectric

Source/drain reverse bias PN junction leakage

$$P_{static} = \left( I_{sub} + I_{gate} + I_{pn} \right) V_{DD}$$

---
# $$ P_{switching}$$ in logic gates

Only output node transitions from low to high consume power from $$V_{DD}$$

Define $$P_i$$ to be the probability that a node is 1

Define $$\overline{P_i} = 1 - P_i$$ to be the probability that a node is 0

Define **activity factor ($$\alpha_i$$)** as the **probability of switching a node from 0 to 1**

If the probabilty is uncorrelated from cycle to cycle

$$\alpha_i = \overline{P_i}P_i$$

---
# Switching probability

Random data $$P = 0.5$$, $$\alpha = 0.25$$

Clocks $$\alpha = 1$$

![left fit](../media/tex/tb_sw_prob.pdf)

---

[.column]
![inline 150%](../media/tex/tb_sw_prob.pdf)

![inline 150%](../media/l16/prob.pdf)


[.column]

 Assume $$P = P_A = P_B = P_C = P_D = \frac{1}{2}$$

 $$P_X = P_Z =  1 - P P = 1 - \frac{1}{4} = \frac{3}{4}$$

 $$ \overline{P_X} = \overline{P_Y} = \frac{1}{4}$$ 

 $$P_Y = \frac{1}{4} \times \frac{1}{4} = \frac{1}{16}$$

 
 $$\alpha = \frac{1}{16}\left(1 - \frac{1}{16}\right) = \frac{15}{16}\frac{1}{16} = \frac{15}{256}$$

---

[.column]

![inline 150%](../media/tex/tb_sw_prob.pdf)

![inline 150%](../media/l16/prob.pdf)

[.column]


# $$ \overline{\overline{\text{AB}} + \overline{\text{CD}}} $$ 

Use *De Morgan* first  $$\overline{A+B}  = \overline{A} \cdot \overline{B}$$


 $$\overline{\overline{\text{AB}} + \overline{\text{CD}}} = \overline{\overline{\text{AB}}} \overline{\overline{\text{CD}}} = ABCD$$

 $$\Rightarrow P_Y = P_A P_B P_C P_D = \left(\frac{1}{2}\right)^4 = \frac{1}{16} $$

---

#[fit] $$P_{tot} = \alpha C V_{DD}^2 f$$

---
# Strategies to reduce dynamic power

1. Stop clock
1. Stop activity
1. Reduce clock frequency
1. Turn off $$V_{DD}$$
1. Reduce $$V_{DD}$$

![right fit](../media/l13/digital_ff_comb.pdf)

---

## Stop clock[^1]

![inline fit ](../media/l16/stop_clock.pdf) 


[^1]: Often called *clock gating*

---

## Stop activity

![inline fit ](../media/l16/logic.pdf)  ![inline fit ](../media/l16/stop_activity.pdf) 

---
## Reduce frequency
![inline fit ](../media/l16/reduce_freq.pdf) 

---
## Turn off power supply [^2]

![inline fit ](../media/l16/powergate.pdf) 

[^2]: Often called power gating

---

### Reduce power supply ($$V_{DD}$$) 

![inline fit ](../media/l16/reduce_vdd.pdf) 

---
### Energy-Delay Product

Chapter 4.4

$$ EDP = k\frac{C^2 V_{DD}^3}{(V_{DD}- V_t)^{\text{1 to 2}}}$$

Differentiating with respect to $$V_{DD}$$ and setting the result to $$0$$ it's possible to work out that

$$ V_{DD-opt} = \frac{3}{3-\text{1 to 2}}V_t  \in[1.5,3]V_{t}$$

---

#[fit] Wires

---

# Wire geometry

Pitch = w + s

Aspect ratio (AR) = t/w

These days $$AR \approx 2$$

![right fit](../ip/l16/wire.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->

---
# Metal stack

Often 5 - 10 layers of metal

|Metal |Material | Thickness |Purpose |
| :--: | :--:|:--:| :--: |
|Metal 1 - 3 | Copper| Thin | in gate routing|
|Metal 4 - 5 | Copper| Thicker| Between gates routing|
|Metal 6 | Copper| Very thick|  Cross chip routing. Local Power/Ground routing|
|Metal 7 - 8 | Copper| Ultra thick | Cross chip power routing. Often used for RF inductors.|
|RDL | Aluminium | Ultra tick | Can tolerate high forces during wire bonding.|

![right 150%](../ip/l16/45stack.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->

---
[.background-color: #000000]
[.text: #FFFFFF]

#[fit] Metal routing rules on IC

Odd numbers metals $$\Rightarrow$$ Horizontal routing (as far as possible)

Even numbers metals $$\Rightarrow$$ Vertical routing (as far as possible)

---
# Modeling Interconnect

**Resistance** 
narrow size impedes flow

**Capacitance** 
through under the leaky pipes

**Inductance** 
paddle wheel intertia opposes changes in flow rate

![right 150%](../ip/l16/int_model.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->

---

# Lumped model

Use 1-segment $$\pi$$-model for Elmore delay

![right 150%](../ip/l16/lumped_model.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->

---
# Wire resistance

 resistivity $$\Rightarrow \rho $$ [$$\Omega$$m]

 $$ R = \frac{\rho}{t}\frac{l}{w} = R_\square \frac{l}{w}$$

 $$ R_\square$$ = sheet resistance [$$\Omega/\square$$]

 To find resistance, count the number of squares

 $$ R = R_\square \times \text{# of squares}$$

![right 150%](../ip/l16/resistance.png)

---
# Most wires: Copper

$$R_{sheet-m1} \approx \frac{1.7 \mu\Omega cm}{200 nm} \approx 0.1 \Omega/\square$$  
$$R_{sheet-m9} \approx \frac{1.7 \mu\Omega cm}{3 \mu m} \approx 0.006 \Omega/\square$$  

**Pitfalls**

Cu atoms diffuse into silicon and can cause damage

Must be surrounded by a diffusion barrier

Difficult high current densities (mA/$$\mu$$m)
and high temperature (125 C)




![right fit](../ip/l16/metals.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->

---
# Contacts

Contacts and vias can have 2-20 $$\Omega$$ 

Must use many contacts/vias for high current wires

![right fit](../ip/l16/contacts.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->

---

# Wire capacitance

### $$C_{total} = C_{top} + C_{bot} + 2C_{adj}$$

![right 150%](../ip/l16/capacitance.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->

---
# Wire Capacitance

Dense wires has about $$0.2 \text{ fF/}\mu\text{m}$$

![right 150%](../ip/l16/cap_estimate.png)

<!-- Figure from lect14-wires Integrated Circuit Design slide set -->


---
**Estimate delay of inverter driving a 1 mm long , 0.1 $$\mu m$$ wide metal 1 wire with inverter load at the end**

 $$R_{sheet} = 0.1 \Omega/\square$$ , $$R_{inv} = 1 k \Omega$$, 
 $$C_{w} = 0.2 fF/\mu m$$, $$C_{inv} = 1 fF$$

Use Elmore (Lecture 14)
 $$t_{pd} = R_{inv}\frac{C_{wire}}{2} + (R_{wire} + R_{inv}) \left(\frac{C_{wire}}{2} + C_{inv}\right) $$
 $$= 1k \times 100f + (1k + 0.1 \times 1k/0.1)\times 101f = 0.3\text{ ns}$$ 

![right 150%](../media/l16/wire_delay.pdf)

---
# Crosstalk

A wire with high capacitance to a neighbor

An aggressor (0-1, 1-0) injects charge into neighbor wire

**Increases delay**

**Noise on nonswitching wires**


![right fit](../media/l16/crosstalk.pdf)

---

#[fit] Demo of Layout

---
#[fit] Thanks!










