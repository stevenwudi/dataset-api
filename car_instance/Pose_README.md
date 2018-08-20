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

## Projecting 3D car Mesh to 2D
For this challenge,  we are given 79 car models' mesh with around 3000 vertices and 5000 faces
of triangles. 

To project the 3D mesh to 2D image plane, Opencv has nice package.

Given  pose of 6 parameters, (roll,pitch,yaw,x,y,z) which are float32 numbers. 
The unit of roll, pitch, yaw are radian, and the unit of x, y, z is meter.

We first convert the 'roll, pitch, yaw' (euler angles) to rotation matrix:
Calculates Rotation Matrix given euler angles can be achieved by:

```
def euler_angles_to_rotation_matrix(angle, is_dir=False):
    """Convert euler angels to quaternions.
    Input:
        angle: [roll, pitch, yaw]
        is_dir: whether just use the 2d direction on a map
    """
    roll, pitch, yaw = angle[0], angle[1], angle[2]

    rollMatrix = np.matrix([
        [1, 0, 0],
        [0, math.cos(roll), -math.sin(roll)],
        [0, math.sin(roll), math.cos(roll)]])

    pitchMatrix = np.matrix([
        [math.cos(pitch), 0, math.sin(pitch)],
        [0, 1, 0],
        [-math.sin(pitch), 0, math.cos(pitch)]])

    yawMatrix = np.matrix([
        [math.cos(yaw), -math.sin(yaw), 0],
        [math.sin(yaw), math.cos(yaw), 0],
        [0, 0, 1]])

    R = yawMatrix * pitchMatrix * rollMatrix
    R = np.array(R)

    if is_dir:
        R = R[:, 2]

    return R

 ```
Then, using Opencv's `projectionPoints` with given Camera intrinsics, 3D points projected into 2D
image plane can be achieved by:
 
```
# project 3D points to 2d image plane
rmat = uts.euler_angles_to_rotation_matrix(pose[:3])
rvect, _ = cv2.Rodrigues(rmat)
imgpts, jac = cv2.projectPoints(np.float32(car['vertices']), rvect, pose[3:], self.intrinsic, distCoeffs=None)
```

If the mask of the mesh is required, we can draw the triangle lines as:
```
mask = np.zeros(image.shape)
for face in car['faces'] - 1:
    pts = np.array([[imgpts[idx, 0, 0], imgpts[idx, 0, 1]] for idx in face], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(mask, [pts], True, (0, 255, 0))
```


## Problem of Gimble lock

“gimbal lock”: drawing its name from certain orientation with three nested moving gimbals in which
two of the three axes become collinear — restricting the available rotations to only two axes. (Watch
a nice video tutorial on gimbal lock at [https://www.youtube.com/watch?v=zc8b2Jo7mno](https://www.youtube.com/watch?v=zc8b2Jo7mno)).