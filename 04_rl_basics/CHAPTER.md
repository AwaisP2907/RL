# Chapter 4 — RL Basics

**Dates:** Dec 7–19

> Dec 20–26 (Brazil): reading and the Chapter 5 project spec only.

## Objective

Understand RL fundamentals and PPO, and train and evaluate PPO on a continuous MuJoCo task.

## Gate

- PPO trained on a continuous MuJoCo task, with separate train and eval, over 3 seeds.
- Explain PPO aloud in 2 minutes.

## Plan

### Topics

- RL framework: states, actions, rewards, policies, returns
- Policy gradients and PPO
- Gymnasium API, Stable-Baselines3, evaluation practice

### Resources

- Hugging Face Deep RL Course: [Unit 1](https://huggingface.co/learn/deep-rl-course/unit1/introduction) + [Unit 8](https://huggingface.co/learn/deep-rl-course/unit8/introduction)
- Spinning Up: [Key Concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html) + [Intro to Policy Optimization](https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html)
- [CleanRL PPO docs](https://docs.cleanrl.dev/rl-algorithms/ppo/) + [The 37 Implementation Details of PPO](https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/)
- [CleanRL `ppo_continuous_action.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_continuous_action.py)
- [Gymnasium — Basic Usage](https://gymnasium.farama.org/introduction/basic_usage/)
- SB3: [PPO](https://stable-baselines3.readthedocs.io/en/master/modules/ppo.html) · [RL Tips](https://stable-baselines3.readthedocs.io/en/master/guide/rl_tips.html) · [Custom Env](https://stable-baselines3.readthedocs.io/en/master/guide/custom_env.html)

### Build

- PPO on Pendulum-v1, then InvertedPendulum-v5.
- `evaluate.py`: compare the trained policy against a random baseline.

## Log

<!-- Copy this template for each session, newest at the bottom.

### YYYY-MM-DD
- **Did:**
- **Broke:**
- **Learned:**
- **Next:**
-->

## Open Questions

