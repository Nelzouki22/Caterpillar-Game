import turtle as t
import random

# إعداد الشاشة
t.bgcolor('yellow')
t.title('Caterpillar Game')

# خصائص الدودة
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()

# سرعة حركة الدودة
caterpillar_speed = 2

# خصائص الورقة (الطعام)
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()

# خصائص النقاط (النتيجة)
score = t.Turtle()
score.hideturtle()
score.penup()
score.setposition(-int(t.window_width() / 2) + 50, int(t.window_height() / 2) - 50)
score.write('Score: 0', align='center', font=('Arial', 24, 'bold'))

# نص "اللعبة انتهت"
game_over = t.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.setposition(0, 0)

# وظيفة لتحريك الدودة
def move_caterpillar():
    global caterpillar_speed
    global score_value
    
    caterpillar.forward(caterpillar_speed)

    # التحقق إذا أكلت الدودة الورقة
    if caterpillar.distance(leaf) < 20:
        move_leaf()
        caterpillar_speed += 1
        score_value += 10
        update_score()

    # التحقق من ملامسة حدود الشاشة
    if caterpillar.xcor() > t.window_width() / 2 or caterpillar.xcor() < -t.window_width() / 2 or \
       caterpillar.ycor() > t.window_height() / 2 or caterpillar.ycor() < -t.window_height() / 2:
        caterpillar.hideturtle()
        leaf.hideturtle()
        game_over_message()
        return  # الخروج من وظيفة التحديث إذا انتهت اللعبة

    # تحديد التحديث التالي
    t.ontimer(move_caterpillar, 100)  # تحديد التحديث بعد 100 مللي ثانية

# وظيفة لتحريك الورقة لموقع عشوائي جديد
def move_leaf():
    leaf.hideturtle()
    leaf.setx(random.randint(-int(t.window_width() / 2) + 50, int(t.window_width() / 2) - 50))
    leaf.sety(random.randint(-int(t.window_height() / 2) + 50, int(t.window_height() / 2) - 50))
    leaf.showturtle()

# وظيفة لتحديث النقاط
def update_score():
    score.clear()
    score.write(f'Score: {score_value}', align='center', font=('Arial', 24, 'bold'))

# وظيفة لعرض رسالة "انتهت اللعبة"
def game_over_message():
    game_over.clear()
    game_over.write('Game Over!', align='center', font=('Arial', 36, 'bold'))

# بدء اللعبة
def start_game():
    global caterpillar_speed
    global score_value
    
    caterpillar_speed = 2
    score_value = 0

    caterpillar.showturtle()
    leaf.showturtle()

    move_leaf()
    move_caterpillar()  # بدء حركة الدودة

# إعداد نافذة الرسم لتحديث الرسوميات
t.tracer(0)  # إيقاف التحديث التلقائي للشاشة
t.onkey(start_game, 'space')
t.listen()
t.mainloop()
