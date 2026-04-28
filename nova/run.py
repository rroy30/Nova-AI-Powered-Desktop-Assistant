import multiprocessing
import sys
import time
# To run Nova (Eel Frontend)
def startNova():
    """Starts the main UI and command processing logic."""
    try:
        print("Process 2: Starting Nova Interface...")
        from main import start
        start()
    except Exception as e:
        print(f"Error in Process 1 (Nova): {e}")

# To run hotword (Background Listener)
def listenHotword():
    """Starts the background wake-word detection."""
    try:
        print("Process 1: Listening for Hotword...")
        from engine.features import hotword
        hotword()
    except Exception as e:
        # This handles missing PyAudio or PvPorcupine errors
        print(f"Error in Process 2 (Hotword): {e}")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    p1 = multiprocessing.Process(target=startNova)
    p2 = multiprocessing.Process(target=listenHotword)

    p2.start() # Start the Listener first
    time.sleep(2) # Wait 2 seconds for it to grab the mic
    p1.start() # Then start the UI

    # Join p1 so the script stays alive as long as the UI is open
    p1.join()

    # If the UI is closed (p1 finished), shut down the background listener
    if p2.is_alive():
        print("Shutting down background listener...")
        p2.terminate()
        p2.join()

    print("System stopped.")
    