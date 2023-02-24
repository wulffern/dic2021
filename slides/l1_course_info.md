---
title: lectures/l1_course_info
output:
  slidy_presentation:
    footer: "Copyright (c) 2023, Carsten Wulff"
    fig_width: 800
---






    
## TFE4152 - Lecture 1 
## Design of Integrated Circuits


## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l1_course_info.md)

---

## Goal for today
* Who
* Course
* Exercises
* Project
* Software
* Why
* Skills
* How

---

##  Who

---

## Carsten Wulff [carstenw@ntnu.no](carstenw@ntnu.no)

![](/aic2023/assets/timeline_black.png)

---

## Teaching assistants

- Ehsan Lari
- Erlend Kristiansen Berg
- Jonas Gjendem Røysland 

---

##  Course

---

## [Description](https://www.ntnu.no/studier/emner/TFE4152#tab=omEmnet)

## [Time schedule](https://tp.uio.no/ntnu/timeplan/?id=TFE4152&sem=21h&sort=form&type=course)

---



![](/aic2023/assets/cjm.png)


![](/aic2023/assets/weste.png)

---

## [Curriculum](https://github.com/wulffern/dicex/blob/main/book/icd.md)

---

## Tentative lecture plan

| Week | Book                    | Monday                                                                    | Book                    | Friday                               |
|------|-------------------------|---------------------------------------------------------------------------|-------------------------|--------------------------------------|
| 34   |                         | Introduction, what are we going to do in this course. Why do you need it? | WH 1 , WH 15            | Manufacturing of integrated circuits |
| 35   | CJM 1.1                 | pn Junctions                                                              | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                   |
| 36   | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                                                        | CJM 1.3 - 1.6           | Modeling and passive devices         |
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

## Exam

- December 2021?
- 4 hours
- D aids code - No handwritten or printed aids allowed. Preapproved calculator, in accordance to the exam regulations,
  allowed
- 70% of the final grade
- A - F grade (F = Fail)

---

##  Exercise

---

## Facts
- 4 exercises on blackboard (somewhat modified from last year), 1 more to come, exercise 6 is special
- last years exercise and solutions on blackboard
- must have 4 of 6 exercises approved
- strict deadline (Friday XX 23:59)
- no second chances

---

## Exercise 6: [Maze](https://github.com/wulffern/dicex/tree/main/maze) in SystemVerilog

![](/aic2023/assets/maze.gif)

---

## Exercise 6: Maze
1. Explain how the mazeEscaper.v works
2. Make a solution that is better
3. Upload PDF with explanation and verilog to Blackboard
4. Send mazeEscaper.v as attachment to carstenw@ntnu.no with subject TFE4152-Comp-Maze

---

## Plan 

| Date       | Week | Topic                          |
| ---        | ---  | ---                            |
| 2021-09-10 | 36   | PN Junctions                   |
| 2021-09-24 | 38   | Transistors                    |
| 2021-10-08 | 40   | Current Mirrors and Amplifiers |
| 2021-10-22 | 42   | CMOS logic                     |
| 2021-11-05 | 44   | Logic circuits                 |
| 2021-11-19 | 46   | Maze

---

##  Project

---

- 30 % of final grade
- Groups of 2 people. Find a partner soon. Sign up on blackboard.
- Deadline: 19'th November before 12:00 (24 hour format). 
- Strict deadline, $$t > 12:00 \equiv fail$$. Both members in group must submit report.

---

## [A 10 000 Frames/s CMOS Digital Pixel Sensor](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=972156)

![](/aic2023/assets/isscc.png)

---

## Goal
Be inspired by the paper, and design a similar system. 

Design analog circuits in SPICE and digital circuits in SystemVerilog.

---

## Minimum implementation 
- 2 x 2 pixel array in SystemVerilog
- state machine to control reset, exposure, analog-to-digital conversion, and readout of the pixel array
- SPICE of pixel sensor (sensor, comparator, memory)
- Report documenting that the circuits (analog and digital) work as designed

---

## Things it's OK to ignore

- Transistor corners
- Gray counter (ask me why)
- Voltage variation
- Temperature variation
- "nice to have features", like power optimalization, testability

---

## What you get

[github.com/wulffern/dicex](https://github.com/wulffern/dicex)

```
project/
├── spice/
│   ├── Makefile                # See https://www.gnu.org/software/make/manual/html_node/Introduction.html
│   ├── pixelSensor.cir         # Empty circuit for pixelSensor
│   └── pixelSensor_tb.cir      # SPICE testbench for pixelSensor, emulates verilog
└── verilog/
    ├── Makefile                
    ├── pixelSensor.fl          # Verilog file list
    ├── pixelSensor_tb.gtkw     # Save file for GTKWave
    ├── pixelSensor_tb.v        # Verilog testbench for pixelSensor
    └── pixelSensor.v           # Verilog model of analog pixelSensor circuit
```

---

## Report 1/2

- **Introduction** = Why?
- **Theory** = How?
  - As little information as possible. Give references to sources. Assume that
  the reader has read the paper. 
- **Implementation** = What?
  - Describe what you designed
  - State diagrams, with explanation
  - Circuit diagrams, with explanation
  - One sub-chapter per block
  
---

## Report 2/2
- **Verification** = Are you sure it works?  
  - Describe your testbenches, and how you verified your design
  - Describe key results
- **Discussion and conclusion** = Why do you deserve a good grade?
- **Appendix**
  - SPICE netlist
  - SystemVerilog netlist
  - SystemVerilog testbench

---

## You need to start now to be able to complete the project with a good grade

---

## Proposed plan

| Week | Plan                            |
|:------:|:---------------------------------|
| 34   | Register group                  |
| 35   | Read and understand paper       |
| 36   | Sketch what you want to do      |
| 37   | Write theory chapter  in report |
| 38   | Design & simulation             |
| 39   | Design & simulation             |
| 40   | Design & simulation             |
| 41   | Design & simulation             |
| 42   | Verification                    |
| 43   | Verification                    |
| 44   | Write report                    |
| 45   | Write report                    |
| 46   | **Deadline**                    |


---

##  Software

---

You may use what ever you want, but exercises and project have been developed using AIM-Spice, ngspice, iverilog, and GKTwave on Ubuntu linux 20.10

**SPICE**
- AIM-Spice [aimspice.com](http://aimspice.com) (Used for exercises)
- NGSpice [ngspice](http://ngspice.sourceforge.net) , version 34 (Recommended for project)

**SystemVerilog**
- iverilog [Icarus Verilog](http://iverilog.icarus.com), version v11_0
- gtkwave  [GTKWave](http://gtkwave.sourceforge.net), version 3.3.104
- ( yosys [Yosys](http://www.clifford.at/yosys/), version 0.9 )

---

## Option 1 : Install everything on your computer

The software can be installed on Windows, Mac, and Linux

| Pros                              | Cons                 |
| :---                              | ---:                 |
| Once it's running, then it's easy | Take time to install |
|                                   | Compile from source  |
|                                   | No support from us on installing   |

---

## Option 2 : Use login.stud.ntnu.no

| Pros                                     | Cons                              |
| :--                                      | ---:                              |
| I've tested with login.ansatt.ntnu.no    | GUI windows require a bit of work |
| Similar to real world (desktop + server) | Online                            |


---

## Option 2: Quickstart for login.stud.ntnu.no

ssh to login.stud.ntnu.no, run 

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/wulffern/dicex/main/ubuntu_install.sh)"
```

Connect to login from a mac/linux so you get GUI also

```sh
ssh -c aes128-ctr -YC -o "ForwardX11Timeout 4W" <username>@login.stud.ntnu.no
```

---

## Option 3: Ubuntu on docker image with VNC frontend

Run Ubuntu linux on your PC via docker and use a VNC client to connect

| Pros                               | Cons                               |
| :--                                | ---:                               |
| If it works, it's easy             | Complex, so maybe there are issues |
| I've tested it                     | Large ( > 3 GB)                      |
| Offline (not for first run though) |                                    |


---

## dicex and ciceda
Design of Integrated Circuits exercises (dicex) are the testbenches and model files you'll need 
[https://github.com/wulffern/dicex](https://github.com/wulffern/dicex)

Custom IC Creator Electronic Design Automation (ciceda) is a docker image of a ubuntu linux with the necessary tools installed
[https://github.com/wulffern/ciceda](https://github.com/wulffern/ciceda)

---

## dicex - Requirements
- Install [Docker](http://www.docker.com)
- Install [GIT](https://git-scm.com/downloads)
- Install [TigerVNC](https://github.com/TigerVNC/tigervnc/releases) (not needed on Mac)

---

## dicex - Getting started 
In a terminal or powershell

```bash
git clone https://github.com/wulffern/dicex
cd dicex
./ciceda_mac.sh
```

See [demo video](https://youtu.be/SpHw1MB3fus)

---

## Lower your expectations on EDA software

---

## Expect that you will spend at least $$2\pi$$ times more time than planned *(mostly due to software issues)* 

---

## Questions?

---

## Memo time
[https://github.com/wulffern/dic2021/tree/main/2021-06-13\_why\_integrated_circuits](https://github.com/wulffern/dic2021/blob/main/2021-06-13_why_integrated_circuits/why_learn_dic.pdf)

---

##  Purpose

---

![](https://www.extremetech.com/wp-content/uploads/2013/08/bell-labs-first-transistor-640x573.jpg)
<sub><sub>1947: First transistor. Invented by Brattain, Bardeen and Shockley, Bell labs</sub></sub>

---

![](https://www.chiphistory.org/chc_upload/content/jpg/7/1499079245/1499079245.jpg)
<sub><sub>1961: First Monolithic Silicon IC Chip. Invented by Robert Noyce, Fairchild</sub></sub>

---

![](/aic2023/assets/unit_shipments_2021.png)

<sub><sub>https://www.statista.com/statistics/802632/world-semiconductor-shipments/</sub></sub>

---

## Virtex UltraScale+ VU19P (35 billion transistors)

![](https://cdn.mos.cms.futurecdn.net/DDWfbHxyrYER875RdBTYXC-970-80.jpg)
---

![](/aic2023/assets/virtex_ultrascale.png)

---

## Why would anyone buy a 1 M NOK FPGA?

---

![](https://cerebras.net/wp-content/uploads/2021/08/Chip-comparison-01.jpg)
<sub><sub>https://cerebras.net/chip/</sub></sub>


---

nRF51, nRF52, nRF53 series devices from Nordic Semiconductor are all the same type of tool.

* Add connectivity (Bluetooth, Zigbee, custom radio protocol) to your product.
* Provide a microcontroller; CPU + peripherals like interfaces (SPI, UART, ADC, COMP, I2C) to process information, and interface with the world. 


---

![](/aic2023/assets/qfn48.svg)

---

![](/aic2023/assets/nrf5340.png)


---

##  Skills

---

- _Project flow support_: Confluence, JIRA, risk management (DFMEA), failure analysis (8D)
- _Language_: English, Writing English (Latex, Word, Email)
- _Psychology_: Personalities, convincing people, presentations (Powerpoint, Deckset), stress management (what makes your brain turn off?)
- _DevOps_: Linux, bulid systems (CMake, make, ninja), continuous integration
  (bamboo, jenkins), version control (git), containers (docker), container orchestration (swarm, kubernetes)
- _Programming_: Python, Go, C, C++, Matlab <sub>Since 1999 I’ve programmed in Python, Go, Visual BASIC, PHP, Ruby, Perl, C#, SKILL, Ocean, Verilog-A, C++, BASH, AWK, VHDL, SPICE, MATLAB, ASP, Java, C, SystemC, Verilog, and probably a few I’ve forgotten.</sub>
- _Firmware_: signal processing, algorithms
- _Infrastructure_: Power management, reset, bias, clocks
- _Domains_: CPUs, peripherals, memories, bus systems
- _Sub-systems_: Radio’s, analog-to-digital converters, comparators
- _Blocks_: Analog Radio, Digital radio baseband
- _Modules_: Transmitter, receiver, de-modulator, timing
recovery, **state machines**
- _Designs_: Opamps, **amplifiers**,  **current-mirrors**, **adders**,
random access memory blocks, **standard cells**
- _Tools_: schematic, layout, parasitic extraction, synthesis, place-and-route, **simulation**,  **(System)Verilog**, **netlist** 
- _Physics_: **transistor**, **pn junctions**, quantum mechanics

---



> Find a problem that you really want to solve, and learn a programming language to solve it. There is absolutely no point in saying "I want to learn programming", then sitting down with a book to read about programming, and expect that you will learn programming that way. It will not happen. The only way to learn programming is to program, a lot. 
-- Carsten Wulff

---

##  How 

---

## If you have questions on the course content (exercise, project, lectures)

---

## Do
- google
- ask a someone in your class
- use the "øvingstime and labratorieøvelse" to talk to teaching assistants. Don't ask about long future (future exercises).

If none of the above works, we'll use first few minutes in each lectures for questions on the previous content (but not future content).

---

## Don't
- send email with questions on excercise, project, lectures etc. Long response time. 
- use Teams. It interrupts the person your contacting. 
- come to the office. I'm only at NTNU 20%. 

There are approx 130 students. Email, teams, f2f does not scale.

---

## Lecture 2: Manufacturing of integrated circuits

## Homework => [Sam Zeloof Home Chip Fab](https://youtu.be/23fTB3hG5cA)

---

##  Thanks!
