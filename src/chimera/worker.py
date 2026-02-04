import time
import random
from .schemas import Task, Result, TaskStatus
from .db import RedisClient
import logging

logger = logging.getLogger(__name__)

class Worker:
    def __init__(self, worker_id: str):
        self.worker_id = worker_id
        self.redis = RedisClient.get_instance()
        self.task_queue = "task_queue"
        self.review_queue = "review_queue"

    def run(self):
        """
        Main worker loop.
        """
        logger.info(f"Worker {self.worker_id} started")
        while True:
            task_data = self.redis.pop(self.task_queue)
            if not task_data:
                # Sleep briefly to avoid busy loop in mock mode
                time.sleep(1)
                continue
                
            task = Task(**task_data)
            self.process_task(task)

    def process_task(self, task: Task):
        logger.info(f"Worker {self.worker_id} processing task: {task.id}")
        
        # Simulate work
        task.status = TaskStatus.IN_PROGRESS
        time.sleep(0.5) # Simulate latency
        
        # Generate result
        result = Result(
            task_id=task.id,
            worker_id=self.worker_id,
            output=f"Executed: {task.description}",
            confidence_score=random.uniform(0.6, 0.99)
        )
        
        self.redis.push(self.review_queue, result.model_dump(mode='json'))
        logger.info(f"Pushed result for task {task.id} to {self.review_queue}")
