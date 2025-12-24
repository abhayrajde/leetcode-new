class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0

        for index, ticket_count in enumerate(tickets):
            if index <= k:
                total_time += min(ticket_count, tickets[k])
            else:
                total_time += min(ticket_count, tickets[k] - 1)
        return total_time
