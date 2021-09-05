footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 6
# MOSFET's cont, models and passives

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l6_model_passive.md)

---

| Week | Book                    | Monday                                                                    | Book                    | Friday                               |
|------|-------------------------|---------------------------------------------------------------------------|-------------------------|--------------------------------------|
| 34   |                         | Introduction, what are we going to do in this course. Why do you need it? | WH 1 , WH 15            | Manufacturing of integrated circuits |
| 35   | CJM 1.1                 | pn Junctions                                                              | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                   |
| 36   | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                                                        | CJM 1.3 - 1.6           | **Modeling and passive devices**         |
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
- Mosfet cont
- Metal
- Resistors
- Capacitors
- Inductors
- Diodes
- Antenna effect

---

# Metal in ICs is not wire in schematic

Resistance ~ m$$\Omega$$/$$\square$$

Capacitance ~ aF/$$\mu$$m to fF/$$\mu$$m

Inductance ~ nH/mm

Max current ~ mA/$$\square$$

![right fit](https://www.researchgate.net/publication/329551868/figure/fig1/AS:702470942629891@1544493532703/General-structure-of-an-IC-with-BEOL-evidenced-a-SEM-section-of-an-Intel-Broadwell.jpg)

---

| Layout | Must simulate/know |
|:--: | :--: |
| All | C Imax |
| Analog, Power | R C Imax |
| Some RF, Some Power | R L C Imax |

---

[.column]

 Layout parasitic extraction
 [Calibre xRC](https://eda.sw.siemens.com/en-US/ic/calibre-design/circuit-verification/xrc/)
 [Synopsys StarRC](https://eda.sw.siemens.com/en-US/ic/calibre-design/circuit-verification/xrc/)
 [Cadence Quantus](https://eda.sw.siemens.com/en-US/ic/calibre-design/circuit-verification/xrc/)

 3D EM Simulators
 [Keysight ADS](https://www.keysight.com/zz/en/products/software/pathwave-design-software/pathwave-advanced-design-system.html)
 [HFSS](https://www.keysight.com/zz/en/products/software/pathwave-design-software/pathwave-advanced-design-system.html)

 Transistor CAD (TCAD)
 [Synopsys TCAD](https://www.synopsys.com/silicon/tcad.html)

---

#[fit] Resistors

---

# Polysilicon

Often two types, with, and without silicide 

Silicide reduces resistance of polysilicon

![right](../media/l6/poly.pdf)

---

# Diffusion

Use doped region as resistor

Usually without silicide

Non-linear capacitance

Tricky temperature dependence


![right fit](../media/l6/ndiff.pdf)

---

# Metal

Usually too low omhic to be a useful resistor

Useful for "separating nets" in schematic and layout

Must be considered for power supply and ground routing (high currents)


![right fit](../media/l6/metal.pdf)

---

#[fit] Capacitors

---

![inline fit](../media/l6/fig_capacitors_vertical.pdf)

---

#[fit] Inductors

Usually two top metals, because they are thick (low ohmic)

Use foundry model

3D simulation often needed

![right 200%](https://s.zeptobars.com/nRF51822.jpg) 

---

# Diodes

Many, many ways

Reverse bias diodes to ground are useful for signals with long routing to transistor gate. Protects gate from breakdown during chemical mechanical polish.

![right fit](../media/l6/diodes.pdf)

---

# Electrostatic Discharge 

If you make an IC, you must consider Electrostatic Discharge (ESD) Protection circuits

![right fit](https://media.wiley.com/product_data/coverImage300/18/04714987/0471498718.jpg)

Standards for testing at [JEDEC](https://www.jedec.org/category/technology-focus-area/esd-electrostatic-discharge-0)

## But I just want a digital input, what do I need?

---

![original fit](../media/l6/esd.pdf)

---

#[fit] Input buffer

![right fit](../media/l6/fig_methodology.pdf)


---
# Variation in passives

Absolute value for resistors and capacitors $$\approx \pm 10$$% to $$\pm 20$$%

Relative precision for closely spaced devices $$ \approx 0.1\text{ % to } 1 \text{%}$$ 

Relative precision for devices on same die $$ > 2 \text{%}$$ or more 

---

# Relative precision

Resistors and Capacitors can be matched extremely well

![right fit ](../media/l6/pres_good.pdf)



---

[.column]

![inline 50% ](../media/l6/pres_bad.pdf)

 $$ i_3 = 0  = i_1 - i_2$$ 
 $$ 0 = \frac{V_i - V_o}{R} - \frac{V_o}{1/sC} $$  
 $$ 0 = V_i - V_o - V_o s R C $$ 
 $$ V_o (1 + sRC) = V_i $$ 
 
[.column]
 
 $$ \frac{V_o}{V_i} = \frac{1}{1 + sRC} $$

 
 Assume standard deviation ($$\sigma$$)[^1] of
 
 $$ \sigma_R = 20$$%, $$ \sigma_C = 20$$%   
 
 $$ \sigma_{RC} = \sqrt{0.2^2 + 0.2^2} = 28$$%
 

[^1]: If you don't remember how standard deviation works, read [Introduction to mathematics of noise sources](http://www.wulff.no/publications/noise.pdf)

---




# Combine transistors

![right fit](../media/l6/fig_saremx.pdf)

---

#[fit] Thanks!

---

