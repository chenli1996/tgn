import open3d as o3d

# # Load the point cloud data
point_cloud = o3d.io.read_point_cloud("./longdress_vox10_1097.ply")

# # Visualize the point cloud
# o3d.visualization.draw_geometries([point_cloud])

# def custom_draw_geometry(pcd):
#     # The following code achieves the same effect as:
#     # o3d.visualization.draw_geometries([pcd])
#     vis = o3d.visualization.Visualizer()
#     vis.create_window()
#     vis.add_geometry(pcd)
#     vis.run()
#     vis.destroy_window()
    
# custom_draw_geometry(point_cloud)

# def custom_draw_geometry_load_option(pcd):
#     vis = o3d.visualization.Visualizer()
#     vis.create_window()
#     vis.add_geometry(pcd)
#     vis.get_render_option().load_from_json("./tile_data/open3d_test_results/camera_params.json")
#     vis.run()
#     vis.destroy_window()
    
# custom_draw_geometry_load_option(point_cloud)    



def custom_draw_geometry_with_custom_fov(pcd, fov_step):
    vis = o3d.visualization.Visualizer()
#     vis.create_window()
    vis.add_geometry(pcd)
#     ctr = vis.get_view_control()
#     print("Field of view (before changing) %.2f" % ctr.get_field_of_view())
#     ctr.change_field_of_view(step=fov_step)
    print(fov_step)
    # print("Field of view (after changing) %.2f" % ctr.get_field_of_view())
    vis.run()
    vis.destroy_window()
    
custom_draw_geometry_with_custom_fov(point_cloud, -20)

# def custom_draw_geometry_with_rotation(point_cloud):

#     def rotate_view(vis):
#         ctr = vis.get_view_control()
#         ctr.rotate(10.0, 0.0)
#         return False

#     o3d.visualization.draw_geometries_with_animation_callback([point_cloud],
#                                                               rotate_view)

# custom_draw_geometry_with_rotation(point_cloud)    