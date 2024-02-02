def findDecision(obj): #obj[0]: NumWaitingJob, obj[1]: STime_A_VS_B_Avg, obj[2]: STime_A_VS_B_Avg_Diff, obj[3]: STime_A_VS_B_Min, obj[4]: STime_A_VS_B_Min_Diff, obj[5]: STime_A_VS_B_Max, obj[6]: STime_A_VS_B_Max_Diff, obj[7]: PTime_A_VS_B_Avg, obj[8]: PTime_A_VS_B_Avg_Diff, obj[9]: PTime_A_VS_B_Min, obj[10]: PTime_A_VS_B_Min_Diff, obj[11]: PTime_A_VS_B_Max, obj[12]: PTime_A_VS_B_Max_Diff, obj[13]: Due_A_VS_B, obj[14]: Due_A_VS_B_Diff
   # {"feature": "Due_A_VS_B", "instances": 6736, "metric_value": 6.9587, "depth": 1}
   if obj[13] == '<':
      # {"feature": "STime_A_VS_B_Min", "instances": 3338, "metric_value": 5.0814, "depth": 2}
      if obj[3] == '=':
         # {"feature": "STime_A_VS_B_Avg", "instances": 1616, "metric_value": 2.3622, "depth": 3}
         if obj[1] == '<':
            # {"feature": "PTime_A_VS_B_Max", "instances": 682, "metric_value": 0.6149, "depth": 4}
            if obj[11] == '<':
               # {"feature": "PTime_A_VS_B_Min", "instances": 354, "metric_value": 0.479, "depth": 5}
               if obj[9] == '<':
                  # {"feature": "STime_A_VS_B_Max", "instances": 193, "metric_value": 1.1317, "depth": 6}
                  if obj[5] == '<':
                     # {"feature": "PTime_A_VS_B_Avg", "instances": 175, "metric_value": 0.2146, "depth": 7}
                     if obj[7] == '<':
                        # {"feature": "NumWaitingJob", "instances": 172, "metric_value": 0.2289, "depth": 8}
                        if obj[0]<=Less_14.5:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 93, "metric_value": 0.0, "depth": 9}
                           if obj[2]<=Greater_-37.0:
                              # {"feature": "STime_A_VS_B_Min_Diff", "instances": 93, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=Less_6.5:
                                 return 4.053763440860215
                              else:
                                 return 4.053763440860215
                           else:
                              return 4.053763440860215
                        elif obj[0]>Less_14.5:
                           # {"feature": "STime_A_VS_B_Avg_Diff", "instances": 79, "metric_value": 0.0, "depth": 9}
                           if obj[2]<=Greater_-37.0:
                              # {"feature": "STime_A_VS_B_Min_Diff", "instances": 79, "metric_value": 0.0, "depth": 10}
                              if obj[4]<=Less_6.5:
                                 return 9.329113924050633
                              else:
                                 return 9.329113924050633
                           else:
                              return 9.329113924050633
