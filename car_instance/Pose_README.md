# Pose

From [wiki](https://en.wikipedia.org/wiki/Pose_(computer_vision)):
In computer vision and robotics, a typical task is to identify specific objects in an image and to
determine each object's position and orientation relative to some coordinate system. This 
information can then be used, for example, to allow a robot to manipulate an object or to avoid
moving into the object. The combination of *position* and *orientation* is referred to as the
**pose** of an object, even though this concept is sometimes used only to describe the orientation.
*Exterior orientation* and *translation* are also used as synonyms of pose.

The image data from which the pose of an image is determined can be either a single image, a stereo
image pair, or an image sequence where, typically, the camera is moving with a known velocity.
The objects which are considered can be rather general, including a living being or body parts, e.g.,
a head or hands. The methods which are used for determining the pose of an object, however, are
usually specific for a class of objects and cannot generally be expected to work well for 
other types of objects.

The pose can be described by means of a rotation and translation transformation which brings
the object from a reference pose to the observed pose. This rotation transformation
can be represented in different ways, e.g., as a rotation matrix or a quaternion.
