"""choices file"""
import enum


class OrderStatus(enum.Enum):
    """ order status """
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
