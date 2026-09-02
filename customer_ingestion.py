def ingest_customer(customer):
    """
    Basic customer ingestion function.
    """

    if not customer:
        raise ValueError("Customer data must be provided")

    if "customer_id" not in customer:
        raise ValueError("customer_id is required")

    if "customer_name" not in customer:
        raise ValueError("customer_name is required")

    return customer


if __name__ == "__main__":
    customer = {
        "customer_id": 101,
        "customer_name": "Narendra"
    }

    result = ingest_customer(customer)
    print(result)