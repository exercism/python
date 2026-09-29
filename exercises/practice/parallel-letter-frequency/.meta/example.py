# -*- coding: utf-8 -*-
from collections import Counter
from threading import Lock, Thread
from time import sleep
from queue import Queue


TOTAL_WORKERS = 3  # Maximum number of threads chosen arbitrarily

class LetterCounter:

    def __init__(self):
        self.lock = Lock()
        self.value = Counter()

    def add_counter(self, counter_to_add):
        self.lock.acquire()
        try:
            self.value = self.value + counter_to_add
        finally:
            self.lock.release()


def count_letters(queue_of_texts, letter_to_frequency, worker_id):
    while not queue_of_texts.empty():
        sleep(worker_id + 1)
        line_input = queue_of_texts.get()
        if line_input is not None:
            letters_in_line = Counter(idx for idx in line_input.lower() if idx.isalpha())
            letter_to_frequency.add_counter(letters_in_line)
        queue_of_texts.task_done()
        if line_input is None:
            break


def calculate(list_of_texts):
    queue_of_texts = Queue()
    for line in list_of_texts:
        queue_of_texts.put(line)
    letter_to_frequency = LetterCounter()
    threads = []
    for idx in range(TOTAL_WORKERS):
        worker = Thread(target=count_letters, args=(queue_of_texts, letter_to_frequency, idx))
        worker.start()
        threads.append(worker)
    queue_of_texts.join()
    for _ in range(TOTAL_WORKERS):
        queue_of_texts.put(None)
    for thread in threads:
        thread.join()
    return letter_to_frequency.value
