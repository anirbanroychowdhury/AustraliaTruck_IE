import threading
from time import sleep


class Camera(object):
    def __init__(self, process):
        self.to_process = []
        self.to_output = []
        self.process = process

        thread = threading.Thread(target=self.keep_processing, args=())
        thread.daemon = True
        thread.start()

    def process_one(self):
        if not self.to_process:
            return
        camera_frame = self.to_process.pop(0)
        output_frame = self.process.process(camera_frame)
        self.to_output.append(output_frame)

    def keep_processing(self):
        while True:
            self.process_one()
            # sleep(0.01)

    def enqueue_input(self, input):
        self.to_process.append(input)

    def get_frame(self):
        while not self.to_output:
            sleep(0.01)
        return self.to_output.pop(0)
