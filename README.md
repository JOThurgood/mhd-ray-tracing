# mhd-ray-tracing
A collection of scripts relating to ray tracing methods (e.g. WKB) for
MHD waves. 

## Current Contents
Currently just consists of the generalised WKB solution for fast waves 
in a zero beta plasma for a user-specified or predefined magnetic field.

The mathematics is discribed in an upcoming paper which will be linked to here once available. 
For now, see section 3.1 of [McLaughlin+2016](https://www.aanda.org/articles/aa/pdf/2016/07/aa27789-15.pdf) instead - the main solve is for equations 15 for a generic magnetic field B.



### magnetic_field.py 

Here there are pre-defined classes for different magnetic fields,
currently 

* **Linear2dNull** B = [y,x,0] [a arbitarilly-rotated version of the field in e.g. McLaughlin & Hood 2004](https://www.aanda.org/articles/aa/full/2004/24/aa0900/aa0900.html)
* **Dipole3dCase1** a 3D dipolar magnetic 'dome' embedded within a uniform vertical magnetic field. Described in McLaughlin, Thurgood, Botha & Wiggs (2018, in prep). 

This is where new fields should be added, as unique classes. No checks
are made on the physicality of the field specified.

The main solver imports one of these classes under the alias
magnetic_field to act as a function to return the fields components and 
derivatives at a set of coordinates. 


### wkb_fast_zerobeta.py

Contains the data structure for an individual ray path (class Ray:),
and functions related to advancing and sampling the path in time.
Will soon also contain classes and functions relating to collections of rays ('Swarms') and their advancement and manipulation en-masse. 

**USE**
Typically import the module into a script under alias wkb

```python
import wkb_fast_zerobeta as wkb
```

Whereon it will immediately ask for the Class of magnetic field you want
to use (from magnetic_field.py) 

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

In future it would be best to allow the user to pass 
the sampling points through to the solver, rather than it assuming 
linear spacing between the two.

### test_linear2dnull.py

Examples of using the solver for the linear 2D magnetic null point
 B=[y,x] and plotting.

### test_3d.py

Examples of using the solver for the 3D dipole field described in
McLaughlin, Thurgood, Botha & Wiggs (2018, in prep). 