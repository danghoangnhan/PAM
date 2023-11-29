from controller import Navigator
import logging

if __name__ == "__main__":
    try:
        navigator = Navigator()
        navigator.start()
    except Exception as e:
        logging.error("An error occurred: %s", str(e))