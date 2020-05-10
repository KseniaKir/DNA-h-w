#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import solid
import os
import argparse
from solid import *
from solid.objects import sphere

parser = argparse.ArgumentParser(prog='DNA',
                                description='''You're going to create your own DNA sequence!''')
parser.add_argument('size', type=int, help=
                    'The size of the nucleotide (integer number)')
parser.add_argument('seq', type=str, help='DNA sequence (ACGT...)')
args = parser.parse_args()


def ostov53(z, angle, nuc, radius):
    element = (union()(
        color("Gainsboro")(translate([radius, 0, 0])(sphere(8))),
        color("Gainsboro")(translate([radius, 15, 0])(sphere(8))),
        color("Gainsboro")(translate([radius, 20, 15])(sphere(8))),
        color("Gainsboro")(translate([radius, -5, 15])(sphere(8))),
        color("Gainsboro")(translate([radius, 7.5, 25])(sphere(10))),
        color("Gainsboro")(translate([radius, -15, 25])(sphere(8))),
        color("Yellow")(translate([radius, -20, 42.5])(sphere(10))),
        color("Yellow")(translate([radius, -20, 60])(sphere(13))),
        color("Yellow")(translate([radius, -20, 80])(sphere(10))),
        color("Yellow")(translate([radius, -40, 60])(sphere(10))),
        color("Yellow")(translate([radius, 0, 60])(sphere(10)))))

    
    element1 = translate([0, 0, z])(rotate(angle)(element))
    element2 = translate([0, 0, z])(rotate(angle)((translate([0, 0, 80])(
                                    rotate(a=[0, 180, 0])(element)))))

    if nuc == "A":
        #        nuc2="T"
        nucleus1 = rotate(angle)(translate([radius/2, 0, z+20])((
        translate([0, 30, 0])(
        rotate(150)(union()(
            color("Green")(translate([0, 0, 0])(sphere(9))),
            color("Blue")(translate([-10, 7.5, 0])(sphere(8))),
            color("Green")(translate([-20, 8, 0])(sphere(9))),
            color("Blue")(translate([-30, 15, 0])(sphere(8))),
            color("Green")(translate([-20, 26, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Green")(translate([10, 22.5, 0])(sphere(9))),
            color("Blue")(translate([10, 7.5, 0])(sphere(8))),
            color("Green")(translate([0, 44, 0])(sphere(9))),
            color("Gray")(translate([0, 54, 0])(sphere(4))),
            color("Gray")(translate([10, 44, 0])(sphere(4)))))))))
        nucleus2 = rotate(angle+180)(translate([radius/1.7, 0, z+20])(
        translate([0, 10, 0])(
        rotate(25)((union()( 
            color("Blue")(translate([0, 0, 0])(sphere(8))),
            color("Green")(translate([-10, 7.5, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Blue")(translate([10, 22.5, 0])(sphere(8))),
            color("Green")(translate([10, 7.5, 0])(sphere(9))),
            color("Red")(translate([0, -14, 0])(sphere(10))),
            color("Red")(translate([-24, 25, 0])(sphere(10))),
            color("Gray")(translate([-20, 7.5, 0])(sphere(4)))))))))

    elif nuc == "G":
        #        nuc2="C"
        nucleus1 = rotate(angle)(translate([radius/2.5, 0, z+20])(
        translate([0, 20, 0])(
        rotate(170)((union()(
            color("Green")(translate([0, 0, 0])(sphere(9))),
            color("Blue")(translate([-10, 7.5, 0])(sphere(8))),
            color("Green")(translate([-20, 4, 0])(sphere(9))),
            color("Blue")(translate([-30, 15, 0])(sphere(8))),
            color("Green")(translate([-20, 26, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Green")(translate([10, 22.5, 0])(sphere(9))),
            color("Blue")(translate([10, 7.5, 0])(sphere(8))),
            color("Green")(translate([20, 0, 0])(sphere(9))),
            color("Gray")(translate([20, -10, 0])(sphere(4))),
            color("Gray")(translate([30, 0, 0])(sphere(4))),
            color("Red")(translate([0, 46, 0])(sphere(10))),
            color("Gray")(translate([20, 22.5, 0])(sphere(4)))))))))
        nucleus2 = rotate(angle+180)(translate([radius/2, 0, z+20])(
        translate([0, 10, 0])(
        rotate(0)((union()(
            color("Blue")(translate([0, 0, 0])(sphere(8))),
            color("Green")(translate([-10, 7.5, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Blue")(translate([10, 22.5, 0])(sphere(8))),
            color("Green")(translate([10, 7.5, 0])(sphere(9))),
            color("Red")(translate([0, -14, 0])(sphere(10))),
            color("Green")(translate([-24, 25, 0])(sphere(9))),
            color("Gray")(translate([-24, 35, 0])(sphere(4))),
            color("Gray")(translate([-34, 25, 0])(sphere(4))))))))) 

    elif nuc == "C":
        #        nuc2="G"
        nucleus1 = rotate(angle)(translate([radius/2, 0, z+20])(
        translate([0, 5, 0])(
        rotate(5)((union()(
            color("Blue")(translate([0, 0, 0])(sphere(8))),
            color("Green")(translate([-10, 7.5, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Blue")(translate([10, 22.5, 0])(sphere(8))),
            color("Green")(translate([10, 7.5, 0])(sphere(9))),
            color("Red")(translate([0, -14, 0])(sphere(10))),
            color("Green")(translate([-24, 25, 0])(sphere(9))),
            color("Gray")(translate([-24, 35, 0])(sphere(4))),
            color("Gray")(translate([-34, 25, 0])(sphere(4)))))))))
        nucleus2 = rotate(angle+180)(translate([radius/2, 0, z+20])(
        translate([0, 20, 0])(
        rotate(160)((union()( 
            color("Green")(translate([0, 0, 0])(sphere(9))),
            color("Blue")(translate([-10, 7.5, 0])(sphere(8))),
            color("Green")(translate([-20, 4, 0])(sphere(9))),
            color("Blue")(translate([-30, 15, 0])(sphere(8))),
            color("Green")(translate([-20, 26, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Green")(translate([10, 22.5, 0])(sphere(9))),
            color("Blue")(translate([10, 7.5, 0])(sphere(8))),
            color("Green")(translate([20, 0, 0])(sphere(9))),
            color("Gray")(translate([20, -10, 0])(sphere(4))),
            color("Gray")(translate([30, 0, 0])(sphere(4))),
            color("Red")(translate([0, 46, 0])(sphere(10))),
            color("Gray")(translate([20, 22.5, 0])(sphere(4)))))))))

    elif nuc == "T":
        #        nuc2="A"
        nucleus1 = rotate(angle)(translate([radius/1.6, 0, z+20])(
        translate([0, 0, 0])(
        rotate(30)((union()(
            color("Blue")(translate([0, 0, 0])(sphere(8))),
            color("Green")(translate([-10, 7.5, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Blue")(translate([10, 22.5, 0])(sphere(8))),
            color("Green")(translate([10, 7.5, 0])(sphere(9))),
            color("Red")(translate([0, -14, 0])(sphere(10))),
            color("Red")(translate([-24, 25, 0])(sphere(10))),
            color("Gray")(translate([-20, 7.5, 0])(sphere(4)))))))))
        nucleus2 = rotate(angle+180)(translate([radius/1.7, 0, z+20])((
        translate([0, 30, 0])(
        rotate(137)(union()(
            color("Green")(translate([0, 0, 0])(sphere(9))),
            color("Blue")(translate([-10, 7.5, 0])(sphere(8))),
            color("Green")(translate([-20, 8, 0])(sphere(9))),
            color("Blue")(translate([-30, 15, 0])(sphere(8))),
            color("Green")(translate([-20, 26, 0])(sphere(9))),
            color("Blue")(translate([-10, 22.5, 0])(sphere(8))),
            color("Blue")(translate([0, 30, 0])(sphere(8))),
            color("Green")(translate([10, 22.5, 0])(sphere(9))),
            color("Blue")(translate([10, 7.5, 0])(sphere(8))),
            color("Green")(translate([0, 44, 0])(sphere(9))),
            color("Gray")(translate([0, 54, 0])(sphere(4))),
            color("Gray")(translate([10, 44, 0])(sphere(4)))))))))

    return element1+element2+nucleus1+nucleus2

def ost(seq):
    obj = 0
    prirost = 0
    i = 0
    radius = 75
    number = 10
    for nuc in seq:
        nuc = nuc.capitalize()
        if (nuc != "A" and nuc != "T" and nuc != "C" and nuc != "G"):
            print ("Wrong sequence!")
            break
        obj += ostov53(prirost, i*360/number, nuc, radius) 
        prirost += 50
        i += 1
    obj = scale([args.size, args.size, args.size])(obj)
    return obj


if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None

    r = ost(args.seq)

    file_out = scad_render_to_file(r, out_dir=out_dir)
    print(f" you can find your DNA in: \n{file_out}")


# In[ ]:




