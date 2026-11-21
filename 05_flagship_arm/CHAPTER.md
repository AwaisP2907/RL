# Chapter 5 — Flagship Arm

**Dates:** Dec 27–Jan 10

> The final project moves to its own repo, `feeding-arm-rl`.

## Objective

Train a PPO policy for my feeding arm in MuJoCo and compare it fairly against a classical IK+PD baseline.

## Gate

- PPO policy compared fairly against an IK+PD baseline.
- Robustness test on held-out mass/friction values.

## Plan

### Topics

- MJCF model of my feeding arm
- IK+PD baseline
- Custom Gymnasium environment
- PPO training
- Domain randomization comparison

### Resources

- [MuJoCo XML reference](https://mujoco.readthedocs.io/en/stable/XMLreference.html)
- [Lilian Weng — Domain Randomization for Sim2Real Transfer](https://lilianweng.github.io/posts/2019-05-05-domain-randomization/)

### Build

- MJCF of the feeding arm.
- IK+PD baseline controller.
- Custom Gymnasium env.
- PPO training, with and without domain randomization.

## Log

<!-- Copy this template for each session, newest at the bottom.

### YYYY-MM-DD
- **Did:**
- **Broke:**
- **Learned:**
- **Next:**
-->

## Open Questions

