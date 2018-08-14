### Instruction for renderer
We modify the renderer based on the render crom from the code provided by [displet](http://www.cvlibs.net/projects/displets/)

<<<<<<< HEAD
Two things are modified: (1) we give the renderer a python wrapper
 (2) we provide an egl context so the the render can performed off-screen.
=======
Dependency: `python-tk libeigen3-dev libglfw3-dev libgles2-mesa-dev libglew-dev libboost-all-dev`
>>>>>>> 0cf12bc7669b2f96a412b4fcb2f7b71f0c19f2c8

Two things are modified: (1) we give the renderer a python wrapper (2) we provide an egl context so the the render can be performed off-screen.

Tested with Ubuntu 14.04 and Python 2.7, nvidia diver 375.26. For other versions, we haven't tested it. 

