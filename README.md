# colorizeSketch
using keras tensorflow to colorize the sketch Image to colored Image

## Result
Testing By image that not in dataset <br>
merg by <br>
original         alpha 1.0 (opaqe bg)<br>
predict result   alpha 0.8 <br>
<br><br>

### modified based from 
https://github.com/eriklindernoren/Keras-GAN

### 128x128 image size dataset prediction result 


![alt text](https://github.com/Telexine/colorizeSketch/blob/master/input128_test2.png "example1")

![alt text](https://github.com/Telexine/colorizeSketch/blob/master/input128_test3.png "example2")


<br>
 stretch prediction result to original size then merge two layer.
 *The result might have some noise and artifact from it 
more detail on merg/dockerize is in https://github.com/Telexine/KubeKeras

