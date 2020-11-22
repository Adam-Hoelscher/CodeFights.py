from heapq import heappop, heappush
from collections import deque, namedtuple

Job = namedtuple('Job', ['jobProcess', 'requestTime', 'id'])


def jobScheduling(requestTime, jobProcess, timeFromStart):

    jobs = deque(
        Job(jp, rt, i)
        for i, (rt, jp) in enumerate(zip(requestTime, jobProcess))
        )

    curr_job = next_finish = None
    queue = []
    
    for t in range(timeFromStart + 1):
        
        while jobs and jobs[0].requestTime <= t:
            heappush(queue, jobs.popleft())
            
        if curr_job and t >= next_finish:
            curr_job = next_finish = None
            
        if next_finish is None and queue:
            curr_job = heappop(queue)
            next_finish = t + curr_job.jobProcess

    size = len(queue)
    return [j.id for j in sorted(queue)]
