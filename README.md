# 2DPrinterImageDetector

## Serial Protocol
- 0xaf -> start flag
- i    -> image index
- len  -> size of data
- data -> data body
- 0xfa -> end flag

## Paramter Description

### cluster_thresh = 4 
The clustering threshold for the same row (one stroke).If it is greater than this value, it is considered as another stroke, which requires lifting the pen.

### binary_thresh = (20, 80) 
Binarization threshold.To filter out pixels outside this interval.

