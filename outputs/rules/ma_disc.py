def findDecision(obj): #obj[0]: STime_A_VS_B_Diff, obj[1]: PTime_A_VS_B_Diff, obj[2]: CompTime_A_VS_B_Diff, obj[3]: Tardy_A_VS_B_Diff
   # {"feature": "STime_A_VS_B_Diff", "instances": 680, "metric_value": 1.6486, "depth": 1}
   if obj[0] == 'Less_39.5':
      # {"feature": "PTime_A_VS_B_Diff", "instances": 533, "metric_value": 1.577, "depth": 2}
      if obj[1] == 'Less_16.5':
         # {"feature": "Tardy_A_VS_B_Diff", "instances": 222, "metric_value": 1.6243, "depth": 3}
         if obj[3] == 'Greater_-29.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 197, "metric_value": 1.6529, "depth": 4}
            if obj[2] == 'Greater_-2.5':
               return '0'
            elif obj[2] == 'Less_-31.5':
               return '0'
            elif obj[2] == 'Less_-2.5':
               return '0'
            else:
               return '0'
         elif obj[3] == 'Less_-29.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 19, "metric_value": 0.953, "depth": 4}
            if obj[2] == 'Less_-31.5':
               return '0'
            elif obj[2] == 'Less_-2.5':
               return '0'
            else:
               return '0'
         elif obj[3] == 'Less_-74.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 6, "metric_value": 0.9183, "depth": 4}
            if obj[2] == 'Less_-31.5':
               return '0'
            else:
               return '0'
         else:
            return '0'
      elif obj[1] == 'Less_-7.5':
         # {"feature": "CompTime_A_VS_B_Diff", "instances": 189, "metric_value": 1.2215, "depth": 3}
         if obj[2] == 'Less_-31.5':
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 79, "metric_value": 1.3894, "depth": 4}
            if obj[3] == 'Greater_-29.5':
               return '0'
            elif obj[3] == 'Less_-29.5':
               return '0'
            elif obj[3] == 'Less_-74.5':
               return '0'
            elif obj[3] == 'Less_-68.5':
               return '0'
            else:
               return '0'
         elif obj[2] == 'Less_-2.5':
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 77, "metric_value": 0.9684, "depth": 4}
            if obj[3] == 'Greater_-29.5':
               return '0'
            else:
               return '0'
         elif obj[2] == 'Greater_-2.5':
            # {"feature": "Tardy_A_VS_B_Diff", "instances": 33, "metric_value": 1.2496, "depth": 4}
            if obj[3] == 'Greater_-29.5':
               return '0'
            else:
               return '0'
         else:
            return '0'
      elif obj[1] == 'Greater_16.5':
         # {"feature": "Tardy_A_VS_B_Diff", "instances": 81, "metric_value": 1.8029, "depth": 3}
         if obj[3] == 'Greater_-29.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 75, "metric_value": 1.799, "depth": 4}
            if obj[2] == 'Greater_-2.5':
               return '5'
            elif obj[2] == 'Less_-2.5':
               return '5'
            elif obj[2] == 'Less_-31.5':
               return '8'
            else:
               return '5'
         elif obj[3] == 'Less_-29.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 4, "metric_value": 0.8113, "depth": 4}
            if obj[2] == 'Less_-31.5':
               return '0'
            elif obj[2] == 'Less_-2.5':
               return '0'
            else:
               return '0'
         elif obj[3] == 'Less_-74.5':
            return '0'
         else:
            return '5'
      elif obj[1] == 'Less_-1.5':
         # {"feature": "Tardy_A_VS_B_Diff", "instances": 41, "metric_value": 1.1409, "depth": 3}
         if obj[3] == 'Greater_-29.5':
            # {"feature": "CompTime_A_VS_B_Diff", "instances": 36, "metric_value": 1.2244, "depth": 4}
            if obj[2] == 'Greater_-2.5':
               return '0'
            elif obj[2] == 'Less_-2.5':
               return '0'
            elif obj[2] == 'Less_-31.5':
               return '0'
            else:
               return '0'
         elif obj[3] == 'Less_-29.5':
            return '0'
         elif obj[3] == 'Less_-74.5':
            return '0'
         else:
            return '0'
      else:
         return '0'
   elif obj[0] == 'Greater_39.5':
      # {"feature": "Tardy_A_VS_B_Diff", "instances": 99, "metric_value": 1.6891, "depth": 2}
      if obj[3] == 'Greater_-29.5':
         # {"feature": "CompTime_A_VS_B_Diff", "instances": 98, "metric_value": 1.6747, "depth": 3}
         if obj[2] == 'Greater_-2.5':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 92, "metric_value": 1.6915, "depth": 4}
            if obj[1] == 'Less_16.5':
               return '5'
            elif obj[1] == 'Less_-7.5':
               return '5'
            elif obj[1] == 'Less_-1.5':
               return '5'
            elif obj[1] == 'Greater_16.5':
               return '5'
            else:
               return '5'
         elif obj[2] == 'Less_-2.5':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 5, "metric_value": 0.7219, "depth": 4}
            if obj[1] == 'Less_-7.5':
               return '5'
            elif obj[1] == 'Less_16.5':
               return '8'
            else:
               return '5'
         elif obj[2] == 'Less_-31.5':
            return '8'
         else:
            return '5'
      elif obj[3] == 'Less_-29.5':
         return '2'
      else:
         return '5'
   elif obj[0] == 'Less_-58.5':
      # {"feature": "Tardy_A_VS_B_Diff", "instances": 48, "metric_value": 0.5573, "depth": 2}
      if obj[3] == 'Greater_-29.5':
         # {"feature": "CompTime_A_VS_B_Diff", "instances": 27, "metric_value": 0.825, "depth": 3}
         if obj[2] == 'Less_-31.5':
            # {"feature": "PTime_A_VS_B_Diff", "instances": 19, "metric_value": 1.0215, "depth": 4}
            if obj[1] == 'Less_16.5':
               return '0'
            elif obj[1] == 'Less_-7.5':
               return '0'
            elif obj[1] == 'Less_-1.5':
               return '0'
            elif obj[1] == 'Greater_16.5':
               return '2'
            else:
               return '0'
         elif obj[2] == 'Less_-2.5':
            return '0'
         elif obj[2] == 'Greater_-2.5':
            return '0'
         else:
            return '0'
      elif obj[3] == 'Less_-29.5':
         return '0'
      elif obj[3] == 'Less_-74.5':
         return '0'
      elif obj[3] == 'Less_-68.5':
         return '0'
      else:
         return '0'
   else:
      return '0'
