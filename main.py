rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random;
uput = input("type r for rock, p for paper, and s for scissors\n");
uput = uput.lower();

rsmin = ["r","p","s"]
rstr =["rock","paper" ,"scissors"];
rps = [rock,paper,scissors];


unum = rsmin.index(uput);
rnum = random.randint(0,2);

ustr =rstr[unum]

user = rps[unum];
com = rps[rnum];
cput = rstr[rnum];

uwin = ("you win");
cwin = ("computer win");
draw = ("match draw");

print(f"\nyou choose {ustr}");
print(user);
print(f"\ncomputer choose {cput}");
print (com);


if user == rock and com == rock:
  winner = draw;
elif user == rock and com == paper:
  winner = cwin;
elif user == rock and com == scissors:
  winner = uwin;

elif user == paper and com == rock:
  winner = uwin;
elif user == paper and com == paper:
  winner = draw;
elif user == paper and com == scissors:
  winner = cwin;

elif user == scissors and com == rock:
  winner = cwin;
elif user == scissors and com == paper:
  winner = uwin;
elif user == scissors and com == scissors:
  winner = draw; 

print (winner)