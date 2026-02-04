from typing import List
from .schemas import Task, TaskStatus
from .db import RedisClient
import logging

logger = logging.getLogger(__name__)

class Planner:
    def __init__(self):
        self.redis = RedisClient.get_instance()
        self.task_queue = "task_queue"

    def decompose(self, goal: str) -> List[Task]:
        """
        Decompose a high-level goal into tasks.
        In a real scenario, this would use an LLM.
        """
        logger.info(f"Decomposing goal: {goal}")
        
        # Mock decomposition
        tasks = [
            Task(description=f"Research: {goal}", priority=1),
            Task(description=f"Draft content for: {goal}", priority=2),
            Task(description=f"Review and finalize: {goal}", priority=3)
        ]
        
        for task in tasks:
            self.redis.push(self.task_queue, task.model_dump(mode='json'))
            logger.info(f"Pushed task {task.id} to {self.task_queue}")
            
        return tasks
