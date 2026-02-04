import redis
import json
import logging
from typing import Optional, Any

logger = logging.getLogger(__name__)

class RedisClient:
    _instance = None
    
    def __init__(self, host='localhost', port=6379, db=0):
        self.mock_mode = False
        self.memory_db = {}
        try:
            self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)
            self.redis.ping()
            logger.info("Connected to Redis")
        except redis.ConnectionError:
            logger.warning("Redis not available, falling back to in-memory mock")
            self.mock_mode = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def push(self, queue_name: str, item: Any):
        data = json.dumps(item) if not isinstance(item, str) else item
        if self.mock_mode:
            if queue_name not in self.memory_db:
                self.memory_db[queue_name] = []
            self.memory_db[queue_name].append(data)
        else:
            self.redis.rpush(queue_name, data)

    def pop(self, queue_name: str) -> Optional[Any]:
        if self.mock_mode:
            if queue_name in self.memory_db and self.memory_db[queue_name]:
                return json.loads(self.memory_db[queue_name].pop(0))
            return None
        else:
            item = self.redis.lpop(queue_name)
            return json.loads(item) if item else None
