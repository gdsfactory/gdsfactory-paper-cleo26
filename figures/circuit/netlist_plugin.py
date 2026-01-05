import gdsfactory as gf
from gdsfactory.generic_tech import get_generic_pdk
from gdsfactory.technology import LayerStack
from gplugins.gmsh import get_mesh
import matplotlib.pyplot as plt

gf.config.rich_output()
PDK = get_generic_pdk()
PDK.activate()

mzi = gf.components.mzi(delta_length=20)
mzi.show()
netlist = mzi.get_netlist().keys()
print(netlist)
mzi.plot_netlist()
plt.show()

from gplugins.klayout.get_netlist import get_l2n, get_netlist
from gplugins.klayout.plot_nets import plot_nets
import pathlib
gdspath = mzi.write_gds()
netlist = get_netlist(gdspath)
print(netlist)
l2n = get_l2n(gdspath)
cwd = pathlib.Path.cwd()
filepath = cwd / f"{mzi.name}.txt"
l2n.write_l2n(str(filepath))
plot_nets(filepath)
plt.show()