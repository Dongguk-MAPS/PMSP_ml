def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B, obj[2]: STime_A_VS_B_Diff, obj[3]: PTime_A_VS_B, obj[4]: PTime_A_VS_B_Diff, obj[5]: CompTime_A_VS_B, obj[6]: CompTime_A_VS_B_Diff, obj[7]: Start_A_VS_B, obj[8]: Start_A_VS_B_Diff, obj[9]: Tardy_A_VS_B, obj[10]: Tardy_A_VS_B_Diff
   # {"feature": "STime_A_VS_B", "instances": 15284, "metric_value": 1.6129, "depth": 1}
   if obj[1] == '<':
      # {"feature": "STime_A_VS_B_Diff", "instances": 6290, "metric_value": 0.951, "depth": 2}
      if obj[2] == 'Greater_-68.5':
         # {"feature": "PTime_A_VS_B", "instances": 5769, "metric_value": 0.9941, "depth": 3}
         if obj[3] == '<':
            # {"feature": "Start_A_VS_B", "instances": 3124, "metric_value": 0.6965, "depth": 4}
            if obj[7] == '<':
               # {"feature": "NumWaitingJob", "instances": 1983, "metric_value": 0.8309, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '0'
               elif obj[0] == 'Less_5.5':
                  return '0'
               elif obj[0] == 'Less_1.5':
                  return '0'
               else:
                  return '2'
            elif obj[7] == '>':
               # {"feature": "NumWaitingJob", "instances": 1127, "metric_value": 0.3935, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Less_5.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '0'
               elif obj[0] == 'Less_1.5':
                  return '1'
               else:
                  return '2'
            elif obj[7] == '=':
               # {"feature": "Tardy_A_VS_B", "instances": 14, "metric_value": 0.3712, "depth": 5}
               if obj[9] == '=':
                  return '0'
               elif obj[9] == '<':
                  return '0'
               else:
                  return '1'
            else:
               return '2'
         elif obj[3] == '>':
            # {"feature": "Start_A_VS_B", "instances": 2452, "metric_value": 1.2655, "depth": 4}
            if obj[7] == '<':
               # {"feature": "CompTime_A_VS_B", "instances": 1428, "metric_value": 1.458, "depth": 5}
               if obj[5] == '<':
                  return '0'
               elif obj[5] == '>':
                  return '1'
               elif obj[5] == '=':
                  return '1'
               else:
                  return '4'
            elif obj[7] == '>':
               # {"feature": "CompTime_A_VS_B", "instances": 1007, "metric_value": 0.8246, "depth": 5}
               if obj[5] == '>':
                  return '0'
               elif obj[5] == '<':
                  return '0'
               elif obj[5] == '=':
                  return '0'
               else:
                  return '4'
            elif obj[7] == '=':
               # {"feature": "Tardy_A_VS_B", "instances": 17, "metric_value": 0.3228, "depth": 5}
               if obj[9] == '=':
                  return '0'
               elif obj[9] == '<':
                  return '0'
               else:
                  return '1'
            else:
               return '4'
         elif obj[3] == '=':
            # {"feature": "Start_A_VS_B", "instances": 193, "metric_value": 0.9583, "depth": 4}
            if obj[7] == '<':
               # {"feature": "NumWaitingJob", "instances": 117, "metric_value": 1.1553, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Less_5.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '0'
               elif obj[0] == 'Less_1.5':
                  return '0'
               else:
                  return '2'
            elif obj[7] == '>':
               # {"feature": "CompTime_A_VS_B", "instances": 75, "metric_value": 0.4898, "depth": 5}
               if obj[5] == '>':
                  return '0'
               elif obj[5] == '<':
                  return '0'
               elif obj[5] == '=':
                  return '1'
               else:
                  return '1'
            elif obj[7] == '=':
               return '0'
            else:
               return '2'
         else:
            return '4'
      elif obj[2] == 'Less_-68.5':
         # {"feature": "PTime_A_VS_B", "instances": 521, "metric_value": 0.2437, "depth": 3}
         if obj[3] == '<':
            # {"feature": "Tardy_A_VS_B", "instances": 309, "metric_value": 0.0789, "depth": 4}
            if obj[9] == '<':
               return '0'
            elif obj[9] == '=':
               # {"feature": "NumWaitingJob", "instances": 100, "metric_value": 0.1944, "depth": 5}
               if obj[0] == 'Greater_15.5':
                  return '0'
               elif obj[0] == 'Less_15.5':
                  return '0'
               else:
                  return '1'
            elif obj[9] == '>':
               return '0'
            else:
               return '1'
         elif obj[3] == '>':
            # {"feature": "Start_A_VS_B", "instances": 198, "metric_value": 0.4395, "depth": 4}
            if obj[7] == '<':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 154, "metric_value": 0.5203, "depth": 5}
               if obj[6] == 'Less_160.5':
                  return '0'
               elif obj[6] == 'Less_-339.0':
                  return '0'
               else:
                  return '1'
            elif obj[7] == '>':
               return '0'
            elif obj[7] == '=':
               return '0'
            else:
               return '1'
         elif obj[3] == '=':
            return '0'
         else:
            return '1'
      else:
         return '4'
   elif obj[1] == '>':
      # {"feature": "PTime_A_VS_B_Diff", "instances": 6290, "metric_value": 1.9062, "depth": 2}
      if obj[4] == 'Greater_-12.5':
         # {"feature": "Start_A_VS_B", "instances": 5381, "metric_value": 1.9269, "depth": 3}
         if obj[7] == '>':
            # {"feature": "CompTime_A_VS_B", "instances": 3446, "metric_value": 1.8468, "depth": 4}
            if obj[5] == '>':
               # {"feature": "PTime_A_VS_B", "instances": 3436, "metric_value": 1.8474, "depth": 5}
               if obj[3] == '>':
                  return '1'
               elif obj[3] == '<':
                  return '1'
               elif obj[3] == '=':
                  return '1'
               else:
                  return '4'
            elif obj[5] == '=':
               # {"feature": "NumWaitingJob", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '1'
               else:
                  return '1'
            elif obj[5] == '<':
               # {"feature": "NumWaitingJob", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '1'
               else:
                  return '1'
            else:
               return '4'
         elif obj[7] == '<':
            # {"feature": "NumWaitingJob", "instances": 1908, "metric_value": 1.9634, "depth": 4}
            if obj[0] == 'Less_15.5':
               # {"feature": "PTime_A_VS_B", "instances": 1542, "metric_value": 1.9973, "depth": 5}
               if obj[3] == '>':
                  return '2'
               elif obj[3] == '<':
                  return '1'
               elif obj[3] == '=':
                  return '1'
               else:
                  return '4'
            elif obj[0] == 'Less_5.5':
               # {"feature": "CompTime_A_VS_B", "instances": 271, "metric_value": 1.5697, "depth": 5}
               if obj[5] == '<':
                  return '1'
               elif obj[5] == '>':
                  return '1'
               else:
                  return '4'
            elif obj[0] == 'Greater_15.5':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 91, "metric_value": 1.7185, "depth": 5}
               if obj[10] == 'Less_11.5':
                  return '1'
               elif obj[10] == 'Greater_11.5':
                  return '2'
               else:
                  return '4'
            elif obj[0] == 'Less_1.5':
               # {"feature": "CompTime_A_VS_B", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[5] == '<':
                  return '0'
               elif obj[5] == '>':
                  return '1'
               else:
                  return '1'
            else:
               return '4'
         elif obj[7] == '=':
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 27, "metric_value": 1.4763, "depth": 4}
            if obj[10] == 'Less_11.5':
               # {"feature": "PTime_A_VS_B", "instances": 15, "metric_value": 1.6402, "depth": 5}
               if obj[3] == '>':
                  return '1'
               elif obj[3] == '<':
                  return '1'
               elif obj[3] == '=':
                  return '2'
               else:
                  return '3'
            elif obj[10] == 'Greater_11.5':
               # {"feature": "NumWaitingJob", "instances": 12, "metric_value": 0.65, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '2'
               else:
                  return '2'
            else:
               return '3'
         else:
            return '4'
      elif obj[4] == 'Less_-12.5':
         # {"feature": "CompTime_A_VS_B_Diff", "instances": 767, "metric_value": 1.5596, "depth": 3}
         if obj[6] == 'Less_160.5':
            # {"feature": "Start_A_VS_B", "instances": 725, "metric_value": 1.5215, "depth": 4}
            if obj[7] == '>':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 403, "metric_value": 1.2105, "depth": 5}
               if obj[10] == 'Less_11.5':
                  return '0'
               elif obj[10] == 'Greater_11.5':
                  return '1'
               else:
                  return '4'
            elif obj[7] == '<':
               # {"feature": "Start_A_VS_B_Diff", "instances": 315, "metric_value": 1.6681, "depth": 5}
               if obj[8] == 'Less_163.5':
                  return '1'
               elif obj[8] == 'Less_-237.5':
                  return '1'
               elif obj[8] == 'Less_-294.0':
                  return '0'
               else:
                  return '4'
            elif obj[7] == '=':
               # {"feature": "Tardy_A_VS_B", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[9] == '=':
                  return '1'
               elif obj[9] == '>':
                  return '2'
               else:
                  return '2'
            else:
               return '4'
         elif obj[6] == 'Greater_160.5':
            # {"feature": "NumWaitingJob", "instances": 42, "metric_value": 1.6301, "depth": 4}
            if obj[0] == 'Less_15.5':
               # {"feature": "Start_A_VS_B_Diff", "instances": 27, "metric_value": 1.3921, "depth": 5}
               if obj[8] == 'Greater_163.5':
                  return '0'
               elif obj[8] == 'Less_163.5':
                  return '2'
               else:
                  return '2'
            elif obj[0] == 'Less_5.5':
               # {"feature": "Start_A_VS_B_Diff", "instances": 9, "metric_value": 1.8366, "depth": 5}
               if obj[8] == 'Greater_163.5':
                  return '0'
               elif obj[8] == 'Less_163.5':
                  return '1'
               else:
                  return '4'
            elif obj[0] == 'Greater_15.5':
               # {"feature": "Tardy_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[9] == '>':
                  return '2'
               elif obj[9] == '=':
                  return '2'
               else:
                  return '2'
            elif obj[0] == 'Less_1.5':
               return '2'
            else:
               return '4'
         else:
            return '4'
      elif obj[4] == 'Less_-23.5':
         # {"feature": "Start_A_VS_B", "instances": 139, "metric_value": 1.3008, "depth": 3}
         if obj[7] == '>':
            # {"feature": "CompTime_A_VS_B", "instances": 80, "metric_value": 0.9397, "depth": 4}
            if obj[5] == '>':
               # {"feature": "NumWaitingJob", "instances": 77, "metric_value": 0.9568, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '0'
               elif obj[0] == 'Less_5.5':
                  return '1'
               else:
                  return '2'
            elif obj[5] == '<':
               return '0'
            else:
               return '2'
         elif obj[7] == '<':
            # {"feature": "CompTime_A_VS_B", "instances": 59, "metric_value": 1.5316, "depth": 4}
            if obj[5] == '<':
               # {"feature": "Start_A_VS_B_Diff", "instances": 57, "metric_value": 1.5466, "depth": 5}
               if obj[8] == 'Less_163.5':
                  return '1'
               elif obj[8] == 'Less_-237.5':
                  return '1'
               else:
                  return '3'
            elif obj[5] == '>':
               return '1'
            else:
               return '3'
         else:
            return '3'
      elif obj[4] == 'Less_-29.5':
         # {"feature": "CompTime_A_VS_B_Diff", "instances": 3, "metric_value": 0.9183, "depth": 3}
         if obj[6] == 'Less_160.5':
            return '0'
         elif obj[6] == 'Greater_160.5':
            return '1'
         else:
            return '1'
      else:
         return '4'
   elif obj[1] == '=':
      # {"feature": "CompTime_A_VS_B_Diff", "instances": 2704, "metric_value": 1.1891, "depth": 2}
      if obj[6] == 'Less_160.5':
         # {"feature": "PTime_A_VS_B", "instances": 2697, "metric_value": 1.185, "depth": 3}
         if obj[3] == '<':
            # {"feature": "Start_A_VS_B_Diff", "instances": 1318, "metric_value": 0.9468, "depth": 4}
            if obj[8] == 'Less_163.5':
               # {"feature": "PTime_A_VS_B_Diff", "instances": 1316, "metric_value": 0.9456, "depth": 5}
               if obj[4] == 'Greater_-12.5':
                  return '0'
               elif obj[4] == 'Less_-12.5':
                  return '0'
               elif obj[4] == 'Less_-23.5':
                  return '0'
               elif obj[4] == 'Less_-29.5':
                  return '0'
               else:
                  return '2'
            elif obj[8] == 'Greater_163.5':
               return '1'
            else:
               return '2'
         elif obj[3] == '>':
            # {"feature": "CompTime_A_VS_B", "instances": 1311, "metric_value": 1.2086, "depth": 4}
            if obj[5] == '>':
               # {"feature": "Start_A_VS_B", "instances": 1299, "metric_value": 1.1858, "depth": 5}
               if obj[7] == '=':
                  return '1'
               elif obj[7] == '>':
                  return '1'
               elif obj[7] == '<':
                  return '2'
               else:
                  return '4'
            elif obj[5] == '<':
               # {"feature": "NumWaitingJob", "instances": 12, "metric_value": 1.7807, "depth": 5}
               if obj[0] == 'Less_5.5':
                  return '0'
               elif obj[0] == 'Less_15.5':
                  return '1'
               elif obj[0] == 'Greater_15.5':
                  return '3'
               else:
                  return '4'
            else:
               return '4'
         elif obj[3] == '=':
            # {"feature": "NumWaitingJob", "instances": 68, "metric_value": 1.0944, "depth": 4}
            if obj[0] == 'Greater_15.5':
               # {"feature": "STime_A_VS_B_Diff", "instances": 34, "metric_value": 1.1614, "depth": 5}
               if obj[2] == 'Greater_-68.5':
                  return '0'
               else:
                  return '2'
            elif obj[0] == 'Less_15.5':
               # {"feature": "STime_A_VS_B_Diff", "instances": 34, "metric_value": 0.9975, "depth": 5}
               if obj[2] == 'Greater_-68.5':
                  return '0'
               else:
                  return '1'
            else:
               return '2'
         else:
            return '4'
      elif obj[6] == 'Greater_160.5':
         # {"feature": "Start_A_VS_B_Diff", "instances": 7, "metric_value": 1.4488, "depth": 3}
         if obj[8] == 'Greater_163.5':
            # {"feature": "NumWaitingJob", "instances": 6, "metric_value": 1.4591, "depth": 4}
            if obj[0] == 'Less_5.5':
               # {"feature": "STime_A_VS_B_Diff", "instances": 4, "metric_value": 1.5, "depth": 5}
               if obj[2] == 'Greater_-68.5':
                  return '0'
               else:
                  return '2'
            elif obj[0] == 'Less_15.5':
               # {"feature": "STime_A_VS_B_Diff", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[2] == 'Greater_-68.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[8] == 'Less_163.5':
            return '2'
         else:
            return '2'
      else:
         return '4'
   else:
      return '4'
