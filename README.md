# mhd-ray-tracing
A python repository of ray tracing methods (e.g. WKB) and plotting tools for MHD wave trajectories.
 
## Current functionality
Currently consists of the generalised WKB solution for fast waves 
in a zero beta plasma for a user-specified or predefined magnetic field. The intention is to further generalise the code in future (e.g. different modes, finite-beta, nonlinearity, etc)

The mathematics is discribed in an upcoming paper which will be linked to here once available. 
For now, see section 3.1 of [McLaughlin+2016](https://www.aanda.org/articles/aa/pdf/2016/07/aa27789-15.pdf) instead - the main solve is for equations 15 for a generic magnetic field B.

## Using the code 

### External packages needed
Requires a number of not-too-exotic packages (matplotlib, numpy, scipy). If you are used to python it should be easy to figure out, if you are not, the anaconda distribution should come pre-packaged with everything you need.

### magnetic_field.py 

*This is where new magnetic fields should be added, as unique classes.* No checks
are made on the physicality of the field specified. This module also contains pre-defined classes for different magnetic fields, currently: 

* **Linear2dNull** B = [y,x,0] [a arbitarilly-rotated version of the field in e.g. McLaughlin & Hood 2004](https://www.aanda.org/articles/aa/full/2004/24/aa0900/aa0900.html)
* **Dipole3dCase1** a 3D dipolar magnetic 'dome' embedded within a uniform vertical magnetic field. Described in McLaughlin, Thurgood, Botha & Wiggs (2018, in prep). 

The main solver imports one of these classes under the alias
magnetic_field to act as a function to return the fields components and 
derivatives at a set of coordinates. 


### wkb_fast_zerobeta.py

This is essentially the main solver.

It contains the data structure for an individual ray path (the class 'Ray'),
and functions related to advancing and sampling the path in time.
Also contains classes and functions relating to collections of rays ('Swarms') and their advancement and manipulation en-masse. 

**Usage** 

Typically import the module into a script or the interactive interpreter under alias wkb. 

```python
import wkb_fast_zerobeta as wkb
```
*However, it requires foreknowledge of the class of magnetic field you want to use* (from magnetic_field.py). To avoid having to edit wkb_fast_zerobeta.py every time we want to use a different field, and to keep scripts relating to different problems self-contained, we can proceed as follows. When the module is first imported it immediately looks for a module called tmp_config.py , which tells it the desired class. If this file does not exist it will throw an error. As such you can initialise your splotting script / interactive session / whatever with the following

```python
# Create a tmp file to pass the chosen field class to wkb class
f = open('tmp_config.py','w')
f.write('fieldclass=\'Dipole3dCase1\'')
f.close()
# Import
import wkb_fast_zerobeta as wkb
# Remove the temporary file
import os
os.remove('tmp_config.py')
```
where you mayreplace 'Dipole3dCase1' with the class name of whatever field is appropriate for your problem. After or before this block, you will likely want to import whatever else you need (e.g. matplotlib). 

This snippet initialises a ray at time 0 at (x0,y0,z0) and 
(p0,q0,r0) 

```python
import wkb_fast_zerobeta as wkb
x0 = 
# y0,z0,p0,q0,r0 etc..
myray = wkb.Ray(x0,y0,z0,p0,q0,r0)
```
We might then ask the solve to integrate the ode up to a end
characteristic time (s_end) with 100 linearly spaced sampling points 
between s0 and s_end

```python
s_end = 1.0
ns = 100
test.solve(s_end,ns)
```

This can be then plotted. We note that this returns the solution at 100 
*sample points*. **The ode solver automatically chooses step sizes within tolerances.** 
This can give the *impression* of larger 'jumps' in regions of high alfven
speed than in regions of slower procession. In reality, it is just that the linear sampling
in time means there are less points to construct the line. The ode 
solution itself *usually* has used an appropriate step size within 
adaptive tolerances. 
Beware of this. 

### Examples

You can get a quick idea of how it works in practice by running and reading the following example 
scripts in the main directory


* **example_3d.py**  Examples of using the solver for the 3D dipole field described in
McLaughlin, Thurgood, Botha & Wiggs (2018, in prep). 
* **example2d.py** Examples of using the solver for the linear 2D magnetic null point
 B=[y,x] and plotting.
