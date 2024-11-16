import time
from queue import Queue

request_id_counter = 1

queue = Queue()


def generate_request():
    global request_id_counter
    # Create a new request with a unique ID
    request = f"Request {request_id_counter}"
    request_id_counter += 1

    # Add the request to the queue
    queue.put(request)
    print(f"Generated and added to queue: {request}, queue size: {queue.qsize()}")


def process_request():
    # Check if there are any requests to process
    if not queue.empty():
        # Remove the request from the queue for processing
        current_request = queue.get()
        print(f"Processing {current_request}, queue size: {queue.qsize()}")
    else:
        print("No requests to process. Queue is empty.")


def main():
    print("Service Center Simulation Started (press Ctrl+C to stop)")

    try:
        # Main loop to continuously generate and process requests
        while True:
            generate_request()
            process_request()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nService Center Simulation Ended.")


if __name__ == "__main__":
    main()
