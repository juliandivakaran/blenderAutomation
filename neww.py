import bpy
import math


# Function to start the scene setup
def start():
    # Delete all objects in the scene (optional, to start fresh)
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Create a cube
    bpy.ops.mesh.primitive_cube_add(size=2, location=(2, 2, 2))
    cube = bpy.context.object
    print("Cube created at:", cube.location)

    # Create a circle
    bpy.ops.mesh.primitive_circle_add(radius=1, location=(4, 2, 2))
    circle = bpy.context.object
    print("Circle created at:", circle.location)

    # Create a star shape (5-pointed star)
    vertices = []
    edges = []
    radius_outer = 2
    radius_inner = 0.6
    num_points = 5
    angle_step = math.pi / num_points

    # Create the star vertices
    for i in range(2 * num_points):
        angle = i * angle_step
        radius = radius_outer if i % 2 == 0 else radius_inner
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y, 0))

    # Connect vertices to form the star
    for i in range(num_points):
        edges.append((i * 2, (i * 2 + 2) % (2 * num_points)))
        edges.append(((i * 2 + 1) % (2 * num_points), (i * 2 + 3) % (2 * num_points)))

    # Create mesh and object for the star
    mesh = bpy.data.meshes.new("star_mesh")
    obj = bpy.data.objects.new("Star", mesh)
    bpy.context.collection.objects.link(obj)

    # Create the mesh from vertices and edges
    mesh.from_pydata(vertices, edges, [])
    mesh.update()

    print("Star created at origin")

    # Update view layer
    bpy.context.view_layer.update()


# Call the start function to initialize everything
start()
