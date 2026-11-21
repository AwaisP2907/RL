"""Sanity check for the CPU-only robotics RL environment."""

import gymnasium as gym
import mujoco
import numpy as np
import stable_baselines3 as sb3
import torch
from stable_baselines3 import PPO

print("== Versions ==")
print(f"torch             {torch.__version__}")
print(f"mujoco            {mujoco.__version__}")
print(f"gymnasium         {gym.__version__}")
print(f"stable_baselines3 {sb3.__version__}")
print(f"torch.cuda.is_available(): {torch.cuda.is_available()}  (expected False)")

print("\n== MuJoCo pendulum ==")
PENDULUM_XML = """
<mujoco model="pendulum">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <body name="pole" pos="0 0 1">
      <joint name="hinge" type="hinge" axis="0 1 0" damping="0.05"/>
      <geom type="capsule" fromto="0 0 0 0 0 -0.5" size="0.02" mass="1"/>
    </body>
  </worldbody>
</mujoco>
"""
model = mujoco.MjModel.from_xml_string(PENDULUM_XML)
data = mujoco.MjData(model)
data.qpos[0] = np.pi / 4  # start tilted so it actually swings
for _ in range(1000):
    mujoco.mj_step(model, data)
print(f"final qpos after 1000 steps: {data.qpos}")

print("\n== Gymnasium InvertedPendulum-v5 ==")
env = gym.make("InvertedPendulum-v5")
obs, _ = env.reset(seed=0)
total_reward = 0.0
for _ in range(100):
    obs, reward, terminated, truncated, _ = env.step(env.action_space.sample())
    total_reward += reward
    if terminated or truncated:
        obs, _ = env.reset()
env.close()
print(f"total reward over 100 random steps: {total_reward}")

print("\n== SB3 PPO on CartPole-v1 ==")
model = PPO("MlpPolicy", "CartPole-v1", device="cpu", verbose=0, seed=0)
model.learn(total_timesteps=5_000)
print("PPO OK")
