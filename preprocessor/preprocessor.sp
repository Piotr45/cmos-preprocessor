*** PREPROCESSOR
.INCLUDE components/AXON.sp
.INCLUDE components/DENDRITE.sp
.INCLUDE components/CMRR.sp

.subckt PREPROCESSOR IN0p IN0m IN1p IN1m IN2p IN2m IN3p IN3m IN4p IN4m IN5p IN5m IN6p IN6m IN7p IN7m IN8p IN8m IN9p IN9m OUT0p OUT0m VSS VDD

xCMp_0 IN0p OUTn_n0p0 OUTn_n1p0 OUTn_n2p0 OUTn_n3p0 OUTn_n4p0 OUTn_n5p0 OUTn_n6p0 OUTn_n7p0 OUTn_n8p0 OUTn_n9p0 VSS VDD CM10
xCMm_0 IN0m OUTp_n0p0 OUTp_n1p0 OUTp_n2p0 OUTp_n3p0 OUTp_n4p0 OUTp_n5p0 OUTp_n6p0 OUTp_n7p0 OUTp_n8p0 OUTp_n9p0 VSS VDD CM10
xCMp_1 IN1p OUTn_n0p1 OUTn_n1p1 OUTn_n2p1 OUTn_n3p1 OUTn_n4p1 OUTn_n5p1 OUTn_n6p1 OUTn_n7p1 OUTn_n8p1 OUTn_n9p1 VSS VDD CM10
xCMm_1 IN1m OUTp_n0p1 OUTp_n1p1 OUTp_n2p1 OUTp_n3p1 OUTp_n4p1 OUTp_n5p1 OUTp_n6p1 OUTp_n7p1 OUTp_n8p1 OUTp_n9p1 VSS VDD CM10
xCMp_2 IN2p OUTn_n0p2 OUTn_n1p2 OUTn_n2p2 OUTn_n3p2 OUTn_n4p2 OUTn_n5p2 OUTn_n6p2 OUTn_n7p2 OUTn_n8p2 OUTn_n9p2 VSS VDD CM10
xCMm_2 IN2m OUTp_n0p2 OUTp_n1p2 OUTp_n2p2 OUTp_n3p2 OUTp_n4p2 OUTp_n5p2 OUTp_n6p2 OUTp_n7p2 OUTp_n8p2 OUTp_n9p2 VSS VDD CM10
xCMp_3 IN3p OUTn_n0p3 OUTn_n1p3 OUTn_n2p3 OUTn_n3p3 OUTn_n4p3 OUTn_n5p3 OUTn_n6p3 OUTn_n7p3 OUTn_n8p3 OUTn_n9p3 VSS VDD CM10
xCMm_3 IN3m OUTp_n0p3 OUTp_n1p3 OUTp_n2p3 OUTp_n3p3 OUTp_n4p3 OUTp_n5p3 OUTp_n6p3 OUTp_n7p3 OUTp_n8p3 OUTp_n9p3 VSS VDD CM10
xCMp_4 IN4p OUTn_n0p4 OUTn_n1p4 OUTn_n2p4 OUTn_n3p4 OUTn_n4p4 OUTn_n5p4 OUTn_n6p4 OUTn_n7p4 OUTn_n8p4 OUTn_n9p4 VSS VDD CM10
xCMm_4 IN4m OUTp_n0p4 OUTp_n1p4 OUTp_n2p4 OUTp_n3p4 OUTp_n4p4 OUTp_n5p4 OUTp_n6p4 OUTp_n7p4 OUTp_n8p4 OUTp_n9p4 VSS VDD CM10
xCMp_5 IN5p OUTn_n0p5 OUTn_n1p5 OUTn_n2p5 OUTn_n3p5 OUTn_n4p5 OUTn_n5p5 OUTn_n6p5 OUTn_n7p5 OUTn_n8p5 OUTn_n9p5 VSS VDD CM10
xCMm_5 IN5m OUTp_n0p5 OUTp_n1p5 OUTp_n2p5 OUTp_n3p5 OUTp_n4p5 OUTp_n5p5 OUTp_n6p5 OUTp_n7p5 OUTp_n8p5 OUTp_n9p5 VSS VDD CM10
xCMp_6 IN6p OUTn_n0p6 OUTn_n1p6 OUTn_n2p6 OUTn_n3p6 OUTn_n4p6 OUTn_n5p6 OUTn_n6p6 OUTn_n7p6 OUTn_n8p6 OUTn_n9p6 VSS VDD CM10
xCMm_6 IN6m OUTp_n0p6 OUTp_n1p6 OUTp_n2p6 OUTp_n3p6 OUTp_n4p6 OUTp_n5p6 OUTp_n6p6 OUTp_n7p6 OUTp_n8p6 OUTp_n9p6 VSS VDD CM10
xCMp_7 IN7p OUTn_n0p7 OUTn_n1p7 OUTn_n2p7 OUTn_n3p7 OUTn_n4p7 OUTn_n5p7 OUTn_n6p7 OUTn_n7p7 OUTn_n8p7 OUTn_n9p7 VSS VDD CM10
xCMm_7 IN7m OUTp_n0p7 OUTp_n1p7 OUTp_n2p7 OUTp_n3p7 OUTp_n4p7 OUTp_n5p7 OUTp_n6p7 OUTp_n7p7 OUTp_n8p7 OUTp_n9p7 VSS VDD CM10
xCMp_8 IN8p OUTn_n0p8 OUTn_n1p8 OUTn_n2p8 OUTn_n3p8 OUTn_n4p8 OUTn_n5p8 OUTn_n6p8 OUTn_n7p8 OUTn_n8p8 OUTn_n9p8 VSS VDD CM10
xCMm_8 IN8m OUTp_n0p8 OUTp_n1p8 OUTp_n2p8 OUTp_n3p8 OUTp_n4p8 OUTp_n5p8 OUTp_n6p8 OUTp_n7p8 OUTp_n8p8 OUTp_n9p8 VSS VDD CM10
xCMp_9 IN9p OUTn_n0p9 OUTn_n1p9 OUTn_n2p9 OUTn_n3p9 OUTn_n4p9 OUTn_n5p9 OUTn_n6p9 OUTn_n7p9 OUTn_n8p9 OUTn_n9p9 VSS VDD CM10
xCMm_9 IN9m OUTp_n0p9 OUTp_n1p9 OUTp_n2p9 OUTp_n3p9 OUTp_n4p9 OUTp_n5p9 OUTp_n6p9 OUTp_n7p9 OUTp_n8p9 OUTp_n9p9 VSS VDD CM10

xDENDRYTw0n0d0 OUTn_n0p0 OUTp_n0p0 OUTmw0_n0 OUTpw0_n0 VSS VSS VDD VSS VSS VDD VDD VSS VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n0d1 OUTn_n0p1 OUTp_n0p1 OUTmw0_n0 OUTpw0_n0 VSS VSS VSS VSS VDD VDD VDD VSS VSS VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n0d2 OUTn_n0p2 OUTp_n0p2 OUTmw0_n0 OUTpw0_n0 VDD VSS VDD VDD VDD VSS VSS VSS VSS VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n0d3 OUTn_n0p3 OUTp_n0p3 OUTmw0_n0 OUTpw0_n0 VSS VSS VSS VDD VSS VSS VSS VSS VSS VSS VSS VDD VSS VDD DENDRYT
xDENDRYTw0n0d4 OUTn_n0p4 OUTp_n0p4 OUTmw0_n0 OUTpw0_n0 VDD VDD VDD VSS VDD VSS VSS VSS VSS VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n0d5 OUTn_n0p5 OUTp_n0p5 OUTmw0_n0 OUTpw0_n0 VSS VSS VDD VSS VDD VDD VSS VDD VDD VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n0d6 OUTn_n0p6 OUTp_n0p6 OUTmw0_n0 OUTpw0_n0 VSS VDD VDD VSS VDD VSS VDD VDD VSS VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n0d7 OUTn_n0p7 OUTp_n0p7 OUTmw0_n0 OUTpw0_n0 VSS VSS VDD VDD VDD VDD VDD VSS VSS VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n0d8 OUTn_n0p8 OUTp_n0p8 OUTmw0_n0 OUTpw0_n0 VSS VSS VDD VDD VSS VDD VSS VDD VDD VDD VSS VDD VSS VDD DENDRYT
xDENDRYTw0n0d9 OUTp_n0p9 OUTn_n0p9 OUTmw0_n0 OUTpw0_n0 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT

xDENDRYTw0n1d0 OUTn_n1p0 OUTp_n1p0 OUTmw0_n1 OUTpw0_n1 VSS VDD VSS VDD VSS VDD VDD VSS VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n1d1 OUTn_n1p1 OUTp_n1p1 OUTmw0_n1 OUTpw0_n1 VDD VSS VDD VDD VDD VSS VSS VSS VDD VSS VSS VDD VSS VDD DENDRYT
xDENDRYTw0n1d2 OUTp_n1p2 OUTn_n1p2 OUTmw0_n1 OUTpw0_n1 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n1d3 OUTp_n1p3 OUTn_n1p3 OUTmw0_n1 OUTpw0_n1 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n1d4 OUTn_n1p4 OUTp_n1p4 OUTmw0_n1 OUTpw0_n1 VSS VSS VSS VSS VDD VSS VDD VSS VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n1d5 OUTn_n1p5 OUTp_n1p5 OUTmw0_n1 OUTpw0_n1 VDD VDD VSS VSS VDD VSS VSS VSS VDD VDD VDD VSS VSS VDD DENDRYT
xDENDRYTw0n1d6 OUTn_n1p6 OUTp_n1p6 OUTmw0_n1 OUTpw0_n1 VSS VDD VDD VSS VDD VSS VSS VDD VDD VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n1d7 OUTp_n1p7 OUTn_n1p7 OUTmw0_n1 OUTpw0_n1 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n1d8 OUTn_n1p8 OUTp_n1p8 OUTmw0_n1 OUTpw0_n1 VSS VDD VDD VSS VSS VSS VSS VDD VSS VDD VDD VSS VSS VDD DENDRYT
xDENDRYTw0n1d9 OUTn_n1p9 OUTp_n1p9 OUTmw0_n1 OUTpw0_n1 VDD VSS VSS VSS VSS VSS VSS VSS VDD VSS VSS VDD VSS VDD DENDRYT

xDENDRYTw0n2d0 OUTp_n2p0 OUTn_n2p0 OUTmw0_n2 OUTpw0_n2 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n2d1 OUTn_n2p1 OUTp_n2p1 OUTmw0_n2 OUTpw0_n2 VDD VSS VDD VDD VDD VDD VSS VDD VSS VDD VSS VDD VSS VDD DENDRYT
xDENDRYTw0n2d2 OUTn_n2p2 OUTp_n2p2 OUTmw0_n2 OUTpw0_n2 VSS VDD VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VDD DENDRYT
xDENDRYTw0n2d3 OUTp_n2p3 OUTn_n2p3 OUTmw0_n2 OUTpw0_n2 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n2d4 OUTn_n2p4 OUTp_n2p4 OUTmw0_n2 OUTpw0_n2 VDD VSS VSS VDD VSS VSS VDD VSS VSS VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n2d5 OUTn_n2p5 OUTp_n2p5 OUTmw0_n2 OUTpw0_n2 VSS VSS VSS VSS VDD VDD VSS VSS VDD VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n2d6 OUTn_n2p6 OUTp_n2p6 OUTmw0_n2 OUTpw0_n2 VSS VSS VDD VDD VSS VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n2d7 OUTp_n2p7 OUTn_n2p7 OUTmw0_n2 OUTpw0_n2 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n2d8 OUTp_n2p8 OUTn_n2p8 OUTmw0_n2 OUTpw0_n2 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n2d9 OUTp_n2p9 OUTn_n2p9 OUTmw0_n2 OUTpw0_n2 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT

xDENDRYTw0n3d0 OUTn_n3p0 OUTp_n3p0 OUTmw0_n3 OUTpw0_n3 VSS VSS VDD VDD VDD VDD VSS VDD VDD VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n3d1 OUTn_n3p1 OUTp_n3p1 OUTmw0_n3 OUTpw0_n3 VSS VSS VDD VDD VSS VSS VDD VDD VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n3d2 OUTn_n3p2 OUTp_n3p2 OUTmw0_n3 OUTpw0_n3 VDD VSS VSS VDD VDD VSS VSS VDD VSS VDD VSS VDD VSS VDD DENDRYT
xDENDRYTw0n3d3 OUTn_n3p3 OUTp_n3p3 OUTmw0_n3 OUTpw0_n3 VSS VSS VSS VDD VSS VSS VSS VDD VSS VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n3d4 OUTn_n3p4 OUTp_n3p4 OUTmw0_n3 OUTpw0_n3 VSS VDD VSS VSS VSS VDD VDD VDD VDD VSS VSS VDD VSS VDD DENDRYT
xDENDRYTw0n3d5 OUTn_n3p5 OUTp_n3p5 OUTmw0_n3 OUTpw0_n3 VDD VDD VSS VDD VSS VSS VSS VSS VDD VDD VDD VSS VSS VDD DENDRYT
xDENDRYTw0n3d6 OUTn_n3p6 OUTp_n3p6 OUTmw0_n3 OUTpw0_n3 VSS VSS VSS VSS VSS VSS VSS VSS VSS VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n3d7 OUTn_n3p7 OUTp_n3p7 OUTmw0_n3 OUTpw0_n3 VDD VDD VDD VSS VSS VDD VSS VSS VDD VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n3d8 OUTn_n3p8 OUTp_n3p8 OUTmw0_n3 OUTpw0_n3 VSS VDD VSS VDD VSS VDD VSS VSS VSS VSS VSS VDD VSS VDD DENDRYT
xDENDRYTw0n3d9 OUTp_n3p9 OUTn_n3p9 OUTmw0_n3 OUTpw0_n3 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT

xDENDRYTw0n4d0 OUTn_n4p0 OUTp_n4p0 OUTmw0_n4 OUTpw0_n4 VDD VDD VDD VDD VSS VDD VSS VDD VSS VDD VDD VSS VSS VDD DENDRYT
xDENDRYTw0n4d1 OUTp_n4p1 OUTn_n4p1 OUTmw0_n4 OUTpw0_n4 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n4d2 OUTp_n4p2 OUTn_n4p2 OUTmw0_n4 OUTpw0_n4 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n4d3 OUTn_n4p3 OUTp_n4p3 OUTmw0_n4 OUTpw0_n4 VDD VSS VSS VSS VSS VSS VSS VSS VDD VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n4d4 OUTn_n4p4 OUTp_n4p4 OUTmw0_n4 OUTpw0_n4 VSS VDD VSS VSS VDD VDD VSS VDD VDD VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n4d5 OUTn_n4p5 OUTp_n4p5 OUTmw0_n4 OUTpw0_n4 VDD VDD VDD VDD VDD VSS VSS VSS VDD VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n4d6 OUTp_n4p6 OUTn_n4p6 OUTmw0_n4 OUTpw0_n4 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n4d7 OUTp_n4p7 OUTn_n4p7 OUTmw0_n4 OUTpw0_n4 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n4d8 OUTn_n4p8 OUTp_n4p8 OUTmw0_n4 OUTpw0_n4 VSS VDD VSS VSS VDD VSS VSS VSS VDD VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n4d9 OUTn_n4p9 OUTp_n4p9 OUTmw0_n4 OUTpw0_n4 VSS VSS VDD VSS VDD VDD VSS VSS VDD VSS VSS VSS VSS VDD DENDRYT

xDENDRYTw0n5d0 OUTp_n5p0 OUTn_n5p0 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n5d1 OUTp_n5p1 OUTn_n5p1 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n5d2 OUTn_n5p2 OUTp_n5p2 OUTmw0_n5 OUTpw0_n5 VDD VSS VSS VSS VSS VDD VDD VSS VSS VSS VSS VDD VSS VDD DENDRYT
xDENDRYTw0n5d3 OUTp_n5p3 OUTn_n5p3 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n5d4 OUTp_n5p4 OUTn_n5p4 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n5d5 OUTn_n5p5 OUTp_n5p5 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VDD VDD VDD VDD VDD VSS VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n5d6 OUTp_n5p6 OUTn_n5p6 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n5d7 OUTp_n5p7 OUTn_n5p7 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n5d8 OUTn_n5p8 OUTp_n5p8 OUTmw0_n5 OUTpw0_n5 VSS VDD VSS VDD VDD VSS VDD VDD VDD VSS VSS VSS VSS VDD DENDRYT
xDENDRYTw0n5d9 OUTp_n5p9 OUTn_n5p9 OUTmw0_n5 OUTpw0_n5 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT

xDENDRYTw0n6d0 OUTp_n6p0 OUTn_n6p0 OUTmw0_n6 OUTpw0_n6 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n6d1 OUTn_n6p1 OUTp_n6p1 OUTmw0_n6 OUTpw0_n6 VSS VSS VDD VDD VDD VDD VSS VSS VDD VSS VSS VSS VSS VDD DENDRYT
xDENDRYTw0n6d2 OUTp_n6p2 OUTn_n6p2 OUTmw0_n6 OUTpw0_n6 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n6d3 OUTn_n6p3 OUTp_n6p3 OUTmw0_n6 OUTpw0_n6 VSS VDD VSS VSS VDD VSS VDD VSS VSS VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n6d4 OUTn_n6p4 OUTp_n6p4 OUTmw0_n6 OUTpw0_n6 VSS VSS VDD VDD VSS VSS VDD VDD VSS VSS VSS VDD VSS VDD DENDRYT
xDENDRYTw0n6d5 OUTp_n6p5 OUTn_n6p5 OUTmw0_n6 OUTpw0_n6 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n6d6 OUTp_n6p6 OUTn_n6p6 OUTmw0_n6 OUTpw0_n6 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n6d7 OUTp_n6p7 OUTn_n6p7 OUTmw0_n6 OUTpw0_n6 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n6d8 OUTp_n6p8 OUTn_n6p8 OUTmw0_n6 OUTpw0_n6 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n6d9 OUTn_n6p9 OUTp_n6p9 OUTmw0_n6 OUTpw0_n6 VDD VDD VSS VSS VDD VDD VSS VSS VDD VSS VSS VSS VSS VDD DENDRYT

xDENDRYTw0n7d0 OUTp_n7p0 OUTn_n7p0 OUTmw0_n7 OUTpw0_n7 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n7d1 OUTn_n7p1 OUTp_n7p1 OUTmw0_n7 OUTpw0_n7 VDD VSS VDD VDD VDD VDD VSS VDD VSS VDD VDD VSS VSS VDD DENDRYT
xDENDRYTw0n7d2 OUTp_n7p2 OUTn_n7p2 OUTmw0_n7 OUTpw0_n7 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n7d3 OUTn_n7p3 OUTp_n7p3 OUTmw0_n7 OUTpw0_n7 VSS VSS VSS VDD VSS VSS VDD VSS VSS VDD VSS VDD VSS VDD DENDRYT
xDENDRYTw0n7d4 OUTp_n7p4 OUTn_n7p4 OUTmw0_n7 OUTpw0_n7 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n7d5 OUTn_n7p5 OUTp_n7p5 OUTmw0_n7 OUTpw0_n7 VDD VSS VDD VDD VDD VSS VSS VDD VDD VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n7d6 OUTp_n7p6 OUTn_n7p6 OUTmw0_n7 OUTpw0_n7 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n7d7 OUTn_n7p7 OUTp_n7p7 OUTmw0_n7 OUTpw0_n7 VSS VSS VDD VSS VSS VDD VSS VSS VSS VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n7d8 OUTp_n7p8 OUTn_n7p8 OUTmw0_n7 OUTpw0_n7 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n7d9 OUTn_n7p9 OUTp_n7p9 OUTmw0_n7 OUTpw0_n7 VSS VDD VSS VDD VDD VDD VSS VDD VDD VDD VSS VSS VSS VDD DENDRYT

xDENDRYTw0n8d0 OUTn_n8p0 OUTp_n8p0 OUTmw0_n8 OUTpw0_n8 VSS VSS VDD VSS VDD VDD VDD VDD VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n8d1 OUTp_n8p1 OUTn_n8p1 OUTmw0_n8 OUTpw0_n8 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n8d2 OUTn_n8p2 OUTp_n8p2 OUTmw0_n8 OUTpw0_n8 VDD VDD VSS VDD VDD VSS VSS VDD VSS VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n8d3 OUTp_n8p3 OUTn_n8p3 OUTmw0_n8 OUTpw0_n8 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n8d4 OUTp_n8p4 OUTn_n8p4 OUTmw0_n8 OUTpw0_n8 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n8d5 OUTn_n8p5 OUTp_n8p5 OUTmw0_n8 OUTpw0_n8 VSS VSS VSS VDD VDD VDD VSS VSS VDD VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n8d6 OUTn_n8p6 OUTp_n8p6 OUTmw0_n8 OUTpw0_n8 VSS VDD VSS VSS VSS VSS VDD VSS VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n8d7 OUTn_n8p7 OUTp_n8p7 OUTmw0_n8 OUTpw0_n8 VSS VDD VSS VDD VDD VDD VDD VSS VSS VSS VDD VDD VSS VDD DENDRYT
xDENDRYTw0n8d8 OUTn_n8p8 OUTp_n8p8 OUTmw0_n8 OUTpw0_n8 VDD VSS VSS VSS VDD VSS VSS VDD VSS VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n8d9 OUTp_n8p9 OUTn_n8p9 OUTmw0_n8 OUTpw0_n8 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT

xDENDRYTw0n9d0 OUTn_n9p0 OUTp_n9p0 OUTmw0_n9 OUTpw0_n9 VSS VSS VDD VSS VSS VDD VSS VDD VDD VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw0n9d1 OUTn_n9p1 OUTp_n9p1 OUTmw0_n9 OUTpw0_n9 VSS VDD VDD VSS VDD VSS VDD VSS VSS VSS VSS VSS VSS VDD DENDRYT
xDENDRYTw0n9d2 OUTp_n9p2 OUTn_n9p2 OUTmw0_n9 OUTpw0_n9 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n9d3 OUTn_n9p3 OUTp_n9p3 OUTmw0_n9 OUTpw0_n9 VDD VDD VSS VDD VSS VSS VSS VSS VDD VSS VSS VSS VSS VDD DENDRYT
xDENDRYTw0n9d4 OUTp_n9p4 OUTn_n9p4 OUTmw0_n9 OUTpw0_n9 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n9d5 OUTp_n9p5 OUTn_n9p5 OUTmw0_n9 OUTpw0_n9 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n9d6 OUTp_n9p6 OUTn_n9p6 OUTmw0_n9 OUTpw0_n9 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n9d7 OUTn_n9p7 OUTp_n9p7 OUTmw0_n9 OUTpw0_n9 VSS VSS VDD VDD VSS VDD VDD VSS VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw0n9d8 OUTp_n9p8 OUTn_n9p8 OUTmw0_n9 OUTpw0_n9 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw0n9d9 OUTp_n9p9 OUTn_n9p9 OUTmw0_n9 OUTpw0_n9 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT

xAKSONw0n0 OUTpw0_n0 OUTmw0_n0 OUTp_w0n0 OUTm_w0n0 VSS VDD AKSON
xAKSONw0n1 OUTpw0_n1 OUTmw0_n1 OUTp_w0n1 OUTm_w0n1 VSS VDD AKSON
xAKSONw0n2 OUTpw0_n2 OUTmw0_n2 OUTp_w0n2 OUTm_w0n2 VSS VDD AKSON
xAKSONw0n3 OUTpw0_n3 OUTmw0_n3 OUTp_w0n3 OUTm_w0n3 VSS VDD AKSON
xAKSONw0n4 OUTpw0_n4 OUTmw0_n4 OUTp_w0n4 OUTm_w0n4 VSS VDD AKSON
xAKSONw0n5 OUTpw0_n5 OUTmw0_n5 OUTp_w0n5 OUTm_w0n5 VSS VDD AKSON
xAKSONw0n6 OUTpw0_n6 OUTmw0_n6 OUTp_w0n6 OUTm_w0n6 VSS VDD AKSON
xAKSONw0n7 OUTpw0_n7 OUTmw0_n7 OUTp_w0n7 OUTm_w0n7 VSS VDD AKSON
xAKSONw0n8 OUTpw0_n8 OUTmw0_n8 OUTp_w0n8 OUTm_w0n8 VSS VDD AKSON
xAKSONw0n9 OUTpw0_n9 OUTmw0_n9 OUTp_w0n9 OUTm_w0n9 VSS VDD AKSON

xCMRRw0n0 OUTp_w0n0 OUTm_w0n0 INw2p_n1p0 INw2m_n1p0 VSS VDD CMRR
xCMRRw0n1 OUTp_w0n1 OUTm_w0n1 INw2p_n1p1 INw2m_n1p1 VSS VDD CMRR
xCMRRw0n2 OUTp_w0n2 OUTm_w0n2 INw2p_n1p2 INw2m_n1p2 VSS VDD CMRR
xCMRRw0n3 OUTp_w0n3 OUTm_w0n3 INw2p_n1p3 INw2m_n1p3 VSS VDD CMRR
xCMRRw0n4 OUTp_w0n4 OUTm_w0n4 INw2p_n1p4 INw2m_n1p4 VSS VDD CMRR
xCMRRw0n5 OUTp_w0n5 OUTm_w0n5 INw2p_n1p5 INw2m_n1p5 VSS VDD CMRR
xCMRRw0n6 OUTp_w0n6 OUTm_w0n6 INw2p_n1p6 INw2m_n1p6 VSS VDD CMRR
xCMRRw0n7 OUTp_w0n7 OUTm_w0n7 INw2p_n1p7 INw2m_n1p7 VSS VDD CMRR
xCMRRw0n8 OUTp_w0n8 OUTm_w0n8 INw2p_n1p8 INw2m_n1p8 VSS VDD CMRR
xCMRRw0n9 OUTp_w0n9 OUTm_w0n9 INw2p_n1p9 INw2m_n1p9 VSS VDD CMRR

xDENDRYTw1n0d0 INw2m_n1p0 INw2p_n1p0 OUTmw1_n0 OUTpw1_n0 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw1n0d1 INw2m_n1p1 INw2p_n1p1 OUTmw1_n0 OUTpw1_n0 VSS VSS VSS VSS VSS VDD VSS VDD VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw1n0d2 INw2m_n1p2 INw2p_n1p2 OUTmw1_n0 OUTpw1_n0 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw1n0d3 INw2m_n1p3 INw2p_n1p3 OUTmw1_n0 OUTpw1_n0 VDD VDD VDD VSS VSS VSS VSS VSS VSS VDD VSS VSS VSS VDD DENDRYT
xDENDRYTw1n0d4 INw2m_n1p4 INw2p_n1p4 OUTmw1_n0 OUTpw1_n0 VSS VDD VDD VSS VSS VSS VSS VDD VSS VSS VSS VDD VSS VDD DENDRYT
xDENDRYTw1n0d5 INw2m_n1p5 INw2p_n1p5 OUTmw1_n0 OUTpw1_n0 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw1n0d6 INw2m_n1p6 INw2p_n1p6 OUTmw1_n0 OUTpw1_n0 VDD VSS VSS VSS VDD VSS VSS VSS VDD VSS VDD VSS VSS VDD DENDRYT
xDENDRYTw1n0d7 INw2m_n1p7 INw2p_n1p7 OUTmw1_n0 OUTpw1_n0 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT
xDENDRYTw1n0d8 INw2m_n1p8 INw2p_n1p8 OUTmw1_n0 OUTpw1_n0 VDD VDD VDD VSS VDD VDD VSS VDD VDD VDD VSS VDD VSS VDD DENDRYT
xDENDRYTw1n0d9 INw2m_n1p9 INw2p_n1p9 OUTmw1_n0 OUTpw1_n0 VSS VSS VSS VSS VDD VSS VDD VDD VDD VDD VDD VDD VSS VDD DENDRYT

xAKSONw1n0 OUTpw1_n0 OUTmw1_n0 OUTp_w1n0 OUTm_w1n0 VSS VDD AKSON

xCMRRw1n0 OUTp_w1n0 OUTm_w1n0 OUT0p OUT0m VSS VDD CMRR

.ends PREPROCESSOR

.subckt CM10 IN OUT1 OUT2 OUT3 OUT4 OUT5 OUT6 OUT7 OUT8 OUT9 OUT10 VSS VDDMn0 IN IN VSS VSS NCH W=0.265u L=0.835u
Mp0 IN IN VDD VDD PCH W=2.075u L=0.835uMn1 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp1 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn2 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp2 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn3 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp3 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn4 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp4 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn5 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp5 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn6 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp6 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn7 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp7 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn8 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp8 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn9 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp9 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
Mn10 OUT1 IN VSS VSS NCH w=0.58u l=0.5u
Mp10 OUT1 IN VDD VDD PCH w=2.05u l=0.5u
.ends CM10