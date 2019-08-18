def sel_sort(data):

  if not isinstance(data, list):
      vals = list(data)
  else:
      vals = data

  size = len(vals)

  for i in range(0, size):

      for j in range(i+1, size):

          if vals[j] < vals[i]:
              _min = vals[j]
              vals[j] = vals[i]
              vals[i] = _min
  return vals
