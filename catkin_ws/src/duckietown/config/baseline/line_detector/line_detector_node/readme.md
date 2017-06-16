# Line detector node configs

## HSV
Using color model is HVS. [0°-360°; 0%-100%; 0%-100%]

In the configuration represented as a three byte where:

[ Hue in degrees divided by two;<br>
Saturation in the range from 0 to 255;<br>
Value in the range from 0 to 255 ]

Can be useful: [HSV color picker](http://alloyui.com/examples/color-picker/hsv/)

## File structure

* `img_size`: size of area for detection
* `top_cutoff`:
* `detector`: sets the detector
  * `-` The first is the name of the class. The class should be an abstract instance of LineDetectorInterface
  * `-configuration`: parameters
    * `dilation_kernel_size`:
    * `canny_thresholds`:
    * `hough_threshold`:
    * `hough_min_line_length`:
    * `hough_max_line_gap`:
    
    * `hsv_white1`: bottom border of white color
    * `hsv_white2`: upper border of white color
    * `hsv_yellow1`: bottom border of yellow color
    * `hsv_yellow2`: upper border of yellow color
    * `hsv_red1`: botton border of the first red color range
    * `hsv_red2`: upper border of the first red color range
    * `hsv_red3`: botton border of the second red color range
    * `hsv_red4`: upper border of the second red color range
