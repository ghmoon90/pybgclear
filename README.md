# pybgclear

## how to use
```
  python -m pybgclear <input file> 
```



## related package

  PIL
  numpy
  sys


## algorithm 

 step 1 . back ground mask 생성
   - 코너 주변 지점에서 추출하여 마스크 생성

 step 2 . mask 에 따라 alpha value 조정
