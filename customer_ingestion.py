def ingest_customer(customer):
    """
    Basic customer ingestion function.
    """
    if not customer:
        raise ValueError("Customer data cannot be empty")

    return customer


if __name__ == "__main__":
    customer = {
        "customer_id": 101,
        "customer_name": "Narendra"
    }

    result = ingest_customer(customer)
    print(result)