import gdsfactory as gf
from gdsfactory.generic_tech import get_generic_pdk
from gdsfactory.technology import LayerStack
from gplugins.gmsh import get_mesh

gf.config.rich_output()
PDK = get_generic_pdk()
PDK.activate()


@gf.cell
def heater_component():
    
    c = gf.Component()
    
    heater = c << gf.components.spiral_racetrack_heater_metal(num=3)
    
    vias = c << gf.components.via_stack_heater_m3()
    vias.connect("e1", destination=heater.ports["e1"])
    
    vias = c << gf.components.via_stack_heater_m3()
    vias.connect("e1", destination=heater.ports["e2"])    
    
    return c

    
heater_component().show()

filtered_layerstack = LayerStack(
    layers={
        k: gf.pdk.get_layer_stack().layers[k]
        for k in ("slab90", "core", "via_contact","via1", "via2", "metal1", "metal2", "metal3", "heater", "box")
    }
)

resolutions = {"core": {"resolution": 0.5, "DistMax": 2.0}, "heater": {"resolution": 0.7}, "metal3": {"resolution": 1.0}}

filename = "mesh3D_simplified"

mesh_3D = get_mesh(heater_component(),
    type="3D",
    layer_stack=filtered_layerstack,
    filename=f"{filename}.msh",
    default_characteristic_length=1.0,
    resolutions=resolutions,
)
# mesh = mesh_with_physicals(mesh, filename)
# mesh = from_meshio(mesh)
# mesh.draw().plot()

# filename = "mesh2D"

# resolutions = {"core": {"resolution": 0.1, "DistMax": 0.5}, "heater": {"resolution": 0.2, "DistMax": 2.0}, "box": {"resolution": 0.3, "DistMax": 1.0}, "clad": {"resolution": 0.3}}


# mesh_uz = get_mesh(heater_component(),
#     type="uz",
#     xsection_bounds=((18,12),(18,-4)),
#     layer_stack=gf.pdk.get_layer_stack(),
#     filename=f"{filename}.msh",
#     default_characteristic_length=5.0,
#     resolutions=resolutions,
# )