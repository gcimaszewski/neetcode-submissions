from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # intuitively: we want to first process the tasks that have the highest number of repeats
        task_counts = Counter(tasks)
        # keep a priority queue: priority = num. of this task
        pqueue = []
        # a map of tasks currently in cooldown.
        cooldown = {} 
        cooldown_queue = []
        for task, count in task_counts.items():
            heapq.heappush(pqueue, (-1 * count, task))
        task_sequence = []
        # strategy: 
        # get the highest priority job from the queue
        # if there is no cooldown for this task: schedule it
        # else: look for another task that can be scheduled now
        # how to handle the required schedule gap for same type tasks:
        # is there a way to read through the priority queue in order?
        # otherwise: should we pop the entry from the queue entirely while still in cooldown phase?
        time = 0
        while len(pqueue) > 0 or len(cooldown_queue) > 0:
            # check if any tasks from the cooldown are ready to be requeued
            
            # for task in list(cooldown):
            #     if cooldown[task]["wait"] == 0:
            #         entry = cooldown.pop(task)
            #         # requeue the task if the cooldown finished
            #         heapq.heappush(pqueue, (-entry.get("count_remaining", 0), task))
            #     else:
            #         cooldown[task]["wait"] -= 1
            
            if cooldown_queue:
                oldest_task = cooldown_queue[0]
                task_name, next_time_to_run, run_count = oldest_task
                if time > next_time_to_run:
                    heapq.heappush(pqueue, (-run_count, task_name))
                    del cooldown_queue[0]

            if pqueue:
                task_count_negated, task_name = heapq.heappop(pqueue)
                task_sequence.append(task_name)
                if -task_count_negated > 1:
                    cooldown_queue.append((task_name, time + n, -task_count_negated - 1))
                    # cooldown[task_name] = {
                    #     "count_remaining": -task_count_negated - 1,
                    #     "wait": n
                    # }
            else:
                task_sequence.append("idle")
            time += 1
        

        print(f'calculated task schedule: {task_sequence}')
        return len(task_sequence)
            
