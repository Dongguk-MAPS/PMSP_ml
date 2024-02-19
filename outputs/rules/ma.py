def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B, obj[2]: STime_A_VS_B_Diff, obj[3]: PTime_A_VS_B, obj[4]: PTime_A_VS_B_Diff, obj[5]: CompTime_A_VS_B, obj[6]: CompTime_A_VS_B_Diff, obj[7]: Start_A_VS_B, obj[8]: Start_A_VS_B_Diff, obj[9]: Tardy_A_VS_B, obj[10]: Tardy_A_VS_B_Diff
   # {"feature": "STime_A_VS_B_Diff", "instances": 7624, "metric_value": 9.4323, "depth": 1}
   if obj[2]<=20.046956977964324:
      # {"feature": "STime_A_VS_B", "instances": 4045, "metric_value": 3.0224, "depth": 2}
      if obj[1] == '<':
         # {"feature": "PTime_A_VS_B_Diff", "instances": 1460, "metric_value": 1.7633, "depth": 3}
         if obj[4]>4.405479452054794:
            # {"feature": "NumWaitingJob", "instances": 731, "metric_value": 2.437, "depth": 4}
            if obj[0]<=14:
               # {"feature": "Start_A_VS_B_Diff", "instances": 558, "metric_value": 3.8971, "depth": 5}
               if obj[8]>-124.24580335618326:
                  # {"feature": "Tardy_A_VS_B", "instances": 475, "metric_value": 2.9982, "depth": 6}
                  if obj[9] == '=':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 206, "metric_value": 1.9501, "depth": 7}
                     if obj[6]>-81.8030827538784:
                        # {"feature": "CompTime_A_VS_B", "instances": 180, "metric_value": 0.6496, "depth": 8}
                        if obj[5] == '<':
                           # {"feature": "Start_A_VS_B", "instances": 135, "metric_value": 1.921, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "PTime_A_VS_B", "instances": 132, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 87.88636363636364
                              else:
                                 return 87.88636363636364
                           elif obj[7] == '>':
                              return 4.666666666666667
                           else:
                              return 86.03703703703704
                        elif obj[5] == '>':
                           # {"feature": "Start_A_VS_B", "instances": 41, "metric_value": 8.8111, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "PTime_A_VS_B", "instances": 36, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 77.52777777777777
                              else:
                                 return 77.52777777777777
                           elif obj[7] == '<':
                              # {"feature": "PTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 176.2
                              else:
                                 return 176.2
                           else:
                              return 89.5609756097561
                        elif obj[5] == '=':
                           return 58.0
                        else:
                           return 86.21666666666667
                     elif obj[6]<=-81.8030827538784:
                        # {"feature": "PTime_A_VS_B", "instances": 26, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 26, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 26, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 116.6923076923077
                              else:
                                 return 116.6923076923077
                           else:
                              return 116.6923076923077
                        else:
                           return 116.6923076923077
                     else:
                        return 90.0631067961165
                  elif obj[9] == '<':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 158, "metric_value": 1.2763, "depth": 7}
                     if obj[6]<=-37.123630419406254:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 131, "metric_value": 2.0071, "depth": 8}
                        if obj[10]>-43.274809160305345:
                           # {"feature": "PTime_A_VS_B", "instances": 73, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 73, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 86.15068493150685
                              else:
                                 return 86.15068493150685
                           else:
                              return 86.15068493150685
                        elif obj[10]<=-43.274809160305345:
                           # {"feature": "PTime_A_VS_B", "instances": 58, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 58, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 58.258620689655174
                              else:
                                 return 58.258620689655174
                           else:
                              return 58.258620689655174
                        else:
                           return 73.80152671755725
                     elif obj[6]>-37.123630419406254:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 27, "metric_value": 7.4187, "depth": 8}
                        if obj[10]>-34:
                           # {"feature": "Start_A_VS_B", "instances": 25, "metric_value": 0.6294, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "PTime_A_VS_B", "instances": 20, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 39.0
                              else:
                                 return 39.0
                           elif obj[7] == '>':
                              # {"feature": "PTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 38.2
                              else:
                                 return 38.2
                           else:
                              return 38.84
                        elif obj[10]<=-34:
                           return 125.5
                        else:
                           return 45.25925925925926
                     else:
                        return 68.92405063291139
                  elif obj[9] == '>':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 111, "metric_value": 1.441, "depth": 7}
                     if obj[6]>28.66004825578446:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 90, "metric_value": 0.947, "depth": 8}
                        if obj[10]>40.333938901261234:
                           # {"feature": "PTime_A_VS_B", "instances": 74, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 74, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 60.648648648648646
                              else:
                                 return 60.648648648648646
                           else:
                              return 60.648648648648646
                        elif obj[10]<=40.333938901261234:
                           # {"feature": "PTime_A_VS_B", "instances": 16, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 16, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 45.4375
                              else:
                                 return 45.4375
                           else:
                              return 45.4375
                        else:
                           return 57.94444444444444
                     elif obj[6]<=28.66004825578446:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 21, "metric_value": 2.9945, "depth": 8}
                        if obj[10]>5:
                           # {"feature": "Start_A_VS_B", "instances": 18, "metric_value": 3.5073, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "PTime_A_VS_B", "instances": 15, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 33.266666666666666
                              else:
                                 return 33.266666666666666
                           elif obj[7] == '<':
                              return 66.66666666666667
                           else:
                              return 38.833333333333336
                        elif obj[10]<=5:
                           return 10.0
                        else:
                           return 34.714285714285715
                     else:
                        return 53.549549549549546
                  else:
                     return 74.49894736842106
               elif obj[8]<=-124.24580335618326:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 83, "metric_value": 3.5243, "depth": 6}
                  if obj[10]>-161.01392804128062:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 69, "metric_value": 3.7783, "depth": 7}
                     if obj[6]>-208.06524527847512:
                        # {"feature": "Tardy_A_VS_B", "instances": 59, "metric_value": 0.683, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "PTime_A_VS_B", "instances": 52, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 52, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 136.76923076923077
                              else:
                                 return 136.76923076923077
                           else:
                              return 136.76923076923077
                        elif obj[9] == '=':
                           # {"feature": "PTime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 107.71428571428571
                              else:
                                 return 107.71428571428571
                           else:
                              return 107.71428571428571
                        else:
                           return 133.32203389830508
                     elif obj[6]<=-208.06524527847512:
                        # {"feature": "PTime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 191.1
                              else:
                                 return 191.1
                           else:
                              return 191.1
                        else:
                           return 191.1
                     else:
                        return 141.69565217391303
                  elif obj[10]<=-161.01392804128062:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 14, "metric_value": 29.6455, "depth": 7}
                     if obj[6]<=-201:
                        # {"feature": "PTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 121.66666666666667
                              else:
                                 return 121.66666666666667
                           else:
                              return 121.66666666666667
                        else:
                           return 121.66666666666667
                     elif obj[6]>-201:
                        # {"feature": "PTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 24.6
                              else:
                                 return 24.6
                           else:
                              return 24.6
                        else:
                           return 24.6
                     else:
                        return 87.0
                  else:
                     return 132.46987951807228
               else:
                  return 83.12186379928315
            elif obj[0]>14:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 173, "metric_value": 4.1264, "depth": 5}
               if obj[10]<=96:
                  # {"feature": "Start_A_VS_B_Diff", "instances": 171, "metric_value": 3.1952, "depth": 6}
                  if obj[8]>-84.70408026764281:
                     # {"feature": "CompTime_A_VS_B", "instances": 147, "metric_value": 1.5219, "depth": 7}
                     if obj[5] == '<':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 125, "metric_value": 3.4424, "depth": 8}
                        if obj[6]>-70.20034221256694:
                           # {"feature": "Tardy_A_VS_B", "instances": 105, "metric_value": 0.8125, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "PTime_A_VS_B", "instances": 100, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 123.41
                              else:
                                 return 123.41
                           elif obj[9] == '<':
                              # {"feature": "PTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 93.4
                              else:
                                 return 93.4
                           else:
                              return 121.98095238095237
                        elif obj[6]<=-70.20034221256694:
                           # {"feature": "Tardy_A_VS_B", "instances": 20, "metric_value": 1.3236, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "PTime_A_VS_B", "instances": 19, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 69.10526315789474
                              else:
                                 return 69.10526315789474
                           elif obj[9] == '<':
                              return 88
                           else:
                              return 70.05
                        else:
                           return 113.672
                     elif obj[5] == '>':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 21, "metric_value": 3.67, "depth": 8}
                        if obj[6]>8:
                           # {"feature": "Tardy_A_VS_B", "instances": 14, "metric_value": 3.3206, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "PTime_A_VS_B", "instances": 12, "metric_value": 0.0, "depth": 10}
                              if obj[3] == '>':
                                 return 79.16666666666667
                              else:
                                 return 79.16666666666667
                           elif obj[9] == '>':
                              return 126.0
                           else:
                              return 85.85714285714286
                        elif obj[6]<=8:
                           # {"feature": "Start_A_VS_B", "instances": 7, "metric_value": 0.3156, "depth": 9}
                           if obj[7] == '<':
                              return 126.75
                           elif obj[7] == '>':
                              return 117.66666666666667
                           else:
                              return 122.85714285714286
                        else:
                           return 98.19047619047619
                     elif obj[5] == '=':
                        return 184
                     else:
                        return 111.93877551020408
                  elif obj[8]<=-84.70408026764281:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 24, "metric_value": 14.8722, "depth": 7}
                     if obj[6]<=-110:
                        # {"feature": "Tardy_A_VS_B", "instances": 13, "metric_value": 7.9579, "depth": 8}
                        if obj[9] == '=':
                           # {"feature": "PTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 94.55555555555556
                              else:
                                 return 94.55555555555556
                           else:
                              return 94.55555555555556
                        elif obj[9] == '<':
                           return 157.0
                        else:
                           return 113.76923076923077
                     elif obj[6]>-110:
                        # {"feature": "Tardy_A_VS_B", "instances": 11, "metric_value": 20.9716, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "PTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 200.16666666666666
                              else:
                                 return 200.16666666666666
                           else:
                              return 200.16666666666666
                        elif obj[9] == '=':
                           # {"feature": "PTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 254.4
                              else:
                                 return 254.4
                           else:
                              return 254.4
                        else:
                           return 224.8181818181818
                     else:
                        return 164.66666666666666
                  else:
                     return 119.3391812865497
               elif obj[10]>96:
                  return 352.5
               else:
                  return 122.03468208092485
            else:
               return 92.33105335157319
         elif obj[4]<=4.405479452054794:
            # {"feature": "Start_A_VS_B_Diff", "instances": 729, "metric_value": 1.1737, "depth": 4}
            if obj[8]>-68.2318244170096:
               # {"feature": "NumWaitingJob", "instances": 389, "metric_value": 1.4986, "depth": 5}
               if obj[0]<=13:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 270, "metric_value": 1.1543, "depth": 6}
                  if obj[6]>-92.90748631367403:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 255, "metric_value": 0.9006, "depth": 7}
                     if obj[10]>-45.46385263276072:
                        # {"feature": "PTime_A_VS_B", "instances": 235, "metric_value": 0.9175, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "Start_A_VS_B", "instances": 157, "metric_value": 0.5488, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 89, "metric_value": 0.1778, "depth": 10}
                              if obj[9] == '=':
                                 return 58.73684210526316
                              elif obj[9] == '<':
                                 return 51.25
                              else:
                                 return 56.04494382022472
                           elif obj[7] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 68, "metric_value": 1.0317, "depth": 10}
                              if obj[9] == '>':
                                 return 43.5609756097561
                              elif obj[9] == '=':
                                 return 50.9375
                              elif obj[9] == '<':
                                 return 34.54545454545455
                              else:
                                 return 43.838235294117645
                           else:
                              return 50.75796178343949
                        elif obj[3] == '>':
                           # {"feature": "Tardy_A_VS_B", "instances": 59, "metric_value": 1.0398, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 30, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 67.8
                              else:
                                 return 67.8
                           elif obj[9] == '=':
                              # {"feature": "Start_A_VS_B", "instances": 20, "metric_value": 1.5882, "depth": 10}
                              if obj[7] == '<':
                                 return 59.73684210526316
                              elif obj[7] == '=':
                                 return 30
                              else:
                                 return 58.25
                           elif obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 85.44444444444444
                              else:
                                 return 85.44444444444444
                           else:
                              return 67.2542372881356
                        elif obj[3] == '=':
                           # {"feature": "CompTime_A_VS_B", "instances": 19, "metric_value": 4.919, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 13, "metric_value": 3.9987, "depth": 10}
                              if obj[9] == '=':
                                 return 84.625
                              elif obj[9] == '<':
                                 return 64.0
                              else:
                                 return 76.6923076923077
                           elif obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 5, "metric_value": 6.4287, "depth": 10}
                              if obj[9] == '>':
                                 return 42.333333333333336
                              elif obj[9] == '=':
                                 return 63
                              else:
                                 return 50.6
                           elif obj[5] == '=':
                              return 40
                           else:
                              return 67.89473684210526
                        else:
                           return 56.285106382978725
                     elif obj[10]<=-45.46385263276072:
                        # {"feature": "PTime_A_VS_B", "instances": 20, "metric_value": 2.7605, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 12, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 12, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 26.333333333333332
                              else:
                                 return 26.333333333333332
                           else:
                              return 26.333333333333332
                        elif obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 42.857142857142854
                              else:
                                 return 42.857142857142854
                           else:
                              return 42.857142857142854
                        elif obj[3] == '=':
                           return 19
                        else:
                           return 31.75
                     else:
                        return 54.36078431372549
                  elif obj[6]<=-92.90748631367403:
                     # {"feature": "PTime_A_VS_B", "instances": 15, "metric_value": 2.2928, "depth": 7}
                     if obj[3] == '<':
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 12, "metric_value": 2.1605, "depth": 8}
                        if obj[10]>-75:
                           # {"feature": "Tardy_A_VS_B", "instances": 11, "metric_value": 0.6924, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 23.77777777777778
                              else:
                                 return 23.77777777777778
                           elif obj[9] == '<':
                              return 35.5
                           else:
                              return 25.90909090909091
                        elif obj[10]<=-75:
                           return 1
                        else:
                           return 23.833333333333332
                     elif obj[3] == '>':
                        return 15.0
                     elif obj[3] == '=':
                        return 4
                     else:
                        return 21.333333333333332
                  else:
                     return 52.525925925925925
               elif obj[0]>13:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 119, "metric_value": 2.4048, "depth": 6}
                  if obj[6]>-91.16330126354818:
                     # {"feature": "Start_A_VS_B", "instances": 105, "metric_value": 0.6624, "depth": 7}
                     if obj[7] == '<':
                        # {"feature": "PTime_A_VS_B", "instances": 88, "metric_value": 0.7581, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "Tardy_A_VS_B_Diff", "instances": 51, "metric_value": 0.6593, "depth": 9}
                           if obj[10]>-15:
                              # {"feature": "Tardy_A_VS_B", "instances": 50, "metric_value": 0.2687, "depth": 10}
                              if obj[9] == '=':
                                 return 79.44680851063829
                              elif obj[9] == '<':
                                 return 101.33333333333333
                              else:
                                 return 80.76
                           elif obj[10]<=-15:
                              return 52
                           else:
                              return 80.19607843137256
                        elif obj[3] == '>':
                           # {"feature": "Tardy_A_VS_B_Diff", "instances": 33, "metric_value": 2.703, "depth": 9}
                           if obj[10]>-3:
                              # {"feature": "Tardy_A_VS_B", "instances": 30, "metric_value": 1.8633, "depth": 10}
                              if obj[9] == '=':
                                 return 84.51724137931035
                              elif obj[9] == '<':
                                 return 140
                              else:
                                 return 86.36666666666666
                           elif obj[10]<=-3:
                              return 38.666666666666664
                           else:
                              return 82.03030303030303
                        elif obj[3] == '=':
                           return 107.0
                        else:
                           return 82.10227272727273
                     elif obj[7] == '>':
                        # {"feature": "PTime_A_VS_B", "instances": 16, "metric_value": 12.247, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "Tardy_A_VS_B_Diff", "instances": 11, "metric_value": 5.393, "depth": 9}
                           if obj[10]<=47:
                              # {"feature": "Tardy_A_VS_B", "instances": 10, "metric_value": 1.6366, "depth": 10}
                              if obj[9] == '=':
                                 return 76.2
                              elif obj[9] == '>':
                                 return 104.0
                              else:
                                 return 90.1
                           elif obj[10]>47:
                              return 28
                           else:
                              return 84.45454545454545
                        elif obj[3] == '>':
                           return 31.25
                        elif obj[3] == '=':
                           return 23
                        else:
                           return 67.3125
                     elif obj[7] == '=':
                        return 38
                     else:
                        return 79.42857142857143
                  elif obj[6]<=-91.16330126354818:
                     # {"feature": "PTime_A_VS_B", "instances": 14, "metric_value": 5.4587, "depth": 7}
                     if obj[3] == '<':
                        # {"feature": "CompTime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[5] == '<':
                           # {"feature": "Start_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 10}
                              if obj[9] == '=':
                                 return 41.81818181818182
                              else:
                                 return 41.81818181818182
                           else:
                              return 41.81818181818182
                        else:
                           return 41.81818181818182
                     elif obj[3] == '>':
                        return 11.666666666666666
                     else:
                        return 35.357142857142854
                  else:
                     return 74.24369747899159
               else:
                  return 59.16966580976864
            elif obj[8]<=-68.2318244170096:
               # {"feature": "PTime_A_VS_B", "instances": 340, "metric_value": 0.7349, "depth": 5}
               if obj[3] == '<':
                  # {"feature": "NumWaitingJob", "instances": 231, "metric_value": 0.3989, "depth": 6}
                  if obj[0]>4:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 223, "metric_value": 0.3667, "depth": 7}
                     if obj[6]>-284.32649179605414:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 213, "metric_value": 0.3605, "depth": 8}
                        if obj[10]>-171.9911769250399:
                           # {"feature": "Tardy_A_VS_B", "instances": 207, "metric_value": 0.0637, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 149, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 74.79194630872483
                              else:
                                 return 74.79194630872483
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 58, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 80.65517241379311
                              else:
                                 return 80.65517241379311
                           else:
                              return 76.43478260869566
                        elif obj[10]<=-171.9911769250399:
                           # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 108.66666666666667
                              else:
                                 return 108.66666666666667
                           else:
                              return 108.66666666666667
                        else:
                           return 77.34272300469483
                     elif obj[6]<=-284.32649179605414:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 10, "metric_value": 4.5448, "depth": 8}
                        if obj[10]>-180:
                           # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 81.66666666666667
                              else:
                                 return 81.66666666666667
                           else:
                              return 81.66666666666667
                        elif obj[10]<=-180:
                           return 40
                        else:
                           return 77.5
                     else:
                        return 77.34977578475336
                  elif obj[0]<=4:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 8, "metric_value": 18.7123, "depth": 7}
                     if obj[6]<=-190:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 6, "metric_value": 6.0442, "depth": 8}
                        if obj[10]<=-168:
                           return 19.0
                        elif obj[10]>-168:
                           return 47.5
                        else:
                           return 28.5
                     elif obj[6]>-190:
                        return 100.5
                     else:
                        return 46.5
                  else:
                     return 76.28138528138528
               elif obj[3] == '>':
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 87, "metric_value": 4.0428, "depth": 6}
                  if obj[10]>-51.62068965517241:
                     # {"feature": "NumWaitingJob", "instances": 54, "metric_value": 3.8374, "depth": 7}
                     if obj[0]>7:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 50, "metric_value": 3.6604, "depth": 8}
                        if obj[6]>-156.76:
                           # {"feature": "Tardy_A_VS_B", "instances": 32, "metric_value": 0.9042, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 25, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 90.16
                              else:
                                 return 90.16
                           elif obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 70.85714285714286
                              else:
                                 return 70.85714285714286
                           else:
                              return 85.9375
                        elif obj[6]<=-156.76:
                           # {"feature": "Tardy_A_VS_B", "instances": 18, "metric_value": 8.0156, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 144.42857142857142
                              else:
                                 return 144.42857142857142
                           elif obj[9] == '=':
                              return 76.0
                           else:
                              return 129.22222222222223
                        else:
                           return 101.52
                     elif obj[0]<=7:
                        return 181.75
                     else:
                        return 107.46296296296296
                  elif obj[10]<=-51.62068965517241:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 33, "metric_value": 2.894, "depth": 7}
                     if obj[6]<=-137.47386318999878:
                        # {"feature": "NumWaitingJob", "instances": 27, "metric_value": 2.0428, "depth": 8}
                        if obj[0]<=8:
                           # {"feature": "CompTime_A_VS_B", "instances": 19, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 19, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 70.73684210526316
                              else:
                                 return 70.73684210526316
                           else:
                              return 70.73684210526316
                        elif obj[0]>8:
                           # {"feature": "CompTime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 92.5
                              else:
                                 return 92.5
                           else:
                              return 92.5
                        else:
                           return 77.18518518518519
                     elif obj[6]>-137.47386318999878:
                        # {"feature": "NumWaitingJob", "instances": 6, "metric_value": 19.8947, "depth": 8}
                        if obj[0]>7:
                           return 66.66666666666667
                        elif obj[0]<=7:
                           return 8.0
                        else:
                           return 37.333333333333336
                     else:
                        return 69.93939393939394
                  else:
                     return 93.22988505747126
               elif obj[3] == '=':
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 22, "metric_value": 9.6217, "depth": 6}
                  if obj[6]>-194:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 18, "metric_value": 10.5844, "depth": 7}
                     if obj[10]<=-46:
                        # {"feature": "NumWaitingJob", "instances": 14, "metric_value": 1.4916, "depth": 8}
                        if obj[0]>2:
                           # {"feature": "CompTime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 48.38461538461539
                              else:
                                 return 48.38461538461539
                           else:
                              return 48.38461538461539
                        elif obj[0]<=2:
                           return 27
                        else:
                           return 46.857142857142854
                     elif obj[10]>-46:
                        return 95.5
                     else:
                        return 57.666666666666664
                  elif obj[6]<=-194:
                     return 114.0
                  else:
                     return 67.9090909090909
               else:
                  return 80.0764705882353
            else:
               return 68.920438957476
         else:
            return 80.6417808219178
      elif obj[1] == '=':
         # {"feature": "PTime_A_VS_B_Diff", "instances": 1349, "metric_value": 2.4582, "depth": 3}
         if obj[4]>5.679021497405485:
            # {"feature": "Tardy_A_VS_B", "instances": 719, "metric_value": 2.5491, "depth": 4}
            if obj[9] == '=':
               # {"feature": "NumWaitingJob", "instances": 704, "metric_value": 2.7171, "depth": 5}
               if obj[0]>15:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 459, "metric_value": 1.4949, "depth": 6}
                  if obj[6]<=14.5599128540305:
                     # {"feature": "Start_A_VS_B", "instances": 249, "metric_value": 0.3686, "depth": 7}
                     if obj[7] == '=':
                        # {"feature": "PTime_A_VS_B", "instances": 248, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 248, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 248, "metric_value": 0.0, "depth": 10}
                              if obj[8]<=0:
                                 return 72.28629032258064
                              else:
                                 return 72.28629032258064
                           else:
                              return 72.28629032258064
                        else:
                           return 72.28629032258064
                     elif obj[7] == '<':
                        return 153
                     else:
                        return 72.61044176706827
                  elif obj[6]>14.5599128540305:
                     # {"feature": "PTime_A_VS_B", "instances": 210, "metric_value": 0.0, "depth": 7}
                     if obj[3] == '>':
                        # {"feature": "CompTime_A_VS_B", "instances": 210, "metric_value": 0.0, "depth": 8}
                        if obj[5] == '>':
                           # {"feature": "Start_A_VS_B", "instances": 210, "metric_value": 0.0, "depth": 9}
                           if obj[7] == '=':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 210, "metric_value": 0.0, "depth": 10}
                              if obj[8]<=0:
                                 return 95.65714285714286
                              else:
                                 return 95.65714285714286
                           else:
                              return 95.65714285714286
                        else:
                           return 95.65714285714286
                     else:
                        return 95.65714285714286
                  else:
                     return 83.15468409586056
               elif obj[0]<=15:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 245, "metric_value": 0.5286, "depth": 6}
                  if obj[6]<=14.926530612244898:
                     # {"feature": "PTime_A_VS_B", "instances": 126, "metric_value": 0.0, "depth": 7}
                     if obj[3] == '>':
                        # {"feature": "CompTime_A_VS_B", "instances": 126, "metric_value": 0.0, "depth": 8}
                        if obj[5] == '>':
                           # {"feature": "Start_A_VS_B", "instances": 126, "metric_value": 0.0, "depth": 9}
                           if obj[7] == '=':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 126, "metric_value": 0.0, "depth": 10}
                              if obj[8]<=0:
                                 return 50.11904761904762
                              else:
                                 return 50.11904761904762
                           else:
                              return 50.11904761904762
                        else:
                           return 50.11904761904762
                     else:
                        return 50.11904761904762
                  elif obj[6]>14.926530612244898:
                     # {"feature": "Start_A_VS_B_Diff", "instances": 119, "metric_value": 0.2552, "depth": 7}
                     if obj[8]<=3:
                        # {"feature": "Start_A_VS_B", "instances": 117, "metric_value": 0.6098, "depth": 8}
                        if obj[7] == '=':
                           # {"feature": "PTime_A_VS_B", "instances": 116, "metric_value": 0.0, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 116, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 60.21551724137931
                              else:
                                 return 60.21551724137931
                           else:
                              return 60.21551724137931
                        elif obj[7] == '>':
                           return 123
                        else:
                           return 60.75213675213675
                     elif obj[8]>3:
                        return 62.5
                     else:
                        return 60.78151260504202
                  else:
                     return 55.29795918367347
               else:
                  return 73.46022727272727
            elif obj[9] == '>':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 11, "metric_value": 13.5814, "depth": 5}
               if obj[6]>24:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 10, "metric_value": 19.4249, "depth": 6}
                  if obj[10]<=145:
                     # {"feature": "Start_A_VS_B_Diff", "instances": 8, "metric_value": 10.6248, "depth": 7}
                     if obj[8]>35:
                        # {"feature": "NumWaitingJob", "instances": 5, "metric_value": 16.3617, "depth": 8}
                        if obj[0]>8:
                           return 69.33333333333333
                        elif obj[0]<=8:
                           return 19
                        else:
                           return 49.2
                     elif obj[8]<=35:
                        return 87.33333333333333
                     else:
                        return 63.5
                  elif obj[10]>145:
                     return 152.0
                  else:
                     return 81.2
               elif obj[6]<=24:
                  return 198
               else:
                  return 91.81818181818181
            elif obj[9] == '<':
               return 289.0
            else:
               return 74.94019471488178
         elif obj[4]<=5.679021497405485:
            # {"feature": "NumWaitingJob", "instances": 630, "metric_value": 0.5926, "depth": 4}
            if obj[0]>15:
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 401, "metric_value": 0.6581, "depth": 5}
               if obj[6]>-4.241895261845387:
                  # {"feature": "PTime_A_VS_B", "instances": 236, "metric_value": 0.126, "depth": 6}
                  if obj[3] == '>':
                     # {"feature": "CompTime_A_VS_B", "instances": 130, "metric_value": 0.0, "depth": 7}
                     if obj[5] == '>':
                        # {"feature": "Start_A_VS_B", "instances": 130, "metric_value": 0.0, "depth": 8}
                        if obj[7] == '=':
                           # {"feature": "Start_A_VS_B_Diff", "instances": 130, "metric_value": 0.0, "depth": 9}
                           if obj[8]<=0:
                              # {"feature": "Tardy_A_VS_B", "instances": 130, "metric_value": 0.0, "depth": 10}
                              if obj[9] == '=':
                                 return 57.43846153846154
                              else:
                                 return 57.43846153846154
                           else:
                              return 57.43846153846154
                        else:
                           return 57.43846153846154
                     else:
                        return 57.43846153846154
                  elif obj[3] == '<':
                     # {"feature": "CompTime_A_VS_B", "instances": 89, "metric_value": 0.0, "depth": 7}
                     if obj[5] == '<':
                        # {"feature": "Start_A_VS_B", "instances": 89, "metric_value": 0.0, "depth": 8}
                        if obj[7] == '=':
                           # {"feature": "Start_A_VS_B_Diff", "instances": 89, "metric_value": 0.0, "depth": 9}
                           if obj[8]<=0:
                              # {"feature": "Tardy_A_VS_B", "instances": 89, "metric_value": 0.0, "depth": 10}
                              if obj[9] == '=':
                                 return 59.80898876404494
                              else:
                                 return 59.80898876404494
                           else:
                              return 59.80898876404494
                        else:
                           return 59.80898876404494
                     else:
                        return 59.80898876404494
                  elif obj[3] == '=':
                     # {"feature": "CompTime_A_VS_B", "instances": 17, "metric_value": 0.0, "depth": 7}
                     if obj[5] == '=':
                        # {"feature": "Start_A_VS_B", "instances": 17, "metric_value": 0.0, "depth": 8}
                        if obj[7] == '=':
                           # {"feature": "Start_A_VS_B_Diff", "instances": 17, "metric_value": 0.0, "depth": 9}
                           if obj[8]<=0:
                              # {"feature": "Tardy_A_VS_B", "instances": 17, "metric_value": 0.0, "depth": 10}
                              if obj[9] == '=':
                                 return 50.411764705882355
                              else:
                                 return 50.411764705882355
                           else:
                              return 50.411764705882355
                        else:
                           return 50.411764705882355
                     else:
                        return 50.411764705882355
                  else:
                     return 57.82627118644068
               elif obj[6]<=-4.241895261845387:
                  # {"feature": "PTime_A_VS_B", "instances": 165, "metric_value": 0.0, "depth": 6}
                  if obj[3] == '<':
                     # {"feature": "CompTime_A_VS_B", "instances": 165, "metric_value": 0.0, "depth": 7}
                     if obj[5] == '<':
                        # {"feature": "Start_A_VS_B", "instances": 165, "metric_value": 0.0, "depth": 8}
                        if obj[7] == '=':
                           # {"feature": "Start_A_VS_B_Diff", "instances": 165, "metric_value": 0.0, "depth": 9}
                           if obj[8]<=0:
                              # {"feature": "Tardy_A_VS_B", "instances": 165, "metric_value": 0.0, "depth": 10}
                              if obj[9] == '=':
                                 return 45.78181818181818
                              else:
                                 return 45.78181818181818
                           else:
                              return 45.78181818181818
                        else:
                           return 45.78181818181818
                     else:
                        return 45.78181818181818
                  else:
                     return 45.78181818181818
               else:
                  return 52.87032418952619
            elif obj[0]<=15:
               # {"feature": "Tardy_A_VS_B", "instances": 229, "metric_value": 2.0916, "depth": 5}
               if obj[9] == '=':
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 210, "metric_value": 0.6422, "depth": 6}
                  if obj[6]>-5.066666666666666:
                     # {"feature": "PTime_A_VS_B", "instances": 123, "metric_value": 0.2466, "depth": 7}
                     if obj[3] == '>':
                        # {"feature": "CompTime_A_VS_B", "instances": 54, "metric_value": 0.0, "depth": 8}
                        if obj[5] == '>':
                           # {"feature": "Start_A_VS_B", "instances": 54, "metric_value": 0.0, "depth": 9}
                           if obj[7] == '=':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 54, "metric_value": 0.0, "depth": 10}
                              if obj[8]<=0:
                                 return 42.46296296296296
                              else:
                                 return 42.46296296296296
                           else:
                              return 42.46296296296296
                        else:
                           return 42.46296296296296
                     elif obj[3] == '<':
                        # {"feature": "CompTime_A_VS_B", "instances": 53, "metric_value": 0.0, "depth": 8}
                        if obj[5] == '<':
                           # {"feature": "Start_A_VS_B", "instances": 53, "metric_value": 0.0, "depth": 9}
                           if obj[7] == '=':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 53, "metric_value": 0.0, "depth": 10}
                              if obj[8]<=0:
                                 return 38.716981132075475
                              else:
                                 return 38.716981132075475
                           else:
                              return 38.716981132075475
                        else:
                           return 38.716981132075475
                     elif obj[3] == '=':
                        # {"feature": "CompTime_A_VS_B", "instances": 16, "metric_value": 0.0, "depth": 8}
                        if obj[5] == '=':
                           # {"feature": "Start_A_VS_B", "instances": 16, "metric_value": 0.0, "depth": 9}
                           if obj[7] == '=':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 16, "metric_value": 0.0, "depth": 10}
                              if obj[8]<=0:
                                 return 42.375
                              else:
                                 return 42.375
                           else:
                              return 42.375
                        else:
                           return 42.375
                     else:
                        return 40.83739837398374
                  elif obj[6]<=-5.066666666666666:
                     # {"feature": "Start_A_VS_B", "instances": 87, "metric_value": 0.398, "depth": 7}
                     if obj[7] == '=':
                        # {"feature": "PTime_A_VS_B", "instances": 86, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 86, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 86, "metric_value": 0.0, "depth": 10}
                              if obj[8]<=0:
                                 return 33.73255813953488
                              else:
                                 return 33.73255813953488
                           else:
                              return 33.73255813953488
                        else:
                           return 33.73255813953488
                     elif obj[7] == '<':
                        return 1
                     else:
                        return 33.35632183908046
                  else:
                     return 37.73809523809524
               elif obj[9] == '<':
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 11, "metric_value": 12.0163, "depth": 6}
                  if obj[6]>-254:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 9, "metric_value": 19.2908, "depth": 7}
                     if obj[10]>-32:
                        # {"feature": "Start_A_VS_B_Diff", "instances": 5, "metric_value": 24.9569, "depth": 8}
                        if obj[8]>-107:
                           return 113.5
                        elif obj[8]<=-107:
                           return 31
                        else:
                           return 97.0
                     elif obj[10]<=-32:
                        return 25.25
                     else:
                        return 65.11111111111111
                  elif obj[6]<=-254:
                     return 143.5
                  else:
                     return 79.36363636363636
               elif obj[9] == '>':
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 8, "metric_value": 49.4068, "depth": 6}
                  if obj[6]<=74:
                     # {"feature": "Start_A_VS_B_Diff", "instances": 5, "metric_value": 4.6549, "depth": 7}
                     if obj[8]>8:
                        return 16.333333333333332
                     elif obj[8]<=8:
                        return 3
                     else:
                        return 11.0
                  elif obj[6]>74:
                     return 130.0
                  else:
                     return 55.625
               else:
                  return 40.36244541484716
            else:
               return 48.32380952380952
         else:
            return 62.510007412898446
      elif obj[1] == '>':
         # {"feature": "Start_A_VS_B_Diff", "instances": 1236, "metric_value": 3.5268, "depth": 3}
         if obj[8]>-111.61254926949853:
            # {"feature": "PTime_A_VS_B", "instances": 1042, "metric_value": 2.1888, "depth": 4}
            if obj[3] == '>':
               # {"feature": "NumWaitingJob", "instances": 651, "metric_value": 2.776, "depth": 5}
               if obj[0]>9:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 368, "metric_value": 1.8906, "depth": 6}
                  if obj[6]>-28.492707811066:
                     # {"feature": "Start_A_VS_B", "instances": 301, "metric_value": 0.7495, "depth": 7}
                     if obj[7] == '>':
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 195, "metric_value": 2.0199, "depth": 8}
                        if obj[10]<=26.620512820512822:
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 123, "metric_value": 0.4095, "depth": 9}
                           if obj[4]>4.980985092303783:
                              # {"feature": "Tardy_A_VS_B", "instances": 109, "metric_value": 0.1588, "depth": 10}
                              if obj[9] == '=':
                                 return 92.30263157894737
                              elif obj[9] == '>':
                                 return 100.72727272727273
                              else:
                                 return 94.85321100917432
                           elif obj[4]<=4.980985092303783:
                              # {"feature": "Tardy_A_VS_B", "instances": 14, "metric_value": 0.4787, "depth": 10}
                              if obj[9] == '=':
                                 return 83.33333333333333
                              elif obj[9] == '>':
                                 return 96.6
                              else:
                                 return 88.07142857142857
                           else:
                              return 94.08130081300813
                        elif obj[10]>26.620512820512822:
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 72, "metric_value": 1.2969, "depth": 9}
                           if obj[4]>1:
                              # {"feature": "CompTime_A_VS_B", "instances": 68, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 126.1029411764706
                              else:
                                 return 126.1029411764706
                           elif obj[4]<=1:
                              return 166.25
                           else:
                              return 128.33333333333334
                        else:
                           return 106.72820512820513
                     elif obj[7] == '<':
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 102, "metric_value": 2.4246, "depth": 8}
                        if obj[10]>-17:
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 95, "metric_value": 0.5078, "depth": 9}
                           if obj[4]<=27.02551137520751:
                              # {"feature": "CompTime_A_VS_B", "instances": 93, "metric_value": 0.3705, "depth": 10}
                              if obj[5] == '>':
                                 return 134.9
                              elif obj[5] == '<':
                                 return 127.93103448275862
                              elif obj[5] == '=':
                                 return 115.0
                              else:
                                 return 131.8709677419355
                           elif obj[4]>27.02551137520751:
                              return 180.0
                           else:
                              return 132.8842105263158
                        elif obj[10]<=-17:
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 7, "metric_value": 13.3975, "depth": 9}
                           if obj[4]<=5:
                              # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 79.83333333333333
                              else:
                                 return 79.83333333333333
                           elif obj[4]>5:
                              return 4
                           else:
                              return 69.0
                        else:
                           return 128.5
                     elif obj[7] == '=':
                        return 113.0
                     else:
                        return 114.18936877076412
                  elif obj[6]<=-28.492707811066:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 67, "metric_value": 2.5508, "depth": 7}
                     if obj[10]>-45:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 55, "metric_value": 2.7862, "depth": 8}
                        if obj[4]>1:
                           # {"feature": "Tardy_A_VS_B", "instances": 50, "metric_value": 2.1744, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 38, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 163.73684210526315
                              else:
                                 return 163.73684210526315
                           elif obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 12, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 189.25
                              else:
                                 return 189.25
                           else:
                              return 169.86
                        elif obj[4]<=1:
                           # {"feature": "Tardy_A_VS_B", "instances": 5, "metric_value": 17.2319, "depth": 9}
                           if obj[9] == '=':
                              return 85.75
                           elif obj[9] == '<':
                              return 182
                           else:
                              return 105.0
                        else:
                           return 163.96363636363637
                     elif obj[10]<=-45:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 12, "metric_value": 9.5546, "depth": 8}
                        if obj[4]>1:
                           # {"feature": "CompTime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 113.4
                              else:
                                 return 113.4
                           else:
                              return 113.4
                        elif obj[4]<=1:
                           return 174
                        else:
                           return 123.5
                     else:
                        return 156.71641791044777
                  else:
                     return 121.9320652173913
               elif obj[0]<=9:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 283, "metric_value": 2.0572, "depth": 6}
                  if obj[10]<=215.76379271627354:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 275, "metric_value": 1.365, "depth": 7}
                     if obj[4]>5.4227399067995465:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 220, "metric_value": 1.5249, "depth": 8}
                        if obj[6]>-27.37467496146565:
                           # {"feature": "CompTime_A_VS_B", "instances": 178, "metric_value": 0.476, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 155, "metric_value": 0.7504, "depth": 10}
                              if obj[9] == '>':
                                 return 84.8
                              elif obj[9] == '=':
                                 return 47.0
                              else:
                                 return 83.58064516129032
                           elif obj[5] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 21, "metric_value": 4.4617, "depth": 10}
                              if obj[9] == '<':
                                 return 85.0625
                              elif obj[9] == '=':
                                 return 129.2
                              else:
                                 return 95.57142857142857
                           elif obj[5] == '=':
                              return 92
                           else:
                              return 85.08988764044943
                        elif obj[6]<=-27.37467496146565:
                           # {"feature": "Tardy_A_VS_B", "instances": 42, "metric_value": 10.6271, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 37, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 96.24324324324324
                              else:
                                 return 96.24324324324324
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 209.2
                              else:
                                 return 209.2
                           else:
                              return 109.69047619047619
                        else:
                           return 89.78636363636363
                     elif obj[4]<=5.4227399067995465:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 55, "metric_value": 4.3321, "depth": 8}
                        if obj[6]<=136.41214020949917:
                           # {"feature": "Tardy_A_VS_B", "instances": 44, "metric_value": 2.4262, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 29, "metric_value": 1.8071, "depth": 10}
                              if obj[7] == '>':
                                 return 52.869565217391305
                              elif obj[7] == '<':
                                 return 53.5
                              else:
                                 return 53.0
                           elif obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 34.18181818181818
                              else:
                                 return 34.18181818181818
                           elif obj[9] == '=':
                              return 75.0
                           else:
                              return 50.29545454545455
                        elif obj[6]>136.41214020949917:
                           # {"feature": "CompTime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 99.27272727272727
                              else:
                                 return 99.27272727272727
                           else:
                              return 99.27272727272727
                        else:
                           return 60.09090909090909
                     else:
                        return 83.84727272727272
                  elif obj[10]>215.76379271627354:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 8, "metric_value": 28.0357, "depth": 7}
                     if obj[6]>240:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 6, "metric_value": 21.929, "depth": 8}
                        if obj[4]<=12:
                           return 168.5
                        elif obj[4]>12:
                           return 104
                        else:
                           return 147.0
                     elif obj[6]<=240:
                        return 260.5
                     else:
                        return 175.375
                  else:
                     return 86.43462897526501
               else:
                  return 106.50076804915514
            elif obj[3] == '<':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 355, "metric_value": 3.8892, "depth": 5}
               if obj[6]<=161.36669604211377:
                  # {"feature": "NumWaitingJob", "instances": 342, "metric_value": 1.0925, "depth": 6}
                  if obj[0]>9:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 202, "metric_value": 0.9443, "depth": 7}
                     if obj[4]>-22.42331235995978:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 189, "metric_value": 0.8803, "depth": 8}
                        if obj[10]>-56.0296140242025:
                           # {"feature": "Start_A_VS_B", "instances": 182, "metric_value": 1.1343, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 99, "metric_value": 3.9356, "depth": 10}
                              if obj[9] == '=':
                                 return 93.83582089552239
                              elif obj[9] == '<':
                                 return 81.66666666666667
                              elif obj[9] == '>':
                                 return 195.5
                              else:
                                 return 92.20202020202021
                           elif obj[7] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 80, "metric_value": 1.5797, "depth": 10}
                              if obj[5] == '>':
                                 return 71.08
                              elif obj[5] == '=':
                                 return 125.66666666666667
                              elif obj[5] == '<':
                                 return 64.0
                              else:
                                 return 72.95
                           elif obj[7] == '=':
                              return 64.66666666666667
                           else:
                              return 83.28571428571429
                        elif obj[10]<=-56.0296140242025:
                           # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 36.142857142857146
                              else:
                                 return 36.142857142857146
                           else:
                              return 36.142857142857146
                        else:
                           return 81.53968253968254
                     elif obj[4]<=-22.42331235995978:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 13, "metric_value": 6.3883, "depth": 8}
                        if obj[10]<=11:
                           # {"feature": "CompTime_A_VS_B", "instances": 10, "metric_value": 5.0257, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 7, "metric_value": 2.7121, "depth": 10}
                              if obj[9] == '=':
                                 return 47.5
                              elif obj[9] == '<':
                                 return 68
                              else:
                                 return 50.42857142857143
                           elif obj[5] == '>':
                              return 20.0
                           else:
                              return 41.3
                        elif obj[10]>11:
                           return 80.33333333333333
                        else:
                           return 50.30769230769231
                     else:
                        return 79.52970297029702
                  elif obj[0]<=9:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 140, "metric_value": 1.9068, "depth": 7}
                     if obj[4]>-9.764285714285714:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 77, "metric_value": 2.435, "depth": 8}
                        if obj[10]<=80.94064420302914:
                           # {"feature": "Tardy_A_VS_B", "instances": 61, "metric_value": 1.8905, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 26, "metric_value": 0.8092, "depth": 10}
                              if obj[7] == '>':
                                 return 50.5
                              elif obj[7] == '<':
                                 return 26.5
                              else:
                                 return 48.65384615384615
                           elif obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 23, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 68.52173913043478
                              else:
                                 return 68.52173913043478
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 12, "metric_value": 8.5119, "depth": 10}
                              if obj[5] == '<':
                                 return 82.71428571428571
                              elif obj[5] == '>':
                                 return 94.75
                              elif obj[5] == '=':
                                 return 4
                              else:
                                 return 80.16666666666667
                           else:
                              return 62.34426229508197
                        elif obj[10]>80.94064420302914:
                           # {"feature": "CompTime_A_VS_B", "instances": 16, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 16, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 99.25
                              else:
                                 return 99.25
                           else:
                              return 99.25
                        else:
                           return 70.01298701298701
                     elif obj[4]<=-9.764285714285714:
                        # {"feature": "Start_A_VS_B", "instances": 63, "metric_value": 2.8262, "depth": 8}
                        if obj[7] == '<':
                           # {"feature": "Tardy_A_VS_B_Diff", "instances": 31, "metric_value": 1.5828, "depth": 9}
                           if obj[10]>-74.04322647992295:
                              # {"feature": "Tardy_A_VS_B", "instances": 27, "metric_value": 1.4882, "depth": 10}
                              if obj[9] == '<':
                                 return 36.57142857142857
                              elif obj[9] == '=':
                                 return 53.0
                              elif obj[9] == '>':
                                 return 31
                              else:
                                 return 39.407407407407405
                           elif obj[10]<=-74.04322647992295:
                              return 20.25
                           else:
                              return 36.935483870967744
                        elif obj[7] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 30, "metric_value": 5.9729, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B_Diff", "instances": 28, "metric_value": 4.3514, "depth": 10}
                              if obj[10]<=52.714285714285715:
                                 return 32.125
                              elif obj[10]>52.714285714285715:
                                 return 64.16666666666667
                              else:
                                 return 45.857142857142854
                           elif obj[5] == '<':
                              return 124.0
                           else:
                              return 51.06666666666667
                        elif obj[7] == '=':
                           return 104.5
                        else:
                           return 45.80952380952381
                     else:
                        return 59.121428571428574
                  else:
                     return 71.17543859649123
               elif obj[6]>161.36669604211377:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 13, "metric_value": 13.3981, "depth": 6}
                  if obj[10]<=251:
                     # {"feature": "NumWaitingJob", "instances": 10, "metric_value": 14.7723, "depth": 7}
                     if obj[0]>4:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 8, "metric_value": 2.2117, "depth": 8}
                        if obj[4]<=-12:
                           # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 177.8
                              else:
                                 return 177.8
                           else:
                              return 177.8
                        elif obj[4]>-12:
                           return 161.66666666666666
                        else:
                           return 171.75
                     elif obj[0]<=4:
                        return 115.5
                     else:
                        return 160.5
                  elif obj[10]>251:
                     return 231.0
                  else:
                     return 176.76923076923077
               else:
                  return 75.04225352112677
            elif obj[3] == '=':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 36, "metric_value": 28.3188, "depth": 5}
               if obj[6]<=118.93009452626649:
                  # {"feature": "Start_A_VS_B", "instances": 31, "metric_value": 4.7144, "depth": 6}
                  if obj[7] == '<':
                     # {"feature": "NumWaitingJob", "instances": 17, "metric_value": 4.4062, "depth": 7}
                     if obj[0]<=14:
                        # {"feature": "Tardy_A_VS_B", "instances": 14, "metric_value": 3.0918, "depth": 8}
                        if obj[9] == '=':
                           # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 2.2286, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "PTime_A_VS_B_Diff", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=0:
                                 return 74.5
                              else:
                                 return 74.5
                           elif obj[5] == '>':
                              return 64
                           else:
                              return 73.0
                        elif obj[9] == '<':
                           # {"feature": "Tardy_A_VS_B_Diff", "instances": 6, "metric_value": 5.2434, "depth": 9}
                           if obj[10]>-69:
                              # {"feature": "PTime_A_VS_B_Diff", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=0:
                                 return 71.2
                              else:
                                 return 71.2
                           elif obj[10]<=-69:
                              return 42
                           else:
                              return 66.33333333333333
                        elif obj[9] == '>':
                           return 91
                        else:
                           return 71.42857142857143
                     elif obj[0]>14:
                        return 27.666666666666668
                     else:
                        return 63.705882352941174
                  elif obj[7] == '>':
                     # {"feature": "NumWaitingJob", "instances": 13, "metric_value": 18.8776, "depth": 7}
                     if obj[0]<=10:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 7, "metric_value": 15.1863, "depth": 8}
                        if obj[10]<=29:
                           return 18.0
                        elif obj[10]>29:
                           return 65.66666666666667
                        else:
                           return 38.42857142857143
                     elif obj[0]>10:
                        # {"feature": "Tardy_A_VS_B", "instances": 6, "metric_value": 9.1808, "depth": 8}
                        if obj[9] == '=':
                           return 107.75
                        elif obj[9] == '>':
                           return 140.5
                        else:
                           return 118.66666666666667
                     else:
                        return 75.46153846153847
                  elif obj[7] == '=':
                     return 162
                  else:
                     return 71.80645161290323
               elif obj[6]>118.93009452626649:
                  # {"feature": "NumWaitingJob", "instances": 5, "metric_value": 22.7429, "depth": 6}
                  if obj[0]>4:
                     return 257.75
                  elif obj[0]<=4:
                     return 176
                  else:
                     return 241.4
               else:
                  return 95.36111111111111
            else:
               return 95.39827255278311
         elif obj[8]<=-111.61254926949853:
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 194, "metric_value": 6.8527, "depth": 4}
            if obj[10]>-96.77319587628865:
               # {"feature": "PTime_A_VS_B_Diff", "instances": 99, "metric_value": 5.928, "depth": 5}
               if obj[4]>-11.375220948888002:
                  # {"feature": "PTime_A_VS_B", "instances": 84, "metric_value": 4.033, "depth": 6}
                  if obj[3] == '>':
                     # {"feature": "NumWaitingJob", "instances": 45, "metric_value": 8.1999, "depth": 7}
                     if obj[0]>7:
                        # {"feature": "Tardy_A_VS_B", "instances": 32, "metric_value": 5.4389, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "CompTime_A_VS_B_Diff", "instances": 21, "metric_value": 6.1279, "depth": 9}
                           if obj[6]<=-107:
                              # {"feature": "CompTime_A_VS_B", "instances": 15, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 235.33333333333334
                              else:
                                 return 235.33333333333334
                           elif obj[6]>-107:
                              # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 166.16666666666666
                              else:
                                 return 166.16666666666666
                           else:
                              return 215.57142857142858
                        elif obj[9] == '=':
                           # {"feature": "CompTime_A_VS_B_Diff", "instances": 11, "metric_value": 15.6972, "depth": 9}
                           if obj[6]>-107:
                              # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 319.3333333333333
                              else:
                                 return 319.3333333333333
                           elif obj[6]<=-107:
                              # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 229.0
                              else:
                                 return 229.0
                           else:
                              return 278.27272727272725
                        else:
                           return 237.125
                     elif obj[0]<=7:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 13, "metric_value": 27.4594, "depth": 8}
                        if obj[6]<=-101:
                           # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 193.55555555555554
                              else:
                                 return 193.55555555555554
                           else:
                              return 193.55555555555554
                        elif obj[6]>-101:
                           return 86.5
                        else:
                           return 160.6153846153846
                     else:
                        return 215.0222222222222
                  elif obj[3] == '<':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 36, "metric_value": 17.4374, "depth": 7}
                     if obj[6]>-187:
                        # {"feature": "NumWaitingJob", "instances": 34, "metric_value": 2.9369, "depth": 8}
                        if obj[0]<=11:
                           # {"feature": "Tardy_A_VS_B", "instances": 23, "metric_value": 0.2616, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 21, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 183.47619047619048
                              else:
                                 return 183.47619047619048
                           elif obj[9] == '=':
                              return 175.5
                           else:
                              return 182.7826086956522
                        elif obj[0]>11:
                           # {"feature": "Tardy_A_VS_B", "instances": 11, "metric_value": 2.4824, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 131.33333333333334
                              else:
                                 return 131.33333333333334
                           elif obj[9] == '=':
                              return 176.0
                           else:
                              return 139.45454545454547
                        else:
                           return 168.76470588235293
                     elif obj[6]<=-187:
                        return 384
                     else:
                        return 180.72222222222223
                  elif obj[3] == '=':
                     return 99.66666666666667
                  else:
                     return 196.20238095238096
               elif obj[4]<=-11.375220948888002:
                  # {"feature": "NumWaitingJob", "instances": 15, "metric_value": 7.6896, "depth": 6}
                  if obj[0]>10:
                     # {"feature": "Tardy_A_VS_B", "instances": 9, "metric_value": 10.581, "depth": 7}
                     if obj[9] == '<':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 6, "metric_value": 31.6795, "depth": 8}
                        if obj[6]<=-159:
                           return 77.5
                        elif obj[6]>-159:
                           return 213.0
                        else:
                           return 122.66666666666667
                     elif obj[9] == '=':
                        return 79.0
                     else:
                        return 108.11111111111111
                  elif obj[0]<=10:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 6, "metric_value": 3.2214, "depth": 7}
                     if obj[6]<=-206:
                        return 129.33333333333334
                     elif obj[6]>-206:
                        return 114.0
                     else:
                        return 121.66666666666667
                  else:
                     return 113.53333333333333
               else:
                  return 183.67676767676767
            elif obj[10]<=-96.77319587628865:
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 95, "metric_value": 7.5525, "depth": 5}
               if obj[6]>-189.97894736842105:
                  # {"feature": "NumWaitingJob", "instances": 51, "metric_value": 3.7385, "depth": 6}
                  if obj[0]>3:
                     # {"feature": "PTime_A_VS_B", "instances": 46, "metric_value": 3.5551, "depth": 7}
                     if obj[3] == '<':
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 23, "metric_value": 4.4979, "depth": 8}
                        if obj[4]<=-7:
                           # {"feature": "CompTime_A_VS_B", "instances": 19, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 19, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 78.15789473684211
                              else:
                                 return 78.15789473684211
                           else:
                              return 78.15789473684211
                        elif obj[4]>-7:
                           return 111.75
                        else:
                           return 84.0
                     elif obj[3] == '>':
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 17, "metric_value": 24.3328, "depth": 8}
                        if obj[4]>3:
                           # {"feature": "CompTime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 75.42857142857143
                              else:
                                 return 75.42857142857143
                           else:
                              return 75.42857142857143
                        elif obj[4]<=3:
                           return 233.0
                        else:
                           return 103.23529411764706
                     elif obj[3] == '=':
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 6, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 71.0
                              else:
                                 return 71.0
                           else:
                              return 71.0
                        else:
                           return 71.0
                     else:
                        return 89.41304347826087
                  elif obj[0]<=3:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 5, "metric_value": 26.929, "depth": 7}
                     if obj[4]>-19:
                        return 9.75
                     elif obj[4]<=-19:
                        return 85
                     else:
                        return 24.8
                  else:
                     return 83.07843137254902
               elif obj[6]<=-189.97894736842105:
                  # {"feature": "PTime_A_VS_B_Diff", "instances": 44, "metric_value": 5.7996, "depth": 6}
                  if obj[4]<=-5.318181818181818:
                     # {"feature": "NumWaitingJob", "instances": 24, "metric_value": 2.9938, "depth": 7}
                     if obj[0]<=6:
                        # {"feature": "PTime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 133.15384615384616
                              else:
                                 return 133.15384615384616
                           else:
                              return 133.15384615384616
                        else:
                           return 133.15384615384616
                     elif obj[0]>6:
                        # {"feature": "PTime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 102.9090909090909
                              else:
                                 return 102.9090909090909
                           else:
                              return 102.9090909090909
                        else:
                           return 102.9090909090909
                     else:
                        return 119.29166666666667
                  elif obj[4]>-5.318181818181818:
                     # {"feature": "NumWaitingJob", "instances": 20, "metric_value": 10.1895, "depth": 7}
                     if obj[0]>6:
                        # {"feature": "PTime_A_VS_B", "instances": 12, "metric_value": 7.8146, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 188.8
                              else:
                                 return 188.8
                           else:
                              return 188.8
                        elif obj[3] == '<':
                           return 280.0
                        else:
                           return 204.0
                     elif obj[0]<=6:
                        # {"feature": "PTime_A_VS_B", "instances": 8, "metric_value": 0.1429, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 133.8
                              else:
                                 return 133.8
                           else:
                              return 133.8
                        elif obj[3] == '<':
                           return 125.33333333333333
                        else:
                           return 130.625
                     else:
                        return 174.65
                  else:
                     return 144.45454545454547
               else:
                  return 111.50526315789473
            else:
               return 148.33505154639175
         else:
            return 103.70711974110033
      else:
         return 81.64276885043263
   elif obj[2]>20.046956977964324:
      # {"feature": "Start_A_VS_B_Diff", "instances": 3579, "metric_value": 3.059, "depth": 2}
      if obj[8]>-80.72659165787546:
         # {"feature": "PTime_A_VS_B", "instances": 3024, "metric_value": 2.8281, "depth": 3}
         if obj[3] == '>':
            # {"feature": "NumWaitingJob", "instances": 1916, "metric_value": 2.6955, "depth": 4}
            if obj[0]>9:
               # {"feature": "Start_A_VS_B", "instances": 1148, "metric_value": 3.0506, "depth": 5}
               if obj[7] == '>':
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 890, "metric_value": 5.2565, "depth": 6}
                  if obj[10]<=76.04403290780901:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 745, "metric_value": 1.5707, "depth": 7}
                     if obj[6]<=110.56644295302013:
                        # {"feature": "Tardy_A_VS_B", "instances": 420, "metric_value": 2.3981, "depth": 8}
                        if obj[9] == '=':
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 275, "metric_value": 0.5444, "depth": 9}
                           if obj[4]<=10.967272727272727:
                              # {"feature": "STime_A_VS_B", "instances": 146, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 116.54109589041096
                              else:
                                 return 116.54109589041096
                           elif obj[4]>10.967272727272727:
                              # {"feature": "STime_A_VS_B", "instances": 129, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 131.37209302325581
                              else:
                                 return 131.37209302325581
                           else:
                              return 123.49818181818182
                        elif obj[9] == '>':
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 145, "metric_value": 0.2128, "depth": 9}
                           if obj[4]>1:
                              # {"feature": "STime_A_VS_B", "instances": 127, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 159.90551181102362
                              else:
                                 return 159.90551181102362
                           elif obj[4]<=1:
                              # {"feature": "STime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 156.83333333333334
                              else:
                                 return 156.83333333333334
                           else:
                              return 159.5241379310345
                        else:
                           return 135.93571428571428
                     elif obj[6]>110.56644295302013:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 325, "metric_value": 2.8066, "depth": 8}
                        if obj[4]>6.02399935086014:
                           # {"feature": "Tardy_A_VS_B", "instances": 254, "metric_value": 0.0375, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "STime_A_VS_B", "instances": 132, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 182.1060606060606
                              else:
                                 return 182.1060606060606
                           elif obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 122, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 177.55737704918033
                              else:
                                 return 177.55737704918033
                           else:
                              return 179.92125984251967
                        elif obj[4]<=6.02399935086014:
                           # {"feature": "Tardy_A_VS_B", "instances": 71, "metric_value": 0.9097, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "STime_A_VS_B", "instances": 41, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 130.21951219512195
                              else:
                                 return 130.21951219512195
                           elif obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 30, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 116.8
                              else:
                                 return 116.8
                           else:
                              return 124.54929577464789
                        else:
                           return 167.82461538461538
                     else:
                        return 149.8469798657718
                  elif obj[10]>76.04403290780901:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 145, "metric_value": 2.689, "depth": 7}
                     if obj[4]>1:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 141, "metric_value": 1.3075, "depth": 8}
                        if obj[6]<=204.82451219892508:
                           # {"feature": "STime_A_VS_B", "instances": 117, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 117, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 237.15384615384616
                              else:
                                 return 237.15384615384616
                           else:
                              return 237.15384615384616
                        elif obj[6]>204.82451219892508:
                           # {"feature": "STime_A_VS_B", "instances": 24, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 24, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 194.95833333333334
                              else:
                                 return 194.95833333333334
                           else:
                              return 194.95833333333334
                        else:
                           return 229.97163120567376
                     elif obj[4]<=1:
                        return 343.0
                     else:
                        return 233.08965517241379
                  else:
                     return 163.40898876404495
               elif obj[7] == '<':
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 250, "metric_value": 4.5928, "depth": 6}
                  if obj[10]<=60.7702416210906:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 241, "metric_value": 2.6666, "depth": 7}
                     if obj[6]>-44:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 239, "metric_value": 1.7147, "depth": 8}
                        if obj[4]>4.880839910075642:
                           # {"feature": "Tardy_A_VS_B", "instances": 202, "metric_value": 0.5828, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 138, "metric_value": 1.2299, "depth": 10}
                              if obj[5] == '>':
                                 return 217.96039603960395
                              elif obj[5] == '<':
                                 return 244.57575757575756
                              elif obj[5] == '=':
                                 return 190.75
                              else:
                                 return 223.53623188405797
                           elif obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 54, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 229.07407407407408
                              else:
                                 return 229.07407407407408
                           elif obj[9] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 188.0
                              else:
                                 return 188.0
                           else:
                              return 223.25742574257427
                        elif obj[4]<=4.880839910075642:
                           # {"feature": "Tardy_A_VS_B", "instances": 37, "metric_value": 1.3256, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 27, "metric_value": 0.2083, "depth": 10}
                              if obj[5] == '>':
                                 return 172.58823529411765
                              elif obj[5] == '<':
                                 return 181.9
                              else:
                                 return 176.03703703703704
                           elif obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 180.28571428571428
                              else:
                                 return 180.28571428571428
                           elif obj[9] == '<':
                              return 156.0
                           else:
                              return 175.21621621621622
                        else:
                           return 215.82008368200837
                     elif obj[6]<=-44:
                        return 446
                     else:
                        return 217.73029045643153
                  elif obj[10]>60.7702416210906:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 9, "metric_value": 9.3273, "depth": 7}
                     if obj[4]<=14:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 5, "metric_value": 6.0768, "depth": 8}
                        if obj[6]<=68:
                           return 379.0
                        elif obj[6]>68:
                           return 392
                        else:
                           return 384.2
                     elif obj[4]>14:
                        return 339.0
                     else:
                        return 364.1111111111111
                  else:
                     return 223.0
               elif obj[7] == '=':
                  # {"feature": "PTime_A_VS_B_Diff", "instances": 8, "metric_value": 20.2969, "depth": 6}
                  if obj[4]>1:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 7, "metric_value": 22.2866, "depth": 7}
                     if obj[6]<=57:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 5, "metric_value": 4.6065, "depth": 8}
                        if obj[10]<=26:
                           return 173.75
                        elif obj[10]>26:
                           return 199
                        else:
                           return 178.8
                     elif obj[6]>57:
                        return 264.0
                     else:
                        return 203.14285714285714
                  elif obj[4]<=1:
                     return 75
                  else:
                     return 187.125
               else:
                  return 176.551393728223
            elif obj[0]<=9:
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 768, "metric_value": 4.2764, "depth": 5}
               if obj[6]<=129.97005208333334:
                  # {"feature": "PTime_A_VS_B_Diff", "instances": 403, "metric_value": 2.7296, "depth": 6}
                  if obj[4]<=11.838709677419354:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 204, "metric_value": 1.0124, "depth": 7}
                     if obj[10]<=87.36918760576457:
                        # {"feature": "Start_A_VS_B", "instances": 162, "metric_value": 0.3266, "depth": 8}
                        if obj[7] == '<':
                           # {"feature": "Tardy_A_VS_B", "instances": 89, "metric_value": 1.4424, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 59, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 90.71186440677967
                              else:
                                 return 90.71186440677967
                           elif obj[9] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 96.83333333333333
                              else:
                                 return 96.83333333333333
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 12, "metric_value": 6.1048, "depth": 10}
                              if obj[5] == '<':
                                 return 107.57142857142857
                              elif obj[5] == '>':
                                 return 158.4
                              else:
                                 return 128.75
                           else:
                              return 97.07865168539325
                        elif obj[7] == '>':
                           # {"feature": "Tardy_A_VS_B", "instances": 73, "metric_value": 0.6721, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 66, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 88.71212121212122
                              else:
                                 return 88.71212121212122
                           elif obj[9] == '=':
                              # {"feature": "STime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 60.42857142857143
                              else:
                                 return 60.42857142857143
                           else:
                              return 86.0
                        else:
                           return 92.08641975308642
                     elif obj[10]>87.36918760576457:
                        # {"feature": "STime_A_VS_B", "instances": 42, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 42, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 42, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 110.5
                              else:
                                 return 110.5
                           else:
                              return 110.5
                        else:
                           return 110.5
                     else:
                        return 95.87745098039215
                  elif obj[4]>11.838709677419354:
                     # {"feature": "Start_A_VS_B", "instances": 199, "metric_value": 2.2509, "depth": 7}
                     if obj[7] == '>':
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 111, "metric_value": 1.4664, "depth": 8}
                        if obj[10]>37.83567891184631:
                           # {"feature": "STime_A_VS_B", "instances": 90, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 90, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 124.65555555555555
                              else:
                                 return 124.65555555555555
                           else:
                              return 124.65555555555555
                        elif obj[10]<=37.83567891184631:
                           # {"feature": "Tardy_A_VS_B", "instances": 21, "metric_value": 3.0096, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 17, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 96.76470588235294
                              else:
                                 return 96.76470588235294
                           elif obj[9] == '=':
                              return 79.0
                           else:
                              return 93.38095238095238
                        else:
                           return 118.73873873873873
                     elif obj[7] == '<':
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 88, "metric_value": 4.6936, "depth": 8}
                        if obj[10]>-10.702638541119008:
                           # {"feature": "Tardy_A_VS_B", "instances": 75, "metric_value": 1.7232, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 59, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 154.25423728813558
                              else:
                                 return 154.25423728813558
                           elif obj[9] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 134.0
                              else:
                                 return 134.0
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 8, "metric_value": 3.7311, "depth": 10}
                              if obj[5] == '>':
                                 return 194.14285714285714
                              elif obj[5] == '<':
                                 return 187
                              else:
                                 return 193.25
                           else:
                              return 156.25333333333333
                        elif obj[10]<=-10.702638541119008:
                           # {"feature": "STime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 97.53846153846153
                              else:
                                 return 97.53846153846153
                           else:
                              return 97.53846153846153
                        else:
                           return 147.57954545454547
                     else:
                        return 131.4924623115578
                  else:
                     return 113.46401985111663
               elif obj[6]>129.97005208333334:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 365, "metric_value": 5.4057, "depth": 6}
                  if obj[10]<=235.36650368112055:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 309, "metric_value": 0.4044, "depth": 7}
                     if obj[4]<=19.424022814005312:
                        # {"feature": "STime_A_VS_B", "instances": 253, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 253, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 253, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 148.63636363636363
                              else:
                                 return 148.63636363636363
                           else:
                              return 148.63636363636363
                        else:
                           return 148.63636363636363
                     elif obj[4]>19.424022814005312:
                        # {"feature": "STime_A_VS_B", "instances": 56, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 56, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 56, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 158.44642857142858
                              else:
                                 return 158.44642857142858
                           else:
                              return 158.44642857142858
                        else:
                           return 158.44642857142858
                     else:
                        return 150.41423948220066
                  elif obj[10]>235.36650368112055:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 56, "metric_value": 4.13, "depth": 7}
                     if obj[4]<=19:
                        # {"feature": "STime_A_VS_B", "instances": 45, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 45, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 45, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 219.4
                              else:
                                 return 219.4
                           else:
                              return 219.4
                        else:
                           return 219.4
                     elif obj[4]>19:
                        # {"feature": "STime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 281.72727272727275
                              else:
                                 return 281.72727272727275
                           else:
                              return 281.72727272727275
                        else:
                           return 281.72727272727275
                     else:
                        return 231.64285714285714
                  else:
                     return 162.87671232876713
               else:
                  return 136.94791666666666
            else:
               return 160.6769311064718
         elif obj[3] == '<':
            # {"feature": "Tardy_A_VS_B", "instances": 1011, "metric_value": 1.587, "depth": 4}
            if obj[9] == '>':
               # {"feature": "NumWaitingJob", "instances": 497, "metric_value": 5.1714, "depth": 5}
               if obj[0]<=11:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 349, "metric_value": 5.0348, "depth": 6}
                  if obj[10]<=164.8886690079105:
                     # {"feature": "Start_A_VS_B", "instances": 291, "metric_value": 1.8495, "depth": 7}
                     if obj[7] == '>':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 233, "metric_value": 1.0774, "depth": 8}
                        if obj[6]<=236.2382775611406:
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 231, "metric_value": 1.2119, "depth": 9}
                           if obj[4]>-23.04733075508237:
                              # {"feature": "STime_A_VS_B", "instances": 221, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 102.21719457013575
                              else:
                                 return 102.21719457013575
                           elif obj[4]<=-23.04733075508237:
                              # {"feature": "STime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 51.6
                              else:
                                 return 51.6
                           else:
                              return 100.02597402597402
                        elif obj[6]>236.2382775611406:
                           return 210
                        else:
                           return 100.96995708154506
                     elif obj[7] == '<':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 54, "metric_value": 5.7163, "depth": 8}
                        if obj[6]<=25.22222222222222:
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 29, "metric_value": 7.3038, "depth": 9}
                           if obj[4]>-16:
                              # {"feature": "STime_A_VS_B", "instances": 23, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 81.73913043478261
                              else:
                                 return 81.73913043478261
                           elif obj[4]<=-16:
                              # {"feature": "STime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 22.833333333333332
                              else:
                                 return 22.833333333333332
                           else:
                              return 69.55172413793103
                        elif obj[6]>25.22222222222222:
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 25, "metric_value": 8.5347, "depth": 9}
                           if obj[4]<=-4:
                              # {"feature": "STime_A_VS_B", "instances": 17, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 92.70588235294117
                              else:
                                 return 92.70588235294117
                           elif obj[4]>-4:
                              # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 157.625
                              else:
                                 return 157.625
                           else:
                              return 113.48
                        else:
                           return 89.88888888888889
                     elif obj[7] == '=':
                        return 214.0
                     else:
                        return 100.46735395189003
                  elif obj[10]>164.8886690079105:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 58, "metric_value": 4.2676, "depth": 7}
                     if obj[6]<=250.82758620689654:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 32, "metric_value": 9.8863, "depth": 8}
                        if obj[4]<=-8:
                           # {"feature": "STime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 119.11111111111111
                              else:
                                 return 119.11111111111111
                           else:
                              return 119.11111111111111
                        elif obj[4]>-8:
                           # {"feature": "STime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 193.5
                              else:
                                 return 193.5
                           else:
                              return 193.5
                        else:
                           return 151.65625
                     elif obj[6]>250.82758620689654:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 26, "metric_value": 3.6503, "depth": 8}
                        if obj[4]<=-5:
                           # {"feature": "STime_A_VS_B", "instances": 23, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 23, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 189.69565217391303
                              else:
                                 return 189.69565217391303
                           else:
                              return 189.69565217391303
                        elif obj[4]>-5:
                           return 227.66666666666666
                        else:
                           return 194.07692307692307
                     else:
                        return 170.67241379310346
                  else:
                     return 112.13467048710602
               elif obj[0]>11:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 148, "metric_value": 4.5262, "depth": 6}
                  if obj[6]>4:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 147, "metric_value": 2.5404, "depth": 7}
                     if obj[4]>-14.124638494420333:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 122, "metric_value": 2.0881, "depth": 8}
                        if obj[10]<=104.73172192104806:
                           # {"feature": "Start_A_VS_B", "instances": 114, "metric_value": 1.543, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 87, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 165.5287356321839
                              else:
                                 return 165.5287356321839
                           elif obj[7] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 22, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 200.4090909090909
                              else:
                                 return 200.4090909090909
                           elif obj[7] == '=':
                              # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 144.8
                              else:
                                 return 144.8
                           else:
                              return 171.35087719298247
                        elif obj[10]>104.73172192104806:
                           # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 234.875
                              else:
                                 return 234.875
                           else:
                              return 234.875
                        else:
                           return 175.51639344262296
                     elif obj[4]<=-14.124638494420333:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 25, "metric_value": 12.1636, "depth": 8}
                        if obj[10]>10:
                           # {"feature": "Start_A_VS_B", "instances": 22, "metric_value": 4.4203, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 16, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 129.625
                              else:
                                 return 129.625
                           elif obj[7] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 152.5
                              else:
                                 return 152.5
                           else:
                              return 135.86363636363637
                        elif obj[10]<=10:
                           return 27.0
                        else:
                           return 122.8
                     else:
                        return 166.55102040816325
                  elif obj[6]<=4:
                     return 515
                  else:
                     return 168.90540540540542
               else:
                  return 129.04024144869214
            elif obj[9] == '=':
               # {"feature": "Start_A_VS_B", "instances": 433, "metric_value": 6.2434, "depth": 5}
               if obj[7] == '>':
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 279, "metric_value": 2.0998, "depth": 6}
                  if obj[6]>86.0:
                     # {"feature": "NumWaitingJob", "instances": 140, "metric_value": 4.3017, "depth": 7}
                     if obj[0]<=16:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 97, "metric_value": 2.0249, "depth": 8}
                        if obj[4]<=-3.267006801498413:
                           # {"feature": "STime_A_VS_B", "instances": 78, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 78, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 78.43589743589743
                              else:
                                 return 78.43589743589743
                           else:
                              return 78.43589743589743
                        elif obj[4]>-3.267006801498413:
                           # {"feature": "STime_A_VS_B", "instances": 19, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 19, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 115.05263157894737
                              else:
                                 return 115.05263157894737
                           else:
                              return 115.05263157894737
                        else:
                           return 85.6082474226804
                     elif obj[0]>16:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 43, "metric_value": 2.6606, "depth": 8}
                        if obj[4]>-23.33276753734593:
                           # {"feature": "STime_A_VS_B", "instances": 41, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 41, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 136.5121951219512
                              else:
                                 return 136.5121951219512
                           else:
                              return 136.5121951219512
                        elif obj[4]<=-23.33276753734593:
                           return 66.0
                        else:
                           return 133.2325581395349
                     else:
                        return 100.23571428571428
                  elif obj[6]<=86.0:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 139, "metric_value": 1.7241, "depth": 7}
                     if obj[4]>-14.712997326154992:
                        # {"feature": "NumWaitingJob", "instances": 120, "metric_value": 1.0963, "depth": 8}
                        if obj[0]<=16:
                           # {"feature": "STime_A_VS_B", "instances": 94, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 94, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 78.70212765957447
                              else:
                                 return 78.70212765957447
                           else:
                              return 78.70212765957447
                        elif obj[0]>16:
                           # {"feature": "STime_A_VS_B", "instances": 26, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 26, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 61.42307692307692
                              else:
                                 return 61.42307692307692
                           else:
                              return 61.42307692307692
                        else:
                           return 74.95833333333333
                     elif obj[4]<=-14.712997326154992:
                        # {"feature": "NumWaitingJob", "instances": 19, "metric_value": 3.7653, "depth": 8}
                        if obj[0]>10:
                           # {"feature": "STime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 40.166666666666664
                              else:
                                 return 40.166666666666664
                           else:
                              return 40.166666666666664
                        elif obj[0]<=10:
                           return 100
                        else:
                           return 43.31578947368421
                     else:
                        return 70.63309352517986
                  else:
                     return 85.48745519713262
               elif obj[7] == '<':
                  # {"feature": "PTime_A_VS_B_Diff", "instances": 150, "metric_value": 2.8978, "depth": 6}
                  if obj[4]>-9.706666666666667:
                     # {"feature": "CompTime_A_VS_B", "instances": 79, "metric_value": 3.6533, "depth": 7}
                     if obj[5] == '<':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 40, "metric_value": 3.306, "depth": 8}
                        if obj[6]<=-13.772980739362517:
                           # {"feature": "NumWaitingJob", "instances": 32, "metric_value": 3.3902, "depth": 9}
                           if obj[0]<=14:
                              # {"feature": "STime_A_VS_B", "instances": 26, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 170.42307692307693
                              else:
                                 return 170.42307692307693
                           elif obj[0]>14:
                              # {"feature": "STime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 119.16666666666667
                              else:
                                 return 119.16666666666667
                           else:
                              return 160.8125
                        elif obj[6]>-13.772980739362517:
                           # {"feature": "NumWaitingJob", "instances": 8, "metric_value": 11.525, "depth": 9}
                           if obj[0]<=13:
                              # {"feature": "STime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 178.66666666666666
                              else:
                                 return 178.66666666666666
                           elif obj[0]>13:
                              return 222.0
                           else:
                              return 189.5
                        else:
                           return 166.55
                     elif obj[5] == '>':
                        # {"feature": "NumWaitingJob", "instances": 37, "metric_value": 2.8835, "depth": 8}
                        if obj[0]>12:
                           # {"feature": "CompTime_A_VS_B_Diff", "instances": 24, "metric_value": 9.552, "depth": 9}
                           if obj[6]<=44:
                              # {"feature": "STime_A_VS_B", "instances": 21, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 147.0
                              else:
                                 return 147.0
                           elif obj[6]>44:
                              return 238.66666666666666
                           else:
                              return 158.45833333333334
                        elif obj[0]<=12:
                           # {"feature": "CompTime_A_VS_B_Diff", "instances": 13, "metric_value": 15.13, "depth": 9}
                           if obj[6]>9:
                              # {"feature": "STime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 146.5
                              else:
                                 return 146.5
                           elif obj[6]<=9:
                              return 76.33333333333333
                           else:
                              return 130.30769230769232
                        else:
                           return 148.56756756756758
                     elif obj[5] == '=':
                        return 286.0
                     else:
                        return 161.15189873417722
                  elif obj[4]<=-9.706666666666667:
                     # {"feature": "NumWaitingJob", "instances": 71, "metric_value": 3.6552, "depth": 7}
                     if obj[0]<=14:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 55, "metric_value": 1.6834, "depth": 8}
                        if obj[6]>-63:
                           # {"feature": "CompTime_A_VS_B", "instances": 53, "metric_value": 0.6567, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 30, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 117.23333333333333
                              else:
                                 return 117.23333333333333
                           elif obj[5] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 23, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 101.0
                              else:
                                 return 101.0
                           else:
                              return 110.18867924528301
                        elif obj[6]<=-63:
                           return 164.0
                        else:
                           return 112.14545454545454
                     elif obj[0]>14:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 16, "metric_value": 12.1778, "depth": 8}
                        if obj[6]<=42:
                           # {"feature": "CompTime_A_VS_B", "instances": 15, "metric_value": 7.6267, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 154.25
                              else:
                                 return 154.25
                           elif obj[5] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 138.85714285714286
                              else:
                                 return 138.85714285714286
                           else:
                              return 147.06666666666666
                        elif obj[6]>42:
                           return 305
                        else:
                           return 156.9375
                     else:
                        return 122.2394366197183
                  else:
                     return 142.73333333333332
               elif obj[7] == '=':
                  return 39.75
               else:
                  return 104.8960739030023
            elif obj[9] == '<':
               # {"feature": "NumWaitingJob", "instances": 81, "metric_value": 2.0412, "depth": 5}
               if obj[0]<=9:
                  # {"feature": "PTime_A_VS_B_Diff", "instances": 53, "metric_value": 4.116, "depth": 6}
                  if obj[4]>-16:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 36, "metric_value": 4.3205, "depth": 7}
                     if obj[10]>-28.057446021243337:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 31, "metric_value": 2.4186, "depth": 8}
                        if obj[6]<=-12:
                           # {"feature": "STime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 83.22222222222223
                              else:
                                 return 83.22222222222223
                           else:
                              return 83.22222222222223
                        elif obj[6]>-12:
                           # {"feature": "STime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 69.0
                              else:
                                 return 69.0
                           else:
                              return 69.0
                        else:
                           return 77.25806451612904
                     elif obj[10]<=-28.057446021243337:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 5, "metric_value": 4.3888, "depth": 8}
                        if obj[6]<=-32:
                           return 30.5
                        elif obj[6]>-32:
                           return 6
                        else:
                           return 25.6
                     else:
                        return 70.08333333333333
                  elif obj[4]<=-16:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 17, "metric_value": 8.415, "depth": 7}
                     if obj[10]>-22:
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 13, "metric_value": 12.3647, "depth": 8}
                        if obj[6]<=-17:
                           # {"feature": "STime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 156.42857142857142
                              else:
                                 return 156.42857142857142
                           else:
                              return 156.42857142857142
                        elif obj[6]>-17:
                           # {"feature": "STime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 91.33333333333333
                              else:
                                 return 91.33333333333333
                           else:
                              return 91.33333333333333
                        else:
                           return 126.38461538461539
                     elif obj[10]<=-22:
                        return 62.5
                     else:
                        return 111.3529411764706
                  else:
                     return 83.32075471698113
               elif obj[0]>9:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 28, "metric_value": 6.212, "depth": 6}
                  if obj[6]>-46.02430999242186:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 22, "metric_value": 11.5732, "depth": 7}
                     if obj[10]>-43:
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 19, "metric_value": 7.617, "depth": 8}
                        if obj[4]<=-8:
                           # {"feature": "STime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 11, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 77.18181818181819
                              else:
                                 return 77.18181818181819
                           else:
                              return 77.18181818181819
                        elif obj[4]>-8:
                           # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 142.375
                              else:
                                 return 142.375
                           else:
                              return 142.375
                        else:
                           return 104.63157894736842
                     elif obj[10]<=-43:
                        return 218.66666666666666
                     else:
                        return 120.18181818181819
                  elif obj[6]<=-46.02430999242186:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 6, "metric_value": 14.1578, "depth": 7}
                     if obj[10]<=-28:
                        return 89.5
                     elif obj[10]>-28:
                        return 43.0
                     else:
                        return 74.0
                  else:
                     return 110.28571428571429
               else:
                  return 92.64197530864197
            else:
               return 115.78338278931751
         elif obj[3] == '=':
            # {"feature": "NumWaitingJob", "instances": 97, "metric_value": 12.7934, "depth": 4}
            if obj[0]<=10:
               # {"feature": "Start_A_VS_B", "instances": 50, "metric_value": 9.0337, "depth": 5}
               if obj[7] == '>':
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 33, "metric_value": 8.417, "depth": 6}
                  if obj[10]<=111.93939393939394:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 18, "metric_value": 2.9166, "depth": 7}
                     if obj[6]<=118:
                        # {"feature": "Tardy_A_VS_B", "instances": 16, "metric_value": 0.272, "depth": 8}
                        if obj[9] == '>':
                           # {"feature": "STime_A_VS_B", "instances": 13, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "PTime_A_VS_B_Diff", "instances": 13, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=0:
                                 return 53.30769230769231
                              else:
                                 return 53.30769230769231
                           else:
                              return 53.30769230769231
                        elif obj[9] == '=':
                           return 59.0
                        else:
                           return 54.375
                     elif obj[6]>118:
                        return 21.0
                     else:
                        return 50.666666666666664
                  elif obj[10]>111.93939393939394:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 15, "metric_value": 5.9188, "depth": 7}
                     if obj[6]>165:
                        # {"feature": "STime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 10, "metric_value": 0.0, "depth": 9}
                           if obj[4]<=0:
                              # {"feature": "CompTime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 83.4
                              else:
                                 return 83.4
                           else:
                              return 83.4
                        else:
                           return 83.4
                     elif obj[6]<=165:
                        # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "PTime_A_VS_B_Diff", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[4]<=0:
                              # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '>':
                                 return 132.6
                              else:
                                 return 132.6
                           else:
                              return 132.6
                        else:
                           return 132.6
                     else:
                        return 99.8
                  else:
                     return 73.0
               elif obj[7] == '<':
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 17, "metric_value": 17.979, "depth": 6}
                  if obj[6]>-25:
                     # {"feature": "Tardy_A_VS_B", "instances": 11, "metric_value": 33.5185, "depth": 7}
                     if obj[9] == '<':
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 5, "metric_value": 43.8924, "depth": 8}
                        if obj[10]>-13:
                           return 126.66666666666667
                        elif obj[10]<=-13:
                           return 259
                        else:
                           return 179.6
                     elif obj[9] == '>':
                        return 101.25
                     elif obj[9] == '=':
                        return 279
                     else:
                        return 169.1818181818182
                  elif obj[6]<=-25:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 6, "metric_value": 36.1038, "depth": 7}
                     if obj[10]>-48:
                        return 39.25
                     elif obj[10]<=-48:
                        return 124
                     else:
                        return 67.5
                  else:
                     return 133.2941176470588
               else:
                  return 93.5
            elif obj[0]>10:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 47, "metric_value": 34.8131, "depth": 5}
               if obj[10]<=35:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 37, "metric_value": 14.4822, "depth": 6}
                  if obj[6]>-36:
                     # {"feature": "Start_A_VS_B", "instances": 35, "metric_value": 7.1957, "depth": 7}
                     if obj[7] == '>':
                        # {"feature": "Tardy_A_VS_B", "instances": 26, "metric_value": 3.4043, "depth": 8}
                        if obj[9] == '=':
                           # {"feature": "STime_A_VS_B", "instances": 18, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "PTime_A_VS_B_Diff", "instances": 18, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=0:
                                 return 128.55555555555554
                              else:
                                 return 128.55555555555554
                           else:
                              return 128.55555555555554
                        elif obj[9] == '>':
                           # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "PTime_A_VS_B_Diff", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=0:
                                 return 96.5
                              else:
                                 return 96.5
                           else:
                              return 96.5
                        else:
                           return 118.6923076923077
                     elif obj[7] == '<':
                        # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 27.1552, "depth": 8}
                        if obj[5] == '>':
                           # {"feature": "Tardy_A_VS_B", "instances": 6, "metric_value": 7.2886, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[1] == '>':
                                 return 231.4
                              else:
                                 return 231.4
                           elif obj[9] == '>':
                              return 185
                           else:
                              return 223.66666666666666
                        elif obj[5] == '<':
                           return 110.33333333333333
                        else:
                           return 185.88888888888889
                     else:
                        return 135.97142857142856
                  elif obj[6]<=-36:
                     return 323
                  else:
                     return 146.0810810810811
               elif obj[10]>35:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 10, "metric_value": 17.9243, "depth": 6}
                  if obj[6]>74:
                     # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1] == '>':
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "CompTime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '>':
                                 return 315.75
                              else:
                                 return 315.75
                           else:
                              return 315.75
                        else:
                           return 315.75
                     else:
                        return 315.75
                  elif obj[6]<=74:
                     return 393
                  else:
                     return 331.2
               else:
                  return 185.46808510638297
            else:
               return 138.06185567010309
         else:
            return 144.94246031746033
      elif obj[8]<=-80.72659165787546:
         # {"feature": "NumWaitingJob", "instances": 555, "metric_value": 6.7555, "depth": 3}
         if obj[0]>5:
            # {"feature": "PTime_A_VS_B", "instances": 449, "metric_value": 6.808, "depth": 4}
            if obj[3] == '>':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 236, "metric_value": 3.0323, "depth": 5}
               if obj[4]<=18.483712503142318:
                  # {"feature": "Tardy_A_VS_B", "instances": 193, "metric_value": 2.0006, "depth": 6}
                  if obj[9] == '<':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 142, "metric_value": 1.6147, "depth": 7}
                     if obj[6]>-98.5:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 79, "metric_value": 1.6319, "depth": 8}
                        if obj[10]>-84:
                           # {"feature": "STime_A_VS_B", "instances": 77, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 77, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 227.15584415584416
                              else:
                                 return 227.15584415584416
                           else:
                              return 227.15584415584416
                        elif obj[10]<=-84:
                           return 162.5
                        else:
                           return 225.51898734177215
                     elif obj[6]<=-98.5:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 63, "metric_value": 5.6476, "depth": 8}
                        if obj[10]>-88.9047619047619:
                           # {"feature": "STime_A_VS_B", "instances": 33, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 33, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 289.54545454545456
                              else:
                                 return 289.54545454545456
                           else:
                              return 289.54545454545456
                        elif obj[10]<=-88.9047619047619:
                           # {"feature": "STime_A_VS_B", "instances": 30, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 30, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 218.5
                              else:
                                 return 218.5
                           else:
                              return 218.5
                        else:
                           return 255.71428571428572
                     else:
                        return 238.91549295774647
                  elif obj[9] == '=':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 51, "metric_value": 4.3693, "depth": 7}
                     if obj[6]>-122:
                        # {"feature": "STime_A_VS_B", "instances": 50, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 50, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 50, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 281.7
                              else:
                                 return 281.7
                           else:
                              return 281.7
                        else:
                           return 281.7
                     elif obj[6]<=-122:
                        return 470
                     else:
                        return 285.3921568627451
                  else:
                     return 251.19689119170985
               elif obj[4]>18.483712503142318:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 43, "metric_value": 17.2102, "depth": 6}
                  if obj[10]>-86:
                     # {"feature": "Tardy_A_VS_B", "instances": 36, "metric_value": 4.2964, "depth": 7}
                     if obj[9] == '=':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 19, "metric_value": 9.4557, "depth": 8}
                        if obj[6]<=-28:
                           # {"feature": "STime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 345.07142857142856
                              else:
                                 return 345.07142857142856
                           else:
                              return 345.07142857142856
                        elif obj[6]>-28:
                           # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 286.2
                              else:
                                 return 286.2
                           else:
                              return 286.2
                        else:
                           return 329.57894736842104
                     elif obj[9] == '<':
                        # {"feature": "CompTime_A_VS_B_Diff", "instances": 16, "metric_value": 21.255, "depth": 8}
                        if obj[6]<=-45:
                           # {"feature": "STime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 10, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 323.7
                              else:
                                 return 323.7
                           else:
                              return 323.7
                        elif obj[6]>-45:
                           # {"feature": "STime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 6, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 419.0
                              else:
                                 return 419.0
                           else:
                              return 419.0
                        else:
                           return 359.4375
                     elif obj[9] == '>':
                        return 296
                     else:
                        return 341.9166666666667
                  elif obj[10]<=-86:
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 7, "metric_value": 16.463, "depth": 7}
                     if obj[6]>-164:
                        # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 170.6
                              else:
                                 return 170.6
                           else:
                              return 170.6
                        else:
                           return 170.6
                     elif obj[6]<=-164:
                        return 238
                     else:
                        return 189.85714285714286
                  else:
                     return 317.16279069767444
               else:
                  return 263.21610169491527
            elif obj[3] == '<':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 198, "metric_value": 3.3567, "depth": 5}
               if obj[4]>-11.272727272727273:
                  # {"feature": "Tardy_A_VS_B", "instances": 115, "metric_value": 2.997, "depth": 6}
                  if obj[9] == '<':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 92, "metric_value": 4.1327, "depth": 7}
                     if obj[6]>-113.54347826086956:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 56, "metric_value": 4.6105, "depth": 8}
                        if obj[10]>-45.392857142857146:
                           # {"feature": "STime_A_VS_B", "instances": 28, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 28, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 200.78571428571428
                              else:
                                 return 200.78571428571428
                           else:
                              return 200.78571428571428
                        elif obj[10]<=-45.392857142857146:
                           # {"feature": "STime_A_VS_B", "instances": 28, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 28, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 146.07142857142858
                              else:
                                 return 146.07142857142858
                           else:
                              return 146.07142857142858
                        else:
                           return 173.42857142857142
                     elif obj[6]<=-113.54347826086956:
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 36, "metric_value": 11.0048, "depth": 8}
                        if obj[10]>-165.04810034138177:
                           # {"feature": "STime_A_VS_B", "instances": 31, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 31, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 248.38709677419354
                              else:
                                 return 248.38709677419354
                           else:
                              return 248.38709677419354
                        elif obj[10]<=-165.04810034138177:
                           # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 117.6
                              else:
                                 return 117.6
                           else:
                              return 117.6
                        else:
                           return 230.22222222222223
                     else:
                        return 195.65217391304347
                  elif obj[9] == '=':
                     # {"feature": "CompTime_A_VS_B_Diff", "instances": 23, "metric_value": 29.2735, "depth": 7}
                     if obj[6]<=-73:
                        # {"feature": "STime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 14, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 186.5
                              else:
                                 return 186.5
                           else:
                              return 186.5
                        else:
                           return 186.5
                     elif obj[6]>-73:
                        # {"feature": "STime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 9, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 350.1111111111111
                              else:
                                 return 350.1111111111111
                           else:
                              return 350.1111111111111
                        else:
                           return 350.1111111111111
                     else:
                        return 250.52173913043478
                  else:
                     return 206.62608695652173
               elif obj[4]<=-11.272727272727273:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 83, "metric_value": 2.3146, "depth": 6}
                  if obj[6]>-250.91808278747226:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 78, "metric_value": 0.8451, "depth": 7}
                     if obj[10]<=-11.59029577033958:
                        # {"feature": "STime_A_VS_B", "instances": 57, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 57, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 57, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 155.9298245614035
                              else:
                                 return 155.9298245614035
                           else:
                              return 155.9298245614035
                        else:
                           return 155.9298245614035
                     elif obj[10]>-11.59029577033958:
                        # {"feature": "Tardy_A_VS_B", "instances": 21, "metric_value": 1.93, "depth": 8}
                        if obj[9] == '=':
                           # {"feature": "STime_A_VS_B", "instances": 20, "metric_value": 0.0, "depth": 9}
                           if obj[1] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 20, "metric_value": 0.0, "depth": 10}
                              if obj[5] == '<':
                                 return 182.05
                              else:
                                 return 182.05
                           else:
                              return 182.05
                        elif obj[9] == '<':
                           return 185
                        else:
                           return 182.1904761904762
                     else:
                        return 163.0
                  elif obj[6]<=-250.91808278747226:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 5, "metric_value": 17.0703, "depth": 7}
                     if obj[10]<=-160:
                        return 116.66666666666667
                     elif obj[10]>-160:
                        return 62
                     else:
                        return 94.8
                  else:
                     return 158.89156626506025
               else:
                  return 186.6161616161616
            elif obj[3] == '=':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 15, "metric_value": 50.2694, "depth": 5}
               if obj[6]>-172:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 13, "metric_value": 27.2348, "depth": 6}
                  if obj[10]<=-46:
                     # {"feature": "STime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 7}
                     if obj[1] == '>':
                        # {"feature": "PTime_A_VS_B_Diff", "instances": 8, "metric_value": 0.0, "depth": 8}
                        if obj[4]<=0:
                           # {"feature": "CompTime_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 8, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 110.875
                              else:
                                 return 110.875
                           else:
                              return 110.875
                        else:
                           return 110.875
                     else:
                        return 110.875
                  elif obj[10]>-46:
                     # {"feature": "Tardy_A_VS_B", "instances": 5, "metric_value": 79.8994, "depth": 7}
                     if obj[9] == '<':
                        return 292.6666666666667
                     elif obj[9] == '=':
                        return 94.0
                     else:
                        return 213.2
                  else:
                     return 150.23076923076923
               elif obj[6]<=-172:
                  return 435.5
               else:
                  return 188.26666666666668
            else:
               return 226.93318485523386
         elif obj[0]<=5:
            # {"feature": "PTime_A_VS_B", "instances": 106, "metric_value": 4.7974, "depth": 4}
            if obj[3] == '>':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 58, "metric_value": 3.7079, "depth": 5}
               if obj[6]>-198.50214831805565:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 56, "metric_value": 2.793, "depth": 6}
                  if obj[10]<=-29.300900245895242:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 47, "metric_value": 2.4115, "depth": 7}
                     if obj[4]<=17:
                        # {"feature": "STime_A_VS_B", "instances": 42, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 42, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 42, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 152.64285714285714
                              else:
                                 return 152.64285714285714
                           else:
                              return 152.64285714285714
                        else:
                           return 152.64285714285714
                     elif obj[4]>17:
                        # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 146.2
                              else:
                                 return 146.2
                           else:
                              return 146.2
                        else:
                           return 146.2
                     else:
                        return 151.95744680851064
                  elif obj[10]>-29.300900245895242:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 9, "metric_value": 17.7862, "depth": 7}
                     if obj[4]<=14:
                        # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 258.2
                              else:
                                 return 258.2
                           else:
                              return 258.2
                        else:
                           return 258.2
                     elif obj[4]>14:
                        return 147.25
                     else:
                        return 208.88888888888889
                  else:
                     return 161.10714285714286
               elif obj[6]<=-198.50214831805565:
                  return 39.5
               else:
                  return 156.91379310344828
            elif obj[3] == '<':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 48, "metric_value": 6.009, "depth": 5}
               if obj[6]<=-99.70577750372507:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 41, "metric_value": 5.0352, "depth": 6}
                  if obj[10]<=-92.80692638063994:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 33, "metric_value": 2.9609, "depth": 7}
                     if obj[4]<=-5:
                        # {"feature": "STime_A_VS_B", "instances": 28, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 28, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 28, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 107.28571428571429
                              else:
                                 return 107.28571428571429
                           else:
                              return 107.28571428571429
                        else:
                           return 107.28571428571429
                     elif obj[4]>-5:
                        # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 5, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 68.6
                              else:
                                 return 68.6
                           else:
                              return 68.6
                        else:
                           return 68.6
                     else:
                        return 101.42424242424242
                  elif obj[10]>-92.80692638063994:
                     # {"feature": "PTime_A_VS_B_Diff", "instances": 8, "metric_value": 16.0613, "depth": 7}
                     if obj[4]<=-4:
                        # {"feature": "STime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 8}
                        if obj[1] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 7, "metric_value": 0.0, "depth": 10}
                              if obj[7] == '<':
                                 return 148.42857142857142
                              else:
                                 return 148.42857142857142
                           else:
                              return 148.42857142857142
                        else:
                           return 148.42857142857142
                     elif obj[4]>-4:
                        return 243
                     else:
                        return 160.25
                  else:
                     return 112.90243902439025
               elif obj[6]>-99.70577750372507:
                  # {"feature": "Tardy_A_VS_B_Diff", "instances": 7, "metric_value": 10.5672, "depth": 6}
                  if obj[10]<=-79:
                     return 66.0
                  elif obj[10]>-79:
                     return 30.0
                  else:
                     return 50.57142857142857
               else:
                  return 103.8125
            else:
               return 132.8679245283019
         else:
            return 208.96756756756756
      else:
         return 154.87091366303437
   else:
      return 116.01888772298007
