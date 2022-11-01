***Dendrite simulation***
.lib 'crn65lp_v1d3.eldo' TT

.OPTION measfile=1 post=1

.inc '../components/DENDRITE.sp'
.inc '../components/DIODE.SP'
.param per=1000u

VSOURCE_P vin_p 0 0.3v 
VSOURCE_M vin_m 0 0.0v 
VPOWER VDD 0 0.3v
R_p vin_p IN_P 115000k
R_n vin_m IN_M 115000k

*XAKSON1 in out1 0.0 VDD MODEL_AKSONU
XDENDRITE IN_P IN_M OUT_P OUT_M W_a1 W_a2 W_a3 W_a4 W_a5 W_a6 W_b1 W_b2 W_b3 W_b4 W_b5 W_b6 0 VDD DENDRITE
XDIODEP DOUT_P 0 vdd DIODE
XDIODEM DOUT_M 0 vdd DIODE
*XDIODE1 oout2 0 vdd DIODA
*XDIODE1 oout3 0 vdd DIODA
Voutp OUT_P DOUT_P 0 
Voutm OUT_M DOUT_M 0 
*Vout3 out3 oout3 0 dc 0

VCP_a1 W_a1 0 DC 0 PULSE(0.3 0 'per/2' 1u 1u 'per/2-1u' 'per') AC 1 0
VCP_a2 W_a2 0 DC 0 PULSE(0.3 0 'per*2/2' 1u 1u 'per*2/2-1u' 'per*2') AC 1 0
VCP_a3 W_a3 0 DC 0 PULSE(0.3 0 'per*4/2' 1u 1u 'per*4/2-1u' 'per*4') AC 1 0
VCP_a4 W_a4 0 DC 0 PULSE(0.3 0 'per*8/2' 1u 1u 'per*8/2-1u' 'per*8') AC 1 0
VCP_a5 W_a5 0 DC 0 PULSE(0.3 0 'per*16/2' 1u 1u 'per*16/2-1u' 'per*16') AC 1 0
VCP_a6 W_a6 0 DC 0 PULSE(0.3 0 'per*32/2' 1u 1u 'per*32/2-1u' 'per*32') AC 1 0
VCP_b1 W_b1 0 DC 0 PULSE(0.3 0 'per*64/2' 1u 1u 'per*64/2-1u' 'per*64') AC 1 0
VCP_b2 W_b2 0 DC 0 PULSE(0.3 0 'per*128/2' 1u 1u 'per*128/2-1u' 'per*128') AC 1 0
VCP_b3 W_b3 0 DC 0 PULSE(0.3 0 'per*256/2' 1u 1u 'per*256/2-1u' 'per*256') AC 1 0
VCP_b4 W_b4 0 DC 0 PULSE(0.3 0 'per*512/2' 1u 1u 'per*512/2-1u' 'per*512') AC 1 0
VCP_b5 W_b5 0 DC 0 PULSE(0.3 0 'per*1024/2' 1u 1u 'per*1024/2-1u' 'per*1024') AC 1 0
VCP_b6 W_b6 0 DC 0 PULSE(0.3 0 'per*2048/2' 1u 1u 'per*2048/2-1u' 'per*2048') AC 1 0

.OPTIONS post
.tran 1u 'per*2048'
.printfile tran I(Voutp) file=m_samples.txt step='per/2'
.printfile tran I(Voutm) file=p_samples.txt step='per/2'
*n*n*n*n*n*n*n*n
