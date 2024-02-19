def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B_Avg, obj[2]: STime_A_VS_B_Avg_Diff, obj[3]: STime_A_VS_B_Min, obj[4]: STime_A_VS_B_Min_Diff, obj[5]: STime_A_VS_B_Max, obj[6]: STime_A_VS_B_Max_Diff, obj[7]: PTime_A_VS_B_Avg, obj[8]: PTime_A_VS_B_Avg_Diff, obj[9]: PTime_A_VS_B_Min, obj[10]: PTime_A_VS_B_Min_Diff, obj[11]: PTime_A_VS_B_Max, obj[12]: PTime_A_VS_B_Max_Diff, obj[13]: Due_A_VS_B, obj[14]: Due_A_VS_B_Diff
<<<<<<< HEAD
   # {"feature": "STime_A_VS_B_Min_Diff", "instances": 6736, "metric_value": 1.0444, "depth": 1}
   if obj[4] == 'Less_20.5':
      # {"feature": "Due_A_VS_B", "instances": 6254, "metric_value": 0.9874, "depth": 2}
      if obj[13] == '<':
         # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 3203, "metric_value": 0.6315, "depth": 3}
         if obj[2] == 'Less_44.166666666666664':
            # {"feature": "Due_A_VS_B_Diff", "instances": 2724, "metric_value": 0.6859, "depth": 4}
            if obj[14] == 'Less_79.5':
               # {"feature": "STime_A_VS_B_Min", "instances": 1981, "metric_value": 0.7504, "depth": 5}
=======
   # {"feature": "Due_A_VS_B", "instances": 6736, "metric_value": 1.2999, "depth": 1}
   if obj[13] == '<':
      # {"feature": "STime_A_VS_B_Min_Diff", "instances": 3338, "metric_value": 0.8688, "depth": 2}
      if obj[4] == 'Less_13.5':
         # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 3016, "metric_value": 0.7644, "depth": 3}
         if obj[2] == 'Greater_-13.000000000000004':
            # {"feature": "STime_A_VS_B_Avg", "instances": 2252, "metric_value": 0.8722, "depth": 4}
            if obj[1] == '>':
               # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 953, "metric_value": 0.9718, "depth": 5}
               if obj[10] == 'Less_18.5':
                  return '0'
               elif obj[10] == 'Greater_18.5':
                  return '0'
               else:
                  return '2'
            elif obj[1] == '<':
               # {"feature": "STime_A_VS_B_Min", "instances": 856, "metric_value": 0.6894, "depth": 5}
>>>>>>> f65158b (feat: local search)
               if obj[3] == '=':
                  return '0'
               elif obj[3] == '<':
                  return '0'
               elif obj[3] == '>':
                  return '0'
               else:
                  return '2'
<<<<<<< HEAD
            elif obj[14] == 'Less_-85.5':
               # {"feature": "STime_A_VS_B_Avg", "instances": 743, "metric_value": 0.4561, "depth": 5}
               if obj[1] == '<':
                  return '0'
               elif obj[1] == '>':
                  return '0'
               elif obj[1] == '=':
                  return '0'
=======
            elif obj[1] == '=':
               # {"feature": "NumWaitingJob", "instances": 443, "metric_value": 0.9044, "depth": 5}
               if obj[0] == 'Greater_6.5':
                  return '0'
               elif obj[0] == 'Less_6.5':
                  return '1'
>>>>>>> f65158b (feat: local search)
               else:
                  return '2'
            else:
               return '2'
<<<<<<< HEAD
         elif obj[2] == 'Less_-21.166666666666664':
            # {"feature": "Due_A_VS_B_Diff", "instances": 479, "metric_value": 0.1689, "depth": 4}
            if obj[14] == 'Less_79.5':
               # {"feature": "STime_A_VS_B_Max", "instances": 300, "metric_value": 0.2268, "depth": 5}
=======
         elif obj[2] == 'Less_-13.000000000000004':
            # {"feature": "NumWaitingJob", "instances": 764, "metric_value": 0.3621, "depth": 4}
            if obj[0] == 'Greater_6.5':
               # {"feature": "STime_A_VS_B_Max", "instances": 661, "metric_value": 0.3191, "depth": 5}
>>>>>>> f65158b (feat: local search)
               if obj[5] == '<':
                  return '0'
               elif obj[5] == '>':
                  return '0'
               elif obj[5] == '=':
                  return '0'
               else:
<<<<<<< HEAD
                  return '1'
            elif obj[14] == 'Less_-85.5':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 179, "metric_value": 0.0498, "depth": 5}
               if obj[7] == '<':
                  return '0'
               elif obj[7] == '>':
                  return '0'
               elif obj[7] == '=':
                  return '0'
               else:
                  return '1'
            else:
               return '1'
         else:
            return '2'
      elif obj[13] == '>':
         # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 2996, "metric_value": 1.0516, "depth": 3}
         if obj[2] == 'Less_44.166666666666664':
            # {"feature": "Due_A_VS_B_Diff", "instances": 2810, "metric_value": 1.0388, "depth": 4}
            if obj[14] == 'Less_79.5':
               # {"feature": "STime_A_VS_B_Min", "instances": 1899, "metric_value": 1.0197, "depth": 5}
               if obj[3] == '=':
                  return '1'
               elif obj[3] == '>':
                  return '1'
               elif obj[3] == '<':
                  return '0'
               else:
                  return '2'
            elif obj[14] == 'Greater_79.5':
               # {"feature": "NumWaitingJob", "instances": 911, "metric_value": 0.9385, "depth": 5}
               if obj[0] == 'Less_14.5':
                  return '1'
               elif obj[0] == 'Less_18.5':
                  return '1'
               elif obj[0] == 'Greater_18.5':
                  return '1'
               elif obj[0] == 'Less_6.5':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[2] == 'Less_-21.166666666666664':
            # {"feature": "STime_A_VS_B_Min", "instances": 180, "metric_value": 0.6873, "depth": 4}
            if obj[3] == '<':
               # {"feature": "NumWaitingJob", "instances": 120, "metric_value": 0.469, "depth": 5}
               if obj[0] == 'Less_14.5':
                  return '0'
               elif obj[0] == 'Less_6.5':
                  return '0'
               elif obj[0] == 'Less_18.5':
                  return '0'
               else:
                  return '1'
            elif obj[3] == '=':
               # {"feature": "PTime_A_VS_B_Min", "instances": 44, "metric_value": 0.8113, "depth": 5}
               if obj[9] == '>':
                  return '0'
               elif obj[9] == '<':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '1'
            elif obj[3] == '>':
               # {"feature": "PTime_A_VS_B_Min", "instances": 16, "metric_value": 0.9544, "depth": 5}
               if obj[9] == '<':
                  return '1'
               elif obj[9] == '>':
                  return '0'
               else:
                  return '1'
            else:
               return '1'
         elif obj[2] == 'Greater_44.166666666666664':
            # {"feature": "NumWaitingJob", "instances": 6, "metric_value": 1.2516, "depth": 4}
            if obj[0] == 'Less_14.5':
               # {"feature": "PTime_A_VS_B_Min", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[9] == '<':
                  return '1'
               elif obj[9] == '>':
                  return '1'
               else:
                  return '2'
            elif obj[0] == 'Less_6.5':
               return '0'
            elif obj[0] == 'Less_18.5':
               return '1'
            else:
               return '2'
         else:
            return '2'
      elif obj[13] == '=':
         # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 55, "metric_value": 0.9457, "depth": 3}
         if obj[2] == 'Less_44.166666666666664':
            # {"feature": "STime_A_VS_B_Max_Diff", "instances": 50, "metric_value": 0.971, "depth": 4}
            if obj[6] == 'Less_33.5':
               # {"feature": "STime_A_VS_B_Avg", "instances": 44, "metric_value": 0.9624, "depth": 5}
               if obj[1] == '<':
                  return '0'
               elif obj[1] == '>':
                  return '1'
               elif obj[1] == '=':
                  return '0'
               else:
                  return '1'
            elif obj[6] == 'Greater_40.5':
               # {"feature": "NumWaitingJob", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[0] == 'Less_18.5':
                  return '0'
               elif obj[0] == 'Less_14.5':
                  return '1'
               else:
                  return '1'
            elif obj[6] == 'Less_40.5':
               return '0'
            elif obj[6] == 'Less_39.5':
               return '1'
            else:
               return '1'
         elif obj[2] == 'Less_-21.166666666666664':
            return '0'
         else:
            return '1'
      else:
         return '2'
   elif obj[4] == 'Less_46.5':
      # {"feature": "STime_A_VS_B_Avg", "instances": 412, "metric_value": 0.7343, "depth": 2}
      if obj[1] == '>':
         # {"feature": "Due_A_VS_B_Diff", "instances": 388, "metric_value": 0.6928, "depth": 3}
         if obj[14] == 'Less_79.5':
            # {"feature": "PTime_A_VS_B_Avg", "instances": 272, "metric_value": 0.5931, "depth": 4}
            if obj[7] == '>':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 153, "metric_value": 0.3483, "depth": 5}
               if obj[6] == 'Less_33.5':
                  return '1'
               elif obj[6] == 'Greater_40.5':
                  return '1'
               elif obj[6] == 'Less_39.5':
                  return '1'
               elif obj[6] == 'Less_40.5':
                  return '2'
               else:
                  return '2'
            elif obj[7] == '<':
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 118, "metric_value": 0.7809, "depth": 5}
               if obj[2] == 'Less_44.166666666666664':
                  return '1'
               elif obj[2] == 'Greater_44.166666666666664':
                  return '1'
               else:
                  return '2'
            elif obj[7] == '=':
               return '2'
            else:
               return '2'
         elif obj[14] == 'Greater_79.5':
            # {"feature": "NumWaitingJob", "instances": 103, "metric_value": 0.8285, "depth": 4}
            if obj[0] == 'Less_14.5':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 73, "metric_value": 0.6778, "depth": 5}
               if obj[6] == 'Less_33.5':
                  return '1'
               elif obj[6] == 'Greater_40.5':
                  return '1'
               elif obj[6] == 'Less_39.5':
                  return '1'
               elif obj[6] == 'Less_40.5':
                  return '2'
               else:
                  return '2'
            elif obj[0] == 'Less_6.5':
               # {"feature": "PTime_A_VS_B_Max", "instances": 16, "metric_value": 0.8684, "depth": 5}
               if obj[11] == '>':
                  return '1'
               elif obj[11] == '=':
                  return '0'
               elif obj[11] == '<':
                  return '1'
               else:
                  return '2'
            elif obj[0] == 'Less_18.5':
               # {"feature": "PTime_A_VS_B_Min", "instances": 14, "metric_value": 0.9852, "depth": 5}
               if obj[9] == '>':
                  return '1'
               elif obj[9] == '<':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[14] == 'Less_-85.5':
            # {"feature": "PTime_A_VS_B_Avg", "instances": 13, "metric_value": 0.3912, "depth": 4}
            if obj[7] == '>':
               return '1'
            elif obj[7] == '<':
               # {"feature": "PTime_A_VS_B_Min", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[9] == '>':
                  return '2'
               elif obj[9] == '<':
                  return '1'
               else:
                  return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[1] == '<':
         # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 24, "metric_value": 0.9183, "depth": 3}
         if obj[12] == 'Greater_-11.5':
            # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 23, "metric_value": 0.9321, "depth": 4}
            if obj[10] == 'Less_8.5':
               # {"feature": "NumWaitingJob", "instances": 15, "metric_value": 0.9968, "depth": 5}
               if obj[0] == 'Less_14.5':
                  return '1'
               elif obj[0] == 'Less_6.5':
                  return '0'
               else:
                  return '1'
            elif obj[10] == 'Greater_8.5':
               # {"feature": "NumWaitingJob", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[0] == 'Less_14.5':
                  return '1'
               elif obj[0] == 'Less_6.5':
                  return '1'
               else:
                  return '1'
            elif obj[10] == 'Less_-14.5':
               return '1'
            else:
               return '1'
         elif obj[12] == 'Less_-11.5':
            return '1'
         else:
            return '1'
      else:
         return '2'
   elif obj[4] == 'Greater_46.5':
      # {"feature": "NumWaitingJob", "instances": 70, "metric_value": 0.6274, "depth": 2}
      if obj[0] == 'Less_14.5':
         # {"feature": "PTime_A_VS_B_Min", "instances": 46, "metric_value": 0.6666, "depth": 3}
         if obj[9] == '>':
            # {"feature": "STime_A_VS_B_Max_Diff", "instances": 27, "metric_value": 0.2285, "depth": 4}
            if obj[6] == 'Less_33.5':
               return '1'
            elif obj[6] == 'Greater_40.5':
               # {"feature": "Due_A_VS_B_Diff", "instances": 6, "metric_value": 0.65, "depth": 5}
               if obj[14] == 'Less_79.5':
                  return '1'
               elif obj[14] == 'Greater_79.5':
                  return '1'
               else:
                  return '2'
            else:
               return '2'
         elif obj[9] == '<':
            # {"feature": "PTime_A_VS_B_Max", "instances": 17, "metric_value": 0.9367, "depth": 4}
            if obj[11] == '<':
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 9, "metric_value": 0.5033, "depth": 5}
               if obj[2] == 'Less_44.166666666666664':
                  return '1'
               elif obj[2] == 'Greater_44.166666666666664':
                  return '1'
               else:
                  return '2'
            elif obj[11] == '>':
               # {"feature": "Due_A_VS_B", "instances": 7, "metric_value": 0.9852, "depth": 5}
               if obj[13] == '>':
                  return '2'
               elif obj[13] == '<':
                  return '1'
               else:
                  return '2'
            elif obj[11] == '=':
               return '2'
            else:
               return '2'
         elif obj[9] == '=':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[2] == 'Greater_44.166666666666664':
               return '1'
            elif obj[2] == 'Less_44.166666666666664':
               return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[0] == 'Less_6.5':
         return '1'
      elif obj[0] == 'Less_18.5':
         # {"feature": "STime_A_VS_B_Max", "instances": 4, "metric_value": 0.8113, "depth": 3}
         if obj[5] == '>':
            return '2'
         elif obj[5] == '<':
            return '1'
         else:
            return '2'
=======
                  return '2'
            elif obj[0] == 'Less_6.5':
               # {"feature": "STime_A_VS_B_Min", "instances": 103, "metric_value": 0.5805, "depth": 5}
               if obj[3] == '<':
                  return '0'
               elif obj[3] == '>':
                  return '0'
               elif obj[3] == '=':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[4] == 'Less_26.5':
         # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 117, "metric_value": 1.4251, "depth": 3}
         if obj[10] == 'Less_18.5':
            # {"feature": "NumWaitingJob", "instances": 116, "metric_value": 1.4286, "depth": 4}
            if obj[0] == 'Greater_6.5':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 87, "metric_value": 1.2848, "depth": 5}
               if obj[8] == 'Greater_-3.333333333333332':
                  return '2'
               elif obj[8] == 'Less_-3.333333333333332':
                  return '0'
               elif obj[8] == 'Less_-16.333333333333336':
                  return '2'
               else:
                  return '2'
            elif obj[0] == 'Less_6.5':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 29, "metric_value": 1.5514, "depth": 5}
               if obj[6] == 'Less_59.5':
                  return '1'
               elif obj[6] == 'Less_-18.5':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[10] == 'Greater_18.5':
            return '2'
         else:
            return '2'
      elif obj[4] == 'Less_-39.5':
         return '0'
      elif obj[4] == 'Greater_26.5':
         # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 93, "metric_value": 0.7411, "depth": 3}
         if obj[10] == 'Less_18.5':
            # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 92, "metric_value": 0.7135, "depth": 4}
            if obj[8] == 'Greater_-3.333333333333332':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 70, "metric_value": 0.6948, "depth": 5}
               if obj[7] == '>':
                  return '2'
               elif obj[7] == '<':
                  return '2'
               elif obj[7] == '=':
                  return '2'
               else:
                  return '2'
            elif obj[8] == 'Less_-3.333333333333332':
               # {"feature": "PTime_A_VS_B_Max", "instances": 21, "metric_value": 0.549, "depth": 5}
               if obj[11] == '<':
                  return '2'
               elif obj[11] == '>':
                  return '2'
               elif obj[11] == '=':
                  return '1'
               else:
                  return '2'
            elif obj[8] == 'Less_-16.333333333333336':
               return '0'
            else:
               return '2'
         elif obj[10] == 'Greater_18.5':
            return '1'
         else:
            return '2'
      else:
         return '2'
   elif obj[13] == '>':
      # {"feature": "STime_A_VS_B_Min_Diff", "instances": 3338, "metric_value": 1.4136, "depth": 2}
      if obj[4] == 'Less_13.5':
         # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 2761, "metric_value": 1.4449, "depth": 3}
         if obj[2] == 'Greater_-13.000000000000004':
            # {"feature": "NumWaitingJob", "instances": 2375, "metric_value": 1.4529, "depth": 4}
            if obj[0] == 'Greater_6.5':
               # {"feature": "Due_A_VS_B_Diff", "instances": 2136, "metric_value": 1.4474, "depth": 5}
               if obj[14] == 'Less_78.5':
                  return '2'
               elif obj[14] == 'Less_140.5':
                  return '2'
               elif obj[14] == 'Less_21.5':
                  return '0'
               elif obj[14] == 'Greater_140.5':
                  return '2'
               else:
                  return '2'
            elif obj[0] == 'Less_6.5':
               # {"feature": "STime_A_VS_B_Avg", "instances": 239, "metric_value": 1.255, "depth": 5}
               if obj[1] == '>':
                  return '0'
               elif obj[1] == '<':
                  return '0'
               elif obj[1] == '=':
                  return '0'
               else:
                  return '2'
            else:
               return '2'
         elif obj[2] == 'Less_-13.000000000000004':
            # {"feature": "STime_A_VS_B_Max", "instances": 386, "metric_value": 1.1806, "depth": 4}
            if obj[5] == '<':
               # {"feature": "STime_A_VS_B_Min", "instances": 367, "metric_value": 1.1987, "depth": 5}
               if obj[3] == '<':
                  return '0'
               elif obj[3] == '=':
                  return '0'
               elif obj[3] == '>':
                  return '2'
               else:
                  return '2'
            elif obj[5] == '>':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 16, "metric_value": 0.3373, "depth": 5}
               if obj[8] == 'Less_-3.333333333333332':
                  return '0'
               elif obj[8] == 'Greater_-3.333333333333332':
                  return '0'
               else:
                  return '2'
            elif obj[5] == '=':
               # {"feature": "STime_A_VS_B_Min", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[3] == '<':
                  return '0'
               elif obj[3] == '>':
                  return '1'
               else:
                  return '1'
            else:
               return '2'
         else:
            return '2'
      elif obj[4] == 'Less_26.5':
         # {"feature": "NumWaitingJob", "instances": 295, "metric_value": 1.2034, "depth": 3}
         if obj[0] == 'Greater_6.5':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 225, "metric_value": 1.0021, "depth": 4}
            if obj[2] == 'Greater_-13.000000000000004':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 221, "metric_value": 1.0133, "depth": 5}
               if obj[6] == 'Less_59.5':
                  return '2'
               elif obj[6] == 'Less_-18.5':
                  return '2'
               elif obj[6] == 'Greater_59.5':
                  return '2'
               else:
                  return '2'
            elif obj[2] == 'Less_-13.000000000000004':
               return '2'
            else:
               return '2'
         elif obj[0] == 'Less_6.5':
            # {"feature": "STime_A_VS_B_Max_Diff", "instances": 70, "metric_value": 1.4867, "depth": 4}
            if obj[6] == 'Less_59.5':
               # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 58, "metric_value": 1.5087, "depth": 5}
               if obj[10] == 'Less_18.5':
                  return '2'
               elif obj[10] == 'Greater_18.5':
                  return '2'
               else:
                  return '2'
            elif obj[6] == 'Less_-18.5':
               # {"feature": "PTime_A_VS_B_Min", "instances": 11, "metric_value": 1.0958, "depth": 5}
               if obj[9] == '>':
                  return '0'
               elif obj[9] == '<':
                  return '2'
               else:
                  return '2'
            elif obj[6] == 'Greater_59.5':
               return '0'
            else:
               return '2'
         else:
            return '2'
      elif obj[4] == 'Greater_26.5':
         # {"feature": "NumWaitingJob", "instances": 250, "metric_value": 0.4221, "depth": 3}
         if obj[0] == 'Greater_6.5':
            # {"feature": "Due_A_VS_B_Diff", "instances": 205, "metric_value": 0.3801, "depth": 4}
            if obj[14] == 'Less_78.5':
               # {"feature": "PTime_A_VS_B_Max", "instances": 88, "metric_value": 0.3557, "depth": 5}
               if obj[11] == '>':
                  return '2'
               elif obj[11] == '<':
                  return '2'
               elif obj[11] == '=':
                  return '2'
               else:
                  return '2'
            elif obj[14] == 'Less_140.5':
               # {"feature": "PTime_A_VS_B_Max", "instances": 61, "metric_value": 0.1207, "depth": 5}
               if obj[11] == '>':
                  return '2'
               elif obj[11] == '<':
                  return '2'
               elif obj[11] == '=':
                  return '2'
               else:
                  return '2'
            elif obj[14] == 'Less_21.5':
               # {"feature": "STime_A_VS_B_Max", "instances": 39, "metric_value": 0.7194, "depth": 5}
               if obj[5] == '>':
                  return '2'
               elif obj[5] == '<':
                  return '2'
               else:
                  return '2'
            elif obj[14] == 'Greater_140.5':
               return '2'
            else:
               return '2'
         elif obj[0] == 'Less_6.5':
            # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 45, "metric_value": 0.5033, "depth": 4}
            if obj[12] == 'Greater_0.5':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 29, "metric_value": 0.5788, "depth": 5}
               if obj[7] == '>':
                  return '2'
               elif obj[7] == '<':
                  return '2'
               else:
                  return '2'
            elif obj[12] == 'Less_0.5':
               return '2'
            elif obj[12] == 'Less_-19.5':
               return '1'
            else:
               return '2'
         else:
            return '2'
      elif obj[4] == 'Less_-39.5':
         return '0'
      else:
         return '2'
   elif obj[13] == '=':
      # {"feature": "STime_A_VS_B_Min_Diff", "instances": 60, "metric_value": 1.3727, "depth": 2}
      if obj[4] == 'Less_13.5':
         # {"feature": "NumWaitingJob", "instances": 52, "metric_value": 1.2737, "depth": 3}
         if obj[0] == 'Greater_6.5':
            # {"feature": "STime_A_VS_B_Min", "instances": 43, "metric_value": 1.2534, "depth": 4}
            if obj[3] == '=':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 36, "metric_value": 1.3297, "depth": 5}
               if obj[8] == 'Greater_-3.333333333333332':
                  return '0'
               elif obj[8] == 'Less_-3.333333333333332':
                  return '2'
               else:
                  return '2'
            elif obj[3] == '<':
               return '0'
            elif obj[3] == '>':
               return '2'
            else:
               return '2'
         elif obj[0] == 'Less_6.5':
            # {"feature": "STime_A_VS_B_Avg", "instances": 9, "metric_value": 0.9183, "depth": 4}
            if obj[1] == '<':
               return '0'
            elif obj[1] == '>':
               # {"feature": "STime_A_VS_B_Min", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[3] == '>':
                  return '1'
               elif obj[3] == '<':
                  return '1'
               elif obj[3] == '=':
                  return '0'
               else:
                  return '1'
            else:
               return '1'
         else:
            return '2'
      elif obj[4] == 'Less_26.5':
         # {"feature": "PTime_A_VS_B_Min", "instances": 5, "metric_value": 0.7219, "depth": 3}
         if obj[9] == '>':
            # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 3, "metric_value": 0.9183, "depth": 4}
            if obj[10] == 'Less_18.5':
               # {"feature": "NumWaitingJob", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[0] == 'Greater_6.5':
                  return '2'
               else:
                  return '2'
            elif obj[10] == 'Greater_18.5':
               return '2'
            else:
               return '2'
         elif obj[9] == '<':
            return '2'
         else:
            return '2'
      elif obj[4] == 'Greater_26.5':
         return '2'
      elif obj[4] == 'Less_-39.5':
         return '0'
>>>>>>> f65158b (feat: local search)
      else:
         return '2'
   else:
      return '2'
