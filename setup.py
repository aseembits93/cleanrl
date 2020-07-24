from setuptools import setup, find_packages

setup(name='cleanrl',
      version='0.2.1',
      install_requires=['gym', 'torch', 'tensorboard', 'wandb', 'stable_baselines3'],
      packages=find_packages()
)
