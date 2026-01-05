# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: gen
#     language: python
#     name: python3
# ---

# +
# %cd -q ..

import logging

import graphviz

logging.basicConfig(format='[%(levelname)s@%(name)s] %(message)s', level=logging.DEBUG)

graphviz.__version__, graphviz.version()

# +
# Formatting
language_to_color = {"Python": '#40e0d0',
                     "C/C++": '#ff000042',
                     "Rust": 'deeppink',
                     "GUI": 'white',
                     }
type_to_container = {"gds": "box",
                     "spatial": "ellipse"}

# Node info
node_dict = {}
node_dict['GEOS'] = {'language': 'C/C++', 
                     'type': 'spatial',
                     }
node_dict['gdstk'] = {'language': 'C/C++', 
                      'type': 'gds',
                      'dependencies': [],
                      'inspirations': ['gdspy'],
                      'URL': 'https://github.com/heitzmann/gdstk'
                      }


u = graphviz.Digraph('Open source EDA landscape as of September 2023', filename="genealogy", format="svg")
u.attr(size='6,6')

# C/C++
u.node('GEOS', shape='ellipse', style='filled', fillcolor='#ff000042')
u.node('gdstk', shape='ellipse', style='filled', fillcolor='#ff000042')
u.node('KLayout', shape='ellipse', style='filled', fillcolor='#ff000042')

# Python
u.attr('node', shape='ellipse', style='filled', fillcolor='#40e0d0')
u.node('shapely')
u.node('phidl')
u.node('gdshelpers')
u.node('gdspy')
u.node('zeropdk')
u.node('gdsfactory')
u.node('kfactory')
u.node('SiEPIC-Tools')
u.node('DPhox')
u.node('Nazca')
u.node('BPG')
u.node('qiskit-metal')
u.node('geopandas')
u.node('KQCircuits')
u.node('OpenFASOC')

# Rust
u.attr('node', shape='ellipse', style='filled', fillcolor='deeppink')
u.node('Layout21')

# C/C++ + Python
u.attr('node', shape='ellipse', style='wedged', fillcolor="#40e0d0:#ff000042")
u.node('numpy')
u.node('pyclipper')
u.node('rtree')

# # Proprietary
# u.attr('node', shape='box', style='wedged', fillcolor="white")
# u.node('Virtuoso')
# u.node('OptoDesigner')
# u.node('IPKISS')


u.edge('GEOS', 'shapely')
u.edge('shapely', 'gdshelpers')

# dphox
u.edge('shapely', 'DPhox', style='solid')
u.edge('numpy', 'DPhox', style='solid')
u.edge('phidl', 'DPhox', style='dashed')
u.edge('gdspy', 'DPhox', style='dashed')
u.edge('Nazca', 'DPhox', style='dashed')

u.edge('numpy', 'gdspy')
u.edge('gdspy', 'phidl')
u.edge('gdspy', 'gdstk', style='dashed')
u.edge('phidl', 'gdsfactory', style='dashed')
u.edge('gdstk', 'gdsfactory', style='solid')

u.edge('KLayout', 'zeropdk', style='solid')

u.edge('gdsfactory', 'kfactory', style='dashed')
u.edge('KLayout', 'kfactory', style='solid')
u.edge('KLayout', 'SiEPIC-Tools', style='solid')


# Nazca
u.edge('pyclipper', 'Nazca', style='solid')
u.edge('numpy', 'Nazca', style='solid')

# BPG
u.edge('numpy', 'BPG', style='solid')
u.edge('rtree', 'BPG', style='solid')
u.edge('shapely', 'BPG', style='solid')

# KQCircuits
u.edge('KLayout', 'KQCircuits', style='solid')

# Layout21
u.edge('gdstk', 'Layout21', style='dashed')

u.render()
# -

# * GEOS
#     * https://libgeos.org/
# * shapely
#     * Python
#     * Backend: GEOS
# * gdspy
#     * https://github.com/heitzmann/gdspy
#     * Python
#     * Backend: numpy
# * Layout21
#     * https://github.com/dan-fritchman/Layout21
#     * Rust
#     * Inspired by gdstk/gdspy
# * SiEPIC-Tools
#     * https://github.com/SiEPIC/SiEPIC-Tools
#     * Python in KLayout
# * Dphox
#     * https://github.com/solgaardlab/dphox
#     * Python
#     * Numpy + shapely backend
#     * Inspired by: Nazca, gdspy, phidl
# * Nazca
#     * https://nazca-design.org/about/
#     * Python
#     * Depends on pyclipper, numpy, others
#
# * pyclipper
#     * https://github.com/fonttools/pyclipper
#     * C/C++
# * qiskit-metal
#     * https://github.com/qiskit-community/qiskit-metal
#     * Python
#     * Selected dependencies: numpy, shapely, ligeos
#
# Proprietary
#
# * IPKISS
#     * https://docs.lucedaphotonics.com/
#     * Proprietary, Luceda Photonics
# * OptoDesigner
#     * https://www.synopsys.com/photonic-solutions/optocompiler/optodesigner.html
#     * Proprietary, Synopsys
# * Virtuoso
#     * https://www.cadence.com/en_US/home/solutions/photonics.html
#     * Proprietary, Cadence
