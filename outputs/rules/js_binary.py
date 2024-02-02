def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B_Avg, obj[2]: STime_A_VS_B_Avg_Diff, obj[3]: STime_A_VS_B_Min, obj[4]: STime_A_VS_B_Min_Diff, obj[5]: STime_A_VS_B_Max, obj[6]: STime_A_VS_B_Max_Diff, obj[7]: PTime_A_VS_B_Avg, obj[8]: PTime_A_VS_B_Avg_Diff, obj[9]: PTime_A_VS_B_Min, obj[10]: PTime_A_VS_B_Min_Diff, obj[11]: PTime_A_VS_B_Max, obj[12]: PTime_A_VS_B_Max_Diff, obj[13]: Due_A_VS_B, obj[14]: Due_A_VS_B_Diff
   # {"feature": "STime_A_VS_B_Min_Diff", "instances": 6736, "metric_value": 0.9746, "depth": 1}
   if obj[4]<=30.093046521266608:
      # {"feature": "Due_A_VS_B_Diff", "instances": 6468, "metric_value": 0.9597, "depth": 2}
      if obj[14]<=148.51304287743076:
         # {"feature": "Due_A_VS_B", "instances": 6318, "metric_value": 0.9501, "depth": 3}
         if obj[13] == '<':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 3271, "metric_value": 0.6584, "depth": 4}
            if obj[2]<=41.85144684409303:
               # {"feature": "STime_A_VS_B_Min", "instances": 3269, "metric_value": 0.6572, "depth": 5}
               if obj[3] == '=':
                  # {"feature": "NumWaitingJob", "instances": 1616, "metric_value": 0.6581, "depth": 6}
                  if obj[0]>3:
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 1614, "metric_value": 0.6586, "depth": 7}
                     if obj[8]<=20.92460360381869:
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 1612, "metric_value": 0.6591, "depth": 8}
                        if obj[6]>-77:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 1611, "metric_value": 0.6593, "depth": 9}
                           if obj[10]>-24:
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 1610, "metric_value": 0.6595, "depth": 10}
                              if obj[12]>-24:
                                 return 'No'
                              elif obj[12]<=-24:
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[10]<=-24:
                              return 'No'
                           else:
                              return 'No'
                        elif obj[6]<=-77:
                           return 'No'
                        else:
                           return 'No'
                     elif obj[8]>20.92460360381869:
                        return 'No'
                     else:
                        return 'No'
                  elif obj[0]<=3:
                     return 'No'
                  else:
                     return 'No'
               elif obj[3] == '<':
                  # {"feature": "STime_A_VS_B_Max_Diff", "instances": 1132, "metric_value": 0.3878, "depth": 6}
                  if obj[6]<=39.56789438484973:
                     # {"feature": "NumWaitingJob", "instances": 1115, "metric_value": 0.379, "depth": 7}
                     if obj[0]>9:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 609, "metric_value": 0.2164, "depth": 8}
                        if obj[10]>-17.439308968467166:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 590, "metric_value": 0.2217, "depth": 9}
                           if obj[12]<=15.995623414896883:
                              # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 574, "metric_value": 0.2264, "depth": 10}
                              if obj[8]>-13.273509644624943:
                                 return 'No'
                              elif obj[8]<=-13.273509644624943:
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[12]>15.995623414896883:
                              return 'No'
                           else:
                              return 'No'
                        elif obj[10]<=-17.439308968467166:
                           return 'No'
                        else:
                           return 'No'
                     elif obj[0]<=9:
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 506, "metric_value": 0.5309, "depth": 8}
                        if obj[12]>-16.854548137284496:
                           # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 491, "metric_value": 0.5414, "depth": 9}
                           if obj[8]>-20.0:
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 490, "metric_value": 0.5364, "depth": 10}
                              if obj[10]<=7.621199807349311:
                                 return 'No'
                              elif obj[10]>7.621199807349311:
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[8]<=-20.0:
                              return 'Yes'
                           else:
                              return 'No'
                        elif obj[12]<=-16.854548137284496:
                           return 'No'
                        else:
                           return 'No'
                     else:
                        return 'No'
                  elif obj[6]>39.56789438484973:
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 17, "metric_value": 0.7871, "depth": 7}
                     if obj[8]>-3.3333333333333286:
                        return 'No'
                     elif obj[8]<=-3.3333333333333286:
                        # {"feature": "NumWaitingJob", "instances": 6, "metric_value": 0.9183, "depth": 8}
                        if obj[0]<=10:
                           # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 5, "metric_value": 0.7219, "depth": 9}
                           if obj[12]>-16:
                              return 'Yes'
                           elif obj[12]<=-16:
                              return 'No'
                           else:
                              return 'Yes'
                        elif obj[0]>10:
                           return 'No'
                        else:
                           return 'Yes'
                     else:
                        return 'No'
                  else:
                     return 'No'
               elif obj[3] == '>':
                  # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 521, "metric_value": 0.9525, "depth": 6}
                  if obj[8]>-21.0:
                     # {"feature": "NumWaitingJob", "instances": 520, "metric_value": 0.9516, "depth": 7}
                     if obj[0]>2:
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 515, "metric_value": 0.9483, "depth": 8}
                        if obj[6]>-64:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 514, "metric_value": 0.9489, "depth": 9}
                           if obj[10]>-22:
                              # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 513, "metric_value": 0.9495, "depth": 10}
                              if obj[12]>-22:
                                 return 'No'
                              elif obj[12]<=-22:
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[10]<=-22:
                              return 'No'
                           else:
                              return 'No'
                        elif obj[6]<=-64:
                           return 'No'
                        else:
                           return 'No'
                     elif obj[0]<=2:
                        # {"feature": "STime_A_VS_B_Max_Diff", "instances": 5, "metric_value": 0.7219, "depth": 8}
                        if obj[6]<=6:
                           return 'Yes'
                        elif obj[6]>6:
                           # {"feature": "PTime_A_VS_B_Min", "instances": 2, "metric_value": 1.0, "depth": 9}
                           if obj[9] == '=':
                              return 'No'
                           elif obj[9] == '>':
                              return 'Yes'
                           else:
                              return 'No'
                        else:
                           return 'Yes'
                     else:
                        return 'No'
                  elif obj[8]<=-21.0:
                     return 'Yes'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[2]>41.85144684409303:
               return 'Yes'
            else:
               return 'No'
         elif obj[13] == '>':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 2989, "metric_value": 0.9783, "depth": 4}
            if obj[2]>-42.677237412200704:
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 2980, "metric_value": 0.9774, "depth": 5}
               if obj[12]>-24.334774056212122:
                  # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 2977, "metric_value": 0.9776, "depth": 6}
                  if obj[8]>-20.732500336018333:
                     # {"feature": "STime_A_VS_B_Max_Diff", "instances": 2975, "metric_value": 0.9778, "depth": 7}
                     if obj[6]>-73:
                        # {"feature": "NumWaitingJob", "instances": 2974, "metric_value": 0.9778, "depth": 8}
                        if obj[0]>8:
                           # {"feature": "STime_A_VS_B_Min", "instances": 2226, "metric_value": 0.9274, "depth": 9}
                           if obj[3] == '=':
                              # {"feature": "STime_A_VS_B_Avg", "instances": 1379, "metric_value": 0.8936, "depth": 10}
                              if obj[1] == '>':
                                 return 'Yes'
                              elif obj[1] == '<':
                                 return 'Yes'
                              elif obj[1] == '=':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[3] == '>':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 545, "metric_value": 0.8163, "depth": 10}
                              if obj[10]>-22:
                                 return 'Yes'
                              elif obj[10]<=-22:
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[3] == '<':
                              # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 302, "metric_value": 0.932, "depth": 10}
                              if obj[10]>-21:
                                 return 'No'
                              elif obj[10]<=-21:
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'Yes'
                        elif obj[0]<=8:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 748, "metric_value": 0.9578, "depth": 9}
                           if obj[10]>-23:
                              # {"feature": "STime_A_VS_B_Min", "instances": 747, "metric_value": 0.9572, "depth": 10}
                              if obj[3] == '>':
                                 return 'Yes'
                              elif obj[3] == '<':
                                 return 'No'
                              elif obj[3] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[10]<=-23:
                              return 'Yes'
                           else:
                              return 'No'
                        else:
                           return 'Yes'
                     elif obj[6]<=-73:
                        return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[8]<=-20.732500336018333:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[12]<=-24.334774056212122:
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[2]<=-42.677237412200704:
               return 'No'
            else:
               return 'Yes'
         elif obj[13] == '=':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 58, "metric_value": 0.9689, "depth": 4}
            if obj[2]<=13.677664886106582:
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 46, "metric_value": 0.859, "depth": 5}
               if obj[6]>-53:
                  # {"feature": "STime_A_VS_B_Min", "instances": 45, "metric_value": 0.8366, "depth": 6}
                  if obj[3] == '=':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 32, "metric_value": 0.896, "depth": 7}
                     if obj[8]>-15.333333333333329:
                        # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 31, "metric_value": 0.8691, "depth": 8}
                        if obj[12]>-16:
                           # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 29, "metric_value": 0.7973, "depth": 9}
                           if obj[10]<=4:
                              # {"feature": "NumWaitingJob", "instances": 18, "metric_value": 0.5033, "depth": 10}
                              if obj[0]<=14:
                                 return 'No'
                              elif obj[0]>14:
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[10]>4:
                              # {"feature": "NumWaitingJob", "instances": 11, "metric_value": 0.994, "depth": 10}
                              if obj[0]>7:
                                 return 'No'
                              elif obj[0]<=7:
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[12]<=-16:
                           return 'Yes'
                        else:
                           return 'No'
                     elif obj[8]<=-15.333333333333329:
                        return 'Yes'
                     else:
                        return 'No'
                  elif obj[3] == '<':
                     return 'No'
                  elif obj[3] == '>':
                     # {"feature": "PTime_A_VS_B_Avg", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[7] == '>':
                        return 'Yes'
                     elif obj[7] == '<':
                        return 'No'
                     else:
                        return 'Yes'
                  else:
                     return 'No'
               elif obj[6]<=-53:
                  return 'Yes'
               else:
                  return 'No'
            elif obj[2]>13.677664886106582:
               # {"feature": "NumWaitingJob", "instances": 12, "metric_value": 0.65, "depth": 5}
               if obj[0]<=17:
                  # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 11, "metric_value": 0.4395, "depth": 6}
                  if obj[8]<=11.0:
                     return 'Yes'
                  elif obj[8]>11.0:
                     return 'No'
                  else:
                     return 'Yes'
               elif obj[0]>17:
                  return 'No'
               else:
                  return 'Yes'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[14]>148.51304287743076:
         # {"feature": "NumWaitingJob", "instances": 150, "metric_value": 0.3534, "depth": 3}
         if obj[0]>8:
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 138, "metric_value": 0.1511, "depth": 4}
            if obj[2]>-17.66713351860531:
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 134, "metric_value": 0.1119, "depth": 5}
               if obj[6]>-11.627100172672435:
                  # {"feature": "STime_A_VS_B_Min", "instances": 118, "metric_value": 0.0705, "depth": 6}
                  if obj[3] == '=':
                     return 'Yes'
                  elif obj[3] == '>':
                     return 'Yes'
                  elif obj[3] == '<':
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 13, "metric_value": 0.3912, "depth": 7}
                     if obj[8]<=1.0:
                        return 'Yes'
                     elif obj[8]>1.0:
                        # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 6, "metric_value": 0.65, "depth": 8}
                        if obj[10]>-7:
                           return 'Yes'
                        elif obj[10]<=-7:
                           return 'No'
                        else:
                           return 'Yes'
                     else:
                        return 'Yes'
                  else:
                     return 'Yes'
               elif obj[6]<=-11.627100172672435:
                  # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 16, "metric_value": 0.3373, "depth": 6}
                  if obj[12]>-12:
                     return 'Yes'
                  elif obj[12]<=-12:
                     # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 3, "metric_value": 0.9183, "depth": 7}
                     if obj[8]<=-7.666666666666664:
                        return 'Yes'
                     elif obj[8]>-7.666666666666664:
                        return 'No'
                     else:
                        return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[2]<=-17.66713351860531:
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[6]<=-21:
                  return 'Yes'
               elif obj[6]>-21:
                  return 'No'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[0]<=8:
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 12, "metric_value": 0.9799, "depth": 4}
            if obj[2]>-19.666666666666664:
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 10, "metric_value": 0.8813, "depth": 5}
               if obj[8]<=7.666666666666671:
                  # {"feature": "PTime_A_VS_B_Max", "instances": 8, "metric_value": 0.5436, "depth": 6}
                  if obj[11] == '<':
                     return 'No'
                  elif obj[11] == '>':
                     # {"feature": "STime_A_VS_B_Min", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[3] == '<':
                        return 'No'
                     elif obj[3] == '>':
                        return 'Yes'
                     else:
                        return 'No'
                  else:
                     return 'No'
               elif obj[8]>7.666666666666671:
                  return 'Yes'
               else:
                  return 'No'
            elif obj[2]<=-19.666666666666664:
               return 'Yes'
            else:
               return 'No'
         else:
            return 'Yes'
      else:
         return 'No'
   elif obj[4]>30.093046521266608:
      # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 268, "metric_value": 0.0886, "depth": 2}
      if obj[8]>-12.733564469362179:
         # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 265, "metric_value": 0.0641, "depth": 3}
         if obj[10]>-13.763413740575533:
            # {"feature": "STime_A_VS_B_Max_Diff", "instances": 253, "metric_value": 0.0372, "depth": 4}
            if obj[6]>-5.76968061415117:
               return 'Yes'
            elif obj[6]<=-5.76968061415117:
               # {"feature": "PTime_A_VS_B_Min", "instances": 38, "metric_value": 0.1756, "depth": 5}
               if obj[9] == '>':
                  return 'Yes'
               elif obj[9] == '<':
                  # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 0.5917, "depth": 6}
                  if obj[2]>4.666666666666664:
                     return 'Yes'
                  elif obj[2]<=4.666666666666664:
                     # {"feature": "PTime_A_VS_B_Max", "instances": 2, "metric_value": 1.0, "depth": 7}
                     if obj[11] == '>':
                        return 'No'
                     elif obj[11] == '<':
                        return 'Yes'
                     else:
                        return 'No'
                  else:
                     return 'Yes'
               elif obj[9] == '=':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[10]<=-13.763413740575533:
            # {"feature": "Due_A_VS_B_Diff", "instances": 12, "metric_value": 0.4138, "depth": 4}
            if obj[14]>-34:
               return 'Yes'
            elif obj[14]<=-34:
               return 'No'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[8]<=-12.733564469362179:
         # {"feature": "NumWaitingJob", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[0]<=12:
            return 'Yes'
         elif obj[0]>12:
            return 'No'
         else:
            return 'Yes'
      else:
         return 'Yes'
   else:
      return 'No'
