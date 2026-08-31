class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_station = 0
        cur_cost = 0
        total_cost = 0


        for i in range(len(gas)):
            cur_gas = gas[i]
            price = cost[i]

            total_cost += (cur_gas - price)
            cur_cost +=  (cur_gas - price)

            if cur_cost < 0:
                cur_station = i + 1
                cur_cost = 0
        

        return cur_station if total_cost >= 0 else -1
        

