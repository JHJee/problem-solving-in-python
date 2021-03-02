# https://leetcode.com/problems/reorder-data-in-log-files/
import re


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dit_logs, let_logs = [], []
        for log in logs:
            if re.search(" [a-z]+", log):
                let_logs.append(log)
            else:
                dit_logs.append(log)
        let_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let_logs + dit_logs
