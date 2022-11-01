.subckt CMRR inp inm outp outm vss vdd

xCM1a inp outm s1 vss vdd CM1
xCM1b inm outp s1 vss vdd CM1
xCM2 s1 outm outp vss vdd CM2


.ends CMRR

.subckt CM1 in out1 out2 vss vdd
Mn0 in in vss vss nch w=0.265u l=0.835u 
Mp0 in in vdd vdd pch w=2.075u l=0.835u 
Mn1 out1 in vss vss nch w=0.58u l=0.5u 
Mp1 out1 in vdd vdd pch w=2.05u l=0.5u 
Mn2 out2 in vss vss nch w=0.58u l=0.5u 
Mp2 out2 in vdd vdd pch w=2.05u l=0.5u 
.ends CM1

.subckt CM2 in out1 out2 vss vdd

Mn0 in in vss vss nch w=0.465u l=0.115u 
Mp0 in in vdd vdd pch w=2.075u l=0.115u 
Mn1 out1 in vss vss nch w=0.605u l=0.5u 
Mp1 out1 in vdd vdd pch w=2.53u l=0.5u 
Mn2 out2 in vss vss nch w=0.605u l=0.5u 
Mp2 out2 in vdd vdd pch w=2.53u l=0.5u 
.ends CM2