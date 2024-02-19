def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B_Avg_Diff, obj[2]: STime_A_VS_B_Min_Diff, obj[3]: STime_A_VS_B_Max_Diff, obj[4]: PTime_A_VS_B_Avg_Diff, obj[5]: PTime_A_VS_B_Max_Diff, obj[6]: Due_A_VS_B_Diff, obj[7]: MDD_A_VS_B_Diff, obj[8]: RT_A_VS_B_Diff, obj[9]: SLK_A_VS_B_Diff, obj[10]: CR_A_VS_B_Diff, obj[11]: COVERT_A_VS_B_Diff
   # {"feature": "MDD_A_VS_B_Diff", "instances": 528, "metric_value": 1.1752, "depth": 1}
   if obj[7] == 'Greater_-9.75':
      # {"feature": "Due_A_VS_B_Diff", "instances": 303, "metric_value": 1.2628, "depth": 2}
      if obj[6] == 'Greater_1.5':
         # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 246, "metric_value": 1.2161, "depth": 3}
         if obj[1] == 'Less_25.75':
            # {"feature": "COVERT_A_VS_B_Diff", "instances": 179, "metric_value": 1.1865, "depth": 4}
            if obj[11] == 'Less_0.00158856335326915':
               # {"feature": "CR_A_VS_B_Diff", "instances": 171, "metric_value": 1.1573, "depth": 5}
               if obj[10] == 'Less_1.3112105862955097':
                  return '2'
               elif obj[10] == 'Less_3.120032187002831':
                  return '2'
               elif obj[10] == 'Less_-0.08851263240576221':
                  return '2'
               elif obj[10] == 'Greater_3.120032187002831':
                  return '2'
               else:
                  return '2'
            elif obj[11] == 'Greater_0.00158856335326915':
               # {"feature": "CR_A_VS_B_Diff", "instances": 8, "metric_value": 1.0613, "depth": 5}
               if obj[10] == 'Less_1.3112105862955097':
                  return '0'
               elif obj[10] == 'Less_-0.08851263240576221':
                  return '0'
               else:
                  return '0'
            else:
               return '2'
         elif obj[1] == 'Greater_25.75':
            # {"feature": "NumWaitingJob", "instances": 45, "metric_value": 0.9201, "depth": 4}
            if obj[0] == 'Less_8.5':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 30, "metric_value": 0.3534, "depth": 5}
               if obj[3] == 'Less_55.5':
                  return '2'
               elif obj[3] == 'Greater_55.5':
                  return '2'
               else:
                  return '2'
            elif obj[0] == 'Less_4.5':
               # {"feature": "CR_A_VS_B_Diff", "instances": 12, "metric_value": 1.4591, "depth": 5}
               if obj[10] == 'Less_-0.08851263240576221':
                  return '1'
               elif obj[10] == 'Less_1.3112105862955097':
                  return '2'
               else:
                  return '2'
            elif obj[0] == 'Greater_8.5':
               # {"feature": "RT_A_VS_B_Diff", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[8] == 'Less_-0.5':
                  return '0'
               elif obj[8] == 'Less_47.25':
                  return '2'
               elif obj[8] == 'Less_72.0':
                  return '2'
               else:
                  return '2'
            else:
               return '2'
         elif obj[1] == 'Less_-19.25':
            # {"feature": "NumWaitingJob", "instances": 22, "metric_value": 1.5022, "depth": 4}
            if obj[0] == 'Less_8.5':
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 9, "metric_value": 1.5305, "depth": 5}
               if obj[5] == 'Greater_-8.5':
                  return '2'
               elif obj[5] == 'Less_-8.5':
                  return '0'
               else:
                  return '0'
            elif obj[0] == 'Less_4.5':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 8, "metric_value": 1.2988, "depth": 5}
               if obj[3] == 'Less_-40.5':
                  return '1'
               elif obj[3] == 'Less_-6.5':
                  return '0'
               elif obj[3] == 'Less_55.5':
                  return '0'
               else:
                  return '0'
            elif obj[0] == 'Greater_8.5':
               return '2'
            else:
               return '2'
         else:
            return '2'
      elif obj[6] == 'Less_1.5':
         # {"feature": "SLK_A_VS_B_Diff", "instances": 57, "metric_value": 1.0796, "depth": 3}
         if obj[9] == 'Greater_-59.0':
            # {"feature": "STime_A_VS_B_Min_Diff", "instances": 45, "metric_value": 0.8748, "depth": 4}
            if obj[2] == 'Greater_-8.5':
               # {"feature": "NumWaitingJob", "instances": 42, "metric_value": 0.9134, "depth": 5}
               if obj[0] == 'Less_8.5':
                  return '0'
               elif obj[0] == 'Less_4.5':
                  return '0'
               elif obj[0] == 'Greater_8.5':
                  return '0'
               else:
                  return '0'
            elif obj[2] == 'Less_-8.5':
               return '0'
            else:
               return '0'
         elif obj[9] == 'Less_-59.0':
            # {"feature": "STime_A_VS_B_Max_Diff", "instances": 12, "metric_value": 1.2807, "depth": 4}
            if obj[3] == 'Less_55.5':
               # {"feature": "NumWaitingJob", "instances": 8, "metric_value": 0.9544, "depth": 5}
               if obj[0] == 'Less_4.5':
                  return '2'
               elif obj[0] == 'Less_8.5':
                  return '2'
               else:
                  return '2'
            elif obj[3] == 'Greater_55.5':
               # {"feature": "NumWaitingJob", "instances": 3, "metric_value": 0.9183, "depth": 5}
               if obj[0] == 'Less_4.5':
                  return '2'
               elif obj[0] == 'Less_8.5':
                  return '2'
               else:
                  return '2'
            elif obj[3] == 'Less_-6.5':
               return '0'
            else:
               return '2'
         else:
            return '0'
      else:
         return '2'
   elif obj[7] == 'Less_-9.75':
      # {"feature": "Due_A_VS_B_Diff", "instances": 225, "metric_value": 0.3984, "depth": 2}
      if obj[6] == 'Less_1.5':
         # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 211, "metric_value": 0.3706, "depth": 3}
         if obj[5] == 'Greater_-8.5':
            # {"feature": "RT_A_VS_B_Diff", "instances": 184, "metric_value": 0.2661, "depth": 4}
            if obj[8] == 'Less_-0.5':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 163, "metric_value": 0.2275, "depth": 5}
               if obj[3] == 'Less_55.5':
                  return '0'
               elif obj[3] == 'Less_-6.5':
                  return '0'
               elif obj[3] == 'Less_-40.5':
                  return '0'
               elif obj[3] == 'Greater_55.5':
                  return '0'
               else:
                  return '0'
            elif obj[8] == 'Less_47.25':
               # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 21, "metric_value": 0.4537, "depth": 5}
               if obj[1] == 'Less_-19.25':
                  return '0'
               elif obj[1] == 'Less_25.75':
                  return '2'
               else:
                  return '0'
            else:
               return '0'
         elif obj[5] == 'Less_-8.5':
            # {"feature": "CR_A_VS_B_Diff", "instances": 27, "metric_value": 0.8711, "depth": 4}
            if obj[10] == 'Less_-0.08851263240576221':
               # {"feature": "SLK_A_VS_B_Diff", "instances": 20, "metric_value": 0.469, "depth": 5}
               if obj[9] == 'Less_-59.0':
                  return '0'
               elif obj[9] == 'Greater_-59.0':
                  return '0'
               else:
                  return '0'
            elif obj[10] == 'Less_1.3112105862955097':
               # {"feature": "STime_A_VS_B_Max_Diff", "instances": 6, "metric_value": 1.4591, "depth": 5}
               if obj[3] == 'Less_55.5':
                  return '2'
               elif obj[3] == 'Less_-40.5':
                  return '0'
               elif obj[3] == 'Less_-6.5':
                  return '0'
               else:
                  return '0'
            elif obj[10] == 'Less_3.120032187002831':
               return '0'
            else:
               return '0'
         else:
            return '0'
      elif obj[6] == 'Greater_1.5':
         # {"feature": "PTime_A_VS_B_Avg_Diff", "instances": 14, "metric_value": 0.5917, "depth": 3}
         if obj[4] == 'Less_6.75':
            # {"feature": "STime_A_VS_B_Max_Diff", "instances": 12, "metric_value": 0.4138, "depth": 4}
            if obj[3] == 'Less_-6.5':
               return '0'
            elif obj[3] == 'Less_55.5':
               # {"feature": "PTime_A_VS_B_Max_Diff", "instances": 4, "metric_value": 0.8113, "depth": 5}
               if obj[5] == 'Less_-8.5':
                  return '0'
               elif obj[5] == 'Greater_-8.5':
                  return '0'
               else:
                  return '0'
            elif obj[3] == 'Less_-40.5':
               return '0'
            else:
               return '0'
         elif obj[4] == 'Greater_6.75':
            # {"feature": "STime_A_VS_B_Min_Diff", "instances": 2, "metric_value": 1.0, "depth": 4}
            if obj[2] == 'Greater_-8.5':
               return '0'
            elif obj[2] == 'Less_-8.5':
               return '1'
            else:
               return '0'
         else:
            return '0'
      else:
         return '0'
   else:
      return '0'
