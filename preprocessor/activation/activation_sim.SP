***axon simulation***simulation
.lib 'crn65lp_v1d3.eldo' TT

.OPTION measfile=1 post=1
.param vina='0.3v'

.inc '../components/AXON.sp'
.inc '../components/DIODE.sp'

ISOURCE1 in1 0 vina
ISOURCE2 in2 0 '-vina'
VPOWER VDD 0 0.3v
*R1 vin1 in1 70000k
*R2 vin2 in2 70000k

XAXON1 in1 in2 out1 out2 0.0 VDD AXON
XDIODE1 oout1 0 vdd DIODE
XDIODE2 oout2 0 vdd DIODE
*XDIODE1 oout2 0 vdd DIODE
*XDIODE1 oout3 0 vdd DIODE
Vout1 oout1 out1 0
Vout2 oout2 out2 0
*Vout2 out2 oout2 0 dc 0
*Vout3 out3 oout3 0 dc 0

.OPTIONS post
.step param vina -1n 1n 0.001n
.dc 
.PLOT DC I(ISOURCE1) I(ISOURCE2) I(Vout1) I(Vout2) I(ISOURCE1) I(ISOURCE2)
.printfile dc I(ISOURCE1) I(ISOURCE2) I(Vout1) I(Vout2) file=currents.txt
