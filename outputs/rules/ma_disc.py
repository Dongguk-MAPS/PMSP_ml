def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B, obj[2]: STime_A_VS_B_Diff, obj[3]: PTime_A_VS_B, obj[4]: PTime_A_VS_B_Diff, obj[5]: CompTime_A_VS_B, obj[6]: CompTime_A_VS_B_Diff, obj[7]: Start_A_VS_B, obj[8]: Start_A_VS_B_Diff, obj[9]: Tardy_A_VS_B, obj[10]: Tardy_A_VS_B_Diff
   # {"feature": "STime_A_VS_B_Diff", "instances": 15284, "metric_value": 1.0652, "depth": 1}
   if obj[2] == 'Less_49.5':
      # {"feature": "PTime_A_VS_B", "instances": 10429, "metric_value": 1.0699, "depth": 2}
      if obj[3] == '>':
         # {"feature": "STime_A_VS_B", "instances": 5184, "metric_value": 0.9642, "depth": 3}
         if obj[1] == '>':
            # {"feature": "Start_A_VS_B", "instances": 2438, "metric_value": 0.7333, "depth": 4}
            if obj[7] == '>':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 1504, "metric_value": 0.8503, "depth": 5}
               if obj[4] == 'Greater_9.5':
                  return '2'
               elif obj[4] == 'Less_9.5':
                  return '2'
               else:
                  return '2'
            elif obj[7] == '<':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 922, "metric_value": 0.4542, "depth": 5}
               if obj[4] == 'Greater_9.5':
                  return '2'
               elif obj[4] == 'Less_9.5':
                  return '2'
               else:
                  return '2'
            elif obj[7] == '=':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 12, "metric_value": 0.4138, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '2'
               elif obj[4] == 'Greater_9.5':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[1] == '<':
            # {"feature": "Start_A_VS_B", "instances": 1428, "metric_value": 1.0644, "depth": 4}
            if obj[7] == '<':
               # {"feature": "Tardy_A_VS_B", "instances": 793, "metric_value": 1.021, "depth": 5}
               if obj[9] == '<':
                  return '2'
               elif obj[9] == '=':
                  return '2'
               elif obj[9] == '>':
                  return '2'
               else:
                  return '2'
            elif obj[7] == '>':
               # {"feature": "CompTime_A_VS_B", "instances": 625, "metric_value": 0.9294, "depth": 5}
               if obj[5] == '>':
                  return '0'
               elif obj[5] == '<':
                  return '0'
               elif obj[5] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[7] == '=':
               # {"feature": "NumWaitingJob", "instances": 10, "metric_value": 0.469, "depth": 5}
               if obj[0] == 'Less_14.5':
                  return '0'
               elif obj[0] == 'Greater_14.5':
                  return '0'
               elif obj[0] == 'Less_10.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[1] == '=':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 1318, "metric_value": 1.0222, "depth": 4}
            if obj[6] == 'Less_211.5':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 1316, "metric_value": 1.0212, "depth": 5}
               if obj[10] == 'Less_70.5':
                  return '2'
               elif obj[10] == 'Greater_70.5':
                  return '2'
               elif obj[10] == 'Less_-105.5':
                  return '0'
               else:
                  return '2'
            elif obj[6] == 'Greater_244.5':
               return '0'
            else:
               return '2'
         else:
            return '2'
      elif obj[3] == '<':
         # {"feature": "STime_A_VS_B", "instances": 4899, "metric_value": 1.0519, "depth": 3}
         if obj[1] == '>':
            # {"feature": "Start_A_VS_B", "instances": 2043, "metric_value": 1.083, "depth": 4}
            if obj[7] == '>':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 1175, "metric_value": 1.0468, "depth": 5}
               if obj[10] == 'Less_70.5':
                  return '0'
               elif obj[10] == 'Greater_70.5':
                  return '2'
               else:
                  return '2'
            elif obj[7] == '<':
               # {"feature": "CompTime_A_VS_B", "instances": 855, "metric_value": 0.9357, "depth": 5}
               if obj[5] == '<':
                  return '2'
               elif obj[5] == '>':
                  return '2'
               elif obj[5] == '=':
                  return '1'
               else:
                  return '2'
            elif obj[7] == '=':
               # {"feature": "CompTime_A_VS_B", "instances": 13, "metric_value": 0.7732, "depth": 5}
               if obj[5] == '>':
                  return '2'
               elif obj[5] == '<':
                  return '2'
               elif obj[5] == '=':
                  return '1'
               else:
                  return '2'
            else:
               return '2'
         elif obj[1] == '<':
            # {"feature": "Start_A_VS_B", "instances": 1538, "metric_value": 0.8565, "depth": 4}
            if obj[7] == '<':
               # {"feature": "Start_A_VS_B_Diff", "instances": 938, "metric_value": 0.97, "depth": 5}
               if obj[8] == 'Less_-2.5':
                  return '0'
               elif obj[8] == 'Less_-154.5':
                  return '0'
               elif obj[8] == 'Greater_-2.5':
                  return '0'
               else:
                  return '2'
            elif obj[7] == '>':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 593, "metric_value": 0.5759, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               elif obj[4] == 'Less_-10.5':
                  return '0'
               elif obj[4] == 'Less_-23.5':
                  return '0'
               else:
                  return '2'
            elif obj[7] == '=':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 7, "metric_value": 0.5917, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               elif obj[4] == 'Less_-10.5':
                  return '0'
               elif obj[4] == 'Less_-23.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[1] == '=':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 1318, "metric_value": 0.9795, "depth": 4}
            if obj[6] == 'Less_211.5':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 1314, "metric_value": 0.9781, "depth": 5}
               if obj[10] == 'Less_70.5':
                  return '0'
               elif obj[10] == 'Less_-105.5':
                  return '0'
               elif obj[10] == 'Greater_70.5':
                  return '2'
               else:
                  return '2'
            elif obj[6] == 'Less_-193.5':
               # {"feature": "NumWaitingJob", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[0] == 'Less_10.5':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[3] == '=':
         # {"feature": "STime_A_VS_B", "instances": 346, "metric_value": 1.0581, "depth": 3}
         if obj[1] == '>':
            # {"feature": "CompTime_A_VS_B", "instances": 163, "metric_value": 0.9094, "depth": 4}
            if obj[5] == '>':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 103, "metric_value": 0.9571, "depth": 5}
               if obj[6] == 'Less_211.5':
                  return '2'
               elif obj[6] == 'Less_244.5':
                  return '2'
               elif obj[6] == 'Greater_244.5':
                  return '2'
               else:
                  return '2'
            elif obj[5] == '<':
               # {"feature": "NumWaitingJob", "instances": 59, "metric_value": 0.5956, "depth": 5}
               if obj[0] == 'Less_10.5':
                  return '2'
               elif obj[0] == 'Less_14.5':
                  return '2'
               elif obj[0] == 'Greater_14.5':
                  return '2'
               else:
                  return '2'
            elif obj[5] == '=':
               return '0'
            else:
               return '2'
         elif obj[1] == '<':
            # {"feature": "CompTime_A_VS_B", "instances": 115, "metric_value": 0.924, "depth": 4}
            if obj[5] == '<':
               # {"feature": "Start_A_VS_B", "instances": 74, "metric_value": 0.9868, "depth": 5}
               if obj[7] == '<':
                  return '0'
               elif obj[7] == '>':
                  return '0'
               elif obj[7] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[5] == '>':
               # {"feature": "NumWaitingJob", "instances": 40, "metric_value": 0.6098, "depth": 5}
               if obj[0] == 'Less_10.5':
                  return '0'
               elif obj[0] == 'Less_14.5':
                  return '0'
               elif obj[0] == 'Greater_14.5':
                  return '0'
               else:
                  return '2'
            elif obj[5] == '=':
               return '2'
            else:
               return '2'
         elif obj[1] == '=':
            # {"feature": "NumWaitingJob", "instances": 68, "metric_value": 1.1594, "depth": 4}
            if obj[0] == 'Greater_14.5':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 34, "metric_value": 1.0, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               else:
                  return '2'
            elif obj[0] == 'Less_14.5':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 28, "metric_value": 1.178, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               else:
                  return '2'
            elif obj[0] == 'Less_10.5':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 6, "metric_value": 1.4591, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         else:
            return '2'
      else:
         return '2'
   elif obj[2] == 'Less_-34.5':
      # {"feature": "Start_A_VS_B", "instances": 2822, "metric_value": 0.4987, "depth": 2}
      if obj[7] == '<':
         # {"feature": "PTime_A_VS_B", "instances": 1939, "metric_value": 0.6137, "depth": 3}
         if obj[3] == '<':
            # {"feature": "Start_A_VS_B_Diff", "instances": 1192, "metric_value": 0.3839, "depth": 4}
            if obj[8] == 'Less_-2.5':
               # {"feature": "Tardy_A_VS_B", "instances": 1014, "metric_value": 0.333, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[8] == 'Less_-154.5':
               # {"feature": "Tardy_A_VS_B", "instances": 159, "metric_value": 0.6657, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '2'
               else:
                  return '2'
            elif obj[8] == 'Greater_-2.5':
               return '0'
            else:
               return '2'
         elif obj[3] == '>':
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 690, "metric_value": 0.8739, "depth": 4}
            if obj[10] == 'Less_70.5':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 586, "metric_value": 0.8869, "depth": 5}
               if obj[6] == 'Less_211.5':
                  return '0'
               elif obj[6] == 'Less_-193.5':
                  return '2'
               else:
                  return '2'
            elif obj[10] == 'Less_-105.5':
               # {"feature": "NumWaitingJob", "instances": 86, "metric_value": 0.8455, "depth": 5}
               if obj[0] == 'Less_10.5':
                  return '0'
               elif obj[0] == 'Less_14.5':
                  return '0'
               elif obj[0] == 'Greater_14.5':
                  return '0'
               else:
                  return '2'
            elif obj[10] == 'Less_-226.5':
               return '0'
            else:
               return '2'
         elif obj[3] == '=':
            # {"feature": "NumWaitingJob", "instances": 57, "metric_value": 0.7087, "depth": 4}
            if obj[0] == 'Less_10.5':
               # {"feature": "Tardy_A_VS_B", "instances": 24, "metric_value": 0.8113, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[0] == 'Greater_14.5':
               return '0'
            elif obj[0] == 'Less_14.5':
               # {"feature": "Tardy_A_VS_B", "instances": 14, "metric_value": 0.9464, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[7] == '>':
         # {"feature": "Tardy_A_VS_B", "instances": 867, "metric_value": 0.1521, "depth": 3}
         if obj[9] == '>':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 340, "metric_value": 0.2609, "depth": 4}
            if obj[4] == 'Less_9.5':
               # {"feature": "NumWaitingJob", "instances": 163, "metric_value": 0.2275, "depth": 5}
               if obj[0] == 'Less_10.5':
                  return '0'
               elif obj[0] == 'Less_14.5':
                  return '0'
               elif obj[0] == 'Greater_14.5':
                  return '0'
               else:
                  return '2'
            elif obj[4] == 'Greater_9.5':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 98, "metric_value": 0.4426, "depth": 5}
               if obj[6] == 'Less_211.5':
                  return '0'
               elif obj[6] == 'Less_244.5':
                  return '0'
               else:
                  return '2'
            elif obj[4] == 'Less_-10.5':
               return '0'
            elif obj[4] == 'Less_-23.5':
               return '0'
            else:
               return '2'
         elif obj[9] == '=':
            # {"feature": "NumWaitingJob", "instances": 303, "metric_value": 0.032, "depth": 4}
            if obj[0] == 'Less_14.5':
               return '0'
            elif obj[0] == 'Less_10.5':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 62, "metric_value": 0.1191, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               elif obj[4] == 'Less_-10.5':
                  return '0'
               elif obj[4] == 'Greater_9.5':
                  return '0'
               elif obj[4] == 'Less_-23.5':
                  return '0'
               else:
                  return '1'
            elif obj[0] == 'Greater_14.5':
               return '0'
            else:
               return '1'
         elif obj[9] == '<':
            # {"feature": "PTime_A_VS_B", "instances": 224, "metric_value": 0.0736, "depth": 4}
            if obj[3] == '<':
               return '0'
            elif obj[3] == '>':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 65, "metric_value": 0.1982, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               elif obj[4] == 'Greater_9.5':
                  return '0'
               else:
                  return '2'
            elif obj[3] == '=':
               return '0'
            else:
               return '2'
         else:
            return '2'
      elif obj[7] == '=':
         return '0'
      else:
         return '2'
   elif obj[2] == 'Greater_49.5':
      # {"feature": "Start_A_VS_B", "instances": 1646, "metric_value": 0.3877, "depth": 2}
      if obj[7] == '>':
         # {"feature": "PTime_A_VS_B_Diff", "instances": 1203, "metric_value": 0.4699, "depth": 3}
         if obj[4] == 'Less_9.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 627, "metric_value": 0.5111, "depth": 4}
            if obj[6] == 'Less_211.5':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 530, "metric_value": 0.4546, "depth": 5}
               if obj[10] == 'Less_70.5':
                  return '2'
               elif obj[10] == 'Greater_70.5':
                  return '2'
               else:
                  return '2'
            elif obj[6] == 'Greater_244.5':
               # {"feature": "NumWaitingJob", "instances": 63, "metric_value": 0.7642, "depth": 5}
               if obj[0] == 'Less_10.5':
                  return '2'
               elif obj[0] == 'Less_14.5':
                  return '2'
               else:
                  return '2'
            elif obj[6] == 'Less_244.5':
               # {"feature": "PTime_A_VS_B", "instances": 34, "metric_value": 0.6723, "depth": 5}
               if obj[3] == '>':
                  return '2'
               elif obj[3] == '<':
                  return '0'
               elif obj[3] == '=':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[4] == 'Greater_9.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 426, "metric_value": 0.2034, "depth": 4}
            if obj[6] == 'Less_211.5':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 369, "metric_value": 0.152, "depth": 5}
               if obj[10] == 'Less_70.5':
                  return '2'
               elif obj[10] == 'Greater_70.5':
                  return '2'
               else:
                  return '2'
            elif obj[6] == 'Greater_244.5':
               # {"feature": "Tardy_A_VS_B", "instances": 36, "metric_value": 0.5813, "depth": 5}
               if obj[9] == '>':
                  return '2'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[6] == 'Less_244.5':
               return '2'
            else:
               return '2'
         elif obj[4] == 'Less_-10.5':
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 134, "metric_value": 0.7395, "depth": 4}
            if obj[10] == 'Less_70.5':
               # {"feature": "NumWaitingJob", "instances": 111, "metric_value": 0.8393, "depth": 5}
               if obj[0] == 'Greater_14.5':
                  return '2'
               elif obj[0] == 'Less_14.5':
                  return '2'
               elif obj[0] == 'Less_10.5':
                  return '2'
               else:
                  return '2'
            elif obj[10] == 'Greater_70.5':
               return '2'
            else:
               return '2'
         elif obj[4] == 'Less_-23.5':
            # {"feature": "NumWaitingJob", "instances": 16, "metric_value": 0.9887, "depth": 4}
            if obj[0] == 'Less_14.5':
               # {"feature": "Tardy_A_VS_B", "instances": 6, "metric_value": 0.9183, "depth": 5}
               if obj[9] == '=':
                  return '0'
               elif obj[9] == '>':
                  return '0'
               else:
                  return '2'
            elif obj[0] == 'Greater_14.5':
               # {"feature": "Tardy_A_VS_B", "instances": 5, "metric_value": 0.971, "depth": 5}
               if obj[9] == '=':
                  return '2'
               elif obj[9] == '>':
                  return '0'
               else:
                  return '2'
            elif obj[0] == 'Less_10.5':
               return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[7] == '<':
         # {"feature": "Tardy_A_VS_B_Diff", "instances": 435, "metric_value": 0.0988, "depth": 3}
         if obj[10] == 'Less_70.5':
            # {"feature": "PTime_A_VS_B", "instances": 399, "metric_value": 0.0708, "depth": 4}
            if obj[3] == '>':
               return '2'
            elif obj[3] == '<':
               # {"feature": "CompTime_A_VS_B", "instances": 170, "metric_value": 0.1442, "depth": 5}
               if obj[5] == '<':
                  return '2'
               elif obj[5] == '>':
                  return '2'
               elif obj[5] == '=':
                  return '2'
               else:
                  return '2'
            elif obj[3] == '=':
               return '2'
            else:
               return '2'
         elif obj[10] == 'Less_-105.5':
            # {"feature": "PTime_A_VS_B", "instances": 34, "metric_value": 0.3228, "depth": 4}
            if obj[3] == '<':
               return '2'
            elif obj[3] == '>':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '2'
               elif obj[4] == 'Greater_9.5':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[10] == 'Greater_70.5':
            return '2'
         else:
            return '2'
      elif obj[7] == '=':
         return '2'
      else:
         return '2'
   elif obj[2] == 'Less_-30.5':
      # {"feature": "Start_A_VS_B", "instances": 387, "metric_value": 0.7042, "depth": 2}
      if obj[7] == '<':
         # {"feature": "Tardy_A_VS_B_Diff", "instances": 236, "metric_value": 0.8848, "depth": 3}
         if obj[10] == 'Less_70.5':
            # {"feature": "Start_A_VS_B_Diff", "instances": 189, "metric_value": 0.9745, "depth": 4}
            if obj[8] == 'Less_-2.5':
               # {"feature": "PTime_A_VS_B", "instances": 174, "metric_value": 0.9427, "depth": 5}
               if obj[3] == '<':
                  return '0'
               elif obj[3] == '>':
                  return '0'
               elif obj[3] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[8] == 'Less_-154.5':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 12, "metric_value": 0.65, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '2'
               elif obj[4] == 'Less_-10.5':
                  return '0'
               else:
                  return '2'
            elif obj[8] == 'Greater_-2.5':
               return '0'
            else:
               return '2'
         elif obj[10] == 'Less_-105.5':
            # {"feature": "Start_A_VS_B_Diff", "instances": 44, "metric_value": 0.1565, "depth": 4}
            if obj[8] == 'Less_-154.5':
               return '0'
            elif obj[8] == 'Less_-2.5':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 22, "metric_value": 0.2668, "depth": 5}
               if obj[4] == 'Less_9.5':
                  return '0'
               elif obj[4] == 'Less_-10.5':
                  return '0'
               elif obj[4] == 'Less_-23.5':
                  return '0'
               elif obj[4] == 'Greater_9.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[10] == 'Less_-226.5':
            return '0'
         else:
            return '2'
      elif obj[7] == '>':
         # {"feature": "CompTime_A_VS_B_Diff", "instances": 151, "metric_value": 0.2411, "depth": 3}
         if obj[6] == 'Less_211.5':
            # {"feature": "CompTime_A_VS_B", "instances": 145, "metric_value": 0.2164, "depth": 4}
            if obj[5] == '>':
               # {"feature": "Tardy_A_VS_B", "instances": 108, "metric_value": 0.2705, "depth": 5}
               if obj[9] == '>':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[5] == '<':
               return '0'
            else:
               return '2'
         elif obj[6] == 'Less_244.5':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[4] == 'Greater_9.5':
               return '0'
            elif obj[4] == 'Less_9.5':
               return '2'
            else:
               return '2'
         elif obj[6] == 'Greater_244.5':
            return '0'
         else:
            return '2'
      else:
         return '2'
   else:
      return '2'
