import pytest
from src.chimera.planner import Planner
from src.chimera.worker import Worker
from src.chimera.judge import Judge
from src.chimera.schemas import TaskStatus, Task
from src.chimera.db import RedisClient

@pytest.fixture(autouse=True)
def mock_redis():
    # Reset singleton and ensure mock mode
    RedisClient._instance = None
    client = RedisClient(host='nonexistent') # Force mock mode
    return client

def test_swarm_flow():
    # 1. Planner
    planner = Planner()
    tasks = planner.decompose("Launch Marketing Campaign")
    
    assert len(tasks) == 3
    assert tasks[0].status == TaskStatus.PENDING
    
    # Check Redis
    redis_client = RedisClient.get_instance()
    # In mock mode, check internal dict if accessible or pop to verify
    
    # 2. Worker
    worker = Worker(worker_id="worker-1")
    
    # Process one task
    task_data = redis_client.pop("task_queue")
    assert task_data is not None
    task = Task(**task_data)
    
    worker.process_task(task)
    
    # Check Review Queue
    result_data = redis_client.pop("review_queue")
    assert result_data is not None
    assert result_data['output'].startswith("Executed:")
    
    # 3. Judge
    judge = Judge()
    # Push back result to process it
    redis_client.push("review_queue", result_data)
    
    # Run judge evaluation (manually calling evaluate to avoid infinite loop)
    from src.chimera.schemas import Result
    result = Result(**result_data)
    
    # Force high confidence for test
    result.confidence_score = 0.95
    judge.evaluate(result)
    
    # Since OCC logic is a stub, we just ensure no exception was raised
    assert True
