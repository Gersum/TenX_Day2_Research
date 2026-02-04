from .schemas import Result, TaskStatus
from .db import RedisClient
import logging

logger = logging.getLogger(__name__)

class Judge:
    def __init__(self):
        self.redis = RedisClient.get_instance()
        self.review_queue = "review_queue"
        self.confidence_threshold = 0.7

    def run(self):
        logger.info("Judge started")
        while True:
            result_data = self.redis.pop(self.review_queue)
            if not result_data:
                import time
                time.sleep(1)
                continue
                
            result = Result(**result_data)
            self.evaluate(result)

    def evaluate(self, result: Result):
        logger.info(f"Evaluating result for task: {result.task_id}")
        
        # Optimistic Concurrency Control (OCC) logic would go here
        # e.g., check if task was updated by another process
        
        if result.confidence_score >= self.confidence_threshold:
            logger.info(f"Task {result.task_id} APPROVED (Score: {result.confidence_score})")
            # Commit state to DB
        else:
            logger.warning(f"Task {result.task_id} REJECTED (Score: {result.confidence_score} < {self.confidence_threshold})")
            # Send back to task_queue or HITL
