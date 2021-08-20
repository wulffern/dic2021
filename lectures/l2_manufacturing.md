footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 2
# How are ICs made

---

# Goal for today

* Why make ICs
* How are they made

---

#[fit] Why

---

#All ICs are made for a purpose

---

![left 100%](../media/lindens_handbook_of_batteries.png)

![right 60%](../media/charge_graph.png)

---
# How

- What does the use case require?
- What IC do we need?
- How is it connected to the real world?
- What pins do we need?
- What states are there?

---

![fit](../media/ch4.pdf)

---

# Printed Circuit Board

---

[.column]

![inline](../media/l2_sch.png)
![inline](../media/l2_pcb.png)

[.column]

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

![left fit](https://s.zeptobars.com/nRF51822.jpg) 

# Die

---

- TSMC, Globalfoundries, Samsung, UMC, SMIC ...
- Very, very, very, very expensive to make
- But, [Sam Zelof](https://www.youtube.com/watch?v=IS5ycm7VfXg&t=3), made one i
  his garage


<sub><sub>Picture: nRF51822 (https://s.zeptobars.com/nRF51822.jpg)</sub></sub> 

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

# Process steps 
- https://en.wikipedia.org/wiki/Semiconductor_device_fabrication
- https://en.wikipedia.org/wiki/Chemical_vapor_deposition
- https://en.wikipedia.org/wiki/Sputtering
- https://en.wikipedia.org/wiki/Chemical-mechanical_polishing
- https://en.wikipedia.org/wiki/Etching_(microfabrication)
- https://en.wikipedia.org/wiki/RCA_clean
- https://en.wikipedia.org/wiki/Reactive-ion_etching
- https://en.wikipedia.org/wiki/Deep_reactive-ion_etching
- https://en.wikipedia.org/wiki/Czochralski_method
- https://en.wikipedia.org/wiki/Ion_implantation
  - axcelis (Purion)
- https://en.wikipedia.org/wiki/Diffusion
- https://en.wikipedia.org/wiki/Photoresist
  - Dow Chemical 
  - JSR
  - Shin-Etsu 
- https://en.wikipedia.org/wiki/Photolithography
  - ASML

---

![fit](https://s.zeptobars.com/nRF51822.jpg) 

---

# How does foundry know what to make?

---

# GDSII DEMO

![](../media/klayout.png) 


---

# Path to GDSII

---

[.column]
#[fit] Analog on top


[.column]

#[fit] Digital on top

---

[.column]
#[fit] Analog top layout


[.column]

#[fit] Place and route

---
[.column]
#[fit] Analog extracted simulation

- Did parasitics (RLC) screw something up
- Does it still work?

[.column]

#[fit] Netlist simulation

- Timing
- Setup/Hold times
- Functionality

---

[.column]
#[fit] Analog Cell Layout

- Polygon pushing
- Power routing
- Expensive tools: Cadence Virtuoso
- Need Process Design Kit (PDK) from foundry
- Free tools ([magic](http://opencircuitdesign.com/magic/)) exists, but what about PDK??

[.column]

#[fit] Synthesis

- Translate Verilog or SystemVerilog (or VHDL) to netlist
- Expensive tools
- But [yosys](http://www.clifford.at/yosys/) is pretty good (and free)

---

[.column]
#[fit] Analog cell layout

- Transistors
- Resistors
- Capacitors
- (Inductors)
- (Diodes)
- (Silicon Rectifiers)

[.column]

#[fit] Digital standard cell design layout

- standard cells (INV, AND, OR, NOR, NAND, XOR, DFF)

---

[.column]
#[fit] Analog Schematic simulation

- Does it work over process, voltage and corners?


[.column]

#[fit] Place and route

---
