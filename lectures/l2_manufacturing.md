footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 2
# Manufacture Integrated Circuits

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l2_manufacturing.md)

---
- Learn to learn
- How did I choose analog
- Exam: December 10'th
---

# Goal for today

* Why
* How

<!-- 
  - Wafer
  - Photolithography
  - Remove stuff
  - Add stuff
  - Cleaning
-->

* What

<!--
  - Digital flow 
  - Analog flow
-->

---

#[fit] Why

---

![left 100%](../media/lindens_handbook_of_batteries.png)

# Let's make a battery charger

---
# How

[.column]

- What does the use case require?
- What IC do we need?
- How is it connected to the real world?
- What pins do we need?
- What states are there?

[.column]
![inline](../media/charge_graph.png)

---

#[fit] How

---

# Printed Circuit Board (PCB)

---

[.column]

![inline](../media/l2_sch.png)


[.column]

![inline](../media/l2_pcb.png)

---

- Many, many vendors 
- I know Ph.D that students have used [PCBway](https://www.pcbway.com/)
- Omega Verksted probably know best option
- Use [Altium](https://www.altium.com) to design the PCB 

---

# Package and Test

---

![left 100%](../media/MQFP.png)

Many package options

Usually done by OSATS (Outsourced Semiconductor Assembly and Test)

[www.amkor.com](https://www.amkor.com)

[ase.aseglobal.com](https://ase.aseglobal.com)

---

![inline 170%](https://www.iue.tuwien.ac.at/phd/poschalko/img410.png) 

<sub><sub>Online, https://www.iue.tuwien.ac.at/phd/poschalko/img410.png</sub></sub>

---

# Die

---

![original 160%](https://s.zeptobars.com/nRF51822.jpg) 

<sub><sub>Picture: nRF51822 (https://s.zeptobars.com/nRF51822.jpg)</sub></sub> 

---

# Who makes dies?

- TSMC, Globalfoundries, Samsung, UMC, SMIC ...
- Extremely high initial cost (k\$ to M\$)
- Low production cost (<< \$ per mm<sup>2</sup>)
- Sam Zeloof, made one i his garage [https://www.youtube.com/watch?v=IS5ycm7VfXg&t=3](https://www.youtube.com/watch?v=IS5ycm7VfXg&t=3)


---

# Wafer

---

### Ingot created with Czochralski Process
![inline](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Czochralski_Process.svg/2560px-Czochralski_Process.svg.png)

---
[.background-color: #000000]


# [Quantum Bound States](https://phet.colorado.edu/sims/cheerpj/bound-states/latest/bound-states.html?simulation=bound-states)

---

[.column]

> Everything should be made as simple as possible, but no simpler. (A. Einstein)

![original](../media/crystal_simplified.png)

[.column]

[Crystal lattice](https://sketchfab.com/3d-models/silicon-crystal-lattice-73e292f32ffe4ca490e166faeba317e7)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Silicon-unit-cell-3D-balls.png/628px-Silicon-unit-cell-3D-balls.png)

---

# Photolithography

---

ArFr light source: 193 nm

Resolution: < 38 nm

Wafers per hour: > 250

Overlay: < 2.0 nm

Price: Don't know. Maybe 100 M$?

[https://www.youtube.com/watch?v=ShYWUlJ2FZs](https://www.youtube.com/watch?v=ShYWUlJ2FZs)

![left](https://www.asml.com/-/media/asml/images/products/duv-lithography-systems/twinscan-nxt1970ci.png?mw=1200&hash=192BA48B205DA9E3CC048A897327E8DF)


---

# EUV lithography

Light source : 13.5 nm
Resolution : ??
Wafers per hour : 100 ??
Price: ???

![left fit](https://www.elinfor.com/article/E/U/EUV%20lithography%20machines%20of%20ASML.jpg)

---
[.background-color: #000000]
[.text: #FFFFFF]


$$E = hf = hc/\lambda$$, where $$h = 4.1e-15 eV/Hz$$ and $$ c = 3e8$$

| Wavelength [nm] | Energy [eV] |
| :---:           | :---:       |
| 1000            | 1.2         |
| 240             | 5.1         |
| 193             | 6.4         |
| 90              | 13.6        |
| 13.5            | 91.1        |

Seems like the highest known band gap is about 13.5 eV (Lithium Fluoride) 

---

![inline ](https://i1.wp.com/semiengineering.com/wp-content/uploads/2016/11/Screen-Shot-2016-11-15-at-4.04.00-PM.png?w=953&ssl=1)

<sub><sub>Online, https://i1.wp.com/semiengineering.com/wp-content/uploads/2016/11/Screen-Shot-2016-11-15-at-4.04.00-PM.png?w=953&ssl=1</sub></sub>

---

![fit](../media/euv_litho.pdf)

---

# Remove stuff

[Etching](https://en.wikipedia.org/wiki/Etching_\(microfabrication\))

[Chemical Mechanical Polish](https://en.wikipedia.org/wiki/Chemical-mechanical_polishing)

[RCA clean](https://en.wikipedia.org/wiki/RCA_clean)

---

# Add stuff

[Thermal oxidation](https://en.wikipedia.org/wiki/Thermal_oxidation)

[Chemical vapor deposition](https://en.wikipedia.org/wiki/Chemical_vapor_deposition)

[Atomic layer deposition](https://en.wikipedia.org/wiki/Atomic_layer_deposition)

[Ion implantation](https://en.wikipedia.org/wiki/Ion_implantation)

[Diffusion](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1050758)

---

# Diffusion

[.column]
[Diffusion Selfaligned MOST; A New Approach to High Speed Devices, 1969](https://confit.atlas.jp/guide/event-img/ssdm1969/4-1/public/pdf_archive?type=in)

![inline](../media/diffusion_most.png)

[.column]
[Complementary DMOS Process for LSI](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=1050758)

![inline](../media/diffusion_dmos.png)

---

![fit](https://s.zeptobars.com/nRF51822.jpg) 

---

#[fit] What

---

# GDSII (DEMO)

![](../media/klayout.png) 

---

# How do we go from idea to GDSII?

---

#[fit] Thanks!


