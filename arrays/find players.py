class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        players = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losses[loser] = losses.get(loser, 0) + 1
            
        zero_loss = sorted([p for p in players if p not in losses])
        one_loss = sorted([p for p in players if losses.get(p) == 1])
        
        return [zero_loss, one_loss]