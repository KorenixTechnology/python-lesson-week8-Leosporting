import random


def hw_week8():
  win_count = 0
  lose_count = 0
  total_count = 0
  data = input()
  while data!='q':
    if data in ['r','p','s']:
      total_count += 1
      sys_data = random.choice(['r','p','s'])
      if data == sys_data:
        print(f'Tie :{data}')
      elif data=='r': 
        if sys_data =='p':
          lose_count += 1 
          print(f'you:{data}, computer:{sys_data}, you lose')
        else:
          win_count += 1 
          print(f'you:{data}, computer:{sys_data}, you win!!')
      elif data=='p' :
        if sys_data =='r':
          lose_count += 1 
          print(f'you:{data}, computer:{sys_data}, you lose')
        else:
          win_count += 1 
          print(f'you:{data}, computer:{sys_data}, you win!!')
      elif data=='s': 
        if sys_data =='p':
          lose_count += 1 
          print(f'you:{data}, computer:{sys_data}, you lose')
        else:
          win_count += 1 
          print(f'you:{data}, computer:{sys_data}, you win!!')
    else:
      print(f'Error Input:{data},\n' 
      f'Please Input : "r" or "p" or "s" or "q"\n'
      f'"r":Rock, "p":Paper, "s":Scissors, "q":Quit')

    data = input()
  print(f'Total:{total_count},Win:{total_count},Lose:{lose_count}')
  



if __name__ == '__main__':
    hw_week8()
