footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 2
# How are ICs made

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l2_manufacturing.md)

---

# Goal for today

* Why
* How
  - PCB
  - Package
  - Die
  - Lithography

---

#[fit] Why

---

# All ICs are made for a purpose

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
![right 60%](../media/charge_graph.png)

---

![fit](../media/ch4.pdf)

---

#[fit] How

---

#[fit] Printed Circuit Board (PCB)

---

[.column]

![inline](../media/l2_sch.png)


[.column]

![inline](../media/l2_pcb.png)

---

# PCB

- Many, many vendors 
- I know Ph.D that students have used [PCBway](https://www.pcbway.com/)
- Omega Verksted probably know best option
- Use [Altium](https://www.altium.com) to design the PCB 

---

# Package and Test

![left 100%](../media/MQFP.png)

Many package options

Usually done by OSATS (Outsourced Semiconductor Assembly and Test)

[www.amkor.com](https://www.amkor.com)

[ase.aseglobal.com](https://ase.aseglobal.com)

---

![inline 170%](https://www.iue.tuwien.ac.at/phd/poschalko/img410.png) 

<sub><sub>Online, https://www.iue.tuwien.ac.at/phd/poschalko/img410.png</sub></sub>

---

![left fit](https://s.zeptobars.com/nRF51822.jpg) 

#[fit] Die

<sub><sub>Picture: nRF51822 (https://s.zeptobars.com/nRF51822.jpg)</sub></sub> 

---

# Who makes dies?

- TSMC, Globalfoundries, Samsung, UMC, SMIC ...
- Very, very, very, very expensive to make
- But, Sam Zeloof, made one i his garage [https://www.youtube.com/watch?v=IS5ycm7VfXg&t=3](https://www.youtube.com/watch?v=IS5ycm7VfXg&t=3)


---

# Let me tell you a secret

---

# Why does a fab cost billions?

---
# Lithography

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

# How does foundry know what to make?

---

# GDSII DEMO

![](../media/klayout.png) 


---

# How do we get to a GDSII file?

