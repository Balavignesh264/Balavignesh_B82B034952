class player:
  def play(self):
    print("player is Playing cricket...")

class Batsman(player):
  def play(self):
    print("the Batsman in batting")

class Bowler(player):
  def play(self):
    print("the bowler is boweling")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()