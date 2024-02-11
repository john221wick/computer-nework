import random
import time

def is_medium_idle():
    return random.choice([True, False])

def wait_for_random_backoff():
    backoff = random.randint(1, 5)
    print(f"Waiting for backoff time: {backoff} seconds")
    time.sleep(backoff)

def transmit_data():
    print("Transmitting data...")

def csma_ca():
    print("Checking if medium is idle...")
    if is_medium_idle():
        print("Medium is idle. Ready to transmit.")
        transmit_data()
    else:
        print("Medium is busy. Initiating backoff...")
        wait_for_random_backoff()
        print("Trying again to transmit.")
        csma_ca() 

if __name__ == "__main__":
    csma_ca()
