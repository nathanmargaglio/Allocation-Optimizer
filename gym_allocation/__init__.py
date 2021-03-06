import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Disaster-v0',
    entry_point='gym_allocation.envs:DisasterEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)

register(
    id='Allocation-v0',
    entry_point='gym_allocation.envs:AllocationEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)