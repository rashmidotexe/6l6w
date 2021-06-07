win=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[1,4,7],[2,5,8],[0,3,6]]
def display_board(board)
  puts " #{board[0]} | #{board[1]} | #{board[2]} "
  puts "---+---+---"
  puts " #{board[3]} | #{board[4]} | #{board[5]} "
  puts "---+---+---"
  puts " #{board[6]} | #{board[7]} | #{board[8]} "
end
board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
player1=[]
player2=[]
display_board(board)
i=0
while i<=8 do
  if (i%2==0)
      puts "player1 choose an index"
      entry=gets.chomp().to_i
      player1.append(entry)
      board[entry]="O"
      i+=1
    else
      puts "player2 choose an index"
      entry=gets.chomp().to_i
      player2.append(entry)
      board[entry]="X"
      i+=1
  end
  display_board(board)
  for x in win
    if (x & player1) == x
      puts "player 1 wins"
      exit!
    elsif (x & player2)==x
      puts "player 2 wins"
      exit!
    end
  end
end
puts "it's a draw"
