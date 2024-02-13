def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B, obj[2]: STime_A_VS_B_Diff, obj[3]: PTime_A_VS_B, obj[4]: PTime_A_VS_B_Diff, obj[5]: CompTime_A_VS_B, obj[6]: CompTime_A_VS_B_Diff, obj[7]: Start_A_VS_B, obj[8]: Start_A_VS_B_Diff, obj[9]: Tardy_A_VS_B, obj[10]: Tardy_A_VS_B_Diff
   # {"feature": "STime_A_VS_B", "instances": 15284, "metric_value": 1.41, "depth": 1}
   if obj[1] == '<':
      # {"feature": "STime_A_VS_B_Diff", "instances": 6290, "metric_value": 0.9008, "depth": 2}
      if obj[2] == 'Greater_-29.5':
         # {"feature": "Start_A_VS_B", "instances": 2995, "metric_value": 1.1504, "depth": 3}
         if obj[7] == '<':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 1740, "metric_value": 1.2965, "depth": 4}
            if obj[4] == 'Greater_-2.5':
               # {"feature": "Tardy_A_VS_B", "instances": 946, "metric_value": 1.392, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '1'
               elif obj[9] == '>':
                  return '1'
               else:
                  return '2'
            elif obj[4] == 'Less_-2.5':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 794, "metric_value": 1.0134, "depth": 5}
               if obj[6] == 'Less_203.5':
                  return '0'
               elif obj[6] == 'Less_-284.5':
                  return '0'
               elif obj[6] == 'Less_-370.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[7] == '>':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 1238, "metric_value": 0.8098, "depth": 4}
            if obj[4] == 'Greater_-2.5':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 734, "metric_value": 0.9484, "depth": 5}
               if obj[6] == 'Less_203.5':
                  return '0'
               elif obj[6] == 'Greater_203.5':
                  return '0'
               else:
                  return '2'
            elif obj[4] == 'Less_-2.5':
               # {"feature": "NumWaitingJob", "instances": 504, "metric_value": 0.5181, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Less_7.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[7] == '=':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 17, "metric_value": 0.5226, "depth": 4}
            if obj[4] == 'Greater_-2.5':
               # {"feature": "PTime_A_VS_B", "instances": 11, "metric_value": 0.684, "depth": 5}
               if obj[3] == '>':
                  return '0'
               elif obj[3] == '=':
                  return '0'
               elif obj[3] == '<':
                  return '1'
               else:
                  return '1'
            elif obj[4] == 'Less_-2.5':
               return '0'
            else:
               return '1'
         else:
            return '2'
      elif obj[2] == 'Less_-29.5':
         # {"feature": "Start_A_VS_B", "instances": 2433, "metric_value": 0.6206, "depth": 3}
         if obj[7] == '<':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 1543, "metric_value": 0.7884, "depth": 4}
            if obj[4] == 'Less_-2.5':
               # {"feature": "Tardy_A_VS_B", "instances": 836, "metric_value": 0.4713, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[4] == 'Greater_-2.5':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 707, "metric_value": 1.0367, "depth": 5}
               if obj[6] == 'Less_203.5':
                  return '0'
               elif obj[6] == 'Less_-284.5':
                  return '1'
               elif obj[6] == 'Less_-370.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[7] == '>':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 878, "metric_value": 0.1981, "depth": 4}
            if obj[4] == 'Greater_-2.5':
               # {"feature": "CompTime_A_VS_B_Diff", "instances": 448, "metric_value": 0.3014, "depth": 5}
               if obj[6] == 'Less_203.5':
                  return '0'
               elif obj[6] == 'Greater_203.5':
                  return '0'
               else:
                  return '1'
            elif obj[4] == 'Less_-2.5':
               # {"feature": "CompTime_A_VS_B", "instances": 430, "metric_value": 0.06, "depth": 5}
               if obj[5] == '>':
                  return '0'
               elif obj[5] == '<':
                  return '0'
               elif obj[5] == '=':
                  return '0'
               else:
                  return '1'
            else:
               return '1'
         elif obj[7] == '=':
            return '0'
         else:
            return '2'
      elif obj[2] == 'Less_-62.5':
         # {"feature": "Start_A_VS_B", "instances": 693, "metric_value": 0.2885, "depth": 3}
         if obj[7] == '<':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 522, "metric_value": 0.3548, "depth": 4}
            if obj[4] == 'Less_-2.5':
               # {"feature": "Start_A_VS_B_Diff", "instances": 293, "metric_value": 0.1807, "depth": 5}
               if obj[8] == 'Greater_-185.5':
                  return '0'
               elif obj[8] == 'Less_-185.5':
                  return '0'
               else:
                  return '1'
            elif obj[4] == 'Greater_-2.5':
               # {"feature": "Tardy_A_VS_B", "instances": 229, "metric_value": 0.5233, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '1'
            else:
               return '1'
         elif obj[7] == '>':
            return '0'
         elif obj[7] == '=':
            return '0'
         else:
            return '1'
      elif obj[2] == 'Less_-80.5':
         # {"feature": "PTime_A_VS_B", "instances": 169, "metric_value": 0.3001, "depth": 3}
         if obj[3] == '<':
            # {"feature": "Tardy_A_VS_B", "instances": 100, "metric_value": 0.1414, "depth": 4}
            if obj[9] == '<':
               return '0'
            elif obj[9] == '=':
               # {"feature": "NumWaitingJob", "instances": 39, "metric_value": 0.2918, "depth": 5}
               if obj[0] == 'Greater_15.5':
                  return '0'
               elif obj[0] == 'Less_15.5':
                  return '0'
               else:
                  return '1'
            else:
               return '1'
         elif obj[3] == '>':
            # {"feature": "Tardy_A_VS_B", "instances": 66, "metric_value": 0.4879, "depth": 4}
            if obj[9] == '=':
               return '0'
            elif obj[9] == '<':
               # {"feature": "NumWaitingJob", "instances": 29, "metric_value": 0.7973, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '0'
               elif obj[0] == 'Less_7.5':
                  return '0'
               else:
                  return '1'
            else:
               return '1'
         elif obj[3] == '=':
            return '0'
         else:
            return '1'
      else:
         return '2'
   elif obj[1] == '>':
      # {"feature": "PTime_A_VS_B_Diff", "instances": 6290, "metric_value": 1.5079, "depth": 2}
      if obj[4] == 'Greater_-2.5':
         # {"feature": "Start_A_VS_B", "instances": 4037, "metric_value": 1.4555, "depth": 3}
         if obj[7] == '>':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 2643, "metric_value": 1.4758, "depth": 4}
            if obj[6] == 'Less_203.5':
               # {"feature": "NumWaitingJob", "instances": 2311, "metric_value": 1.4511, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '1'
               elif obj[0] == 'Less_7.5':
                  return '1'
               elif obj[0] == 'Greater_15.5':
                  return '1'
               else:
                  return '2'
            elif obj[6] == 'Greater_203.5':
               # {"feature": "PTime_A_VS_B", "instances": 332, "metric_value": 1.5522, "depth": 5}
               if obj[3] == '>':
                  return '2'
               elif obj[3] == '<':
                  return '0'
               elif obj[3] == '=':
                  return '1'
               else:
                  return '2'
            else:
               return '2'
         elif obj[7] == '<':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 1375, "metric_value": 1.3258, "depth": 4}
            if obj[6] == 'Less_203.5':
               # {"feature": "NumWaitingJob", "instances": 1374, "metric_value": 1.326, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '2'
               elif obj[0] == 'Less_7.5':
                  return '1'
               elif obj[0] == 'Greater_15.5':
                  return '2'
               else:
                  return '2'
            elif obj[6] == 'Less_-284.5':
               return '2'
            else:
               return '2'
         elif obj[7] == '=':
            # {"feature": "PTime_A_VS_B", "instances": 19, "metric_value": 1.378, "depth": 4}
            if obj[3] == '>':
               # {"feature": "NumWaitingJob", "instances": 14, "metric_value": 1.2958, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '2'
               elif obj[0] == 'Less_7.5':
                  return '1'
               else:
                  return '2'
            elif obj[3] == '<':
               # {"feature": "Tardy_A_VS_B", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[9] == '=':
                  return '1'
               elif obj[9] == '>':
                  return '1'
               else:
                  return '1'
            elif obj[3] == '=':
               return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[4] == 'Less_-2.5':
         # {"feature": "Start_A_VS_B", "instances": 2253, "metric_value": 1.4564, "depth": 3}
         if obj[7] == '>':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 1331, "metric_value": 1.3522, "depth": 4}
            if obj[6] == 'Less_203.5':
               # {"feature": "CompTime_A_VS_B", "instances": 1255, "metric_value": 1.2997, "depth": 5}
               if obj[5] == '>':
                  return '0'
               elif obj[5] == '<':
                  return '0'
               elif obj[5] == '=':
                  return '0'
               else:
                  return '2'
            elif obj[6] == 'Greater_203.5':
               # {"feature": "NumWaitingJob", "instances": 76, "metric_value": 1.5301, "depth": 5}
               if obj[0] == 'Less_7.5':
                  return '2'
               elif obj[0] == 'Less_15.5':
                  return '2'
               elif obj[0] == 'Greater_15.5':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[7] == '<':
            # {"feature": "CompTime_A_VS_B", "instances": 907, "metric_value": 1.4237, "depth": 4}
            if obj[5] == '<':
               # {"feature": "Start_A_VS_B_Diff", "instances": 764, "metric_value": 1.4513, "depth": 5}
               if obj[8] == 'Greater_-185.5':
                  return '1'
               elif obj[8] == 'Less_-185.5':
                  return '1'
               else:
                  return '2'
            elif obj[5] == '>':
               # {"feature": "NumWaitingJob", "instances": 141, "metric_value": 1.1532, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '1'
               elif obj[0] == 'Less_7.5':
                  return '1'
               elif obj[0] == 'Greater_15.5':
                  return '2'
               else:
                  return '2'
            elif obj[5] == '=':
               # {"feature": "NumWaitingJob", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[0] == 'Less_7.5':
                  return '1'
               elif obj[0] == 'Greater_15.5':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[7] == '=':
            # {"feature": "Tardy_A_VS_B", "instances": 15, "metric_value": 0.9968, "depth": 4}
            if obj[9] == '>':
               # {"feature": "NumWaitingJob", "instances": 8, "metric_value": 0.5436, "depth": 5}
               if obj[0] == 'Less_15.5':
                  return '2'
               elif obj[0] == 'Less_7.5':
                  return '2'
               else:
                  return '2'
            elif obj[9] == '=':
               return '1'
            else:
               return '2'
         else:
            return '2'
      else:
         return '2'
   elif obj[1] == '=':
      # {"feature": "PTime_A_VS_B_Diff", "instances": 2704, "metric_value": 1.1209, "depth": 2}
      if obj[4] == 'Greater_-2.5':
         # {"feature": "Tardy_A_VS_B_Diff", "instances": 1545, "metric_value": 1.1151, "depth": 3}
         if obj[10] == 'Greater_-39.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 1540, "metric_value": 1.1136, "depth": 4}
            if obj[6] == 'Less_203.5':
               # {"feature": "Tardy_A_VS_B", "instances": 1538, "metric_value": 1.113, "depth": 5}
               if obj[9] == '=':
                  return '1'
               elif obj[9] == '>':
                  return '1'
               elif obj[9] == '<':
                  return '1'
               else:
                  return '2'
            elif obj[6] == 'Greater_203.5':
               return '0'
            else:
               return '2'
         elif obj[10] == 'Less_-39.5':
            return '0'
         else:
            return '2'
      elif obj[4] == 'Less_-2.5':
         # {"feature": "Start_A_VS_B_Diff", "instances": 1159, "metric_value": 0.8609, "depth": 3}
         if obj[8] == 'Greater_-185.5':
            # {"feature": "CompTime_A_VS_B", "instances": 1157, "metric_value": 0.8592, "depth": 4}
            if obj[5] == '<':
               # {"feature": "Tardy_A_VS_B_Diff", "instances": 1145, "metric_value": 0.8547, "depth": 5}
               if obj[10] == 'Greater_-39.5':
                  return '0'
               elif obj[10] == 'Less_-39.5':
                  return '0'
               else:
                  return '2'
            elif obj[5] == '>':
               # {"feature": "NumWaitingJob", "instances": 12, "metric_value": 0.9799, "depth": 5}
               if obj[0] == 'Less_7.5':
                  return '1'
               elif obj[0] == 'Less_15.5':
                  return '0'
               elif obj[0] == 'Greater_15.5':
                  return '0'
               else:
                  return '1'
            else:
               return '2'
         elif obj[8] == 'Less_-185.5':
            return '1'
         else:
            return '2'
      else:
         return '2'
   else:
      return '2'
