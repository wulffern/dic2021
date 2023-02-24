---
title: lectures/l20_adders
output:
  slidy_presentation:
    footer: "Copyright (c) 2023, Carsten Wulff"
    fig_width: 800
---







## TFE4152 - Lecture 20
## Adders

## [Source](https://github.com/wulffern/dic2021/blob/main/lectures/l19_fsm.md)

---

| Week | Book                    | Monday                                                                    | Book                    | Friday                               |
|------|-------------------------|---------------------------------------------------------------------------|-------------------------|--------------------------------------|
| 34   |                         | Introduction, what are we going to do in this course. Why do you need it? | WH 1 , WH 15            | Manufacturing of integrated circuits |
| 35   | CJM 1.1                 | pn Junctions                                                              | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                   |
| 36   | CJM 1.2 WH 1.3, 2.1-2.4 | Mosfet transistors                                                        | CJM 1.3 - 1.6           | Modeling and passive devices         |
| 37   |                         | Guest Lecture - Sony                                                      | CJM 3.1, 3.5, 3.6       | Current mirrors                      |
| 38   | CJM 3.2, 3.3,3.4 3.7    | Amplifiers                                                                | CJM, CJM 2 WH 1.5   | SPICE simulation
| 39   |                         | Verilog                                                                   |                         | Verilog                              |
| 40   | WH 1.4 WH 2.5           | CMOS Logic                                                                | WH 3                    | Speed                                |
| 41   | WH 4                    | Power                                                                     | WH 5                    | Wires                                |
| 42   | WH 6                    | Scaling Reliability and Variability                                       | WH 8                    | Gates                                |
| 43   | WH 9                    | Sequencing and FSM                                                                | WH 10                   | **Datapaths - Adders**                   |
| 44   | WH 10                   | Datapaths - Multipliers, Counters                                         | WH 11                   | Hacking circuits (Nordic). Memories                             |
| 45   | WH 12                   | Packaging                                                                 | WH 14                   | Test                                 |
| 46   |                         | Guest lecture - Nordic Semiconductor                                      |                         |                                      |
| 47   | CJM                     | Recap of CJM                                                              | WH                      | Recap of WH                          |



---
## Housekeeping

[https://folk.ntnu.no/carstenw/TFE4152/scoreboard.html](https://folk.ntnu.no/carstenw/TFE4152/scoreboard.html)

[https://github.com/wulffern/dic2021/blob/main/2021-10-19\_project\_report/project\_report.pdf](https://github.com/wulffern/dic2021/blob/main/2021-10-19_project_report/project_report.pdf)


---

## Want to make your own IC?

[https://efabless.com/](https://efabless.com/)

[https://github.com/google/skywater-pdk](https://github.com/google/skywater-pdk)

[https://skywater-pdk.readthedocs.io/en/latest/index.html](https://skywater-pdk.readthedocs.io/en/latest/index.html)

---

**Honesty:** Making integrated circuits is an expensive endeavor. As humans, we will always make mistakes, or fail to imagine how things will fail. The cost of failures increases exponentially the closer we are to a volume product. As such, finding mistakes early is necessary to reduce cost. If people are honest, and acknowledge immediately that something has gone wrong, that can give us time to fix the problem before it costs millions.

**Responsibility:** Time to market is essential in integrated circuits. We must meet the market window for a particular product. Complex projects will be broken down into pieces, and milestones. We require those milestones to be met, as such, we need people that take responsibility, and ensure that milestones are met. If their milestone depends on a delivery from someone else, they need to follow up, and help to ensure that the overall milestones are met.

**Logical thinking:** When things go wrong, we need people that will dig into the problem and find the real physical root cause. There is no place for “hand-wavy” arguments, or arguments from authority “I know everything, so you should listen to me”. We deal with physics, and in integrated circuits, how something fails always have a physical reason.

**Humility:** Realizing that humans are fallible, but we should strive for not doing the same mistake twice.

**Diversity:** An employee’s brain must have the right skills and the right qualities. We strive for diversity, free from discrimination due to gender, nationality, origin, and religion.

**Ability to learn:** As an engineer you’re never finished learning. Integrated circuits is a deep skill, and you will need the ability to learn new things.

**Curiosity:** We want engineers that like to understand how things work. There should be an inherent drive to figure things out.

**Be fearless:** Don’t be afraid of asking questions. Be forward leaning. Act. Champion your ideas.

---
##  +

---

## Together with a partner (or alone), figure out the logic circuit for the sum of two 1-bit signals, A + B, with the sum as a 1-bit output (S) and a 1-bit carry (C) 

---
### Half adder

![](/aic2023/assets/half_adder.svg)


---

## Together with a partner (or alone), figure out the logic circuit for the sum of **three 1-bit signals, A, B, and carry input (Ci)** with the sum as a 1-bit output (S) and a 1-bit carry (C) 

---

### Full adder


![](/aic2023/assets/full_adder.svg)

---

### Full adder

$$ S = A \oplus B \oplus Ci$$

$$ C = (A \oplus B)Ci + AB$$


![](/aic2023/assets/full_adder_block.svg)


---

### 1-bit adder

```verilog
module adder (input logic [WIDTH-1:0] A,
              input logic [WIDTH-1:0] B,
              output logic [WIDTH:0] Y
              );

   localparam WIDTH=1;

   assign Y = A + B;
endmodule
```

![](/aic2023/assets/adder_1bit.svg)

---
### 2-bit adder

```verilog
module adder (input logic [WIDTH-1:0] A,
              input logic [WIDTH-1:0] B,
              output logic [WIDTH:0] Y
              );

   localparam WIDTH=2;

   assign Y = A + B;
endmodule
```

![](/aic2023/assets/adder_2bit.svg)

---

### 4-bit adder

```verilog
module adder (input logic [WIDTH-1:0] A,
              input logic [WIDTH-1:0] B,
              output logic [WIDTH:0] Y
              );

   localparam WIDTH=4;

   assign Y = A + B;
endmodule
```

![](/aic2023/assets/adder_4bit.svg)

---

### 8-bit adder

```verilog
module adder (input logic [WIDTH-1:0] A,
              input logic [WIDTH-1:0] B,
              output logic [WIDTH:0] Y
              );

   localparam WIDTH=8;

   assign Y = A + B;
endmodule
```

![](/aic2023/assets/adder_8bit.svg)

---

### 16-bit adder

```verilog
module adder (input logic [WIDTH-1:0] A,
              input logic [WIDTH-1:0] B,
              output logic [WIDTH:0] Y
              );

   localparam WIDTH=16;

   assign Y = A + B;
endmodule
```

![](/aic2023/assets/adder_16bit.svg)

---

##  Straightforward adders become deep, can we make it better?

---




