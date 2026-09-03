def ingest_orders(orders):
    """
    Validate and ingest a list of orders.
    """

    if not orders:
        raise ValueError("Order data cannot be empty")

    required_fields = [
        "order_id",
        "customer_id",
        "order_amount"
    ]

    for order in orders:
        for field in required_fields:
            if field not in order:
                raise ValueError(f"{field} is required")

        if order["order_amount"] < 0:
            raise ValueError("Order amount cannot be negative")

    return orders


if __name__ == "__main__":
    orders = [
        {
            "order_id": 1001,
            "customer_id": 101,
            "order_amount": 2500
        },
        {
            "order_id": 1002,
            "customer_id": 102,
            "order_amount": 1500
        }
    ]

    result = ingest_orders(orders)
    print(result)