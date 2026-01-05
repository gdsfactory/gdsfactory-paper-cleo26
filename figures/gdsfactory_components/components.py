from matplotlib import pyplot as plt
import os

# change workig directory to __file__
os.chdir(os.path.dirname(__file__))

# BEGIN VERBATIM
import gdsfactory as gf

@gf.cell
def mzi_with_bend(radius=10) -> gf.Component:
    c = gf.Component()
    mzi = c.add_ref(gf.components.mzi())
    bend = c.add_ref(gf.components.bend_euler(radius=radius))
    bend.connect('o1', mzi['o2'])
    c.add_port('o1', port=mzi['o1'])
    c.add_port('o2', port=bend['o2'])
    return c

c = mzi_with_bend(radius=20)
# END VERBATIM


c.plot_matplotlib(show_ports=True, show_subports=False)
# TODO only some ports?


plt.axis('off')
plt.savefig('mzi_with_bend.pdf')

# BEGIN VERBATIM
@gf.cell
def nxn_to_nxn() -> gf.Component:
    c = gf.Component()
    c1 = c.add_ref(gf.components.nxn(east=3, ysize=20))
    c2 = c.add_ref(gf.components.nxn(west=3))
    c2.move((40, 10))
    routes = gf.routing.get_bundle(
        c1.get_ports_list(orientation=0),
        c2.get_ports_list(orientation=180),
        with_sbend=True,
        enforce_port_ordering=False,
    )
    for route in routes:
        c.add(route.references)
    return c

c = nxn_to_nxn()
# END VERBATIM

print(c.to_yaml())

# Plotting details
c.plot_matplotlib(show_ports=True, show_subports=not True)
# TODO only some ports?


plt.axis('off')
plt.savefig('nxn.pdf')
"""
            show_ports: Sets whether ports are drawn.
            show_subports: Sets whether subports (ports that belong to references) are drawn.
            label_aliases: Sets whether aliases are labeled with a text name.
            new_window: If True, each call to quickplot() will generate a separate window.
            blocking: If True, calling quickplot() will pause execution of ("block") the
                remainder of the python code until the quickplot() window is closed.
                If False, the window will be opened and code will continue to run.
            zoom_factor: Sets the scaling factor when zooming the quickplot window with the
                mousewheel/trackpad.
            interactive_zoom: Enables using mousewheel/trackpad to zoom.
            fontsize: for labels.
            layers_excluded: list of layers to exclude.
            layer_views: layer_views colors loaded from Klayout.
            min_aspect: minimum aspect ratio.
"""
plt.show()




c = gf.read.from_yaml('nxn_to_nxn.yaml')
c.show()

