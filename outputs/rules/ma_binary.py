def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B, obj[2]: STime_A_VS_B_Diff, obj[3]: PTime_A_VS_B, obj[4]: PTime_A_VS_B_Diff, obj[5]: CompTime_A_VS_B, obj[6]: CompTime_A_VS_B_Diff, obj[7]: Start_A_VS_B, obj[8]: Start_A_VS_B_Diff, obj[9]: Tardy_A_VS_B, obj[10]: Tardy_A_VS_B_Diff
   # {"feature": "STime_A_VS_B_Diff", "instances": 15284, "metric_value": 1.0, "depth": 1}
   if obj[2]>-37.09453395174409:
      # {"feature": "CompTime_A_VS_B_Diff", "instances": 12696, "metric_value": 0.9812, "depth": 2}
      if obj[6]>-374:
         # {"feature": "STime_A_VS_B", "instances": 12695, "metric_value": 0.9812, "depth": 3}
         if obj[1] == '>':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 6290, "metric_value": 0.7858, "depth": 4}
            if obj[4]>-23.585624260033477:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 6148, "metric_value": 0.7723, "depth": 5}
               if obj[10]>-281:
                  # {"feature": "PTime_A_VS_B", "instances": 6146, "metric_value": 0.7718, "depth": 6}
                  if obj[3] == '>':
                     # {"feature": "Start_A_VS_B_Diff", "instances": 3433, "metric_value": 0.5929, "depth": 7}
                     if obj[8]>26.3221672006991:
                        # {"feature": "NumWaitingJob", "instances": 1946, "metric_value": 0.7155, "depth": 8}
                        if obj[0]>1:
                           # {"feature": "Tardy_A_VS_B", "instances": 1920, "metric_value": 0.7209, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 1307, "metric_value": 0.6396, "depth": 10}
                              if obj[5] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 613, "metric_value": 0.854, "depth": 10}
                              if obj[5] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           else:
                              return 'Yes'
                        elif obj[0]<=1:
                           return 'Yes'
                        else:
                           return 'Yes'
                     elif obj[8]<=26.3221672006991:
                        # {"feature": "NumWaitingJob", "instances": 1487, "metric_value": 0.3781, "depth": 8}
                        if obj[0]>3:
                           # {"feature": "Start_A_VS_B", "instances": 1416, "metric_value": 0.355, "depth": 9}
                           if obj[7] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 1105, "metric_value": 0.3228, "depth": 10}
                              if obj[9] == '<':
                                 return 'Yes'
                              elif obj[9] == '=':
                                 return 'Yes'
                              elif obj[9] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[7] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 297, "metric_value": 0.4615, "depth": 10}
                              if obj[9] == '>':
                                 return 'Yes'
                              elif obj[9] == '=':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[7] == '=':
                              # {"feature": "Tardy_A_VS_B", "instances": 14, "metric_value": 0.3712, "depth": 10}
                              if obj[9] == '=':
                                 return 'Yes'
                              elif obj[9] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           else:
                              return 'Yes'
                        elif obj[0]<=3:
                           # {"feature": "CompTime_A_VS_B", "instances": 71, "metric_value": 0.7163, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 37, "metric_value": 0.9569, "depth": 10}
                              if obj[7] == '<':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[5] == '>':
                              return 'Yes'
                           else:
                              return 'Yes'
                        else:
                           return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[3] == '<':
                     # {"feature": "Start_A_VS_B", "instances": 2506, "metric_value": 0.924, "depth": 7}
                     if obj[7] == '>':
                        # {"feature": "NumWaitingJob", "instances": 1499, "metric_value": 0.9915, "depth": 8}
                        if obj[0]>1:
                           # {"feature": "CompTime_A_VS_B", "instances": 1481, "metric_value": 0.9931, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 1458, "metric_value": 0.9919, "depth": 10}
                              if obj[9] == '>':
                                 return 'Yes'
                              elif obj[9] == '=':
                                 return 'No'
                              else:
                                 return 'Yes'
                           elif obj[5] == '<':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 15, "metric_value": 0.8366, "depth": 10}
                              if obj[8]<=3:
                                 return 'No'
                              elif obj[8]>3:
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[5] == '=':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 8, "metric_value": 0.9544, "depth": 10}
                              if obj[8]>2:
                                 return 'No'
                              elif obj[8]<=2:
                                 return 'Yes'
                              else:
                                 return 'No'
                           else:
                              return 'Yes'
                        elif obj[0]<=1:
                           return 'Yes'
                        else:
                           return 'Yes'
                     elif obj[7] == '<':
                        # {"feature": "NumWaitingJob", "instances": 988, "metric_value": 0.687, "depth": 8}
                        if obj[0]>1:
                           # {"feature": "CompTime_A_VS_B", "instances": 987, "metric_value": 0.6852, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 812, "metric_value": 0.7426, "depth": 10}
                              if obj[8]<=-31.392211400007426:
                                 return 'Yes'
                              elif obj[8]>-31.392211400007426:
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[5] == '>':
                              # {"feature": "Start_A_VS_B_Diff", "instances": 172, "metric_value": 0.2962, "depth": 10}
                              if obj[8]>-28.11334735407318:
                                 return 'Yes'
                              elif obj[8]<=-28.11334735407318:
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[5] == '=':
                              return 'Yes'
                           else:
                              return 'Yes'
                        elif obj[0]<=1:
                           return 'No'
                        else:
                           return 'Yes'
                     elif obj[7] == '=':
                        # {"feature": "NumWaitingJob", "instances": 19, "metric_value": 0.2975, "depth": 8}
                        if obj[0]<=12:
                           # {"feature": "Tardy_A_VS_B", "instances": 10, "metric_value": 0.469, "depth": 9}
                           if obj[9] == '>':
                              return 'Yes'
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[5] == '>':
                                 return 'Yes'
                              elif obj[5] == '<':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           else:
                              return 'Yes'
                        elif obj[0]>12:
                           return 'Yes'
                        else:
                           return 'Yes'
                     else:
                        return 'Yes'
                  elif obj[3] == '=':
                     # {"feature": "NumWaitingJob", "instances": 207, "metric_value": 0.7976, "depth": 7}
                     if obj[0]<=17:
                        # {"feature": "Start_A_VS_B_Diff", "instances": 202, "metric_value": 0.8073, "depth": 8}
                        if obj[8]>-168.54261593884223:
                           # {"feature": "Start_A_VS_B", "instances": 198, "metric_value": 0.8153, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 125, "metric_value": 0.9209, "depth": 10}
                              if obj[9] == '>':
                                 return 'Yes'
                              elif obj[9] == '=':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[7] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 72, "metric_value": 0.5033, "depth": 10}
                              if obj[5] == '<':
                                 return 'Yes'
                              elif obj[5] == '>':
                                 return 'Yes'
                              elif obj[5] == '=':
                                 return 'No'
                              else:
                                 return 'Yes'
                           elif obj[7] == '=':
                              return 'Yes'
                           else:
                              return 'Yes'
                        elif obj[8]<=-168.54261593884223:
                           return 'Yes'
                        else:
                           return 'Yes'
                     elif obj[0]>17:
                        return 'Yes'
                     else:
                        return 'Yes'
                  else:
                     return 'Yes'
               elif obj[10]<=-281:
                  return 'No'
               else:
                  return 'Yes'
            elif obj[4]<=-23.585624260033477:
               # {"feature": "Start_A_VS_B_Diff", "instances": 142, "metric_value": 0.9856, "depth": 5}
               if obj[8]>-206.89426140027297:
                  # {"feature": "NumWaitingJob", "instances": 138, "metric_value": 0.9781, "depth": 6}
                  if obj[0]>2:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 135, "metric_value": 0.971, "depth": 7}
                     if obj[10]>-215:
                        # {"feature": "Start_A_VS_B", "instances": 134, "metric_value": 0.9727, "depth": 8}
                        if obj[7] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 81, "metric_value": 0.8438, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 78, "metric_value": 0.8582, "depth": 10}
                              if obj[9] == '=':
                                 return 'No'
                              elif obj[9] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[5] == '<':
                              return 'No'
                           else:
                              return 'No'
                        elif obj[7] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 53, "metric_value": 0.9687, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 51, "metric_value": 0.9774, "depth": 10}
                              if obj[9] == '<':
                                 return 'Yes'
                              elif obj[9] == '=':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[5] == '>':
                              return 'Yes'
                           else:
                              return 'Yes'
                        else:
                           return 'No'
                     elif obj[10]<=-215:
                        return 'No'
                     else:
                        return 'No'
                  elif obj[0]<=2:
                     return 'Yes'
                  else:
                     return 'No'
               elif obj[8]<=-206.89426140027297:
                  return 'Yes'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[1] == '<':
            # {"feature": "Start_A_VS_B_Diff", "instances": 3701, "metric_value": 0.9106, "depth": 4}
            if obj[8]<=-11.534179951364496:
               # {"feature": "NumWaitingJob", "instances": 1922, "metric_value": 0.9914, "depth": 5}
               if obj[0]>1:
                  # {"feature": "PTime_A_VS_B_Diff", "instances": 1889, "metric_value": 0.9937, "depth": 6}
                  if obj[4]>-29:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 1883, "metric_value": 0.994, "depth": 7}
                     if obj[10]>-297:
                        # {"feature": "PTime_A_VS_B", "instances": 1882, "metric_value": 0.9941, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "Tardy_A_VS_B", "instances": 994, "metric_value": 0.8976, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 677, "metric_value": 0.8419, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 317, "metric_value": 0.9749, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[3] == '>':
                           # {"feature": "Tardy_A_VS_B", "instances": 825, "metric_value": 0.955, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 444, "metric_value": 0.9967, "depth": 10}
                              if obj[5] == '<':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 381, "metric_value": 0.842, "depth": 10}
                              if obj[5] == '<':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           else:
                              return 'Yes'
                        elif obj[3] == '=':
                           # {"feature": "Tardy_A_VS_B", "instances": 63, "metric_value": 0.9955, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 41, "metric_value": 0.9789, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 22, "metric_value": 0.994, "depth": 10}
                              if obj[5] == '<':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[10]<=-297:
                        return 'No'
                     else:
                        return 'No'
                  elif obj[4]<=-29:
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]<=1:
                  return 'No'
               else:
                  return 'No'
            elif obj[8]>-11.534179951364496:
               # {"feature": "PTime_A_VS_B_Diff", "instances": 1779, "metric_value": 0.7154, "depth": 5}
               if obj[4]<=12.45804190015377:
                  # {"feature": "NumWaitingJob", "instances": 1484, "metric_value": 0.6287, "depth": 6}
                  if obj[0]>2:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 1457, "metric_value": 0.6157, "depth": 7}
                     if obj[10]>-60:
                        # {"feature": "PTime_A_VS_B", "instances": 1455, "metric_value": 0.6163, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 848, "metric_value": 0.4772, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 485, "metric_value": 0.4389, "depth": 10}
                              if obj[9] == '>':
                                 return 'No'
                              elif obj[9] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[5] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 355, "metric_value": 0.5326, "depth": 10}
                              if obj[9] == '=':
                                 return 'No'
                              elif obj[9] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[5] == '=':
                              return 'No'
                           else:
                              return 'No'
                        elif obj[3] == '>':
                           # {"feature": "Start_A_VS_B", "instances": 538, "metric_value": 0.7853, "depth": 9}
                           if obj[7] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 466, "metric_value": 0.7502, "depth": 10}
                              if obj[5] == '>':
                                 return 'No'
                              elif obj[5] == '<':
                                 return 'No'
                              elif obj[5] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[7] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 65, "metric_value": 0.9612, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              elif obj[5] == '=':
                                 return 'Yes'
                              elif obj[5] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[7] == '=':
                              # {"feature": "Tardy_A_VS_B", "instances": 7, "metric_value": 0.5917, "depth": 10}
                              if obj[9] == '=':
                                 return 'No'
                              elif obj[9] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[3] == '=':
                           # {"feature": "CompTime_A_VS_B", "instances": 69, "metric_value": 0.5586, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 51, "metric_value": 0.4627, "depth": 10}
                              if obj[9] == '>':
                                 return 'No'
                              elif obj[9] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 17, "metric_value": 0.6723, "depth": 10}
                              if obj[7] == '>':
                                 return 'No'
                              elif obj[7] == '<':
                                 return 'No'
                              elif obj[7] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[5] == '=':
                              return 'Yes'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[10]<=-60:
                        return 'No'
                     else:
                        return 'No'
                  elif obj[0]<=2:
                     # {"feature": "CompTime_A_VS_B", "instances": 27, "metric_value": 0.9911, "depth": 7}
                     if obj[5] == '>':
                        # {"feature": "Tardy_A_VS_B_Diff", "instances": 18, "metric_value": 0.9183, "depth": 8}
                        if obj[10]<=131:
                           # {"feature": "PTime_A_VS_B", "instances": 16, "metric_value": 0.9544, "depth": 9}
                           if obj[3] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 8, "metric_value": 1.0, "depth": 10}
                              if obj[7] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[3] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 6, "metric_value": 0.65, "depth": 10}
                              if obj[7] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[3] == '=':
                              # {"feature": "Start_A_VS_B", "instances": 2, "metric_value": 1.0, "depth": 10}
                              if obj[7] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'Yes'
                        elif obj[10]>131:
                           return 'Yes'
                        else:
                           return 'Yes'
                     elif obj[5] == '<':
                        return 'No'
                     else:
                        return 'No'
                  else:
                     return 'No'
               elif obj[4]>12.45804190015377:
                  # {"feature": "NumWaitingJob", "instances": 295, "metric_value": 0.9668, "depth": 6}
                  if obj[0]>1:
                     # {"feature": "Tardy_A_VS_B_Diff", "instances": 294, "metric_value": 0.9655, "depth": 7}
                     if obj[10]>-24:
                        # {"feature": "Start_A_VS_B", "instances": 293, "metric_value": 0.9642, "depth": 8}
                        if obj[7] == '>':
                           # {"feature": "CompTime_A_VS_B", "instances": 253, "metric_value": 0.9247, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Tardy_A_VS_B", "instances": 248, "metric_value": 0.9274, "depth": 10}
                              if obj[9] == '>':
                                 return 'No'
                              elif obj[9] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[5] == '<':
                              # {"feature": "Tardy_A_VS_B", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[9] == '<':
                                 return 'No'
                              elif obj[9] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[7] == '<':
                           # {"feature": "Tardy_A_VS_B", "instances": 36, "metric_value": 0.7642, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "PTime_A_VS_B", "instances": 25, "metric_value": 0.7219, "depth": 10}
                              if obj[3] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[9] == '>':
                              # {"feature": "PTime_A_VS_B", "instances": 6, "metric_value": 0.65, "depth": 10}
                              if obj[3] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[9] == '<':
                              # {"feature": "PTime_A_VS_B", "instances": 5, "metric_value": 0.971, "depth": 10}
                              if obj[3] == '>':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           else:
                              return 'Yes'
                        elif obj[7] == '=':
                           return 'No'
                        else:
                           return 'No'
                     elif obj[10]<=-24:
                        return 'Yes'
                     else:
                        return 'No'
                  elif obj[0]<=1:
                     return 'Yes'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[1] == '=':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 2704, "metric_value": 1.0, "depth": 4}
            if obj[4]<=0.0:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 1386, "metric_value": 0.9048, "depth": 5}
               if obj[10]<=40.60268666593762:
                  # {"feature": "Start_A_VS_B_Diff", "instances": 1381, "metric_value": 0.9021, "depth": 6}
                  if obj[8]>-236:
                     # {"feature": "NumWaitingJob", "instances": 1379, "metric_value": 0.901, "depth": 7}
                     if obj[0]>2:
                        # {"feature": "PTime_A_VS_B", "instances": 1378, "metric_value": 0.9012, "depth": 8}
                        if obj[3] == '<':
                           # {"feature": "Tardy_A_VS_B", "instances": 1310, "metric_value": 0.8913, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "Start_A_VS_B", "instances": 1284, "metric_value": 0.8895, "depth": 10}
                              if obj[7] == '=':
                                 return 'No'
                              elif obj[7] == '<':
                                 return 'No'
                              elif obj[7] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[9] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 19, "metric_value": 0.9819, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[9] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 7, "metric_value": 0.8631, "depth": 10}
                              if obj[5] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[3] == '=':
                           # {"feature": "CompTime_A_VS_B", "instances": 68, "metric_value": 0.9994, "depth": 9}
                           if obj[5] == '=':
                              # {"feature": "Start_A_VS_B", "instances": 68, "metric_value": 0.9994, "depth": 10}
                              if obj[7] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[0]<=2:
                        return 'No'
                     else:
                        return 'No'
                  elif obj[8]<=-236:
                     return 'Yes'
                  else:
                     return 'No'
               elif obj[10]>40.60268666593762:
                  return 'Yes'
               else:
                  return 'No'
            elif obj[4]>0.0:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 1318, "metric_value": 0.897, "depth": 5}
               if obj[10]>-41.61099035379464:
                  # {"feature": "Start_A_VS_B_Diff", "instances": 1313, "metric_value": 0.894, "depth": 6}
                  if obj[8]>-33.33957269773844:
                     # {"feature": "CompTime_A_VS_B", "instances": 1308, "metric_value": 0.8954, "depth": 7}
                     if obj[5] == '>':
                        # {"feature": "NumWaitingJob", "instances": 1306, "metric_value": 0.8942, "depth": 8}
                        if obj[0]>4:
                           # {"feature": "Tardy_A_VS_B", "instances": 1303, "metric_value": 0.895, "depth": 9}
                           if obj[9] == '=':
                              # {"feature": "Start_A_VS_B", "instances": 1284, "metric_value": 0.8913, "depth": 10}
                              if obj[7] == '=':
                                 return 'Yes'
                              elif obj[7] == '>':
                                 return 'Yes'
                              elif obj[7] == '<':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           elif obj[9] == '>':
                              # {"feature": "PTime_A_VS_B", "instances": 19, "metric_value": 0.998, "depth": 10}
                              if obj[3] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'Yes'
                        elif obj[0]<=4:
                           return 'Yes'
                        else:
                           return 'Yes'
                     elif obj[5] == '<':
                        return 'No'
                     else:
                        return 'Yes'
                  elif obj[8]<=-33.33957269773844:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[10]<=-41.61099035379464:
                  return 'No'
               else:
                  return 'Yes'
            else:
               return 'No'
         else:
            return 'Yes'
      elif obj[6]<=-374:
         return 'No'
      else:
         return 'Yes'
   elif obj[2]<=-37.09453395174409:
      # {"feature": "PTime_A_VS_B_Diff", "instances": 2588, "metric_value": 0.4631, "depth": 2}
      if obj[4]<=22.020355092771737:
         # {"feature": "Start_A_VS_B_Diff", "instances": 2525, "metric_value": 0.4361, "depth": 3}
         if obj[8]<=-29.019801980198018:
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 1564, "metric_value": 0.569, "depth": 4}
            if obj[6]<=-85.68480792377257:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 1432, "metric_value": 0.5114, "depth": 5}
               if obj[10]>-234.05318325822316:
                  # {"feature": "NumWaitingJob", "instances": 1363, "metric_value": 0.5282, "depth": 6}
                  if obj[0]>2:
                     # {"feature": "PTime_A_VS_B", "instances": 1324, "metric_value": 0.5382, "depth": 7}
                     if obj[3] == '<':
                        # {"feature": "Tardy_A_VS_B", "instances": 886, "metric_value": 0.3866, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "STime_A_VS_B", "instances": 594, "metric_value": 0.3232, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 594, "metric_value": 0.3232, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[9] == '=':
                           # {"feature": "STime_A_VS_B", "instances": 292, "metric_value": 0.4987, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 292, "metric_value": 0.4987, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '>':
                        # {"feature": "Tardy_A_VS_B", "instances": 398, "metric_value": 0.7622, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "STime_A_VS_B", "instances": 235, "metric_value": 0.8261, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 235, "metric_value": 0.8261, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[9] == '=':
                           # {"feature": "STime_A_VS_B", "instances": 163, "metric_value": 0.6476, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 163, "metric_value": 0.6476, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '=':
                        # {"feature": "Tardy_A_VS_B", "instances": 40, "metric_value": 0.7219, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "STime_A_VS_B", "instances": 30, "metric_value": 0.7838, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 30, "metric_value": 0.7838, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[9] == '=':
                           # {"feature": "STime_A_VS_B", "instances": 10, "metric_value": 0.469, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 10, "metric_value": 0.469, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     else:
                        return 'No'
                  elif obj[0]<=2:
                     return 'No'
                  else:
                     return 'No'
               elif obj[10]<=-234.05318325822316:
                  return 'No'
               else:
                  return 'No'
            elif obj[6]>-85.68480792377257:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 132, "metric_value": 0.9394, "depth": 5}
               if obj[10]>-11.227272727272727:
                  # {"feature": "NumWaitingJob", "instances": 103, "metric_value": 0.9885, "depth": 6}
                  if obj[0]<=18:
                     # {"feature": "Tardy_A_VS_B", "instances": 97, "metric_value": 0.9938, "depth": 7}
                     if obj[9] == '=':
                        # {"feature": "PTime_A_VS_B", "instances": 93, "metric_value": 0.9959, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "STime_A_VS_B", "instances": 70, "metric_value": 0.9976, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 70, "metric_value": 0.9976, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[3] == '<':
                           # {"feature": "STime_A_VS_B", "instances": 18, "metric_value": 1.0, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 18, "metric_value": 1.0, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[3] == '=':
                           # {"feature": "STime_A_VS_B", "instances": 5, "metric_value": 0.7219, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 5, "metric_value": 0.7219, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[9] == '<':
                        # {"feature": "PTime_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[3] == '>':
                           # {"feature": "STime_A_VS_B", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[3] == '=':
                           return 'No'
                        else:
                           return 'No'
                     else:
                        return 'No'
                  elif obj[0]>18:
                     # {"feature": "PTime_A_VS_B", "instances": 6, "metric_value": 0.65, "depth": 7}
                     if obj[3] == '>':
                        # {"feature": "STime_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 8}
                        if obj[1] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 10}
                              if obj[7] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '=':
                        return 'No'
                     elif obj[3] == '<':
                        return 'No'
                     else:
                        return 'No'
                  else:
                     return 'No'
               elif obj[10]<=-11.227272727272727:
                  # {"feature": "NumWaitingJob", "instances": 29, "metric_value": 0.3621, "depth": 6}
                  if obj[0]>6:
                     # {"feature": "PTime_A_VS_B", "instances": 25, "metric_value": 0.2423, "depth": 7}
                     if obj[3] == '>':
                        # {"feature": "STime_A_VS_B", "instances": 23, "metric_value": 0.258, "depth": 8}
                        if obj[1] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 23, "metric_value": 0.258, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 23, "metric_value": 0.258, "depth": 10}
                              if obj[7] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '<':
                        return 'No'
                     else:
                        return 'No'
                  elif obj[0]<=6:
                     # {"feature": "PTime_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 7}
                     if obj[3] == '>':
                        # {"feature": "STime_A_VS_B", "instances": 3, "metric_value": 0.9183, "depth": 8}
                        if obj[1] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 3, "metric_value": 0.9183, "depth": 9}
                           if obj[5] == '<':
                              # {"feature": "Start_A_VS_B", "instances": 3, "metric_value": 0.9183, "depth": 10}
                              if obj[7] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '=':
                        return 'No'
                     else:
                        return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[8]>-29.019801980198018:
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 961, "metric_value": 0.1283, "depth": 4}
            if obj[10]<=105.41450793936849:
               # {"feature": "NumWaitingJob", "instances": 899, "metric_value": 0.0953, "depth": 5}
               if obj[0]<=10:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 474, "metric_value": 0.1591, "depth": 6}
                  if obj[6]<=124.76182261076842:
                     # {"feature": "PTime_A_VS_B", "instances": 459, "metric_value": 0.1632, "depth": 7}
                     if obj[3] == '<':
                        # {"feature": "Tardy_A_VS_B", "instances": 280, "metric_value": 0.108, "depth": 8}
                        if obj[9] == '<':
                           # {"feature": "Start_A_VS_B", "instances": 153, "metric_value": 0.0568, "depth": 9}
                           if obj[7] == '>':
                              return 'No'
                           elif obj[7] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 49, "metric_value": 0.1437, "depth": 10}
                              if obj[1] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[9] == '>':
                           # {"feature": "STime_A_VS_B", "instances": 93, "metric_value": 0.2056, "depth": 9}
                           if obj[1] == '<':
                              # {"feature": "CompTime_A_VS_B", "instances": 93, "metric_value": 0.2056, "depth": 10}
                              if obj[5] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[9] == '=':
                           return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '>':
                        # {"feature": "Start_A_VS_B", "instances": 171, "metric_value": 0.2466, "depth": 8}
                        if obj[7] == '>':
                           # {"feature": "Tardy_A_VS_B", "instances": 129, "metric_value": 0.2366, "depth": 9}
                           if obj[9] == '>':
                              # {"feature": "STime_A_VS_B", "instances": 73, "metric_value": 0.2473, "depth": 10}
                              if obj[1] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[9] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 35, "metric_value": 0.1872, "depth": 10}
                              if obj[1] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[9] == '=':
                              # {"feature": "CompTime_A_VS_B", "instances": 21, "metric_value": 0.2762, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              elif obj[5] == '>':
                                 return 'No'
                              elif obj[5] == '=':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        elif obj[7] == '<':
                           # {"feature": "Tardy_A_VS_B", "instances": 38, "metric_value": 0.2975, "depth": 9}
                           if obj[9] == '<':
                              # {"feature": "STime_A_VS_B", "instances": 33, "metric_value": 0.3298, "depth": 10}
                              if obj[1] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           elif obj[9] == '=':
                              return 'No'
                           else:
                              return 'No'
                        elif obj[7] == '=':
                           return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '=':
                        return 'No'
                     else:
                        return 'No'
                  elif obj[6]>124.76182261076842:
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>10:
                  return 'No'
               else:
                  return 'No'
            elif obj[10]>105.41450793936849:
               # {"feature": "NumWaitingJob", "instances": 62, "metric_value": 0.4587, "depth": 5}
               if obj[0]>2:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 61, "metric_value": 0.4091, "depth": 6}
                  if obj[6]<=191.53695579273253:
                     # {"feature": "PTime_A_VS_B", "instances": 52, "metric_value": 0.4567, "depth": 7}
                     if obj[3] == '>':
                        # {"feature": "STime_A_VS_B", "instances": 32, "metric_value": 0.5436, "depth": 8}
                        if obj[1] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 32, "metric_value": 0.5436, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 32, "metric_value": 0.5436, "depth": 10}
                              if obj[7] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     elif obj[3] == '<':
                        # {"feature": "STime_A_VS_B", "instances": 20, "metric_value": 0.2864, "depth": 8}
                        if obj[1] == '<':
                           # {"feature": "CompTime_A_VS_B", "instances": 20, "metric_value": 0.2864, "depth": 9}
                           if obj[5] == '>':
                              # {"feature": "Start_A_VS_B", "instances": 20, "metric_value": 0.2864, "depth": 10}
                              if obj[7] == '>':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     else:
                        return 'No'
                  elif obj[6]>191.53695579273253:
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]<=2:
                  return 'Yes'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      elif obj[4]>22.020355092771737:
         # {"feature": "Start_A_VS_B_Diff", "instances": 63, "metric_value": 0.9852, "depth": 3}
         if obj[8]<=-16.46031746031746:
            # {"feature": "NumWaitingJob", "instances": 41, "metric_value": 0.9474, "depth": 4}
            if obj[0]<=17:
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 39, "metric_value": 0.9612, "depth": 5}
               if obj[10]>-83:
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 37, "metric_value": 0.974, "depth": 6}
                  if obj[6]>-203:
                     # {"feature": "Tardy_A_VS_B", "instances": 36, "metric_value": 0.9799, "depth": 7}
                     if obj[9] == '=':
                        # {"feature": "STime_A_VS_B", "instances": 21, "metric_value": 0.9183, "depth": 8}
                        if obj[1] == '<':
                           # {"feature": "PTime_A_VS_B", "instances": 21, "metric_value": 0.9183, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 21, "metric_value": 0.9183, "depth": 10}
                              if obj[5] == '<':
                                 return 'Yes'
                              else:
                                 return 'Yes'
                           else:
                              return 'Yes'
                        else:
                           return 'Yes'
                     elif obj[9] == '<':
                        # {"feature": "STime_A_VS_B", "instances": 15, "metric_value": 0.9968, "depth": 8}
                        if obj[1] == '<':
                           # {"feature": "PTime_A_VS_B", "instances": 15, "metric_value": 0.9968, "depth": 9}
                           if obj[3] == '>':
                              # {"feature": "CompTime_A_VS_B", "instances": 15, "metric_value": 0.9968, "depth": 10}
                              if obj[5] == '<':
                                 return 'No'
                              else:
                                 return 'No'
                           else:
                              return 'No'
                        else:
                           return 'No'
                     else:
                        return 'Yes'
                  elif obj[6]<=-203:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[10]<=-83:
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]>17:
               return 'Yes'
            else:
               return 'Yes'
         elif obj[8]>-16.46031746031746:
            # {"feature": "NumWaitingJob", "instances": 22, "metric_value": 0.2668, "depth": 4}
            if obj[0]>6:
               return 'No'
            elif obj[0]<=6:
               # {"feature": "CompTime_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[5] == '>':
                  # {"feature": "CompTime_A_VS_B_Diff", "instances": 2, "metric_value": 1.0, "depth": 6}
                  if obj[6]<=23:
                     return 'Yes'
                  elif obj[6]>23:
                     return 'No'
                  else:
                     return 'Yes'
               elif obj[5] == '<':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      else:
         return 'No'
   else:
      return 'No'
