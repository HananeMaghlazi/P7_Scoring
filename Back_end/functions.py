def function_cost(y_test, y_pred):

  tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
  cost = (tn*1) +(fp* 0)+(fn* -10)+(tp*0)