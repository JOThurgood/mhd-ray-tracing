# mhd-ray-tracing
A collection of scripts relating to ray tracing methods (e.g. WKB) for
MHD waves 

## Current Contents
Currently just consists of the generalised WKB solution for fast waves 
in a zero beta plasma for a user-specified or predefined magnetic field.

### magnetic_field.py 

Here there are pre-defined classes for different magnetic fields,
currently 

This is where new fields should be added, as unique classes. No checks
are made on the physicality of the field specified.

The main solver imports one of these classes under the alias
magnetic_field to act as a function to return the fields components and 
derivatives at a set of coordinates. 


### wkb_fast_zerobeta.py

Contains the data structure for an individual ray path (class Ray:),
and functions related to advancing and sampling the path in time. 

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
If we have appropriately 

