MAX_SPEED = 120
MAX_ACTIONS = 10
MAX_SCORE_CHANGE = 500
MAX_POSITION_JUMP = 200

players = [
{"id":101,"speed":85,"actions":3,"score_change":120,"position_jump":20},
{"id":102,"speed":95,"actions":4,"score_change":200,"position_jump":30},
{"id":666,"speed":310,"actions":2,"score_change":100,"position_jump":15},
{"id":777,"speed":90,"actions":22,"score_change":80,"position_jump":10},
{"id":888,"speed":100,"actions":3,"score_change":1500,"position_jump":50},
{"id":999,"speed":75,"actions":3,"score_change":50,"position_jump":900}
]

def detect_cheat(player):

if player["speed"] > MAX_SPEED:
return "Speed Hack"

if player["actions"] > MAX_ACTIONS:
return "Macro Spam"

if player["score_change"] > MAX_SCORE_CHANGE:
return "Score Exploit"

if player["position_jump"] > MAX_POSITION_JUMP:
return "Teleport Hack"

return None


for player in players:

cheat = detect_cheat(player)

if cheat:
print(f"ALERT: Player {player['id']} flagged for {cheat}")
