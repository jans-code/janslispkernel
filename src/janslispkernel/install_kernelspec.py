#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""lisp kernel install helper"""

import os
import shutil
from jupyter_client.kernelspec import KernelSpecManager

JSON ="""{"argv":["python","-m","janslispkernel", "-f", "{connection_file}"],
 "display_name":"Lisp"
}"""

SVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   width="300"
   height="300"
   id="svg2"
   version="1.1"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dc="http://purl.org/dc/elements/1.1/">
  <defs
     id="defs4">
    <linearGradient
       id="linearGradient6891">
      <stop
         style="stop-color:#ff003b;stop-opacity:1;"
         offset="0"
         id="stop6893" />
      <stop
         style="stop-color:#cfb9b9;stop-opacity:0;"
         offset="1"
         id="stop6895" />
    </linearGradient>
    <linearGradient
       id="linearGradient5105">
      <stop
         style="stop-color:#643ec4;stop-opacity:1;"
         offset="0"
         id="stop5107" />
      <stop
         style="stop-color:lime;stop-opacity:0;"
         offset="1"
         id="stop5109" />
    </linearGradient>
  </defs>
  <metadata
     id="metadata7">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     id="layer1"
     transform="translate(-403.3627,-342.52874)">
    <g
       id="g1884"
       transform="matrix(1.1748294,0,0,1.1748294,231.59212,297.18846)"
       style="fill:#c40804;fill-opacity:1;stroke:#000000;stroke-width:0;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1">
      <path
         id="path2426"
         d="m 349.04829,213.25522 c 0,18.25189 -26.25845,19.11077 -26.25845,1 l 0.5,-46.81607 c 0,-16.25658 17.11988,-33.9858 40.36972,-34.25 17.25743,0 17.79396,-26.79433 0,-26.79433 H 232.45719 c -12.92263,0 -18.70236,7.625 -18.45236,17.125 v 77.65638 c 0,18.27957 -26.25845,18.00174 -26.25845,0 0,0 -0.5,-59.1601 -0.5,-79.14749 0,-19.48739 15.34761,-43.000001 44.4094,-43.000001 29.56172,0 131.4094,0 131.4094,0 25.5,0.25 38.75,19.768996 38.5,38.781221 -0.0883,26.25461 -20.22637,42.03122 -35.75,42.03122 -11.52842,0 -16.40924,6.4732 -16.40924,17.25 z"
         style="fill:#c40804;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
      <path
         id="path2424"
         d="m 146.43482,120.57408 -0.22586,91.86364 c 1.36668,25.83027 19.74304,40.57597 39.77414,41.07595 l 85.3378,-0.82177 c 20.29248,0 36.73205,-16.86411 36.73205,-39.11973 0,-20.76355 -13.62805,-38.40945 -39.38767,-39.11974 -18.75482,0 -18.50169,-26.79433 0,-26.79433 h 38.65682 c 17.58241,0 17.13935,-27.86611 0,-27.86611 l -41.24187,0.5 c -20.28043,0 -38.7149,17.11535 -38.5,39.24067 0.2149,22.12532 15.40551,41.32322 39.30061,41.32322 18.58623,0 18.17852,26.64934 0.17678,26.64934 h -75.7991 c -10.25934,0 -17.98108,-5.58364 -17.98108,-18.12132 l -0.5,-88.59492 c 0,-19.8673 -26.34262,-19.55711 -26.34262,-0.2149 z"
         style="fill:#c40804;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    </g>
  </g>
</svg>
"""

def install_kernelspec():
    """create dir + files and install the kernel"""
    kerneldir = "/tmp/janslispkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w", encoding="UTF-8") as file:
        file.write(JSON)

    with open(kerneldir + "logo-svg.svg", "w", encoding="UTF-8") as file:
        file.write(SVG)

    print(' Done!')
    print('Installing Jupyter kernel...', end="")

    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'janslispkernel', user=os.getenv('USER'))

    print(' Done!')
    print('Cleaning up tmp files...', end="")

    shutil.rmtree(kerneldir)

    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall janslispkernel')
