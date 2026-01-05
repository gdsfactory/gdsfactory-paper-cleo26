import gdsfactory as gf
from gplugins import gmsh

def my_heater():

    c = gf.Component()

    heater = c << gf.components.spiral_racetrack_heater_metal(num=3, waveguide_cross_section=gf.cross_section.xs_rc)

    via1 = c << gf.components.via_stack_heater_m3()
    via1.connect("e1", destination=heater.ports["e1"])

    via2 = c << gf.components.via_stack_heater_m3()
    via2.connect("e1", destination=heater.ports["e2"])

    return c

c = my_heater()
c.show()


layer_stack = gf.generic_tech.layer_stack.get_layer_stack()

mesh = gmsh.get_mesh(component=c,
                     layer_stack=layer_stack,
                     type="3D",
                     default_characteristic_length=2,
                     filename="mesh3D.msh"
                     )