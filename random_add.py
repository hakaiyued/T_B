import mujoco_py

# Load the model from XML
model = mujoco_py.load_model_from_path('/home/kyle/workspaces/mujoco-3.2.2/model/Lar_T/T-bar.xml')
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewer(sim)

target_position = 0.0
process = 1

# Example: Run simulation loop
while True:
    if target_position > 0.8:
        process = -1
    elif target_position < 0:
        process = 1
    #sim.data.ctrl[0] = target_position
    sim.data.qpos[0] = target_position
    target_position += 0.001 * process
    sim.step()
    viewer.render()

