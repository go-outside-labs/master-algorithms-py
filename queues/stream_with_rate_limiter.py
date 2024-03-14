#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

class Logger:

    def __init__(self):
        self.msg_set = set()
        self.msg_queue = deque()
        
    def print_message(self, timestamp, message) -> bool:
        
        while self.msg_queue:
            msg, msg_timestamp = self.msg_queue[0]
            if timestamp - msg_timestamp >= 10:
                self.msg_queue.popleft()
                self.msg_set.remove(msg)
            else:
                break
        
        if message not in self.msg_set:
            self.msg_set.add(message)
            self.msg_queue.append((message, timestamp))
            return True
            
        return False
    
