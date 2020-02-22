# How to Run TRNSYS Simulations from Python
This Python script  automates the running of the TRNSYS simulations. The aim here is to ease the running of several simulations of the same model for various different parameter values as might be required for parametric analysis, sensitivity analysis etc.

## Table of Contents
- [How2Use](README.md#how2use)
- [License](README.md#license)
- [Acknowledgement](README.md#acknowledgement)

## How2Use
An example Python script is given: [ExamplePYTHONscript.py](https://github.com/DrTol/TRNSYSfromPython/blob/master/ExamplePYTHONscript.py), from which the example TRNSYS simulation [ExampleTRNSYSmodel.tpf](https://github.com/DrTol/TRNSYSfromPython/blob/master/ExampleTRNSYSmodel.tpf) is run. However, there needs some asjustments in the Python script, for that please follow these steps: 

1. "Clone or Download" this repository to the directory "C:\zGithub\" (or change the directory in the line 42 of the Python script to the directory where your TRNSYS model located)

2. In the Python script at line 42, change the directory of TRNSYS application, i.e. "C:\Trnsys17\Exe\TRNExe.exe" (How to find the directory of your TRNSYS Simulation Studio: i) File, ii) Settings, iii) Directories, and iv) Copy the directory stated for the TRNSYS Application there)

3. Then run the [ExamplePYTHONscript.py](https://github.com/DrTol/TRNSYSfromPython/blob/master/ExamplePYTHONscript.py)

4. You can see in the folder "C:\zGithub\" that automated TRNSYS output results will be saved in an order. 

The main idea behind this Python script is simple, change parameter values in the deck file (in this case: [ExampleTRNSYSmodel.dck](https://github.com/DrTol/TRNSYSfromPython/blob/master/ExampleTRNSYSmodel.dck) and ask the TRNSYS to run the simulation/s as to this deck file/s. Keep in mind that for your case you need to dublicate (copy & paste) your .dck file in order to create a template .dck file. Then, change the parameters to be changed by Python to some tag names, such as the case in [z_pyt_TEMPLATE.dck](https://github.com/DrTol/TRNSYSfromPython/blob/master/z_pyt_TEMPLATE.dck) - check the lines 98 - 101 there:

```
t_on = pyt_t_on ! [hour] starting time of high operation
t_off = pyt_t_off ! [hour] end time of high operation
s_high = pyt_s_high ! [-] control signal at high
s_low = pyt_s_low ! [-] control signal at low
```


