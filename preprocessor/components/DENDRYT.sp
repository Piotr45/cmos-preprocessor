.subckt DENDRYT inp inm outp outm A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 vss vdd

xDENDRYT_P inp outp_ A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 vss vdd DENDRYT_CORE
xDENDRYT_N inm outm_ A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 vss vdd DENDRYT_CORE
xCMRR outp_ outm_ outp outm vss vdd CMRR1

*xDENDRYT_P inp outp_ A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 vss vdd DENDRYT_CORE
*xDENDRYT_P inm outm_ A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 vss vdd DENDRYT_CORE
*xCMRR outp_ outm_ outp outm vss vdd CMRR

.ends DENDRYT

.subckt DENDRYT_CORE in out A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 vss vdd

*T = 0.5ms
*f = 2kHz
*zrodlem najwiekszego opoznienia jest wyjscie a, czyli out1

Mn0 in in vss vss nch w=0.265u l=0.06u 
Mp0 in in vdd vdd pch w=0.68u l=0.06u 

*a = 0.1108
Mna1a out_1na in vss vss nch w=0.14u l=20u 
Mpa2a out_1pa in vdd vdd pch w=12.6u l=20u 
Mna3a out1a in out_1na vss nch w=0.14u l=20u 
Mpa4a out1a in out_1pa vdd pch w=12.6u l=20u 

*b - 0.118 GOTOWY
Mnb1a out_1nb in vss vss nch w=0.14u l=15u 
Mpb2a out_1pb in vdd vdd pch w=11.15u l=15u 
Mnb3a out2a in out_1nb vss nch w=0.14u l=15u 
Mpb4a out2a in out_1pb vdd pch w=11.15u l=15u 

*c - 0.136 GOTOWY
Mnc1a out3a in vss vss nch w=0.14u l=20u 
Mpc2a out3a in vdd vdd pch w=8.7u l=20u 

*d - 0.2028 GOTOWY
Mnd1a out4a in vss vss nch w=0.14u l=7.8u 
Mpd2a out4a in vdd vdd pch w=8.25u l=7.8u 

*e - 0.3521 GOTOWY
Mne1a out5a in vss vss nch w=0.265u l=0.8u 
Mpe2a out5a in vdd vdd pch w=2.35u l=0.8u 

*f - 0.6685 GOTOWY
Mnf1a out6a in vss vss nch w=0.25u l=0.06u 
Mpf2a out6a in vdd vdd pch w=0.58u l=0.06u 

xTG1 out1a A1 outa vss vdd TG1
xTG2 out2a A2 outa vss vdd TG1
xTG3 out3a A3 outa vss vdd TG1
xTG4 out4a A4 outa vss vdd TG1
xTG5 out5a A5 outa vss vdd TG1
xTG6 out6a A6 outa vss vdd TG1
*******************************************

Mn1b outa outa vss vss nch w=0.265u l=0.06u 
Mp2b outa outa vdd vdd pch w=0.68u l=0.06u 

*a = 0.1108
Mna1b out_2na outa vss vss nch w=0.14u l=20u 
Mpa2b out_2pa outa vdd vdd pch w=12.6u l=20u 
Mna3b out1b outa out_2na vss nch w=0.14u l=20u 
Mpa4b out1b outa out_2pa vdd pch w=12.6u l=20u 

*b - 0.118 GOTOWY
Mnb1b out_2nb outa vss vss nch w=0.14u l=15u 
Mpb2b out_2pb outa vdd vdd pch w=11.15u l=15u 
Mnb3b out2b outa out_2nb vss nch w=0.14u l=15u 
Mpb4b out2b outa out_2pb vdd pch w=11.15u l=15u 

*c - 0.136 GOTOWY
Mnc1b out3b outa vss vss nch w=0.14u l=20u 
Mpc2b out3b outa vdd vdd pch w=8.7u l=20u 

*d - 0.2028 GOTOWY
Mnd1b out4b outa vss vss nch w=0.14u l=7.8u 
Mpd2b out4b outa vdd vdd pch w=8.25u l=7.8u 

*e - 0.3521 GOTOWY
Mne1b out5b outa vss vss nch w=0.265u l=0.8u 
Mpe2b out5b outa vdd vdd pch w=2.35u l=0.8u 

*f - 0.6685 GOTOWY
Mnf1b out6b outa vss vss nch w=0.25u l=0.06u 
Mpf2b out6b outa vdd vdd pch w=0.58u l=0.06u 


xTG21 out1b B1 out vss vdd TG1
xTG22 out2b B2 out vss vdd TG1
xTG23 out3b B3 out vss vdd TG1
xTG24 out4b B4 out vss vdd TG1
xTG25 out5b B5 out vss vdd TG1
xTG26 out6b B6 out vss vdd TG1

.ends DENDRYT_CORE

.subckt TG1 in clk out vss vdd
Mn1 out_1 clk in vss nch w=20u l=0.06u 
Mp2 out n_clk out_1 vdd pch w=20u l=0.06u 
Mn5 out clk out_2 vss nch w=20u l=0.06u 
Mp6 out_2 n_clk in vdd pch w=20u l=0.06u 
*Mp7 out n_clk out_ vdd pch w=20u l=0.06u 


Mn3 n_clk clk vss vss nch w=0.32u l=0.06u 
Mp4 n_clk clk vdd vdd pch w=1.18u l=0.06u
.ends TG1

.subckt CMRR1 inp inm outp outm vss vdd

xCM1a inp outm s1 vss vdd CM_1
xCM1b inm outp s1 vss vdd CM_1
xCM2 s1 outm outp vss vdd CM_2


.ends CMRR1

.subckt CM_1 in out1 out2 vss vdd
Mn0 in in vss vss nch w=0.265u l=0.835u 
Mp0 in in vdd vdd pch w=2.075u l=0.835u 
Mn1 out1 in vss vss nch w=0.58u l=0.5u 
Mp1 out1 in vdd vdd pch w=2.05u l=0.5u 
Mn2 out2 in vss vss nch w=0.58u l=0.5u 
Mp2 out2 in vdd vdd pch w=2.05u l=0.5u 
.ends CM_1

.subckt CM_2 in out1 out2 vss vdd

Mn0 in in vss vss nch w=0.465u l=0.115u 
Mp0 in in vdd vdd pch w=2.075u l=0.115u 
Mn1 out1 in vss vss nch w=0.605u l=0.5u 
Mp1 out1 in vdd vdd pch w=2.53u l=0.5u 
Mn2 out2 in vss vss nch w=0.605u l=0.5u 
Mp2 out2 in vdd vdd pch w=2.53u l=0.5u 
.ends CM_2


