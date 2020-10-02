def gettime(timeanddate):
  return timeanddate[11:16]
def samelocation(previous, current):
  plat = previous['latitude']
  plng = previous['longitude']
  clat = current['latitude']
  clng = current['longitude']
  if(plat==clat and plng == clng):
    return True
  else:
    return False
def mapfunction(data):
  response = []
  data = data.data
  previousRow = ''
  curpath = []
  curtype = ''
  starttime = ''
  endtime = ''
  startvol = 0
  endvolume = 0
  for row in data:
    if previousRow != '':
      print(str(samelocation(previousRow, row)) + curtype)
      if (samelocation(previousRow, row) and (curtype == 'stop' or curtype == '')):
        curtype = 'stop'
      elif (samelocation(previousRow, row) and curtype == 'moving'):
        curpath.append({'lat': float(row['latitude']), 'lng': float(row['longitude'])})
        response.append({'type': curtype, 'path': curpath, 'starttime': starttime, 'endtime': endtime, 'voa': startvol, 'vol': endvolume})
        startvol = row['volume_left']
        curpath = [{'lat': float(row['latitude']), 'lng': float(row['longitude'])}]
        starttime = gettime(row['created_at'])
        curtype = 'stop'
      elif ((not(samelocation(previousRow, row))) and (curtype == 'moving' or curtype == '')):
        curpath.append({'lat': float(row['latitude']), 'lng': float(row['longitude'])})
      elif ((not(samelocation(previousRow, row))) and curtype == 'stop'):
        curpath.append({'lat': float(row['latitude']), 'lng': float(row['longitude'])})
        response.append({'type': curtype, 'path': curpath, 'starttime': starttime, 'endtime': endtime, 'voa': startvol, 'vol': endvolume})
        startvol = row['volume_left']
        curpath = [{'lat': float(row['latitude']), 'lng': float(row['longitude'])}]
        starttime = gettime(row['created_at'])
        curtype = 'moving'
    else:
      starttime = gettime(row['created_at'])
      startvol = row['volume_left']
      curpath.append({'lat': float(row['latitude']), 'lng': float(row['longitude'])})
    endvolume = row['volume_left']
    endtime = gettime(row['created_at'])
    previousRow = row
  curpath.append({'lat': float(row['latitude']), 'lng': float(row['longitude'])})
  response.append({'type': curtype, 'path': curpath, 'starttime': starttime, 'endtime': endtime, 'voa': startvol, 'vol': endvolume})
  return response