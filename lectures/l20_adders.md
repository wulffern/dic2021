footer: Carsten Wulff 2021
slidenumbers:true
autoscale:true
theme: Plain Jane, 1
text:  Helvetica
header:  Helvetica

## TFE4152 - Lecture 20
# Adders

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
# Housekeeping

[https://folk.ntnu.no/carstenw/TFE4152/scoreboard.html](https://folk.ntnu.no/carstenw/TFE4152/scoreboard.html)

[https://github.com/wulffern/dic2021/blob/main/2021-10-19\_project\_report/project\_report.pdf](https://github.com/wulffern/dic2021/blob/main/2021-10-19_project_report/project_report.pdf)


---

#[fit] +

---

# Together with a partner, figure out the logic circuit for the sum of two 1-bit signals, A + B, with the sum as a 1-bit output (S) and a 1-bit carry (C) 

---
### Half adder

![inline fit](../media/l20/half_adder.pdf)


---

# Together with a partner, figure out the logic circuit for the sum of **three 1-bit signals, A, B, and carry input (Ci)** with the sum as a 1-bit output (S) and a 1-bit carry (C) 

---

### Full adder


![inline fit](../media/l20/full_adder.pdf) 

---

### Full adder

$$ S = A \oplus B \oplus Ci$$

$$ C = (A \oplus B)Ci + AB$$


![right fit](../media/l20/full_adder_block.pdf)


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

![right fit](../media/l20/adder_1bit.pdf)

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

![right fit](../media/l20/adder_2bit.pdf)

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

![right fit](../media/l20/adder_4bit.pdf)

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

![right fit](../media/l20/adder_8bit.pdf)

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

![right fit](../media/l20/adder_16bit.pdf)

---

#[fit] Straightforward adders become deep, can we make it better?

---




