#=====================================================================
youGOTOX = 15
youGOTOY = -24

yourD = 15


enemyHP             = []
enemyHPMax = list(enemyHP)
enemyX              = []
enemyY              = []
enemyD              = []
enemySpeed          = []
enemyATT            = []
enemyATTRange       = []
enemyDistanceDetect = []

stenaX        = [-194.0, -193.0, -194.0, -181.0, 1538.0, 1511.0, 3296.0, 3217.0, 3216.0, -181.0, 586.0, 467.0, -100.0, -181.0, 87.0, 88.0, -4.0, 17.0, 44.0, 60.0, 92.0, 113.0, 147.0, 171.0, 203.0, 231.0, 264.0, 304.0, 337.0, 283.0, 321.0, 363.0, 383.0, 399.0, 422.0, 446.0, 478.0, 497.0, 515.0, 526.0, 549.0, 584.0, 599.0, 620.0, 647.0, 675.0, 701.0, 716.0, -28.0, -49.0, -182.0, 1195.0, 1193.0, 1203.0, 1945.0, 1943.0, 1672.0, 1671.0, 722.0, 476.0]
stenaY        = [-59.0, -47.0, 1672.0, 3377.0, 3379.0, -60.0, -19.0, -55.0, 1661.0, 32.0, 46.0, 242.0, 243.0, 399.0, 527.0, 1060.0, 2856.0, 2883.0, 2924.0, 2947.0, 2988.0, 3018.0, 3057.0, 3088.0, 3049.0, 3006.0, 2949.0, 2857.0, 2783.0, 2910.0, 2819.0, 3087.0, 3036.0, 3006.0, 2972.0, 2922.0, 2855.0, 2810.0, 2813.0, 2841.0, 2870.0, 2907.0, 2928.0, 2964.0, 2996.0, 3032.0, 3071.0, 3088.0, 2827.0, 2790.0, 2562.0, 2607.0, 1860.0, 1871.0, 1118.0, 363.0, 366.0, 117.0, 38.0, 988.0]
stenaDX       = [1726, 21, 21, 1726, 1726, 1726, 1726, 21, 21, 790, 21, 21, 586, 550, 21, 21, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 1176, 32, 32, 779, 32, 32, 289, 53, 889, 889]
stenaDY       = [20, 1726, 1726, 21, 21, 21, 21, 1726, 1726, 21, 790, 790, 21, 21, 550, 550, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 32, 779, 779, 32, 779, 779, 53, 289, 42, 42]

smallHPSupplyX = [-84.0, -28.0, 31.0, 119.0, 198.0, 328.0, 461.0, 530.0, 629.0, 764.0, 842.0, 887.0, 841.0, 716.0, 554.0, 344.0, 185.0, 26.0, -49.0, -129.0, -140.0, -114.0, -43.0, 76.0, 145.0, 233.0, 245.0, 189.0, 111.0, 143.0, 212.0, 231.0, 273.0, 387.0, 467.0, 461.0, 408.0, 372.0, 329.0, 328.0, 482.0, 506.0, 592.0, 541.0, 591.0, 595.0, 551.0, 597.0, 643.0, 808.0, 798.0, 923.0, 971.0, 875.0, 773.0, 741.0, 651.0, 504.0, 333.0, 74.0, -117.0, -94.0, 15.0, -2.0, -36.0, 220.0, 475.0, 776.0, 941.0, 996.0, 875.0, 734.0, 579.0, 572.0, 385.0]
smallHPSupplyY = [2705.0, 2703.0, 2696.0, 2698.0, 2693.0, 2695.0, 2718.0, 2724.0, 2760.0, 2847.0, 2960.0, 3090.0, 3192.0, 3247.0, 3238.0, 3243.0, 3246.0, 3201.0, 3128.0, 2990.0, 2877.0, 2768.0, 2726.0, 2761.0, 2872.0, 2937.0, 2859.0, 2840.0, 2838.0, 2777.0, 2779.0, 2790.0, 2739.0, 2747.0, 2766.0, 2851.0, 2924.0, 3029.0, 3144.0, 3249.0, 3290.0, 3185.0, 3115.0, 3177.0, 3151.0, 3054.0, 3034.0, 3166.0, 3264.0, 3277.0, 3195.0, 3177.0, 3160.0, 3027.0, 2998.0, 2884.0, 2800.0, 2742.0, 2719.0, 2714.0, 2730.0, 2946.0, 3070.0, 3185.0, 3332.0, 3233.0, 3308.0, 3338.0, 3287.0, 3172.0, 2980.0, 2834.0, 2714.0, 2763.0, 2484.0]

backgroundX = 476.0
backgroundY = 988.0
backgroundDX = 4546.0
backgroundDY = 2412.0

NextLevelBlockX = 258.0
NextLevelBlockY = 3342.0
NextLevel = "None"
#=====================================================================
