1.
import turtle                 # 터틀 라이브러리를 불러옴
t = turtle.Turtle()
t.shape("turtle")
t.color("black", "white")
s = turtle.Screen(); s.bgcolor('skyblue');       # 색 지정
def draw_snowman(x, y):                      # 함수 생성 x,y 변수 지정
    t.up()                                   # 펜을 든다.
    t.goto(x, y)                              # (x, y)으로 이동한다.
    t.down()                                  # 펜을 내린다.
    t.begin_fill()                            # 채울 모양을 그리기 직전에 호출
    t.circle(20)                              # 20으로 원을 생성
    t.end_fill()                              # 마지막으로 호출한 후 그린 모양을 채운다.
    t.goto(x, y-25)
    t.setheading(135)                         # 거북이의 방향을 135도로 설정
    t.forward(50)                             # 거북이가 향한 방향으로, 지정된 50만큼 거북이를 앞으로 움직임
    t.backward(50)                            # 거북이가 향한 반대 방향으로, 50만큼 거북이를 뒤로 움직임 
    t.setheading(30)   
    t.forward(50)
    t.backward(50)
    t.setheading(0
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.goto(x, y-70)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    
draw_snowman(0, 0)
draw_snowman(100, 0)
draw_snowman(200, 0)
2.
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

 
def hexagon():                 # 함수 생성
 for i in range(6):            # 작성한 함수 6회 반복
     turtle.forward(100)
     turtle.left(360/6)        # 정수 나눗셈은 //으로 한다

     
for i in range (6):
   hexagon()
   turtle.forward(100)
   turtle.right(60)
3.
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
def f(x):      # 함수 생성
 return x**2+1

t.goto(200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

for x in range(150):
      t.goto(x, int(0.01*f(x)))
4.
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def draw_line():
    t.forward(100)
    t.backward(100)

    
for x in range(12):
      t.right(30)
      draw_line()
