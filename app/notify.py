"""Send an order status change to the fulfilment webhook."""

from __future__ import annotations

import json

import urllib3

http = urllib3.PoolManager()
WEBHOOK_URL = "https://fulfilment.example.com/hooks/orders"


def notify_status(order_id: int, status: str) -> int:
    resp = http.request(
        "POST",
        WEBHOOK_URL,
        body=json.dumps({"order_id": order_id, "status": status}),
        headers={"Content-Type": "application/json"},
        timeout=5.0,
    )
    return resp.status
