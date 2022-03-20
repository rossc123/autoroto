# autoroto

## General Info
This python program uses Machine Learning to create mattes that can be used for visual effects work.
The user specifies a directory and the program will use Semantic Segmentation to seperate the subjects from the background for all the images in the directory.
In addition to this the subjects are classified by type, allowing artists to handle people,vehicles,animals etc. seperately.
Origianlly this was a command line program. However, I added a GUI to make is easier for artists to use and to minimise erroneous input.


<p align="center">
  <img src="https://lh3.googleusercontent.com/-ELUnFgFJqUU/XPPXOOmhfMI/AAAAAAAAAP0/2cabsTI9uGUYxM3O3w4EOxjR_iJvEQAvACK8BGAs/s374/index3.png" width="350" title="hover text">
  <img src="https://lh3.googleusercontent.com/-gdUavPeOxdg/XPPXQngAnvI/AAAAAAAAAQA/yoksBterCGQGt-lv3aX4kfyMUDXTar7yACK8BGAs/s374/index4.png" width="350" alt="accessibility text">
</p>
Original Image:
![alt text](https://lh3.googleusercontent.com/-ELUnFgFJqUU/XPPXOOmhfMI/AAAAAAAAAP0/2cabsTI9uGUYxM3O3w4EOxjR_iJvEQAvACK8BGAs/s374/index3.png)

Produced Matte:
![alt text](https://lh3.googleusercontent.com/-gdUavPeOxdg/XPPXQngAnvI/AAAAAAAAAQA/yoksBterCGQGt-lv3aX4kfyMUDXTar7yACK8BGAs/s374/index4.png)

## Dependencies
To run this program you will need
*pyTorch
*Tkinter
*NumPy

## Inspiration
This project was inspired by:
LearnOpenCV: https://learnopencv.com/pytorch-for-beginners-semantic-segmentation-using-torchvision/ 
Moviola: https://youtu.be/rTH5lMPp4Qw 
