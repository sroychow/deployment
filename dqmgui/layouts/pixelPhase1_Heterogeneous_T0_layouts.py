def pixelheterolayout(i, p, *rows): i["PixelPhase1Heterogeneous/Layouts/" + p] = DQMItem(layout=rows)

pixelheterolayout(dqmitems, "000 - PixelPhase1 RecHit Position: GPU vs CPU",
   [{ 'path':  "SiPixelHeterogeneous/PixelRecHitsCompareGPUvsCPU/recHitsBLay1Posx",
      'description': "RecHit x-Position GPU vs CPU",
      'draw': { 'withref': "no", 'drawopts': "COLZTEXT" }}]
   )
