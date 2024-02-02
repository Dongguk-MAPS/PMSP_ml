def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B_Avg, obj[2]: STime_A_VS_B_Avg_Diff, obj[3]: STime_A_VS_B_Min, obj[4]: STime_A_VS_B_Min_Diff, obj[5]: STime_A_VS_B_Max, obj[6]: STime_A_VS_B_Max_Diff, obj[7]: PTime_A_VS_B_Avg, obj[8]: PTime_A_VS_B_Avg_Diff, obj[9]: PTime_A_VS_B_Min, obj[10]: PTime_A_VS_B_Min_Diff, obj[11]: PTime_A_VS_B_Max, obj[12]: PTime_A_VS_B_Max_Diff, obj[13]: Due_A_VS_B, obj[14]: Due_A_VS_B_Diff
   # {"feature": "STime_A_VS_B_Avg", "instances": 2738, "metric_value": 3.1733, "depth": 1}
   if obj[1] == '>':
      # {"feature": "NumWaitingJob", "instances": 1650, "metric_value": 4.3711, "depth": 2}
      if obj[0]<=12:
         # {"feature": "STime_A_VS_B_Min_Diff", "instances": 944, "metric_value": 2.3508, "depth": 3}
         if obj[4]<=32.49084748344646:
            # {"feature": "Due_A_VS_B_Diff", "instances": 768, "metric_value": 0.9257, "depth": 4}
            if obj[14]<=87.19317593302394:
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 647, "metric_value": 0.3082, "depth": 5}
               if obj[6]>-3.776496248986316:
                  # {"feature": "STime_A_VS_B_Min", "instances": 539, "metric_value": 0.4088, "depth": 6}
                  if obj[3] == '>':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 315, "metric_value": 0.5277, "depth": 7}
                     if obj[8]<=8.570686115128256:
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 265, "metric_value": 0.4935, "depth": 8}
                        if obj[2]<=36.76917555350233:
                           # {"feature": "PTime_A_VS_B_Min", "instances": 256, "metric_value": 0.5148, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "PTime_A_VS_B_Avg", "instances": 134, "metric_value": 0.4513, "depth": 10}
                              if obj[7] == '<':
                                 return 78.97169811320755
                              elif obj[7] == '>':
                                 return 84.33333333333333
                              elif obj[7] == '=':
                                 return 33
                              else:
                                 return 79.7089552238806
                           elif obj[9] == '>':
                              # {"feature": "Due_A_VS_B", "instances": 110, "metric_value": 0.45, "depth": 10}
                              if obj[13] == '>':
                                 return 88.19117647058823
                              elif obj[13] == '<':
                                 return 80.7
                              elif obj[13] == '=':
                                 return 65.0
                              else:
                                 return 85.04545454545455
                           elif obj[9] == '=':
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 12, "metric_value": 5.3302, "depth": 10}
                              if obj[12]<=1:
                                 return 91.0
                              elif obj[12]>1:
                                 return 126.33333333333333
                              else:
                                 return 108.66666666666667
                           else:
                              return 83.359375
                        elif obj[2]>36.76917555350233:
                           # {"feature": "Due_A_VS_B", "instances": 9, "metric_value": 15.4876, "depth": 9}
                           if obj[13] == '>':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 7, "metric_value": 25.5053, "depth": 10}
                              if obj[10]>-5:
                                 return 166.75
                              elif obj[10]<=-5:
                                 return 89.66666666666667
                              else:
                                 return 133.71428571428572
                           elif obj[13] == '<':
                              return 55.5
                           else:
                              return 116.33333333333333
                        else:
                           return 84.47924528301887
                     elif obj[8]>8.570686115128256:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 50, "metric_value": 2.9279, "depth": 8}
                        if obj[9] == '>':
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 46, "metric_value": 1.8509, "depth": 9}
                           if obj[12]<=14:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 33, "metric_value": 2.1735, "depth": 10}
                              if obj[2]<=41.03756147156517:
                                 return 71.93548387096774
                              elif obj[2]>41.03756147156517:
                                 return 35
                              else:
                                 return 69.6969696969697
                           elif obj[12]>14:
                              # {"feature": "STime_A_VS_B_Max", "instances": 13, "metric_value": 6.7201, "depth": 10}
                              if obj[5] == '>':
                                 return 36.8
                              elif obj[5] == '=':
                                 return 85.0
                              elif obj[5] == '<':
                                 return 50
                              else:
                                 return 45.23076923076923
                           else:
                              return 62.78260869565217
                        elif obj[9] == '<':
                           return 109.5
                        elif obj[9] == '=':
                           return 121.0
                        else:
                           return 66.98
                     else:
                        return 81.7015873015873
                  elif obj[3] == '=':
                     # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 171, "metric_value": 1.2591, "depth": 7}
                     if obj[2]>4.3441278257014115:
                        # {"feature": "STime_A_VS_B_Max", "instances": 143, "metric_value": 0.7383, "depth": 8}
                        if obj[5] == '>':
                           # {"feature": "PTime_A_VS_B_Min", "instances": 138, "metric_value": 0.998, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 76, "metric_value": 1.5433, "depth": 10}
                              if obj[10]<=5:
                                 return 68.025
                              elif obj[10]>5:
                                 return 88.44444444444444
                              else:
                                 return 77.69736842105263
                           elif obj[9] == '<':
                              # {"feature": "Due_A_VS_B", "instances": 59, "metric_value": 0.8045, "depth": 10}
                              if obj[13] == '>':
                                 return 62.17777777777778
                              elif obj[13] == '<':
                                 return 74.58333333333333
                              elif obj[13] == '=':
                                 return 36.5
                              else:
                                 return 63.83050847457627
                           elif obj[9] == '=':
                              return 47.666666666666664
                           else:
                              return 71.1159420289855
                        elif obj[5] == '<':
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 5, "metric_value": 28.0476, "depth": 9}
                           if obj[10]>-8:
                              return 84.66666666666667
                           elif obj[10]<=-8:
                              return 157
                           else:
                              return 113.6
                        else:
                           return 72.6013986013986
                     elif obj[2]<=4.3441278257014115:
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 28, "metric_value": 2.3466, "depth": 8}
                        if obj[12]<=1:
                           # {"feature": "Due_A_VS_B", "instances": 16, "metric_value": 2.6215, "depth": 9}
                           if obj[13] == '>':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 14, "metric_value": 2.4917, "depth": 10}
                              if obj[8]>-4.666666666666671:
                                 return 36.888888888888886
                              elif obj[8]<=-4.666666666666671:
                                 return 45.4
                              else:
                                 return 39.92857142857143
                           elif obj[13] == '<':
                              return 70.0
                           else:
                              return 43.6875
                        elif obj[12]>1:
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 12, "metric_value": 5.7038, "depth": 9}
                           if obj[8]<=8.333333333333329:
                              # {"feature": "Due_A_VS_B", "instances": 9, "metric_value": 4.8333, "depth": 10}
                              if obj[13] == '>':
                                 return 62.833333333333336
                              elif obj[13] == '<':
                                 return 35.5
                              elif obj[13] == '=':
                                 return 57
                              else:
                                 return 56.111111111111114
                           elif obj[8]>8.333333333333329:
                              return 89.0
                           else:
                              return 64.33333333333333
                        else:
                           return 52.535714285714285
                     else:
                        return 69.3157894736842
                  elif obj[3] == '<':
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 53, "metric_value": 2.633, "depth": 7}
                     if obj[10]<=9.665833392733862:
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 45, "metric_value": 2.3409, "depth": 8}
                        if obj[2]<=26.509366259339536:
                           # {"feature": "PTime_A_VS_B_Min", "instances": 43, "metric_value": 1.4594, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 20, "metric_value": 2.3852, "depth": 10}
                              if obj[12]>-13:
                                 return 80.36842105263158
                              elif obj[12]<=-13:
                                 return 32
                              else:
                                 return 77.95
                           elif obj[9] == '<':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 20, "metric_value": 3.5335, "depth": 10}
                              if obj[8]<=-1.3333333333333357:
                                 return 72.36363636363636
                              elif obj[8]>-1.3333333333333357:
                                 return 50.22222222222222
                              else:
                                 return 62.4
                           elif obj[9] == '=':
                              return 93.33333333333333
                           else:
                              return 71.79069767441861
                        elif obj[2]>26.509366259339536:
                           return 17.5
                        else:
                           return 69.37777777777778
                     elif obj[10]>9.665833392733862:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 8, "metric_value": 5.4056, "depth": 8}
                        if obj[8]<=7.666666666666664:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 3.9339, "depth": 9}
                           if obj[2]<=15.333333333333336:
                              return 108.0
                           elif obj[2]>15.333333333333336:
                              return 126
                           else:
                              return 111.6
                        elif obj[8]>7.666666666666664:
                           return 86.33333333333333
                        else:
                           return 102.125
                     else:
                        return 74.32075471698113
                  else:
                     return 77.04638218923934
               elif obj[6]<=-3.776496248986316:
                  # {"feature": "STime_A_VS_B_Min", "instances": 108, "metric_value": 2.6532, "depth": 6}
                  if obj[3] == '>':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 78, "metric_value": 3.362, "depth": 7}
                     if obj[8]<=6.635204703126315:
                        # {"feature": "Due_A_VS_B", "instances": 63, "metric_value": 2.906, "depth": 8}
                        if obj[13] == '>':
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 40, "metric_value": 1.6498, "depth": 9}
                           if obj[10]<=-1.525:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 23, "metric_value": 2.9978, "depth": 10}
                              if obj[11] == '>':
                                 return 70.9090909090909
                              elif obj[11] == '<':
                                 return 72.18181818181819
                              elif obj[11] == '=':
                                 return 103
                              else:
                                 return 72.91304347826087
                           elif obj[10]>-1.525:
                              # {"feature": "PTime_A_VS_B_Avg", "instances": 17, "metric_value": 4.1333, "depth": 10}
                              if obj[7] == '<':
                                 return 99.0
                              elif obj[7] == '>':
                                 return 74.25
                              elif obj[7] == '=':
                                 return 120
                              else:
                                 return 88.58823529411765
                           else:
                              return 79.575
                        elif obj[13] == '<':
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 23, "metric_value": 8.4715, "depth": 9}
                           if obj[2]>2.999999999999993:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 16, "metric_value": 7.0817, "depth": 10}
                              if obj[11] == '>':
                                 return 80.42857142857143
                              elif obj[11] == '<':
                                 return 95.0
                              elif obj[11] == '=':
                                 return 136.5
                              else:
                                 return 93.8125
                           elif obj[2]<=2.999999999999993:
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 7, "metric_value": 22.6632, "depth": 10}
                              if obj[10]<=-6:
                                 return 169.8
                              elif obj[10]>-6:
                                 return 100.5
                              else:
                                 return 150.0
                           else:
                              return 110.91304347826087
                        else:
                           return 91.01587301587301
                     elif obj[8]>6.635204703126315:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 15, "metric_value": 5.1529, "depth": 8}
                        if obj[10]<=8:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 9, "metric_value": 1.9872, "depth": 9}
                           if obj[2]>2.0:
                              # {"feature": "Due_A_VS_B", "instances": 7, "metric_value": 2.4658, "depth": 10}
                              if obj[13] == '>':
                                 return 41.5
                              elif obj[13] == '<':
                                 return 60
                              else:
                                 return 44.142857142857146
                           elif obj[2]<=2.0:
                              return 26.5
                           else:
                              return 40.22222222222222
                        elif obj[10]>8:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 12.1621, "depth": 9}
                           if obj[12]<=9:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 8.2424, "depth": 10}
                              if obj[2]>2.6666666666666714:
                                 return 93.0
                              elif obj[2]<=2.6666666666666714:
                                 return 59.0
                              else:
                                 return 79.4
                           elif obj[12]>9:
                              return 18
                           else:
                              return 69.16666666666667
                        else:
                           return 51.8
                     else:
                        return 83.47435897435898
                  elif obj[3] == '=':
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 24, "metric_value": 2.6925, "depth": 7}
                     if obj[10]>-5:
                        # {"feature": "PTime_A_VS_B_Avg", "instances": 22, "metric_value": 3.5527, "depth": 8}
                        if obj[7] == '>':
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 17, "metric_value": 7.1125, "depth": 9}
                           if obj[2]>3.666666666666672:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 10, "metric_value": 8.2339, "depth": 10}
                              if obj[11] == '>':
                                 return 144.85714285714286
                              elif obj[11] == '=':
                                 return 99.0
                              elif obj[11] == '<':
                                 return 94
                              else:
                                 return 130.6
                           elif obj[2]<=3.666666666666672:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 6.4615, "depth": 10}
                              if obj[8]>0.6666666666666643:
                                 return 102.83333333333333
                              elif obj[8]<=0.6666666666666643:
                                 return 75
                              else:
                                 return 98.85714285714286
                           else:
                              return 117.52941176470588
                        elif obj[7] == '<':
                           return 145.75
                        elif obj[7] == '=':
                           return 80
                        else:
                           return 120.95454545454545
                     elif obj[10]<=-5:
                        return 70.0
                     else:
                        return 116.70833333333333
                  elif obj[3] == '<':
                     # {"feature": "PTime_A_VS_B_Max", "instances": 6, "metric_value": 14.8241, "depth": 7}
                     if obj[11] == '>':
                        return 50.75
                     elif obj[11] == '<':
                        return 104.0
                     else:
                        return 68.5
                  else:
                     return 90.02777777777777
               else:
                  return 79.21329211746523
            elif obj[14]>87.19317593302394:
               # {"feature": "STime_A_VS_B_Min", "instances": 121, "metric_value": 2.1801, "depth": 5}
               if obj[3] == '>':
                  # {"feature": "STime_A_VS_B_Max", "instances": 82, "metric_value": 2.0478, "depth": 6}
                  if obj[5] == '>':
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 68, "metric_value": 1.3124, "depth": 7}
                     if obj[10]>-17.245613026170297:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 66, "metric_value": 1.5484, "depth": 8}
                        if obj[8]>-7.281700378040486:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 54, "metric_value": 2.4278, "depth": 9}
                           if obj[12]>-15.970842252556247:
                              # {"feature": "PTime_A_VS_B_Min", "instances": 52, "metric_value": 1.559, "depth": 10}
                              if obj[9] == '>':
                                 return 119.35483870967742
                              elif obj[9] == '<':
                                 return 111.3157894736842
                              elif obj[9] == '=':
                                 return 168.5
                              else:
                                 return 118.3076923076923
                           elif obj[12]<=-15.970842252556247:
                              return 191.0
                           else:
                              return 121.0
                        elif obj[8]<=-7.281700378040486:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 12, "metric_value": 14.1642, "depth": 9}
                           if obj[2]<=27.666666666666668:
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 11, "metric_value": 3.8484, "depth": 10}
                              if obj[12]>-13:
                                 return 91.28571428571429
                              elif obj[12]<=-13:
                                 return 71.75
                              else:
                                 return 84.18181818181819
                           elif obj[2]>27.666666666666668:
                              return 185
                           else:
                              return 92.58333333333333
                        else:
                           return 115.83333333333333
                     elif obj[10]<=-17.245613026170297:
                        return 162.0
                     else:
                        return 117.19117647058823
                  elif obj[5] == '<':
                     # {"feature": "PTime_A_VS_B_Min", "instances": 13, "metric_value": 14.8362, "depth": 7}
                     if obj[9] == '>':
                        # {"feature": "PTime_A_VS_B_Max", "instances": 7, "metric_value": 9.6529, "depth": 8}
                        if obj[11] == '>':
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 18.0112, "depth": 9}
                           if obj[2]<=20.666666666666668:
                              return 50.25
                           elif obj[2]>20.666666666666668:
                              return 109
                           else:
                              return 62.0
                        elif obj[11] == '<':
                           return 106
                        elif obj[11] == '=':
                           return 44
                        else:
                           return 65.71428571428571
                     elif obj[9] == '<':
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 15.0653, "depth": 8}
                        if obj[8]>-10.0:
                           return 136.25
                        elif obj[8]<=-10.0:
                           return 69
                        else:
                           return 122.8
                     elif obj[9] == '=':
                        return 31
                     else:
                        return 85.0
                  elif obj[5] == '=':
                     return 64
                  else:
                     return 111.4390243902439
               elif obj[3] == '=':
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 22, "metric_value": 4.1499, "depth": 6}
                  if obj[12]>-12:
                     # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 19, "metric_value": 4.4404, "depth": 7}
                     if obj[2]<=18.333333333333336:
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 13, "metric_value": 4.796, "depth": 8}
                        if obj[6]>8:
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 12, "metric_value": 4.037, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 7, "metric_value": 11.4747, "depth": 10}
                              if obj[10]>3:
                                 return 78.0
                              elif obj[10]<=3:
                                 return 33.5
                              else:
                                 return 65.28571428571429
                           elif obj[7] == '<':
                              return 51.0
                           elif obj[7] == '=':
                              return 96
                           else:
                              return 63.083333333333336
                        elif obj[6]<=8:
                           return 116
                        else:
                           return 67.15384615384616
                     elif obj[2]>18.333333333333336:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 12.5922, "depth": 8}
                        if obj[8]<=4.0:
                           # {"feature": "STime_A_VS_B_Max_Diff", "instances": 5, "metric_value": 9.0203, "depth": 9}
                           if obj[6]<=59:
                              return 98.75
                           elif obj[6]>59:
                              return 66
                           else:
                              return 92.2
                        elif obj[8]>4.0:
                           return 148
                        else:
                           return 101.5
                     else:
                        return 78.0
                  elif obj[12]<=-12:
                     return 122.0
                  else:
                     return 84.0
               elif obj[3] == '<':
                  # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 17, "metric_value": 5.3302, "depth": 6}
                  if obj[2]>5.666666666666664:
                     # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 11, "metric_value": 7.574, "depth": 7}
                     if obj[12]<=2:
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 10, "metric_value": 10.6612, "depth": 8}
                        if obj[6]<=30:
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 6, "metric_value": 13.6068, "depth": 9}
                           if obj[7] == '>':
                              return 109.0
                           elif obj[7] == '<':
                              return 155.5
                           else:
                              return 124.5
                        elif obj[6]>30:
                           return 79.25
                        else:
                           return 106.4
                     elif obj[12]>2:
                        return 37
                     else:
                        return 100.0909090909091
                  elif obj[2]<=5.666666666666664:
                     # {"feature": "PTime_A_VS_B_Max", "instances": 6, "metric_value": 15.6025, "depth": 7}
                     if obj[11] == '<':
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 5, "metric_value": 11.3333, "depth": 8}
                        if obj[12]<=-4:
                           return 61.0
                        elif obj[12]>-4:
                           return 29.5
                        else:
                           return 48.4
                     elif obj[11] == '>':
                        return 116
                     else:
                        return 59.666666666666664
                  else:
                     return 85.82352941176471
               else:
                  return 102.85123966942149
            else:
               return 82.9375
         elif obj[4]>32.49084748344646:
            # {"feature": "PTime_A_VS_B_Max", "instances": 176, "metric_value": 0.9437, "depth": 4}
            if obj[11] == '>':
               # {"feature": "Due_A_VS_B_Diff", "instances": 104, "metric_value": 2.1227, "depth": 5}
               if obj[14]<=92.96824271501427:
                  # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 85, "metric_value": 2.2094, "depth": 6}
                  if obj[8]>-4.669248179931405:
                     # {"feature": "Due_A_VS_B", "instances": 82, "metric_value": 1.4626, "depth": 7}
                     if obj[13] == '>':
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 52, "metric_value": 2.486, "depth": 8}
                        if obj[2]<=45.225030226895214:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 42, "metric_value": 2.1557, "depth": 9}
                           if obj[10]>-9:
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 41, "metric_value": 1.4253, "depth": 10}
                              if obj[12]>1:
                                 return 121.1025641025641
                              elif obj[12]<=1:
                                 return 148.0
                              else:
                                 return 122.41463414634147
                           elif obj[10]<=-9:
                              return 43
                           else:
                              return 120.52380952380952
                        elif obj[2]>45.225030226895214:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 10, "metric_value": 18.4289, "depth": 9}
                           if obj[10]>-2:
                              # {"feature": "PTime_A_VS_B_Min", "instances": 8, "metric_value": 14.2115, "depth": 10}
                              if obj[9] == '>':
                                 return 150.33333333333334
                              elif obj[9] == '=':
                                 return 122
                              elif obj[9] == '<':
                                 return 73
                              else:
                                 return 137.125
                           elif obj[10]<=-2:
                              return 242.5
                           else:
                              return 158.2
                        else:
                           return 127.76923076923077
                     elif obj[13] == '<':
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 29, "metric_value": 8.3436, "depth": 8}
                        if obj[12]>6:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 16, "metric_value": 8.3092, "depth": 9}
                           if obj[2]>11.0:
                              # {"feature": "STime_A_VS_B_Max", "instances": 15, "metric_value": 4.2186, "depth": 10}
                              if obj[5] == '>':
                                 return 85.5
                              elif obj[5] == '<':
                                 return 55.666666666666664
                              else:
                                 return 79.53333333333333
                           elif obj[2]<=11.0:
                              return 163
                           else:
                              return 84.75
                        elif obj[12]<=6:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 13, "metric_value": 11.4059, "depth": 9}
                           if obj[10]<=2:
                              # {"feature": "PTime_A_VS_B_Min", "instances": 11, "metric_value": 6.773, "depth": 10}
                              if obj[9] == '<':
                                 return 128.83333333333334
                              elif obj[9] == '>':
                                 return 101.33333333333333
                              elif obj[9] == '=':
                                 return 143.0
                              else:
                                 return 123.9090909090909
                           elif obj[10]>2:
                              return 199
                           else:
                              return 135.46153846153845
                        else:
                           return 107.48275862068965
                     elif obj[13] == '=':
                        return 161
                     else:
                        return 121.0
                  elif obj[8]<=-4.669248179931405:
                     return 201.0
                  else:
                     return 123.82352941176471
               elif obj[14]>92.96824271501427:
                  # {"feature": "STime_A_VS_B_Max", "instances": 19, "metric_value": 3.0924, "depth": 6}
                  if obj[5] == '>':
                     # {"feature": "STime_A_VS_B_Max_Diff", "instances": 12, "metric_value": 5.1654, "depth": 7}
                     if obj[6]>24:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 10.4127, "depth": 8}
                        if obj[8]<=4.0:
                           return 106.66666666666667
                        elif obj[8]>4.0:
                           return 70.0
                        else:
                           return 88.33333333333333
                     elif obj[6]<=24:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 5.5987, "depth": 8}
                        if obj[10]>1:
                           return 128.25
                        elif obj[10]<=1:
                           return 105.0
                        else:
                           return 120.5
                     else:
                        return 104.41666666666667
                  elif obj[5] == '<':
                     # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 10.5271, "depth": 7}
                     if obj[2]>0.6666666666666714:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 2.855, "depth": 8}
                        if obj[8]>3.666666666666672:
                           return 67.25
                        elif obj[8]<=3.666666666666672:
                           return 77.0
                        else:
                           return 70.5
                     elif obj[2]<=0.6666666666666714:
                        return 123
                     else:
                        return 78.0
                  else:
                     return 94.6842105263158
               else:
                  return 118.5
            elif obj[11] == '<':
               # {"feature": "STime_A_VS_B_Max", "instances": 66, "metric_value": 1.6516, "depth": 5}
               if obj[5] == '>':
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 47, "metric_value": 2.1018, "depth": 6}
                  if obj[12]<=-3:
                     # {"feature": "STime_A_VS_B_Max_Diff", "instances": 31, "metric_value": 3.0734, "depth": 7}
                     if obj[6]>1:
                        # {"feature": "PTime_A_VS_B_Avg", "instances": 30, "metric_value": 2.1472, "depth": 8}
                        if obj[7] == '<':
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 22, "metric_value": 2.6819, "depth": 9}
                           if obj[8]>-15.333333333333332:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 21, "metric_value": 2.2384, "depth": 10}
                              if obj[2]<=39.0:
                                 return 115.2
                              elif obj[2]>39.0:
                                 return 87.83333333333333
                              else:
                                 return 107.38095238095238
                           elif obj[8]<=-15.333333333333332:
                              return 50
                           else:
                              return 104.77272727272727
                        elif obj[7] == '>':
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 13.1724, "depth": 9}
                           if obj[8]<=4.333333333333329:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 13.3669, "depth": 10}
                              if obj[2]>32.666666666666664:
                                 return 98.25
                              elif obj[2]<=32.666666666666664:
                                 return 138
                              else:
                                 return 111.5
                           elif obj[8]>4.333333333333329:
                              return 42
                           else:
                              return 101.57142857142857
                        elif obj[7] == '=':
                           return 159
                        else:
                           return 105.83333333333333
                     elif obj[6]<=1:
                        return 185
                     else:
                        return 108.38709677419355
                  elif obj[12]>-3:
                     # {"feature": "STime_A_VS_B_Max_Diff", "instances": 16, "metric_value": 11.2004, "depth": 7}
                     if obj[6]>18:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 11, "metric_value": 10.6261, "depth": 8}
                        if obj[8]<=1.6666666666666714:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 10, "metric_value": 7.592, "depth": 9}
                           if obj[10]<=2:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 7.2057, "depth": 10}
                              if obj[2]>40.0:
                                 return 149.25
                              elif obj[2]<=40.0:
                                 return 179.66666666666666
                              else:
                                 return 162.28571428571428
                           elif obj[10]>2:
                              return 114.0
                           else:
                              return 147.8
                        elif obj[8]>1.6666666666666714:
                           return 240
                        else:
                           return 156.1818181818182
                     elif obj[6]<=18:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 5, "metric_value": 16.4796, "depth": 8}
                        if obj[9] == '>':
                           return 108.66666666666667
                        elif obj[9] == '<':
                           return 84
                        elif obj[9] == '=':
                           return 56
                        else:
                           return 93.2
                     else:
                        return 136.5
                  else:
                     return 117.95744680851064
               elif obj[5] == '<':
                  # {"feature": "STime_A_VS_B_Max_Diff", "instances": 17, "metric_value": 6.7393, "depth": 6}
                  if obj[6]>-24:
                     # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 15, "metric_value": 2.8321, "depth": 7}
                     if obj[12]>-8:
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 10, "metric_value": 2.259, "depth": 8}
                        if obj[2]<=19.000000000000007:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 9, "metric_value": 2.0029, "depth": 9}
                           if obj[10]<=4:
                              # {"feature": "Due_A_VS_B_Diff", "instances": 8, "metric_value": 2.6535, "depth": 10}
                              if obj[14]<=57:
                                 return 118.71428571428571
                              elif obj[14]>57:
                                 return 139
                              else:
                                 return 121.25
                           elif obj[10]>4:
                              return 103
                           else:
                              return 119.22222222222223
                        elif obj[2]>19.000000000000007:
                           return 141
                        else:
                           return 121.4
                     elif obj[12]<=-8:
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 3.6718, "depth": 8}
                        if obj[2]>8.666666666666671:
                           return 106.5
                        elif obj[2]<=8.666666666666671:
                           return 89
                        else:
                           return 103.0
                     else:
                        return 115.26666666666667
                  elif obj[6]<=-24:
                     return 161.0
                  else:
                     return 120.6470588235294
               elif obj[5] == '=':
                  return 118.5
               else:
                  return 118.66666666666667
            elif obj[11] == '=':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 28.4015, "depth": 5}
               if obj[6]<=30:
                  return 129.5
               elif obj[6]>30:
                  return 226.5
               else:
                  return 161.83333333333334
            else:
               return 120.03977272727273
         else:
            return 89.85487288135593
      elif obj[0]>12:
         # {"feature": "STime_A_VS_B_Min_Diff", "instances": 706, "metric_value": 3.9333, "depth": 3}
         if obj[4]<=21.299772136269926:
            # {"feature": "Due_A_VS_B_Diff", "instances": 592, "metric_value": 4.5372, "depth": 4}
            if obj[14]>68.07601351351352:
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 312, "metric_value": 1.3148, "depth": 5}
               if obj[2]<=14.506410256410257:
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 178, "metric_value": 0.8325, "depth": 6}
                  if obj[12]>-15.069836359030292:
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 175, "metric_value": 0.8106, "depth": 7}
                     if obj[10]>-23:
                        # {"feature": "STime_A_VS_B_Max", "instances": 174, "metric_value": 0.8348, "depth": 8}
                        if obj[5] == '>':
                           # {"feature": "STime_A_VS_B_Min", "instances": 143, "metric_value": 0.7852, "depth": 9}
                           if obj[3] == '=':
                              # {"feature": "PTime_A_VS_B_Max", "instances": 120, "metric_value": 0.7527, "depth": 10}
                              if obj[11] == '>':
                                 return 134.38709677419354
                              elif obj[11] == '<':
                                 return 124.35416666666667
                              elif obj[11] == '=':
                                 return 104.7
                              else:
                                 return 127.9
                           elif obj[3] == '>':
                              # {"feature": "STime_A_VS_B_Max_Diff", "instances": 18, "metric_value": 23.263, "depth": 10}
                              if obj[6]>11:
                                 return 125.75
                              elif obj[6]<=11:
                                 return 212.16666666666666
                              else:
                                 return 154.55555555555554
                           elif obj[3] == '<':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 17.8962, "depth": 10}
                              if obj[8]<=4.666666666666664:
                                 return 118.0
                              elif obj[8]>4.666666666666664:
                                 return 199
                              else:
                                 return 134.2
                           else:
                              return 131.47552447552448
                        elif obj[5] == '<':
                           # {"feature": "PTime_A_VS_B_Min", "instances": 27, "metric_value": 4.8208, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "PTime_A_VS_B_Avg", "instances": 15, "metric_value": 5.8664, "depth": 10}
                              if obj[7] == '>':
                                 return 113.91666666666667
                              elif obj[7] == '<':
                                 return 117.66666666666667
                              else:
                                 return 114.66666666666667
                           elif obj[9] == '<':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 11, "metric_value": 17.4402, "depth": 10}
                              if obj[8]>-9.333333333333336:
                                 return 177.0
                              elif obj[8]<=-9.333333333333336:
                                 return 78.5
                              else:
                                 return 159.0909090909091
                           elif obj[9] == '=':
                              return 140
                           else:
                              return 133.7037037037037
                        elif obj[5] == '=':
                           return 186.75
                        else:
                           return 133.09195402298852
                     elif obj[10]<=-23:
                        return 246
                     else:
                        return 133.73714285714286
                  elif obj[12]<=-15.069836359030292:
                     return 79.33333333333333
                  else:
                     return 132.82022471910113
               elif obj[2]>14.506410256410257:
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 134, "metric_value": 0.8655, "depth": 6}
                  if obj[12]>-13.124847955352237:
                     # {"feature": "PTime_A_VS_B_Min", "instances": 132, "metric_value": 0.8435, "depth": 7}
                     if obj[9] == '>':
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 63, "metric_value": 0.84, "depth": 8}
                        if obj[6]>40.79365079365079:
                           # {"feature": "PTime_A_VS_B_Max", "instances": 34, "metric_value": 5.2112, "depth": 9}
                           if obj[11] == '>':
                              # {"feature": "PTime_A_VS_B_Avg", "instances": 21, "metric_value": 5.1773, "depth": 10}
                              if obj[7] == '>':
                                 return 147.5
                              elif obj[7] == '<':
                                 return 52
                              else:
                                 return 142.95238095238096
                           elif obj[11] == '<':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 12, "metric_value": 6.6981, "depth": 10}
                              if obj[10]<=8:
                                 return 141.0
                              elif obj[10]>8:
                                 return 190.0
                              else:
                                 return 157.33333333333334
                           elif obj[11] == '=':
                              return 265
                           else:
                              return 151.61764705882354
                        elif obj[6]<=40.79365079365079:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 29, "metric_value": 2.365, "depth": 9}
                           if obj[10]<=7:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 22, "metric_value": 3.5274, "depth": 10}
                              if obj[8]>0.3333333333333357:
                                 return 137.22222222222223
                              elif obj[8]<=0.3333333333333357:
                                 return 177.25
                              else:
                                 return 144.5
                           elif obj[10]>7:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 9.8397, "depth": 10}
                              if obj[8]<=9.0:
                                 return 165.5
                              elif obj[8]>9.0:
                                 return 223
                              else:
                                 return 173.71428571428572
                           else:
                              return 151.55172413793105
                        else:
                           return 151.5873015873016
                     elif obj[9] == '<':
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 59, "metric_value": 1.738, "depth": 8}
                        if obj[10]>-12:
                           # {"feature": "STime_A_VS_B_Min", "instances": 57, "metric_value": 2.0692, "depth": 9}
                           if obj[3] == '=':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 42, "metric_value": 1.9616, "depth": 10}
                              if obj[8]<=7.4491434855646474:
                                 return 163.6829268292683
                              elif obj[8]>7.4491434855646474:
                                 return 239
                              else:
                                 return 165.47619047619048
                           elif obj[3] == '>':
                              # {"feature": "STime_A_VS_B_Max_Diff", "instances": 12, "metric_value": 8.3422, "depth": 10}
                              if obj[6]<=60:
                                 return 151.8
                              elif obj[6]>60:
                                 return 72.0
                              else:
                                 return 138.5
                           elif obj[3] == '<':
                              return 192.66666666666666
                           else:
                              return 161.2280701754386
                        elif obj[10]<=-12:
                           return 223.5
                        else:
                           return 163.33898305084745
                     elif obj[9] == '=':
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 10, "metric_value": 12.1205, "depth": 8}
                        if obj[6]<=60:
                           # {"feature": "PTime_A_VS_B_Max", "instances": 9, "metric_value": 14.2608, "depth": 9}
                           if obj[11] == '>':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 26.9704, "depth": 10}
                              if obj[8]>0.6666666666666714:
                                 return 132.0
                              elif obj[8]<=0.6666666666666714:
                                 return 210.0
                              else:
                                 return 163.2
                           elif obj[11] == '<':
                              return 131.66666666666666
                           elif obj[11] == '=':
                              return 68
                           else:
                              return 142.11111111111111
                        elif obj[6]>60:
                           return 39
                        else:
                           return 131.8
                     else:
                        return 155.3409090909091
                  elif obj[12]<=-13.124847955352237:
                     return 214.5
                  else:
                     return 156.22388059701493
               else:
                  return 142.87179487179486
            elif obj[14]<=68.07601351351352:
               # {"feature": "STime_A_VS_B_Min", "instances": 280, "metric_value": 3.3401, "depth": 5}
               if obj[3] == '=':
                  # {"feature": "Due_A_VS_B", "instances": 220, "metric_value": 0.9285, "depth": 6}
                  if obj[13] == '>':
                     # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 136, "metric_value": 0.7749, "depth": 7}
                     if obj[2]<=30.924626961758747:
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 131, "metric_value": 0.6584, "depth": 8}
                        if obj[6]>-19:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 130, "metric_value": 0.5988, "depth": 9}
                           if obj[10]>-6.676828884811854:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 103, "metric_value": 0.6858, "depth": 10}
                              if obj[8]>-7.272917966116545:
                                 return 95.60606060606061
                              elif obj[8]<=-7.272917966116545:
                                 return 116.5
                              else:
                                 return 96.41747572815534
                           elif obj[10]<=-6.676828884811854:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 27, "metric_value": 4.1891, "depth": 10}
                              if obj[11] == '<':
                                 return 71.86666666666666
                              elif obj[11] == '>':
                                 return 100.88888888888889
                              elif obj[11] == '=':
                                 return 48.666666666666664
                              else:
                                 return 78.96296296296296
                           else:
                              return 92.79230769230769
                        elif obj[6]<=-19:
                           return 171
                        else:
                           return 93.38931297709924
                     elif obj[2]>30.924626961758747:
                        # {"feature": "PTime_A_VS_B_Max", "instances": 5, "metric_value": 15.916, "depth": 8}
                        if obj[11] == '>':
                           return 138.66666666666666
                        elif obj[11] == '<':
                           return 91
                        elif obj[11] == '=':
                           return 158
                        else:
                           return 133.0
                     else:
                        return 94.84558823529412
                  elif obj[13] == '<':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 79, "metric_value": 2.437, "depth": 7}
                     if obj[8]>-5.300414090580577:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 66, "metric_value": 2.4501, "depth": 8}
                        if obj[10]<=2.3333333333333335:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 38, "metric_value": 2.3924, "depth": 9}
                           if obj[2]<=26.730158708410883:
                              # {"feature": "STime_A_VS_B_Max", "instances": 35, "metric_value": 2.0837, "depth": 10}
                              if obj[5] == '>':
                                 return 86.24242424242425
                              elif obj[5] == '<':
                                 return 121
                              else:
                                 return 88.22857142857143
                           elif obj[2]>26.730158708410883:
                              return 139.33333333333334
                           else:
                              return 92.26315789473684
                        elif obj[10]>2.3333333333333335:
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 28, "metric_value": 7.7219, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "STime_A_VS_B_Max_Diff", "instances": 23, "metric_value": 3.488, "depth": 10}
                              if obj[6]>21:
                                 return 79.35714285714286
                              elif obj[6]<=21:
                                 return 52.77777777777778
                              else:
                                 return 68.95652173913044
                           elif obj[7] == '<':
                              return 45.75
                           elif obj[7] == '=':
                              return 165
                           else:
                              return 69.07142857142857
                        else:
                           return 82.42424242424242
                     elif obj[8]<=-5.300414090580577:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 13, "metric_value": 7.7432, "depth": 8}
                        if obj[10]>-6:
                           # {"feature": "PTime_A_VS_B_Min", "instances": 7, "metric_value": 3.6485, "depth": 9}
                           if obj[9] == '<':
                              return 28.333333333333332
                           elif obj[9] == '>':
                              return 34.666666666666664
                           elif obj[9] == '=':
                              return 9
                           else:
                              return 28.285714285714285
                        elif obj[10]<=-6:
                           # {"feature": "PTime_A_VS_B_Max", "instances": 6, "metric_value": 10.9805, "depth": 9}
                           if obj[11] == '<':
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 5, "metric_value": 14.1011, "depth": 10}
                              if obj[12]<=-13:
                                 return 54.333333333333336
                              elif obj[12]>-13:
                                 return 103.5
                              else:
                                 return 74.0
                           elif obj[11] == '>':
                              return 9
                           else:
                              return 63.166666666666664
                        else:
                           return 44.38461538461539
                     else:
                        return 76.16455696202532
                  elif obj[13] == '=':
                     # {"feature": "PTime_A_VS_B_Max", "instances": 5, "metric_value": 13.5616, "depth": 7}
                     if obj[11] == '>':
                        return 118.5
                     elif obj[11] == '<':
                        return 109.0
                     elif obj[11] == '=':
                        return 54
                     else:
                        return 101.8
                  else:
                     return 88.29545454545455
               elif obj[3] == '>':
                  # {"feature": "PTime_A_VS_B_Max", "instances": 51, "metric_value": 6.2313, "depth": 6}
                  if obj[11] == '>':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 32, "metric_value": 4.9909, "depth": 7}
                     if obj[8]>-7.333333333333336:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 31, "metric_value": 2.9341, "depth": 8}
                        if obj[9] == '>':
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 15, "metric_value": 6.7457, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "STime_A_VS_B_Max", "instances": 14, "metric_value": 5.6221, "depth": 10}
                              if obj[5] == '>':
                                 return 108.27272727272727
                              elif obj[5] == '<':
                                 return 146.5
                              elif obj[5] == '=':
                                 return 133
                              else:
                                 return 115.5
                           elif obj[7] == '<':
                              return 36
                           else:
                              return 110.2
                        elif obj[9] == '<':
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 13, "metric_value": 7.0849, "depth": 9}
                           if obj[2]<=22.333333333333336:
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 7, "metric_value": 9.1061, "depth": 10}
                              if obj[10]<=-5:
                                 return 172.0
                              elif obj[10]>-5:
                                 return 134.66666666666666
                              else:
                                 return 156.0
                           elif obj[2]>22.333333333333336:
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 15.7004, "depth": 10}
                              if obj[12]<=8:
                                 return 132.0
                              elif obj[12]>8:
                                 return 78.5
                              else:
                                 return 114.16666666666667
                           else:
                              return 136.69230769230768
                        elif obj[9] == '=':
                           return 149.0
                        else:
                           return 125.06451612903226
                     elif obj[8]<=-7.333333333333336:
                        return 234
                     else:
                        return 128.46875
                  elif obj[11] == '<':
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 16, "metric_value": 8.2216, "depth": 7}
                     if obj[10]>-7:
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 14, "metric_value": 6.0415, "depth": 8}
                        if obj[2]>7.666666666666664:
                           # {"feature": "Due_A_VS_B", "instances": 10, "metric_value": 12.4061, "depth": 9}
                           if obj[13] == '>':
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 7, "metric_value": 7.5935, "depth": 10}
                              if obj[12]>-8:
                                 return 193.5
                              elif obj[12]<=-8:
                                 return 160.0
                              else:
                                 return 179.14285714285714
                           elif obj[13] == '<':
                              return 122.66666666666667
                           else:
                              return 162.2
                        elif obj[2]<=7.666666666666664:
                           return 127.0
                        else:
                           return 152.14285714285714
                     elif obj[10]<=-7:
                        return 232.0
                     else:
                        return 162.125
                  elif obj[11] == '=':
                     return 60.666666666666664
                  else:
                     return 135.0392156862745
               elif obj[3] == '<':
                  # {"feature": "PTime_A_VS_B_Min", "instances": 9, "metric_value": 31.4273, "depth": 6}
                  if obj[9] == '>':
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 5, "metric_value": 21.9217, "depth": 7}
                     if obj[10]>8:
                        return 91.0
                     elif obj[10]<=8:
                        return 11
                     else:
                        return 75.0
                  elif obj[9] == '<':
                     return 174.66666666666666
                  elif obj[9] == '=':
                     return 170
                  else:
                     return 118.77777777777777
               else:
                  return 97.78928571428571
            else:
               return 121.54898648648648
         elif obj[4]>21.299772136269926:
            # {"feature": "PTime_A_VS_B_Avg", "instances": 114, "metric_value": 3.2763, "depth": 4}
            if obj[7] == '>':
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 60, "metric_value": 4.3447, "depth": 5}
               if obj[2]<=38.74592813846535:
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 50, "metric_value": 3.533, "depth": 6}
                  if obj[12]<=10:
                     # {"feature": "STime_A_VS_B_Max", "instances": 42, "metric_value": 2.5967, "depth": 7}
                     if obj[5] == '>':
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 31, "metric_value": 5.2941, "depth": 8}
                        if obj[6]>1:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 29, "metric_value": 4.3804, "depth": 9}
                           if obj[10]<=6:
                              # {"feature": "Due_A_VS_B_Diff", "instances": 19, "metric_value": 10.6676, "depth": 10}
                              if obj[14]>-44:
                                 return 162.64705882352942
                              elif obj[14]<=-44:
                                 return 257.0
                              else:
                                 return 172.57894736842104
                           elif obj[10]>6:
                              # {"feature": "Due_A_VS_B_Diff", "instances": 10, "metric_value": 6.023, "depth": 10}
                              if obj[14]>-46:
                                 return 129.375
                              elif obj[14]<=-46:
                                 return 163
                              else:
                                 return 136.1
                           else:
                              return 160.0
                        elif obj[6]<=1:
                           return 246.5
                        else:
                           return 165.58064516129033
                     elif obj[5] == '<':
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 11, "metric_value": 26.7394, "depth": 8}
                        if obj[6]<=-2:
                           # {"feature": "Due_A_VS_B_Diff", "instances": 10, "metric_value": 7.235, "depth": 9}
                           if obj[14]<=114:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 8, "metric_value": 7.9815, "depth": 10}
                              if obj[11] == '>':
                                 return 91.6
                              elif obj[11] == '<':
                                 return 109.0
                              elif obj[11] == '=':
                                 return 152
                              else:
                                 return 103.5
                           elif obj[14]>114:
                              return 160.5
                           else:
                              return 114.9
                        elif obj[6]>-2:
                           return 293
                        else:
                           return 131.0909090909091
                     else:
                        return 156.54761904761904
                  elif obj[12]>10:
                     # {"feature": "Due_A_VS_B_Diff", "instances": 8, "metric_value": 13.6338, "depth": 7}
                     if obj[14]<=91:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 5, "metric_value": 4.5772, "depth": 8}
                        if obj[10]>3:
                           return 174.66666666666666
                        elif obj[10]<=3:
                           return 193.5
                        else:
                           return 182.2
                     elif obj[14]>91:
                        return 229.0
                     else:
                        return 199.75
                  else:
                     return 163.46
               elif obj[2]>38.74592813846535:
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 10, "metric_value": 15.5312, "depth": 6}
                  if obj[12]>4:
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 8, "metric_value": 20.7439, "depth": 7}
                     if obj[10]<=4:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 6, "metric_value": 4.6, "depth": 8}
                        if obj[9] == '>':
                           return 249.0
                        elif obj[9] == '=':
                           return 258.0
                        elif obj[9] == '<':
                           return 275
                        else:
                           return 256.3333333333333
                     elif obj[10]>4:
                        return 183.0
                     else:
                        return 238.0
                  elif obj[12]<=4:
                     return 155.5
                  else:
                     return 221.5
               else:
                  return 173.13333333333333
            elif obj[7] == '<':
               # {"feature": "Due_A_VS_B_Diff", "instances": 52, "metric_value": 4.3546, "depth": 5}
               if obj[14]>-88:
                  # {"feature": "Due_A_VS_B", "instances": 51, "metric_value": 3.8765, "depth": 6}
                  if obj[13] == '>':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 46, "metric_value": 3.1992, "depth": 7}
                     if obj[8]>-12.828514485200614:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 44, "metric_value": 3.556, "depth": 8}
                        if obj[10]>-12:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 37, "metric_value": 3.893, "depth": 9}
                           if obj[12]<=1.133234536253906:
                              # {"feature": "PTime_A_VS_B_Min", "instances": 30, "metric_value": 3.1728, "depth": 10}
                              if obj[9] == '>':
                                 return 187.88888888888889
                              elif obj[9] == '<':
                                 return 183.0
                              elif obj[9] == '=':
                                 return 224.66666666666666
                              else:
                                 return 190.1
                           elif obj[12]>1.133234536253906:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 14.7054, "depth": 10}
                              if obj[2]>26.333333333333336:
                                 return 111.75
                              elif obj[2]<=26.333333333333336:
                                 return 173.0
                              else:
                                 return 138.0
                           else:
                              return 180.24324324324326
                        elif obj[10]<=-12:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 29.394, "depth": 9}
                           if obj[2]<=21.333333333333336:
                              return 189.5
                           elif obj[2]>21.333333333333336:
                              return 298.6666666666667
                           else:
                              return 236.28571428571428
                        else:
                           return 189.1590909090909
                     elif obj[8]<=-12.828514485200614:
                        return 101.5
                     else:
                        return 185.34782608695653
                  elif obj[13] == '<':
                     return 164.75
                  elif obj[13] == '=':
                     return 69
                  else:
                     return 181.45098039215685
               elif obj[14]<=-88:
                  return 341
               else:
                  return 184.51923076923077
            elif obj[7] == '=':
               return 317.5
            else:
               return 180.859649122807
         else:
            return 131.12606232294618
      else:
         return 107.5139393939394
   elif obj[1] == '<':
      # {"feature": "NumWaitingJob", "instances": 686, "metric_value": 2.6311, "depth": 2}
      if obj[0]>11:
         # {"feature": "Due_A_VS_B_Diff", "instances": 347, "metric_value": 2.3619, "depth": 3}
         if obj[14]<=62.04899135446686:
            # {"feature": "STime_A_VS_B_Min", "instances": 178, "metric_value": 2.5065, "depth": 4}
            if obj[3] == '=':
               # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 109, "metric_value": 1.1769, "depth": 5}
               if obj[10]>-9.398184161012137:
                  # {"feature": "Due_A_VS_B", "instances": 98, "metric_value": 1.1433, "depth": 6}
                  if obj[13] == '>':
                     # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 69, "metric_value": 1.7985, "depth": 7}
                     if obj[2]<=-1.972925825048998:
                        # {"feature": "STime_A_VS_B_Max", "instances": 59, "metric_value": 2.6254, "depth": 8}
                        if obj[5] == '<':
                           # {"feature": "PTime_A_VS_B_Max", "instances": 56, "metric_value": 4.1497, "depth": 9}
                           if obj[11] == '>':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 31, "metric_value": 2.9677, "depth": 10}
                              if obj[8]<=5.580645161290325:
                                 return 81.0
                              elif obj[8]>5.580645161290325:
                                 return 54.53333333333333
                              else:
                                 return 68.19354838709677
                           elif obj[11] == '<':
                              # {"feature": "STime_A_VS_B_Max_Diff", "instances": 23, "metric_value": 7.0128, "depth": 10}
                              if obj[6]<=-14:
                                 return 110.2
                              elif obj[6]>-14:
                                 return 43.0
                              else:
                                 return 101.43478260869566
                           elif obj[11] == '=':
                              return 99.5
                           else:
                              return 82.96428571428571
                        elif obj[5] == '>':
                           return 151.0
                        else:
                           return 86.42372881355932
                     elif obj[2]>-1.972925825048998:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 10, "metric_value": 9.3755, "depth": 8}
                        if obj[8]<=7.0:
                           # {"feature": "STime_A_VS_B_Max_Diff", "instances": 7, "metric_value": 7.9263, "depth": 9}
                           if obj[6]<=-2:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 5, "metric_value": 13.0262, "depth": 10}
                              if obj[11] == '<':
                                 return 40.25
                              elif obj[11] == '>':
                                 return 78
                              else:
                                 return 47.8
                           elif obj[6]>-2:
                              return 12.0
                           else:
                              return 37.57142857142857
                        elif obj[8]>7.0:
                           return 87.33333333333333
                        else:
                           return 52.5
                     else:
                        return 81.5072463768116
                  elif obj[13] == '<':
                     # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 27, "metric_value": 4.1184, "depth": 7}
                     if obj[12]<=-3:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 14, "metric_value": 8.4569, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 9.8734, "depth": 9}
                           if obj[2]>-6.666666666666667:
                              return 91.75
                           elif obj[2]<=-6.666666666666667:
                              return 45.666666666666664
                           else:
                              return 72.0
                        elif obj[9] == '>':
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 15.252, "depth": 9}
                           if obj[2]>-20.666666666666664:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 16.501, "depth": 10}
                              if obj[8]>-4.333333333333336:
                                 return 74.25
                              elif obj[8]<=-4.333333333333336:
                                 return 127
                              else:
                                 return 84.8
                           elif obj[2]<=-20.666666666666664:
                              return 157
                           else:
                              return 96.83333333333333
                        elif obj[9] == '=':
                           return 9
                        else:
                           return 78.14285714285714
                     elif obj[12]>-3:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 13, "metric_value": 2.6281, "depth": 8}
                        if obj[8]<=12.0:
                           # {"feature": "PTime_A_VS_B_Min", "instances": 11, "metric_value": 2.4482, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "PTime_A_VS_B_Max", "instances": 7, "metric_value": 5.2355, "depth": 10}
                              if obj[11] == '>':
                                 return 48.75
                              elif obj[11] == '<':
                                 return 66.0
                              elif obj[11] == '=':
                                 return 44
                              else:
                                 return 53.0
                           elif obj[9] == '>':
                              return 52.0
                           elif obj[9] == '=':
                              return 73
                           else:
                              return 54.54545454545455
                        elif obj[8]>12.0:
                           return 73
                        else:
                           return 57.38461538461539
                     else:
                        return 68.14814814814815
                  elif obj[13] == '=':
                     return 52.5
                  else:
                     return 77.23469387755102
               elif obj[10]<=-9.398184161012137:
                  # {"feature": "STime_A_VS_B_Max_Diff", "instances": 11, "metric_value": 8.4255, "depth": 6}
                  if obj[6]>-36:
                     # {"feature": "PTime_A_VS_B_Max", "instances": 8, "metric_value": 5.7942, "depth": 7}
                     if obj[11] == '<':
                        return 43.75
                     elif obj[11] == '>':
                        return 46.0
                     elif obj[11] == '=':
                        return 15
                     else:
                        return 41.0
                  elif obj[6]<=-36:
                     return 79.33333333333333
                  else:
                     return 51.45454545454545
               else:
                  return 74.63302752293578
            elif obj[3] == '>':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 44, "metric_value": 2.9844, "depth": 5}
               if obj[8]>-18.0:
                  # {"feature": "STime_A_VS_B_Max", "instances": 43, "metric_value": 2.8383, "depth": 6}
                  if obj[5] == '<':
                     # {"feature": "PTime_A_VS_B_Min", "instances": 34, "metric_value": 4.0013, "depth": 7}
                     if obj[9] == '>':
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 23, "metric_value": 4.019, "depth": 8}
                        if obj[12]<=4:
                           # {"feature": "STime_A_VS_B_Min_Diff", "instances": 13, "metric_value": 11.018, "depth": 9}
                           if obj[4]<=9:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 9, "metric_value": 9.9695, "depth": 10}
                              if obj[2]>-20.33333333333333:
                                 return 128.14285714285714
                              elif obj[2]<=-20.33333333333333:
                                 return 73.0
                              else:
                                 return 115.88888888888889
                           elif obj[4]>9:
                              return 172.25
                           else:
                              return 133.23076923076923
                        elif obj[12]>4:
                           # {"feature": "Due_A_VS_B", "instances": 10, "metric_value": 7.5355, "depth": 9}
                           if obj[13] == '>':
                              # {"feature": "STime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 5.5849, "depth": 10}
                              if obj[4]<=15:
                                 return 109.5
                              elif obj[4]>15:
                                 return 91.5
                              else:
                                 return 103.5
                           elif obj[13] == '<':
                              return 90.0
                           else:
                              return 98.1
                        else:
                           return 117.95652173913044
                     elif obj[9] == '<':
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 10, "metric_value": 12.2481, "depth": 8}
                        if obj[12]>-13:
                           # {"feature": "STime_A_VS_B_Max_Diff", "instances": 7, "metric_value": 15.6789, "depth": 9}
                           if obj[6]>-15:
                              return 125.5
                           elif obj[6]<=-15:
                              return 66.66666666666667
                           else:
                              return 100.28571428571429
                        elif obj[12]<=-13:
                           return 47.0
                        else:
                           return 84.3
                     elif obj[9] == '=':
                        return 151
                     else:
                        return 109.02941176470588
                  elif obj[5] == '>':
                     # {"feature": "PTime_A_VS_B_Max", "instances": 7, "metric_value": 16.6962, "depth": 7}
                     if obj[11] == '>':
                        return 71.66666666666667
                     elif obj[11] == '=':
                        return 140.0
                     elif obj[11] == '<':
                        return 94
                     else:
                        return 104.14285714285714
                  elif obj[5] == '=':
                     return 45.5
                  else:
                     return 105.27906976744185
               elif obj[8]<=-18.0:
                  return 206
               else:
                  return 107.56818181818181
            elif obj[3] == '<':
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 25, "metric_value": 9.5038, "depth": 5}
               if obj[2]>-15.733333333333333:
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 15, "metric_value": 9.564, "depth": 6}
                  if obj[12]<=1:
                     # {"feature": "STime_A_VS_B_Min_Diff", "instances": 12, "metric_value": 8.2631, "depth": 7}
                     if obj[4]<=-6:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 7, "metric_value": 8.1254, "depth": 8}
                        if obj[10]<=8:
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 6, "metric_value": 7.0329, "depth": 9}
                           if obj[7] == '>':
                              return 143.0
                           elif obj[7] == '<':
                              return 153
                           elif obj[7] == '=':
                              return 120
                           else:
                              return 140.83333333333334
                        elif obj[10]>8:
                           return 182
                        else:
                           return 146.71428571428572
                     elif obj[4]>-6:
                        # {"feature": "Due_A_VS_B", "instances": 5, "metric_value": 13.0386, "depth": 8}
                        if obj[13] == '>':
                           return 94.25
                        elif obj[13] == '<':
                           return 163
                        else:
                           return 108.0
                     else:
                        return 130.58333333333334
                  elif obj[12]>1:
                     return 63.333333333333336
                  else:
                     return 117.13333333333334
               elif obj[2]<=-15.733333333333333:
                  # {"feature": "PTime_A_VS_B_Max", "instances": 10, "metric_value": 8.571, "depth": 6}
                  if obj[11] == '<':
                     # {"feature": "STime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 8.0123, "depth": 7}
                     if obj[4]>-12:
                        return 68.75
                     elif obj[4]<=-12:
                        return 98.0
                     else:
                        return 78.5
                  elif obj[11] == '=':
                     return 43.5
                  elif obj[11] == '>':
                     return 60.5
                  else:
                     return 67.9
               else:
                  return 97.44
            else:
               return 85.97752808988764
         elif obj[14]>62.04899135446686:
            # {"feature": "PTime_A_VS_B_Avg", "instances": 169, "metric_value": 1.7026, "depth": 4}
            if obj[7] == '<':
               # {"feature": "PTime_A_VS_B_Max", "instances": 94, "metric_value": 2.2581, "depth": 5}
               if obj[11] == '<':
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 68, "metric_value": 1.4835, "depth": 6}
                  if obj[12]<=-2:
                     # {"feature": "STime_A_VS_B_Min_Diff", "instances": 63, "metric_value": 2.1429, "depth": 7}
                     if obj[4]<=5:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 56, "metric_value": 2.6346, "depth": 8}
                        if obj[10]<=9.140028011177286:
                           # {"feature": "STime_A_VS_B_Min", "instances": 55, "metric_value": 2.1196, "depth": 9}
                           if obj[3] == '=':
                              # {"feature": "PTime_A_VS_B_Min", "instances": 42, "metric_value": 1.8461, "depth": 10}
                              if obj[9] == '<':
                                 return 107.54054054054055
                              elif obj[9] == '>':
                                 return 113.5
                              elif obj[9] == '=':
                                 return 122
                              else:
                                 return 108.45238095238095
                           elif obj[3] == '<':
                              # {"feature": "PTime_A_VS_B_Min", "instances": 9, "metric_value": 12.3896, "depth": 10}
                              if obj[9] == '=':
                                 return 96.33333333333333
                              elif obj[9] == '>':
                                 return 108.0
                              elif obj[9] == '<':
                                 return 153.66666666666666
                              else:
                                 return 119.33333333333333
                           elif obj[3] == '>':
                              return 71.5
                           else:
                              return 107.54545454545455
                        elif obj[10]>9.140028011177286:
                           return 212
                        else:
                           return 109.41071428571429
                     elif obj[4]>5:
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 7, "metric_value": 27.8249, "depth": 8}
                        if obj[6]>-24:
                           return 115.25
                        elif obj[6]<=-24:
                           return 202.66666666666666
                        else:
                           return 152.71428571428572
                     else:
                        return 114.22222222222223
                  elif obj[12]>-2:
                     # {"feature": "PTime_A_VS_B_Min", "instances": 5, "metric_value": 22.1943, "depth": 7}
                     if obj[9] == '<':
                        return 134.33333333333334
                     elif obj[9] == '=':
                        return 162
                     elif obj[9] == '>':
                        return 224
                     else:
                        return 157.8
                  else:
                     return 117.42647058823529
               elif obj[11] == '>':
                  # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 23, "metric_value": 5.3386, "depth": 6}
                  if obj[10]<=-2:
                     # {"feature": "STime_A_VS_B_Min", "instances": 16, "metric_value": 7.3091, "depth": 7}
                     if obj[3] == '=':
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 11, "metric_value": 11.9368, "depth": 8}
                        if obj[8]<=-0.6666666666666643:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 10, "metric_value": 9.0287, "depth": 9}
                           if obj[2]>-18.666666666666664:
                              # {"feature": "STime_A_VS_B_Max_Diff", "instances": 9, "metric_value": 7.0422, "depth": 10}
                              if obj[6]>-27:
                                 return 143.0
                              elif obj[6]<=-27:
                                 return 178.0
                              else:
                                 return 158.55555555555554
                           elif obj[2]<=-18.666666666666664:
                              return 86
                           else:
                              return 151.3
                        elif obj[8]>-0.6666666666666643:
                           return 53
                        else:
                           return 142.36363636363637
                     elif obj[3] == '>':
                        return 176.33333333333334
                     elif obj[3] == '<':
                        return 188.5
                     else:
                        return 154.5
                  elif obj[10]>-2:
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 10.7992, "depth": 7}
                     if obj[8]>-2.6666666666666714:
                        return 97.75
                     elif obj[8]<=-2.6666666666666714:
                        return 135.66666666666666
                     else:
                        return 114.0
                  else:
                     return 142.17391304347825
               elif obj[11] == '=':
                  return 170.0
               else:
                  return 125.15957446808511
            elif obj[7] == '>':
               # {"feature": "STime_A_VS_B_Max", "instances": 73, "metric_value": 3.3581, "depth": 5}
               if obj[5] == '<':
                  # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 63, "metric_value": 2.4416, "depth": 6}
                  if obj[10]<=5.190476190476191:
                     # {"feature": "PTime_A_VS_B_Min", "instances": 33, "metric_value": 1.9105, "depth": 7}
                     if obj[9] == '<':
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 17, "metric_value": 3.4812, "depth": 8}
                        if obj[8]<=7.666666666666671:
                           # {"feature": "STime_A_VS_B_Max_Diff", "instances": 16, "metric_value": 4.0663, "depth": 9}
                           if obj[6]>-24:
                              # {"feature": "STime_A_VS_B_Min", "instances": 9, "metric_value": 10.2632, "depth": 10}
                              if obj[3] == '=':
                                 return 103.16666666666667
                              elif obj[3] == '>':
                                 return 56.666666666666664
                              else:
                                 return 87.66666666666667
                           elif obj[6]<=-24:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 7, "metric_value": 8.3588, "depth": 10}
                              if obj[11] == '>':
                                 return 127.25
                              elif obj[11] == '<':
                                 return 112.0
                              elif obj[11] == '=':
                                 return 81
                              else:
                                 return 116.28571428571429
                           else:
                              return 100.1875
                        elif obj[8]>7.666666666666671:
                           return 45
                        else:
                           return 96.94117647058823
                     elif obj[9] == '>':
                        # {"feature": "PTime_A_VS_B_Max", "instances": 13, "metric_value": 7.4249, "depth": 8}
                        if obj[11] == '>':
                           # {"feature": "STime_A_VS_B_Min", "instances": 8, "metric_value": 11.1588, "depth": 9}
                           if obj[3] == '=':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 12.9163, "depth": 10}
                              if obj[8]>1.0:
                                 return 62.666666666666664
                              elif obj[8]<=1.0:
                                 return 19.0
                              else:
                                 return 45.2
                           elif obj[3] == '>':
                              return 72.5
                           elif obj[3] == '<':
                              return 115
                           else:
                              return 60.75
                        elif obj[11] == '<':
                           return 122.33333333333333
                        elif obj[11] == '=':
                           return 81.5
                        else:
                           return 78.15384615384616
                     elif obj[9] == '=':
                        return 102.66666666666667
                     else:
                        return 90.06060606060606
                  elif obj[10]>5.190476190476191:
                     # {"feature": "STime_A_VS_B_Max_Diff", "instances": 30, "metric_value": 5.5735, "depth": 7}
                     if obj[6]>-21.933333333333334:
                        # {"feature": "STime_A_VS_B_Min_Diff", "instances": 16, "metric_value": 9.622, "depth": 8}
                        if obj[4]>-3:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 14, "metric_value": 12.1448, "depth": 9}
                           if obj[2]<=-1.3333333333333357:
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 12, "metric_value": 5.2719, "depth": 10}
                              if obj[12]<=10:
                                 return 169.36363636363637
                              elif obj[12]>10:
                                 return 107
                              else:
                                 return 164.16666666666666
                           elif obj[2]>-1.3333333333333357:
                              return 70.0
                           else:
                              return 150.71428571428572
                        elif obj[4]<=-3:
                           return 59.0
                        else:
                           return 139.25
                     elif obj[6]<=-21.933333333333334:
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 14, "metric_value": 16.5722, "depth": 8}
                        if obj[2]<=-3.666666666666664:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 13, "metric_value": 9.2522, "depth": 9}
                           if obj[12]>-3:
                              # {"feature": "STime_A_VS_B_Min", "instances": 11, "metric_value": 2.7144, "depth": 10}
                              if obj[3] == '=':
                                 return 75.8
                              elif obj[3] == '<':
                                 return 104
                              else:
                                 return 78.36363636363636
                           elif obj[12]<=-3:
                              return 129.0
                           else:
                              return 86.15384615384616
                        elif obj[2]>-3.666666666666664:
                           return 208
                        else:
                           return 94.85714285714286
                     else:
                        return 118.53333333333333
                  else:
                     return 103.61904761904762
               elif obj[5] == '>':
                  # {"feature": "STime_A_VS_B_Min", "instances": 9, "metric_value": 8.399, "depth": 6}
                  if obj[3] == '<':
                     # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 6.9038, "depth": 7}
                     if obj[2]>-8.666666666666664:
                        return 99.33333333333333
                     elif obj[2]<=-8.666666666666664:
                        return 80
                     else:
                        return 91.6
                  elif obj[3] == '=':
                     return 78.0
                  elif obj[3] == '>':
                     return 41
                  else:
                     return 81.44444444444444
               elif obj[5] == '=':
                  return 207
               else:
                  return 102.3013698630137
            elif obj[7] == '=':
               return 174.0
            else:
               return 115.86390532544378
         else:
            return 100.53314121037464
      elif obj[0]<=11:
         # {"feature": "STime_A_VS_B_Max_Diff", "instances": 339, "metric_value": 0.9986, "depth": 3}
         if obj[6]>-36.98304547491777:
            # {"feature": "STime_A_VS_B_Min_Diff", "instances": 276, "metric_value": 0.9232, "depth": 4}
            if obj[4]>-18.47925732201054:
               # {"feature": "Due_A_VS_B_Diff", "instances": 266, "metric_value": 0.7301, "depth": 5}
               if obj[14]<=142.51067802511267:
                  # {"feature": "Due_A_VS_B", "instances": 260, "metric_value": 0.7066, "depth": 6}
                  if obj[13] == '>':
                     # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 165, "metric_value": 0.4623, "depth": 7}
                     if obj[2]>-13.804273718403014:
                        # {"feature": "PTime_A_VS_B_Max", "instances": 135, "metric_value": 0.7122, "depth": 8}
                        if obj[11] == '>':
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 70, "metric_value": 0.671, "depth": 9}
                           if obj[12]<=7:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 47, "metric_value": 1.2771, "depth": 10}
                              if obj[8]<=7.817536748935931:
                                 return 77.60526315789474
                              elif obj[8]>7.817536748935931:
                                 return 54.55555555555556
                              else:
                                 return 73.19148936170212
                           elif obj[12]>7:
                              # {"feature": "PTime_A_VS_B_Min", "instances": 23, "metric_value": 3.6813, "depth": 10}
                              if obj[9] == '>':
                                 return 78.8125
                              elif obj[9] == '<':
                                 return 116.0
                              elif obj[9] == '=':
                                 return 86.0
                              else:
                                 return 87.52173913043478
                           else:
                              return 77.9
                        elif obj[11] == '<':
                           # {"feature": "STime_A_VS_B_Min", "instances": 59, "metric_value": 1.697, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 27, "metric_value": 4.0947, "depth": 10}
                              if obj[10]<=3:
                                 return 84.0
                              elif obj[10]>3:
                                 return 48.6
                              else:
                                 return 77.44444444444444
                           elif obj[3] == '=':
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 21, "metric_value": 4.6962, "depth": 10}
                              if obj[12]>-5:
                                 return 45.18181818181818
                              elif obj[12]<=-5:
                                 return 69.7
                              else:
                                 return 56.857142857142854
                           elif obj[3] == '<':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 11, "metric_value": 6.4773, "depth": 10}
                              if obj[10]>-5:
                                 return 54.77777777777778
                              elif obj[10]<=-5:
                                 return 105.5
                              else:
                                 return 64.0
                           else:
                              return 67.61016949152543
                        elif obj[11] == '=':
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 17.0744, "depth": 9}
                           if obj[8]>-5.666666666666664:
                              # {"feature": "PTime_A_VS_B_Min", "instances": 5, "metric_value": 8.8303, "depth": 10}
                              if obj[9] == '<':
                                 return 55.333333333333336
                              elif obj[9] == '>':
                                 return 20.0
                              else:
                                 return 41.2
                           elif obj[8]<=-5.666666666666664:
                              return 124
                           else:
                              return 55.0
                        else:
                           return 72.38518518518518
                     elif obj[2]<=-13.804273718403014:
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 30, "metric_value": 2.3171, "depth": 8}
                        if obj[12]>-2:
                           # {"feature": "STime_A_VS_B_Min", "instances": 20, "metric_value": 3.4066, "depth": 9}
                           if obj[3] == '<':
                              # {"feature": "PTime_A_VS_B_Max", "instances": 8, "metric_value": 4.7734, "depth": 10}
                              if obj[11] == '>':
                                 return 59.0
                              elif obj[11] == '<':
                                 return 88
                              elif obj[11] == '=':
                                 return 62
                              else:
                                 return 63.0
                           elif obj[3] == '=':
                              # {"feature": "PTime_A_VS_B_Min", "instances": 7, "metric_value": 8.7827, "depth": 10}
                              if obj[9] == '<':
                                 return 90.0
                              elif obj[9] == '>':
                                 return 82.5
                              elif obj[9] == '=':
                                 return 81
                              else:
                                 return 86.57142857142857
                           elif obj[3] == '>':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 19.4266, "depth": 10}
                              if obj[8]<=0.3333333333333357:
                                 return 63.333333333333336
                              elif obj[8]>0.3333333333333357:
                                 return 127.5
                              else:
                                 return 89.0
                           else:
                              return 77.75
                        elif obj[12]<=-2:
                           # {"feature": "STime_A_VS_B_Min", "instances": 10, "metric_value": 15.5303, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 3.3833, "depth": 10}
                              if obj[10]>-3:
                                 return 91.33333333333333
                              elif obj[10]<=-3:
                                 return 101.33333333333333
                              else:
                                 return 96.33333333333333
                           elif obj[3] == '<':
                              return 155.5
                           elif obj[3] == '=':
                              return 77.5
                           else:
                              return 104.4
                        else:
                           return 86.63333333333334
                     else:
                        return 74.97575757575757
                  elif obj[13] == '<':
                     # {"feature": "PTime_A_VS_B_Max", "instances": 92, "metric_value": 2.2272, "depth": 7}
                     if obj[11] == '<':
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 45, "metric_value": 2.691, "depth": 8}
                        if obj[2]>-12.096457324174292:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 38, "metric_value": 3.2313, "depth": 9}
                           if obj[12]<=-2:
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 35, "metric_value": 2.0457, "depth": 10}
                              if obj[10]<=5:
                                 return 77.0
                              elif obj[10]>5:
                                 return 32.5
                              else:
                                 return 74.45714285714286
                           elif obj[12]>-2:
                              return 139.0
                           else:
                              return 79.55263157894737
                        elif obj[2]<=-12.096457324174292:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 7, "metric_value": 12.8172, "depth": 9}
                           if obj[12]>-15:
                              # {"feature": "PTime_A_VS_B_Min", "instances": 6, "metric_value": 13.5899, "depth": 10}
                              if obj[9] == '<':
                                 return 117.5
                              elif obj[9] == '=':
                                 return 66
                              elif obj[9] == '>':
                                 return 132
                              else:
                                 return 111.33333333333333
                           elif obj[12]<=-15:
                              return 184
                           else:
                              return 121.71428571428571
                        else:
                           return 86.11111111111111
                     elif obj[11] == '>':
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 42, "metric_value": 5.0235, "depth": 8}
                        if obj[12]>1:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 38, "metric_value": 4.6452, "depth": 9}
                           if obj[2]<=-2.951017159669939:
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 32, "metric_value": 2.042, "depth": 10}
                              if obj[10]<=11:
                                 return 55.46666666666667
                              elif obj[10]>11:
                                 return 95.0
                              else:
                                 return 57.9375
                           elif obj[2]>-2.951017159669939:
                              # {"feature": "STime_A_VS_B_Min", "instances": 6, "metric_value": 25.107, "depth": 10}
                              if obj[3] == '>':
                                 return 82.25
                              elif obj[3] == '<':
                                 return 148
                              elif obj[3] == '=':
                                 return 157
                              else:
                                 return 105.66666666666667
                           else:
                              return 65.47368421052632
                        elif obj[12]<=1:
                           return 126.0
                        else:
                           return 71.23809523809524
                     elif obj[11] == '=':
                        # {"feature": "STime_A_VS_B_Min", "instances": 5, "metric_value": 10.6794, "depth": 8}
                        if obj[3] == '<':
                           return 49.333333333333336
                        elif obj[3] == '>':
                           return 22
                        elif obj[3] == '=':
                           return 24
                        else:
                           return 38.8
                     else:
                        return 76.75
                  elif obj[13] == '=':
                     return 46.666666666666664
                  else:
                     return 75.27692307692308
               elif obj[14]>142.51067802511267:
                  # {"feature": "PTime_A_VS_B_Min", "instances": 6, "metric_value": 20.0864, "depth": 6}
                  if obj[9] == '>':
                     return 159.33333333333334
                  elif obj[9] == '<':
                     return 94.0
                  else:
                     return 126.66666666666667
               else:
                  return 76.43609022556392
            elif obj[4]<=-18.47925732201054:
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 10, "metric_value": 6.3678, "depth": 5}
               if obj[2]<=-4.666666666666664:
                  # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 9, "metric_value": 3.2116, "depth": 6}
                  if obj[8]<=4.0:
                     # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 8.7972, "depth": 7}
                     if obj[12]>-8:
                        return 46.25
                     elif obj[12]<=-8:
                        return 15.5
                     else:
                        return 36.0
                  elif obj[8]>4.0:
                     return 15.666666666666666
                  else:
                     return 29.22222222222222
               elif obj[2]>-4.666666666666664:
                  return 78
               else:
                  return 34.1
            else:
               return 74.90217391304348
         elif obj[6]<=-36.98304547491777:
            # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 63, "metric_value": 2.256, "depth": 4}
            if obj[10]<=8.005950057618323:
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 58, "metric_value": 1.6135, "depth": 5}
               if obj[2]>-18.75862068965517:
                  # {"feature": "PTime_A_VS_B_Min", "instances": 30, "metric_value": 3.5491, "depth": 6}
                  if obj[9] == '<':
                     # {"feature": "STime_A_VS_B_Min", "instances": 16, "metric_value": 8.1849, "depth": 7}
                     if obj[3] == '=':
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 9, "metric_value": 6.1808, "depth": 8}
                        if obj[8]<=-4.666666666666671:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 6.2271, "depth": 9}
                           if obj[12]<=-8:
                              return 22.75
                           elif obj[12]>-8:
                              return 46.0
                           else:
                              return 30.5
                        elif obj[8]>-4.666666666666671:
                           return 5.333333333333333
                        else:
                           return 22.11111111111111
                     elif obj[3] == '>':
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 9.4304, "depth": 8}
                        if obj[8]<=2.6666666666666643:
                           return 65.5
                        elif obj[8]>2.6666666666666643:
                           return 35
                        else:
                           return 59.4
                     elif obj[3] == '<':
                        return 39.5
                     else:
                        return 35.9375
                  elif obj[9] == '>':
                     # {"feature": "STime_A_VS_B_Min", "instances": 12, "metric_value": 8.2431, "depth": 7}
                     if obj[3] == '=':
                        # {"feature": "Due_A_VS_B_Diff", "instances": 7, "metric_value": 24.91, "depth": 8}
                        if obj[14]>-96:
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 6, "metric_value": 5.3168, "depth": 9}
                           if obj[7] == '<':
                              return 43.25
                           elif obj[7] == '>':
                              return 67.5
                           else:
                              return 51.333333333333336
                        elif obj[14]<=-96:
                           return 157
                        else:
                           return 66.42857142857143
                     elif obj[3] == '>':
                        return 28.333333333333332
                     elif obj[3] == '<':
                        return 64.5
                     else:
                        return 56.583333333333336
                  elif obj[9] == '=':
                     return 19.0
                  else:
                     return 43.06666666666667
               elif obj[2]<=-18.75862068965517:
                  # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 28, "metric_value": 1.9159, "depth": 6}
                  if obj[8]>1.5476190476190481:
                     # {"feature": "Due_A_VS_B_Diff", "instances": 15, "metric_value": 6.6224, "depth": 7}
                     if obj[14]>-29:
                        # {"feature": "STime_A_VS_B_Min", "instances": 10, "metric_value": 11.6556, "depth": 8}
                        if obj[3] == '=':
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 2.3773, "depth": 9}
                           if obj[12]<=18:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 5, "metric_value": 1.9049, "depth": 10}
                              if obj[11] == '>':
                                 return 49.0
                              elif obj[11] == '<':
                                 return 57
                              else:
                                 return 50.6
                           elif obj[12]>18:
                              return 35
                           else:
                              return 48.0
                        elif obj[3] == '>':
                           return 92.5
                        elif obj[3] == '<':
                           return 89.0
                        else:
                           return 65.1
                     elif obj[14]<=-29:
                        # {"feature": "STime_A_VS_B_Min", "instances": 5, "metric_value": 5.8221, "depth": 8}
                        if obj[3] == '<':
                           return 35.0
                        elif obj[3] == '=':
                           return 12
                        else:
                           return 30.4
                     else:
                        return 53.53333333333333
                  elif obj[8]<=1.5476190476190481:
                     # {"feature": "PTime_A_VS_B_Max", "instances": 13, "metric_value": 5.4702, "depth": 7}
                     if obj[11] == '<':
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 4.5471, "depth": 8}
                        if obj[12]<=-2:
                           # {"feature": "STime_A_VS_B_Min", "instances": 5, "metric_value": 7.5447, "depth": 9}
                           if obj[3] == '>':
                              return 77.5
                           elif obj[3] == '=':
                              return 57.0
                           elif obj[3] == '<':
                              return 72
                           else:
                              return 68.2
                        elif obj[12]>-2:
                           return 44
                        else:
                           return 64.16666666666667
                     elif obj[11] == '>':
                        # {"feature": "STime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 6.6897, "depth": 8}
                        if obj[4]>-17:
                           # {"feature": "Due_A_VS_B_Diff", "instances": 5, "metric_value": 7.033, "depth": 9}
                           if obj[14]<=35:
                              return 73.0
                           elif obj[14]>35:
                              return 53.0
                           else:
                              return 65.0
                        elif obj[4]<=-17:
                           return 98
                        else:
                           return 70.5
                     elif obj[11] == '=':
                        return 113
                     else:
                        return 70.84615384615384
                  else:
                     return 61.57142857142857
               else:
                  return 52.0
            elif obj[10]>8.005950057618323:
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 3.6647, "depth": 5}
               if obj[2]>-17.333333333333336:
                  return 82.66666666666667
               elif obj[2]<=-17.333333333333336:
                  return 94.0
               else:
                  return 87.2
            else:
               return 54.79365079365079
         else:
            return 71.16519174041298
      else:
         return 86.0204081632653
   elif obj[1] == '=':
      # {"feature": "Due_A_VS_B_Diff", "instances": 402, "metric_value": 3.6802, "depth": 2}
      if obj[14]>46.62686567164179:
         # {"feature": "NumWaitingJob", "instances": 201, "metric_value": 2.4688, "depth": 3}
         if obj[0]>11:
            # {"feature": "PTime_A_VS_B_Max", "instances": 170, "metric_value": 1.5631, "depth": 4}
            if obj[11] == '<':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 81, "metric_value": 1.2043, "depth": 5}
               if obj[8]<=6.328783852578465:
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 79, "metric_value": 0.7111, "depth": 6}
                  if obj[12]>-23:
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 78, "metric_value": 0.5223, "depth": 7}
                     if obj[10]>-23:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 77, "metric_value": 0.466, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 55, "metric_value": 3.2459, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 53, "metric_value": 0.0, "depth": 10}
                              if obj[2]<=0.0:
                                 return 82.90566037735849
                              else:
                                 return 82.90566037735849
                           elif obj[7] == '=':
                              return 66
                           elif obj[7] == '>':
                              return 188
                           else:
                              return 84.50909090909092
                        elif obj[9] == '>':
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 20, "metric_value": 2.0602, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 12, "metric_value": 0.0, "depth": 10}
                              if obj[2]<=0.0:
                                 return 89.75
                              else:
                                 return 89.75
                           elif obj[7] == '>':
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[2]<=0.0:
                                 return 80.125
                              else:
                                 return 80.125
                           else:
                              return 85.9
                        elif obj[9] == '=':
                           return 89.5
                        else:
                           return 85.0
                     elif obj[10]<=-23:
                        return 126
                     else:
                        return 85.52564102564102
                  elif obj[12]<=-23:
                     return 31
                  else:
                     return 84.83544303797468
               elif obj[8]>6.328783852578465:
                  return 143.0
               else:
                  return 86.27160493827161
            elif obj[11] == '>':
               # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 80, "metric_value": 0.8348, "depth": 5}
               if obj[10]>-18:
                  # {"feature": "PTime_A_VS_B_Avg", "instances": 79, "metric_value": 0.7081, "depth": 6}
                  if obj[7] == '>':
                     # {"feature": "PTime_A_VS_B_Min", "instances": 73, "metric_value": 0.4648, "depth": 7}
                     if obj[9] == '>':
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 43, "metric_value": 0.8949, "depth": 8}
                        if obj[12]<=15.989427971966123:
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 35, "metric_value": 2.6517, "depth": 9}
                           if obj[8]<=15.39100935751643:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 32, "metric_value": 0.0, "depth": 10}
                              if obj[2]<=0.0:
                                 return 72.84375
                              else:
                                 return 72.84375
                           elif obj[8]>15.39100935751643:
                              return 29.666666666666668
                           else:
                              return 69.14285714285714
                        elif obj[12]>15.989427971966123:
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 8, "metric_value": 6.0475, "depth": 9}
                           if obj[8]<=15.0:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[2]<=0.0:
                                 return 99.5
                              else:
                                 return 99.5
                           elif obj[8]>15.0:
                              return 54.0
                           else:
                              return 88.125
                        else:
                           return 72.67441860465117
                     elif obj[9] == '<':
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 26, "metric_value": 6.4427, "depth": 8}
                        if obj[8]<=4.666666666666664:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 21, "metric_value": 4.3767, "depth": 9}
                           if obj[12]>1:
                              # {"feature": "STime_A_VS_B_Max", "instances": 18, "metric_value": 1.288, "depth": 10}
                              if obj[5] == '=':
                                 return 93.05882352941177
                              elif obj[5] == '>':
                                 return 75
                              else:
                                 return 92.05555555555556
                           elif obj[12]<=1:
                              return 40.666666666666664
                           else:
                              return 84.71428571428571
                        elif obj[8]>4.666666666666664:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 5, "metric_value": 2.9165, "depth": 9}
                           if obj[12]<=17:
                              return 38.0
                           elif obj[12]>17:
                              return 51
                           else:
                              return 40.6
                        else:
                           return 76.23076923076923
                     elif obj[9] == '=':
                        return 58.75
                     else:
                        return 73.17808219178082
                  elif obj[7] == '<':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 3.5219, "depth": 7}
                     if obj[8]<=-2.0:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 5, "metric_value": 2.171, "depth": 8}
                        if obj[9] == '<':
                           return 60.0
                        elif obj[9] == '>':
                           return 48
                        else:
                           return 57.6
                     elif obj[8]>-2.0:
                        return 79
                     else:
                        return 61.166666666666664
                  else:
                     return 72.26582278481013
               elif obj[10]<=-18:
                  return 12
               else:
                  return 71.5125
            elif obj[11] == '=':
               # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 9, "metric_value": 16.0816, "depth": 5}
               if obj[10]>-7:
                  # {"feature": "STime_A_VS_B_Max", "instances": 6, "metric_value": 13.323, "depth": 6}
                  if obj[5] == '=':
                     return 129.0
                  elif obj[5] == '<':
                     return 137
                  elif obj[5] == '>':
                     return 192
                  else:
                     return 140.83333333333334
               elif obj[10]<=-7:
                  return 64.33333333333333
               else:
                  return 115.33333333333333
            else:
               return 80.86470588235294
         elif obj[0]<=11:
            # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 31, "metric_value": 1.6255, "depth": 4}
            if obj[8]<=7.391567289252913:
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 24, "metric_value": 1.7759, "depth": 5}
               if obj[12]>-8:
                  # {"feature": "STime_A_VS_B_Min", "instances": 16, "metric_value": 1.5389, "depth": 6}
                  if obj[3] == '=':
                     # {"feature": "PTime_A_VS_B_Max", "instances": 15, "metric_value": 1.8191, "depth": 7}
                     if obj[11] == '>':
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 5.6542, "depth": 8}
                        if obj[10]<=10:
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 5, "metric_value": 3.3658, "depth": 9}
                           if obj[7] == '>':
                              return 46.5
                           elif obj[7] == '<':
                              return 58
                           else:
                              return 48.8
                        elif obj[10]>10:
                           return 12
                        else:
                           return 42.666666666666664
                     elif obj[11] == '<':
                        # {"feature": "PTime_A_VS_B_Avg", "instances": 6, "metric_value": 3.6556, "depth": 8}
                        if obj[7] == '>':
                           return 45.0
                        elif obj[7] == '<':
                           return 65.0
                        else:
                           return 55.0
                     elif obj[11] == '=':
                        return 41.666666666666664
                     else:
                        return 47.4
                  elif obj[3] == '>':
                     return 22
                  else:
                     return 45.8125
               elif obj[12]<=-8:
                  # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 8, "metric_value": 2.9909, "depth": 6}
                  if obj[10]<=4:
                     # {"feature": "PTime_A_VS_B_Min", "instances": 7, "metric_value": 1.1668, "depth": 7}
                     if obj[9] == '<':
                        # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[2]<=0.0:
                           # {"feature": "STime_A_VS_B_Min", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '=':
                              # {"feature": "STime_A_VS_B_Min_Diff", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=0:
                                 return 38.2
                              else:
                                 return 38.2
                           else:
                              return 38.2
                        else:
                           return 38.2
                     elif obj[9] == '=':
                        return 41
                     elif obj[9] == '>':
                        return 43
                     else:
                        return 39.285714285714285
                  elif obj[10]>4:
                     return 21
                  else:
                     return 37.0
               else:
                  return 42.875
            elif obj[8]>7.391567289252913:
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 7, "metric_value": 5.3882, "depth": 5}
               if obj[12]>5:
                  # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 5, "metric_value": 6.0285, "depth": 6}
                  if obj[10]<=8:
                     return 65.75
                  elif obj[10]>8:
                     return 95
                  else:
                     return 71.6
               elif obj[12]<=5:
                  return 40.5
               else:
                  return 62.714285714285715
            else:
               return 47.354838709677416
         else:
            return 75.69651741293532
      elif obj[14]<=46.62686567164179:
         # {"feature": "STime_A_VS_B_Max", "instances": 201, "metric_value": 1.4755, "depth": 3}
         if obj[5] == '=':
            # {"feature": "NumWaitingJob", "instances": 193, "metric_value": 1.3522, "depth": 4}
            if obj[0]>11:
               # {"feature": "PTime_A_VS_B_Avg", "instances": 167, "metric_value": 1.065, "depth": 5}
               if obj[7] == '>':
                  # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 85, "metric_value": 2.4546, "depth": 6}
                  if obj[10]>-1.424808052793085:
                     # {"feature": "PTime_A_VS_B_Min", "instances": 72, "metric_value": 1.0145, "depth": 7}
                     if obj[9] == '>':
                        # {"feature": "PTime_A_VS_B_Max", "instances": 64, "metric_value": 0.8445, "depth": 8}
                        if obj[11] == '>':
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 55, "metric_value": 1.27, "depth": 9}
                           if obj[12]<=12:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 50, "metric_value": 0.6551, "depth": 10}
                              if obj[8]<=13.019788132026903:
                                 return 46.95918367346939
                              elif obj[8]>13.019788132026903:
                                 return 14
                              else:
                                 return 46.3
                           elif obj[12]>12:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 2.256, "depth": 10}
                              if obj[8]<=10.666666666666671:
                                 return 67.5
                              elif obj[8]>10.666666666666671:
                                 return 56
                              else:
                                 return 65.2
                           else:
                              return 48.018181818181816
                        elif obj[11] == '<':
                           # {"feature": "Due_A_VS_B", "instances": 7, "metric_value": 15.0719, "depth": 9}
                           if obj[13] == '>':
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 15.5057, "depth": 10}
                              if obj[8]>0.3333333333333286:
                                 return 77.0
                              elif obj[8]<=0.3333333333333286:
                                 return 31
                              else:
                                 return 67.8
                           elif obj[13] == '<':
                              return 12.0
                           else:
                              return 51.857142857142854
                        elif obj[11] == '=':
                           return 76.0
                        else:
                           return 49.3125
                     elif obj[9] == '<':
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 8.949, "depth": 8}
                        if obj[8]>1.6666666666666643:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 5, "metric_value": 3.2874, "depth": 9}
                           if obj[12]<=10:
                              return 27.666666666666668
                           elif obj[12]>10:
                              return 33.0
                           else:
                              return 29.8
                        elif obj[8]<=1.6666666666666643:
                           return 76
                        else:
                           return 37.5
                     elif obj[9] == '=':
                        return 13.5
                     else:
                        return 47.333333333333336
                  elif obj[10]<=-1.424808052793085:
                     # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 13, "metric_value": 8.2485, "depth": 7}
                     if obj[12]<=12:
                        # {"feature": "Due_A_VS_B", "instances": 11, "metric_value": 11.4165, "depth": 8}
                        if obj[13] == '>':
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 8.788, "depth": 9}
                           if obj[8]>1.6666666666666643:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[2]<=0.0:
                                 return 75.33333333333333
                              else:
                                 return 75.33333333333333
                           elif obj[8]<=1.6666666666666643:
                              return 120
                           else:
                              return 81.71428571428571
                        elif obj[13] == '<':
                           return 77.75
                        else:
                           return 80.27272727272727
                     elif obj[12]>12:
                        return 14.5
                     else:
                        return 70.15384615384616
                  else:
                     return 50.8235294117647
               elif obj[7] == '<':
                  # {"feature": "Due_A_VS_B", "instances": 79, "metric_value": 0.8439, "depth": 6}
                  if obj[13] == '<':
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 40, "metric_value": 1.2768, "depth": 7}
                     if obj[10]<=1:
                        # {"feature": "PTime_A_VS_B_Max", "instances": 37, "metric_value": 1.2794, "depth": 8}
                        if obj[11] == '<':
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 33, "metric_value": 1.8204, "depth": 9}
                           if obj[8]<=-0.3627290308092288:
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 32, "metric_value": 1.081, "depth": 10}
                              if obj[12]>-16:
                                 return 34.07142857142857
                              elif obj[12]<=-16:
                                 return 52.75
                              else:
                                 return 36.40625
                           elif obj[8]>-0.3627290308092288:
                              return 82
                           else:
                              return 37.78787878787879
                        elif obj[11] == '>':
                           return 18.75
                        else:
                           return 35.729729729729726
                     elif obj[10]>1:
                        return 12.333333333333334
                     else:
                        return 33.975
                  elif obj[13] == '>':
                     # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 37, "metric_value": 1.6896, "depth": 7}
                     if obj[10]<=-7.486486486486487:
                        # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 21, "metric_value": 3.2628, "depth": 8}
                        if obj[8]<=-2.6666666666666643:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 19, "metric_value": 2.7323, "depth": 9}
                           if obj[12]>-9:
                              # {"feature": "PTime_A_VS_B_Max", "instances": 12, "metric_value": 4.3769, "depth": 10}
                              if obj[11] == '<':
                                 return 63.77777777777778
                              elif obj[11] == '=':
                                 return 28.0
                              elif obj[11] == '>':
                                 return 72
                              else:
                                 return 58.5
                           elif obj[12]<=-9:
                              # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[2]<=0.0:
                                 return 44.285714285714285
                              else:
                                 return 44.285714285714285
                           else:
                              return 53.26315789473684
                        elif obj[8]>-2.6666666666666643:
                           return 12.5
                        else:
                           return 49.38095238095238
                     elif obj[10]>-7.486486486486487:
                        # {"feature": "PTime_A_VS_B_Min", "instances": 16, "metric_value": 3.4833, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 8, "metric_value": 1.6292, "depth": 9}
                           if obj[12]<=-4:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 6, "metric_value": 5.0071, "depth": 10}
                              if obj[8]>-6.666666666666664:
                                 return 26.0
                              elif obj[8]<=-6.666666666666664:
                                 return 43.333333333333336
                              else:
                                 return 34.666666666666664
                           elif obj[12]>-4:
                              return 45.5
                           else:
                              return 37.375
                        elif obj[9] == '>':
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 7.8654, "depth": 9}
                           if obj[8]>-3.666666666666664:
                              return 41.5
                           elif obj[8]<=-3.666666666666664:
                              return 13.666666666666666
                           else:
                              return 29.571428571428573
                        elif obj[9] == '=':
                           return 61
                        else:
                           return 35.4375
                     else:
                        return 43.351351351351354
                  elif obj[13] == '=':
                     return 44.0
                  else:
                     return 38.620253164556964
               elif obj[7] == '=':
                  return 33.666666666666664
               else:
                  return 44.74251497005988
            elif obj[0]<=11:
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 26, "metric_value": 1.3868, "depth": 5}
               if obj[12]>-12:
                  # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 24, "metric_value": 2.6302, "depth": 6}
                  if obj[8]<=3.0:
                     # {"feature": "Due_A_VS_B", "instances": 16, "metric_value": 1.7109, "depth": 7}
                     if obj[13] == '>':
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 12, "metric_value": 1.4751, "depth": 8}
                        if obj[10]<=2:
                           # {"feature": "PTime_A_VS_B_Max", "instances": 7, "metric_value": 0.9763, "depth": 9}
                           if obj[11] == '>':
                              return 15.666666666666666
                           elif obj[11] == '=':
                              return 18.5
                           elif obj[11] == '<':
                              return 15.0
                           else:
                              return 16.285714285714285
                        elif obj[10]>2:
                           # {"feature": "PTime_A_VS_B_Avg", "instances": 5, "metric_value": 3.5904, "depth": 9}
                           if obj[7] == '<':
                              return 31.0
                           elif obj[7] == '>':
                              return 19.5
                           else:
                              return 26.4
                        else:
                           return 20.5
                     elif obj[13] == '<':
                        return 9.0
                     else:
                        return 17.625
                  elif obj[8]>3.0:
                     # {"feature": "PTime_A_VS_B_Min", "instances": 8, "metric_value": 3.0432, "depth": 7}
                     if obj[9] == '>':
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 5.8244, "depth": 8}
                        if obj[10]>3:
                           # {"feature": "PTime_A_VS_B_Max", "instances": 5, "metric_value": 1.2339, "depth": 9}
                           if obj[11] == '>':
                              return 29.5
                           elif obj[11] == '<':
                              return 24
                           else:
                              return 28.4
                        elif obj[10]<=3:
                           return 57
                        else:
                           return 33.166666666666664
                     elif obj[9] == '<':
                        return 26
                     elif obj[9] == '=':
                        return 49
                     else:
                        return 34.25
                  else:
                     return 23.166666666666668
               elif obj[12]<=-12:
                  return 45.0
               else:
                  return 24.846153846153847
            else:
               return 42.06217616580311
         elif obj[5] == '>':
            # {"feature": "NumWaitingJob", "instances": 5, "metric_value": 18.3859, "depth": 4}
            if obj[0]<=8:
               return 26.666666666666668
            elif obj[0]>8:
               return 68.0
            else:
               return 43.2
         elif obj[5] == '<':
            return 118.33333333333333
         else:
            return 43.22885572139303
      else:
         return 59.46268656716418
   else:
      return 95.07377647918189
