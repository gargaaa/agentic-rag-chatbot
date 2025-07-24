def create_message(sender, receiver, type_, payload, trace_id):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": type_,
        "trace_id": trace_id,
        "payload": payload
    }
