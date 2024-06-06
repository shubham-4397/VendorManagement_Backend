"""purchase order messages file"""

SUCCESS_MESSAGE = {
    'order_created': 'Purchase Order created successfully',
    'order_updated': 'Purchase Order updated successfully',
    'order_deleted': 'Purchase Order deleted successfully'
}

ERROR_MESSAGE = {
    'not_found': 'Purchase Order not found',
    'order_not_found': 'No purchase order found',
    'quantity-not-allowed': 'Quantity of the order cannot be less than 1',
    'future_date': 'Date cannot be in future'
}
