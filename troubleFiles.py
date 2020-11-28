from heapq import heappush, heappop, merge

FILE = 0
END = 1
START = 2


def troubleFiles(files, backups):

    queue_size = 0
    trouble = {}

    files = ((time, FILE, size) for time, size in sorted(files))
    backups = ((time, START, None) for time in sorted(backups))
    queue = list(merge(files, backups))
    busy = 0
    
    while queue:

        event_time, event_type, file_size = heappop(queue)

        if event_type == FILE and not busy:
            queue_size += file_size
        elif event_type == FILE and busy:
            trouble[busy] += 1

        elif event_type == END:
            busy = 0

        elif event_type == START:
            trouble[event_time] = 0
            if queue_size:
                busy = event_time
                heappush(queue, (event_time + queue_size, END, None))
                queue_size = 0
            
    return list(trouble.values())