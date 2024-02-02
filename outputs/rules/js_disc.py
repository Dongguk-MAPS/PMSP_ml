def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B_Avg, obj[2]: STime_A_VS_B_Avg_Diff, obj[3]: STime_A_VS_B_Min, obj[4]: STime_A_VS_B_Min_Diff, obj[5]: STime_A_VS_B_Max, obj[6]: STime_A_VS_B_Max_Diff, obj[7]: PTime_A_VS_B_Avg, obj[8]: PTime_A_VS_B_Avg_Diff, obj[9]: PTime_A_VS_B_Min, obj[10]: PTime_A_VS_B_Min_Diff, obj[11]: PTime_A_VS_B_Max, obj[12]: PTime_A_VS_B_Max_Diff, obj[13]: Due_A_VS_B, obj[14]: Due_A_VS_B_Diff
   # {"feature": "Due_A_VS_B", "instances": 6736, "metric_value": 1.4261, "depth": 1}
   if obj[13] == '<':
      # {"feature": "STime_A_VS_B_Min", "instances": 3338, "metric_value": 0.9049, "depth": 2}
      if obj[3] == '=':
         # {"feature": "Due_A_VS_B_Diff", "instances": 1616, "metric_value": 0.8415, "depth": 3}
         if obj[14] == 'Less_-46.5':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 885, "metric_value": 0.5109, "depth": 4}
            if obj[2] == 'Less_42.49999999999999':
               # {"feature": "NumWaitingJob", "instances": 651, "metric_value": 0.5873, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '0'
               elif obj[0] == 'Greater_19.5':
                  return '0'
               else:
                  return '3'
            elif obj[2] == 'Less_-8.999999999999996':
               # {"feature": "NumWaitingJob", "instances": 234, "metric_value": 0.2373, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '0'
               elif obj[0] == 'Less_4.5':
                  return '0'
               else:
                  return '3'
            else:
               return '3'
         elif obj[14] == 'Less_61.5':
            # {"feature": "STime_A_VS_B_Avg", "instances": 439, "metric_value": 1.2544, "depth": 4}
            if obj[1] == '<':
               # {"feature": "PTime_A_VS_B_Min", "instances": 167, "metric_value": 0.7773, "depth": 5}
               if obj[9] == '<':
                  return '0'
               elif obj[9] == '>':
                  return '0'
               elif obj[9] == '=':
                  return '0'
               else:
                  return '4'
            elif obj[1] == '>':
               # {"feature": "NumWaitingJob", "instances": 151, "metric_value": 1.3835, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '0'
               elif obj[0] == 'Less_4.5':
                  return '0'
               else:
                  return '3'
            elif obj[1] == '=':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 121, "metric_value": 1.372, "depth": 5}
               if obj[6] == 'Less_15.5':
                  return '0'
               elif obj[6] == 'Greater_15.5':
                  return '3'
               else:
                  return '4'
            else:
               return '4'
         elif obj[14] == 'Less_-26.5':
            # {"feature": "NumWaitingJob", "instances": 292, "metric_value": 0.9094, "depth": 4}
            if obj[0] == 'Less_19.5':
               # {"feature": "STime_A_VS_B_Avg", "instances": 280, "metric_value": 0.8833, "depth": 5}
               if obj[1] == '<':
                  return '0'
               elif obj[1] == '>':
                  return '0'
               elif obj[1] == '=':
                  return '0'
               else:
                  return '3'
            elif obj[0] == 'Greater_19.5':
               # {"feature": "PTime_A_VS_B_Min_Diff", "instances": 8, "metric_value": 1.2988, "depth": 5}
               if obj[10] == 'Greater_-5.5':
                  return '0'
               elif obj[10] == 'Less_-5.5':
                  return '3'
               else:
                  return '3'
            elif obj[0] == 'Less_4.5':
               # {"feature": "STime_A_VS_B_Avg", "instances": 4, "metric_value": 1.0, "depth": 5}
               if obj[1] == '<':
                  return '0'
               elif obj[1] == '>':
                  return '3'
               else:
                  return '3'
            else:
               return '3'
         else:
            return '4'
      elif obj[3] == '<':
         # {"feature": "STime_A_VS_B_Min_Diff", "instances": 1132, "metric_value": 0.4716, "depth": 3}
         if obj[4] == 'Less_-12.5':
            # {"feature": "STime_A_VS_B_Max_Diff", "instances": 573, "metric_value": 0.2555, "depth": 4}
            if obj[6] == 'Less_15.5':
               # {"feature": "Due_A_VS_B_Diff", "instances": 505, "metric_value": 0.2296, "depth": 5}
               if obj[14] == 'Less_-46.5':
                  return '0'
               elif obj[14] == 'Less_61.5':
                  return '0'
               elif obj[14] == 'Less_-26.5':
                  return '0'
               else:
                  return '4'
            elif obj[6] == 'Greater_15.5':
               # {"feature": "Due_A_VS_B_Diff", "instances": 57, "metric_value": 0.4235, "depth": 5}
               if obj[14] == 'Less_-46.5':
                  return '0'
               elif obj[14] == 'Less_61.5':
                  return '0'
               elif obj[14] == 'Less_-26.5':
                  return '0'
               else:
                  return '3'
            elif obj[6] == 'Less_-61.5':
               return '0'
            else:
               return '4'
         elif obj[4] == 'Less_-3.5':
            # {"feature": "PTime_A_VS_B_Max", "instances": 372, "metric_value": 0.5636, "depth": 4}
            if obj[11] == '>':
               # {"feature": "NumWaitingJob", "instances": 178, "metric_value": 0.6279, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '0'
               elif obj[0] == 'Less_4.5':
                  return '0'
               else:
                  return '4'
            elif obj[11] == '<':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 173, "metric_value": 0.3953, "depth": 5}
               if obj[7] == '<':
                  return '0'
               elif obj[7] == '>':
                  return '0'
               elif obj[7] == '=':
                  return '0'
               else:
                  return '3'
            elif obj[11] == '=':
               # {"feature": "NumWaitingJob", "instances": 21, "metric_value": 1.0488, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '0'
               elif obj[0] == 'Less_4.5':
                  return '3'
               else:
                  return '3'
            else:
               return '4'
         elif obj[4] == 'Less_43.5':
            # {"feature": "STime_A_VS_B_Avg", "instances": 187, "metric_value": 0.7874, "depth": 4}
            if obj[1] == '<':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 107, "metric_value": 0.7565, "depth": 5}
               if obj[6] == 'Less_15.5':
                  return '0'
               elif obj[6] == 'Less_-61.5':
                  return '0'
               elif obj[6] == 'Greater_15.5':
                  return '0'
               else:
                  return '3'
            elif obj[1] == '>':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 78, "metric_value": 0.7442, "depth": 5}
               if obj[8] == 'Less_9.66666666666667':
                  return '0'
               elif obj[8] == 'Less_-3.1666666666666643':
                  return '0'
               elif obj[8] == 'Greater_9.66666666666667':
                  return '0'
               elif obj[8] == 'Less_-11.166666666666664':
                  return '3'
               else:
                  return '3'
            elif obj[1] == '=':
               # {"feature": "STime_A_VS_B_Max", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[5] == '=':
                  return '3'
               elif obj[5] == '>':
                  return '2'
               else:
                  return '3'
            else:
               return '3'
         else:
            return '4'
      elif obj[3] == '>':
         # {"feature": "STime_A_VS_B_Min_Diff", "instances": 590, "metric_value": 1.4607, "depth": 3}
         if obj[4] == 'Less_43.5':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 567, "metric_value": 1.4248, "depth": 4}
            if obj[2] == 'Less_42.49999999999999':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 491, "metric_value": 1.4878, "depth": 5}
               if obj[8] == 'Less_9.66666666666667':
                  return '0'
               elif obj[8] == 'Less_-3.1666666666666643':
                  return '0'
               elif obj[8] == 'Greater_9.66666666666667':
                  return '0'
               elif obj[8] == 'Less_-11.166666666666664':
                  return '0'
               else:
                  return '4'
            elif obj[2] == 'Less_-8.999999999999996':
               # {"feature": "NumWaitingJob", "instances": 72, "metric_value": 0.6391, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '0'
               elif obj[0] == 'Less_4.5':
                  return '0'
               else:
                  return '3'
            elif obj[2] == 'Greater_42.49999999999999':
               return '3'
            else:
               return '4'
         elif obj[4] == 'Greater_43.5':
            # {"feature": "PTime_A_VS_B_Max", "instances": 23, "metric_value": 0.7554, "depth": 4}
            if obj[11] == '>':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 15, "metric_value": 0.5665, "depth": 5}
               if obj[7] == '>':
                  return '3'
               elif obj[7] == '<':
                  return '4'
               else:
                  return '4'
            elif obj[11] == '<':
               # {"feature": "NumWaitingJob", "instances": 7, "metric_value": 0.8631, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '3'
               elif obj[0] == 'Less_4.5':
                  return '3'
               else:
                  return '4'
            elif obj[11] == '=':
               return '4'
            else:
               return '4'
         else:
            return '4'
      else:
         return '4'
   elif obj[13] == '>':
      # {"feature": "STime_A_VS_B_Min_Diff", "instances": 3338, "metric_value": 1.6272, "depth": 2}
      if obj[4] == 'Less_43.5':
         # {"feature": "Due_A_VS_B_Diff", "instances": 2801, "metric_value": 1.6319, "depth": 3}
         if obj[14] == 'Less_61.5':
            # {"feature": "STime_A_VS_B_Avg", "instances": 1570, "metric_value": 1.556, "depth": 4}
            if obj[1] == '>':
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 832, "metric_value": 1.5213, "depth": 5}
               if obj[2] == 'Less_42.49999999999999':
                  return '3'
               elif obj[2] == 'Greater_42.49999999999999':
                  return '3'
               else:
                  return '4'
            elif obj[1] == '<':
               # {"feature": "STime_A_VS_B_Max", "instances": 479, "metric_value": 1.3962, "depth": 5}
               if obj[5] == '<':
                  return '0'
               elif obj[5] == '>':
                  return '0'
               elif obj[5] == '=':
                  return '0'
               else:
                  return '4'
            elif obj[1] == '=':
               # {"feature": "STime_A_VS_B_Max", "instances": 259, "metric_value": 1.6091, "depth": 5}
               if obj[5] == '=':
                  return '0'
               elif obj[5] == '<':
                  return '0'
               elif obj[5] == '>':
                  return '2'
               else:
                  return '3'
            else:
               return '4'
         elif obj[14] == 'Greater_61.5':
            # {"feature": "NumWaitingJob", "instances": 1231, "metric_value": 1.5662, "depth": 4}
            if obj[0] == 'Less_19.5':
               # {"feature": "STime_A_VS_B_Avg", "instances": 1164, "metric_value": 1.5679, "depth": 5}
               if obj[1] == '>':
                  return '3'
               elif obj[1] == '<':
                  return '3'
               elif obj[1] == '=':
                  return '3'
               else:
                  return '4'
            elif obj[0] == 'Greater_19.5':
               # {"feature": "PTime_A_VS_B_Min", "instances": 41, "metric_value": 0.9933, "depth": 5}
               if obj[9] == '>':
                  return '3'
               elif obj[9] == '<':
                  return '3'
               elif obj[9] == '=':
                  return '3'
               else:
                  return '4'
            elif obj[0] == 'Less_4.5':
               # {"feature": "STime_A_VS_B_Min", "instances": 26, "metric_value": 1.1416, "depth": 5}
               if obj[3] == '>':
                  return '3'
               elif obj[3] == '<':
                  return '2'
               elif obj[3] == '=':
                  return '0'
               else:
                  return '3'
            else:
               return '4'
         else:
            return '4'
      elif obj[4] == 'Less_-12.5':
         # {"feature": "NumWaitingJob", "instances": 230, "metric_value": 0.5824, "depth": 3}
         if obj[0] == 'Less_19.5':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 204, "metric_value": 0.6341, "depth": 4}
            if obj[2] == 'Less_-8.999999999999996':
               # {"feature": "PTime_A_VS_B_Max", "instances": 125, "metric_value": 0.395, "depth": 5}
               if obj[11] == '<':
                  return '0'
               elif obj[11] == '>':
                  return '0'
               elif obj[11] == '=':
                  return '0'
               else:
                  return '3'
            elif obj[2] == 'Less_42.49999999999999':
               # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 79, "metric_value": 0.9207, "depth": 5}
               if obj[8] == 'Less_9.66666666666667':
                  return '0'
               elif obj[8] == 'Less_-3.1666666666666643':
                  return '0'
               elif obj[8] == 'Greater_9.66666666666667':
                  return '0'
               elif obj[8] == 'Less_-11.166666666666664':
                  return '3'
               else:
                  return '3'
            else:
               return '3'
         elif obj[0] == 'Less_4.5':
            return '0'
         else:
            return '3'
      elif obj[4] == 'Less_-3.5':
         # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 223, "metric_value": 1.2486, "depth": 3}
         if obj[8] == 'Less_9.66666666666667':
            # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 136, "metric_value": 1.3577, "depth": 4}
            if obj[12] == 'Less_4.5':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 94, "metric_value": 1.2599, "depth": 5}
               if obj[6] == 'Less_15.5':
                  return '0'
               elif obj[6] == 'Greater_15.5':
                  return '3'
               elif obj[6] == 'Less_-61.5':
                  return '3'
               else:
                  return '4'
            elif obj[12] == 'Less_14.5':
               # {"feature": "NumWaitingJob", "instances": 40, "metric_value": 1.4793, "depth": 5}
               if obj[0] == 'Less_19.5':
                  return '0'
               elif obj[0] == 'Less_4.5':
                  return '0'
               else:
                  return '4'
            elif obj[12] == 'Less_20.5':
               return '0'
            else:
               return '4'
         elif obj[8] == 'Less_-3.1666666666666643':
            # {"feature": "PTime_A_VS_B_Max", "instances": 60, "metric_value": 0.9552, "depth": 4}
            if obj[11] == '<':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 48, "metric_value": 0.7906, "depth": 5}
               if obj[6] == 'Less_15.5':
                  return '0'
               elif obj[6] == 'Greater_15.5':
                  return '0'
               else:
                  return '4'
            elif obj[11] == '>':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 10, "metric_value": 1.361, "depth": 5}
               if obj[6] == 'Less_15.5':
                  return '0'
               elif obj[6] == 'Greater_15.5':
                  return '2'
               else:
                  return '3'
            elif obj[11] == '=':
               return '0'
            else:
               return '4'
         elif obj[8] == 'Greater_9.66666666666667':
            # {"feature": "NumWaitingJob", "instances": 17, "metric_value": 1.1661, "depth": 4}
            if obj[0] == 'Less_19.5':
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 14, "metric_value": 1.0949, "depth": 5}
               if obj[12] == 'Less_14.5':
                  return '0'
               elif obj[12] == 'Less_4.5':
                  return '0'
               elif obj[12] == 'Less_20.5':
                  return '3'
               else:
                  return '3'
            elif obj[0] == 'Less_4.5':
               # {"feature": "STime_A_VS_B_Avg", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1] == '>':
                  return '3'
               elif obj[1] == '<':
                  return '0'
               else:
                  return '3'
            else:
               return '3'
         elif obj[8] == 'Less_-11.166666666666664':
            # {"feature": "Due_A_VS_B_Diff", "instances": 10, "metric_value": 0.469, "depth": 4}
            if obj[14] == 'Less_61.5':
               return '0'
            elif obj[14] == 'Greater_61.5':
               # {"feature": "NumWaitingJob", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[0] == 'Less_4.5':
                  return '0'
               elif obj[0] == 'Less_19.5':
                  return '4'
               else:
                  return '4'
            else:
               return '4'
         else:
            return '4'
      elif obj[4] == 'Greater_43.5':
         # {"feature": "PTime_A_VS_B_Min", "instances": 84, "metric_value": 0.9924, "depth": 3}
         if obj[9] == '>':
            # {"feature": "NumWaitingJob", "instances": 53, "metric_value": 0.7717, "depth": 4}
            if obj[0] == 'Less_19.5':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 46, "metric_value": 0.8281, "depth": 5}
               if obj[7] == '>':
                  return '3'
               elif obj[7] == '<':
                  return '3'
               elif obj[7] == '=':
                  return '3'
               else:
                  return '4'
            elif obj[0] == 'Less_4.5':
               return '3'
            else:
               return '4'
         elif obj[9] == '<':
            # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 24, "metric_value": 0.995, "depth": 4}
            if obj[12] == 'Less_4.5':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 21, "metric_value": 0.9587, "depth": 5}
               if obj[7] == '<':
                  return '3'
               elif obj[7] == '>':
                  return '3'
               else:
                  return '4'
            elif obj[12] == 'Less_14.5':
               return '4'
            else:
               return '4'
         elif obj[9] == '=':
            # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 7, "metric_value": 1.3788, "depth": 4}
            if obj[8] == 'Less_9.66666666666667':
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 5, "metric_value": 0.7219, "depth": 5}
               if obj[2] == 'Less_42.49999999999999':
                  return '4'
               elif obj[2] == 'Greater_42.49999999999999':
                  return '4'
               else:
                  return '4'
            elif obj[8] == 'Less_-3.1666666666666643':
               # {"feature": "PTime_A_VS_B_Max", "instances": 2, "metric_value": 1.0, "depth": 5}
               if obj[11] == '<':
                  return '2'
               elif obj[11] == '=':
                  return '3'
               else:
                  return '3'
            else:
               return '4'
         else:
            return '4'
      else:
         return '4'
   elif obj[13] == '=':
      # {"feature": "STime_A_VS_B_Min_Diff", "instances": 60, "metric_value": 1.3363, "depth": 2}
      if obj[4] == 'Less_43.5':
         # {"feature": "STime_A_VS_B_Min", "instances": 50, "metric_value": 1.4277, "depth": 3}
         if obj[3] == '=':
            # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 38, "metric_value": 1.2959, "depth": 4}
            if obj[8] == 'Less_9.66666666666667':
               # {"feature": "PTime_A_VS_B_Avg", "instances": 22, "metric_value": 1.2159, "depth": 5}
               if obj[7] == '>':
                  return '0'
               elif obj[7] == '<':
                  return '0'
               else:
                  return '3'
            elif obj[8] == 'Less_-3.1666666666666643':
               # {"feature": "STime_A_VS_B_Avg", "instances": 10, "metric_value": 0.971, "depth": 5}
               if obj[1] == '>':
                  return '3'
               elif obj[1] == '<':
                  return '0'
               elif obj[1] == '=':
                  return '3'
               else:
                  return '3'
            elif obj[8] == 'Greater_9.66666666666667':
               return '0'
            elif obj[8] == 'Less_-11.166666666666664':
               # {"feature": "STime_A_VS_B_Avg", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[1] == '<':
                  return '2'
               elif obj[1] == '>':
                  return '3'
               else:
                  return '3'
            else:
               return '3'
         elif obj[3] == '>':
            # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 11, "metric_value": 1.0958, "depth": 4}
            if obj[2] == 'Less_42.49999999999999':
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 10, "metric_value": 0.7219, "depth": 5}
               if obj[12] == 'Less_14.5':
                  return '3'
               elif obj[12] == 'Less_4.5':
                  return '3'
               elif obj[12] == 'Greater_20.5':
                  return '2'
               else:
                  return '3'
            elif obj[2] == 'Less_-8.999999999999996':
               return '0'
            else:
               return '3'
         elif obj[3] == '<':
            return '3'
         else:
            return '3'
      elif obj[4] == 'Less_-12.5':
         return '0'
      elif obj[4] == 'Less_-3.5':
         return '0'
      else:
         return '3'
   else:
      return '4'
