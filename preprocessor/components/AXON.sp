.subckt AXON inp inm outp outm vss vdd

*INP
*zwierciadlo
Mn0a inp inp vss vss nch w=0.265u l=5.535u 
Mp0a inp inp vdd vdd pch w=2.075u l=5.535u 
Mn4a outp1 inp vss vss nch w=0.14u l=0.5u 
Mp4a outp1 inp vdd vdd pch w=0.43u l=0.5u 

*inwerter wyjsciowy
Mn6a outp_n outp1 vss vss nch w=0.14u l=14.4u
Mp7a outp_p outp1 vdd vdd pch w=5.7u l=14.4u
Mn8a outp outp1 outp_n vss nch w=0.14u l=14.4u
Mp9a outp outp1 outp_p vdd pch w=5.7u l=14.4u

*INM
Mn0b inm inm vss vss nch w=0.265u l=5.535u 
Mp0b inm inm vdd vdd pch w=2.075u l=5.535u 
Mn4b outm1 inm vss vss nch w=0.14u l=0.5u 
Mp4b outm1 inm vdd vdd pch w=0.43u l=0.5u 

*inwerter wyjsciowy
Mn6b outm_n outm1 vss vss nch w=0.14u l=14.4u
Mp7b outm_p outm1 vdd vdd pch w=5.7u l=14.4u
Mn8b outm outm1 outm_n vss nch w=0.14u l=14.4u
Mp9b outm outm1 outm_p vdd pch w=5.7u l=14.4u
.ends AXON
