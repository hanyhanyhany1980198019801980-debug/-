import json
import os
import random
import time
import tkinter as tk
import turtle  # مكتبة turtle المدمجة
import webbrowser  # مكتبة لفتح الروابط في المتصفح

MEMORY_FILE = "mostafa_gui_brain.json"


def load_brain():
  if os.path.exists(MEMORY_FILE):
    try:
      with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    except:
      return {
          "notes": [],
          "user": "",
          "pass": "",
          "logged_in": False,
          "dev_mode": False,
          "extra_attempts": 0,
          "chat_history": [],
          "part1_completed": False,
      }
  return {
      "notes": [],
      "user": "",
      "pass": "",
      "logged_in": False,
      "dev_mode": False,
      "extra_attempts": 0,
      "chat_history": [],
      "part1_completed": False,
  }


def save_brain(data):
  try:
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
  except:
    pass


class MostafaGUIHub:

  def __init__(self, root):
    self.root = root
    self.root.title("Mostafa Ultimate Hub - GUI")
    self.root.geometry("400x880")
    self.root.config(bg="#0b0f19")
    self.current_lang = "ar"
    self.luck_balance = 3
    self.puzzle_index = 0

    self.translation_list_ar = [
        ("مرحباً", "hello"),
        ("شكراً", "thank you"),
        ("تفاحة", "apple"),
        ("قطة", "cat"),
        ("كلب", "dog"),
        ("ماء", "water"),
        ("كتاب", "book"),
        ("قلم", "pen"),
        ("شمس", "sun"),
        ("قمر", "moon"),
        ("سيارة", "car"),
        ("منزل", "house"),
        ("مدرسة", "school"),
        ("حاسوب", "computer"),
        ("لعبة", "game"),
        ("صديق", "friend"),
        ("طائر", "bird"),
        ("شجرة", "tree"),
        ("نهر", "river"),
        ("بحر", "sea"),
    ] * 5

    self.translation_list_en = [
        ("hello", "مرحباً"),
        ("thank you", "شكراً"),
        ("apple", "تفاحة"),
        ("cat", "قطة"),
        ("dog", "كلب"),
        ("water", "ماء"),
        ("book", "كتاب"),
        ("pen", "قلم"),
        ("sun", "شمس"),
        ("moon", "قمر"),
        ("car", "سيارة"),
        ("house", "منزل"),
        ("school", "مدرسة"),
        ("computer", "حاسوب"),
        ("game", "لعبة"),
        ("friend", "صديق"),
        ("bird", "طائر"),
        ("tree", "شجرة"),
        ("river", "نهر"),
        ("sea", "بحر"),
    ] * 5
    self.trans_index = 0

    self.puzzles_ar_100 = [
        ("ما هو الشيء الذي كلما أخذت منه كبر؟", "الحفرة"),
        (
            "لغة برمجة شهيرة تبدأ بحرف الباء وتستخدم للذكاء الاصطناعي؟",
            "بايثون",
        ),
        ("ما هو الشيء الذي له عيون ولا يرى؟", "الإبرة"),
        ("ما هو الشيء الذي يتكلم جميع اللغات ولكنه ليس له لسان؟", "الصدى"),
        ("ما هو الشيء الذي يمشي بلا رجلين ولا يدخل إلا بالأذنين؟", "الصوت"),
        ("ما هو الحيوان الذي يحك أذنه بأنفه؟", "الفيل"),
        ("ما هو الباب الذي لا يمكن فتحه؟", "الباب المفتوح"),
        (
            "ما هو الشيء الذي يربط بين شخصين ولكنه لا يلمس أياً منهما؟",
            "الطريق",
        ),
        ("ما هو الشيء الذي كلما جرى تقصر خطاه؟", "العمر"),
        ("ما هو الشيء الذي إذا أزلت نصفه طار؟", "قطار"),
        ("ما هو الشيء الذي يوجد في وسط مكة؟", "حرف الكاف"),
        ("ما هو الشيء الذي تذبح وتبكي عليه؟", "البصل"),
        ("ما هو الشيء الذي يقرصك ولا تراه؟", "الجوع"),
        ("ما هو البيت الذي ليس فيه أبواب ولا نوافذ؟", "بيت الشعر"),
        ("ما هو الشيء الذي لا يسقط أبداً حتى لو رميته من أعلى قمة؟", "الظل"),
        (
            "ما هو الشيء الذي يمشي على أربعة أصباع ثم اثنين ثم ثلاثة؟",
            "الانسان",
        ),
        ("ما هو الشيء الذي يحرق نفسه ليفيد غيره؟", "الشمعة"),
        ("ما هو الشيء الذي كلما زاد نقص؟", "الحفرة"),
        (
            "ما هو الشيء الذي تراه في الليل ثلاث مرات وفي النهار مرة واحدة؟",
            "حرف اللام",
        ),
        ("من هو القائل 'أنا الماء'؟", "السحاب"),
        ("ما هو الشيء الذي له طاقية واحدة وليس له رأس؟", "المسمار"),
        ("ما هو الشيء الذي كلما خطا خطوة فقد جزءاً من جسمه؟", "الحبر"),
        ("ما هو الشيء الذي يولد كبيراً ويموت صغيراً؟", "القمر"),
        (
            "ما هو الشيء الذي تملكه أنت ويستخدمه الآخرون أكثر منك؟",
            "اسمك",
        ),
        ("ما هو الشيء الذي يغنيك عن النور ويحرقك إذا اقتربت منه؟", "الشمس"),
        ("ما هو الشيء الذي يمشي بلا أقدام ويطير بلا أجنحة؟", "السحاب"),
        ("ما هو الشيء الذي لا يمكنه المشي إلا بالضرب؟", "المسمار"),
        ("ما هو الشيء الذي كلما أكل غرق وكلما شرب جاع؟", "النار"),
        ("ما هو الشيء الذي يكتب ولا يقرأ؟", "القلم"),
        ("ما هو الشيء الذي ينبض بلا قلب؟", "الساعة"),
        ("ما هو الشيء الذي يحملك وتحمله في نفس الوقت؟", "الحذاء"),
        (
            "ما هو الشيء الذي له خمس أصابع ولكن ليس له لحم ولا عظم؟",
            "القفاز",
        ),
        (
            "ما هو الشيء الذي يتكون من أربعة حروف وإذا حذفت حرفه الأول طار؟",
            "طائر",
        ),
        ("ما هو الشيء الذي له رقبة ولا رأس له؟", "القميص"),
        ("ما هو الشيء الذي لا يبتل حتى لو دخل البحر؟", "الظل"),
        (
            "ما هو الشيء الذي إذا دخل الماء لا يتغير لونه ولا يذوب؟",
            "الضوء",
        ),
        ("ما هو الشيء الذي نأكله قبل أن يُولد ونأكله بعد أن يموت؟", "البيضة"),
        ("ما هو الشيء الذي يمشي ويقف وليس له أرجل؟", "الساعة"),
        ("ما هو الشيء الذي إذا وضعته في المبردة لا يبرد؟", "الفلفل الحار"),
        ("ما هو الشيء الذي له أسنان كثيرة ولا يعض؟", "المشط"),
        ("ما هو الشيء الذي يرتفع كلما هبط المطر؟", "المظلة"),
        ("ما هو الشيء الذي يمتلك قلباً واحداً لكنه لا ينبض أبداً؟", "الخس"),
        ("ما هو الشيء الذي له بداية وليست له نهاية؟", "الدائرة"),
        ("ما هو الشيء الذي لا يمشي إلا إذا لطمته على رأسه؟", "المسمار"),
        ("ما هو الشيء الذي يمر عبر الزجاج ولا يكسره؟", "الضوء"),
        ("ما هو الشيء الذي يجري ولا يستطيع المشي؟", "الماء"),
        (
            "ما هو الشيء الذي يوجد في القطب الشمالي ولا يوجد في الجنوبي؟",
            "حرف القاف",
        ),
        (
            "ما هو الشيء الذي يفتح بابه أمامك دائماً ولكنك لا تدخل منه؟",
            "المصعد",
        ),
        ("ما هو الشيء الذي إذا غليته تجده جافاً؟", "البيض"),
        ("ما هو الشيء الذي له ورقتان وليس له جذور؟", "الكتاب"),
        ("ما هو الشيء الذي يخترق الجدران ولكنه لا يترك أثراً؟", "الضوء"),
        ("ما هو الشيء الذي يسير بسرعة هائلة ولا يتعب أبداً؟", "الوقت"),
        ("ما هو الشيء الذي يصنع من الخشب ولكنه يحمل طائراً؟", "السفينة"),
        ("ما هو الشيء الذي كلما استعملته صغر حجمه؟", "الصابون"),
        ("ما هو الشيء الذي إذا سقط على الأرض لا ينكسر؟", "الظل"),
        ("ما هو الشيء الذي له أسنان ولكنه لا يأكل ولا يشرب؟", "المنشار"),
        (
            "ما هو الشيء الذي تراه في دقيقة مرتين وفي سنة لا تراه؟",
            "حرف القاف",
        ),
        (
            "ما هو الشيء الذي يجمع بين الزوجين ويفرقهما في نفس الوقت؟",
            "المحامي",
        ),
        ("ما هو الشيء الذي لا يفتح إلا بمفتاح واحد وهو مغلق دائماً؟", "القفل"),
        ("ما هو الشيء الذي يعبر النار ولا يحترق؟", "الماء"),
        ("ما هو الشيء الذي يدخل في النار ولا يشتعل؟", "الماء"),
        ("ما هو الشيء الذي يعلو على الجبال ولا يقدر على حمل ذبابة؟", "الدخان"),
        ("ما هو الشيء الذي يتسع لمئات الأفراد ولكنه لا يسع طفلاً؟", "البحر"),
        ("ما هو الشيء الذي لونه أسود ولا يستطيع العيش إلا في النور؟", "الظل"),
        (
            "ما هو الشيء الذي إذا أكلته كله نفعك وإذا أكلت نصفه قتلك؟",
            "السمسم",
        ),
        ("ما هو الشيء الذي كلما كثر عندك قل وإن قل كثر؟", "المال"),
        ("ما هو الشيء الذي ينام ولا يستيقظ؟", "الميت"),
        (
            "ما هو الشيء الذي يتحدث بدون صوت ولا يفهم لغته إلا العاقل؟",
            "الكتاب",
        ),
        ("ما هو الشيء الذي إذا شرب ماءً مات؟", "النار"),
        (
            "ما هو الشيء الذي نراه في الشتاء خمس مرات وفي الصيف مرتان؟",
            "حرف الشين",
        ),
        ("ما هو الشيء الذي تحمله ويحملك في نفس الوقت؟", "القارب"),
        ("ما هو الشيء الذي لا يمكن كسره بأي شكل؟", "المبتدأ"),
        ("ما هو الشيء الذي له إبهام وأربع أصابع وليس حياً؟", "القفاز"),
        (
            "ما هو الشيء الذي يوجد في أول الشتاء وفي آخر الصيف؟",
            "حرف الشين",
        ),
        ("ما هو الشيء الذي إذا لمسته صاح في وجهك؟", "الجرس"),
        ("ما هو الشيء الذي يجري كالماء ولكنه ليس بماء؟", "الدم"),
        ("ما هو الشيء الذي تحرقه لتستفيد من نوره؟", "الشمعة"),
        ("ما هو الشيء الذي يولد صغيراً ويموت كبيراً؟", "النار"),
        ("ما هو الشيء الذي له وجه بلا عيون وقفاً بلا أذنين؟", "الساعة"),
        ("ما هو الشيء الذي تقطعه ويبكي وتقطعه ويضحكك؟", "البصل"),
        ("ما هو الحيوان الذي إذا قطعت ذيله رجع ونبت من جديد؟", "السحلية"),
        ("ما هو الشيء الذي له لون أحمر وليس له دم؟", "التفاح"),
        ("ما هو الشيء الذي يخترق الزجاج دون أن يخدشه؟", "الضوء"),
        ("ما هو الشيء الذي كلما أخذت منه صغر؟", "الكومة"),
        ("ما هو الشيء الذي يجري أمامك ولا تراه أبداً؟", "الهواء"),
        ("ما هو الشيء الذي يمتلك جناحين ولا يطير؟", "الفندق"),
        ("ما هو الشيء الذي يقرصك بدون أن تلمحه؟", "البرد"),
        ("ما هو الشيء الذي له مفاتيح كثيرة ولا يفتح أي باب؟", "البيانو"),
        ("ما هو الشيء الذي يحترق ليضيء للآخرين؟", "المصباح"),
        (
            "ما هو الشيء الذي يقف في مكانه ولا يتحرك ويوجه الناس؟",
            "إشارة المرور",
        ),
        ("ما هو الشيء الذي له رأس واحد وأربع أرجل وليس له ذراعان؟", "المنضدة"),
        ("ما هو الشيء الذي نأكله طازجاً ونشربه عصيراً؟", "برتقال"),
        ("ما هو الشيء الذي يغطي وجه الإنسان ولكنه يظهر جماله؟", "الابتسامة"),
        ("ما هو الشيء الذي يمشي معك في النور ويختفي في الظلام؟", "الظل"),
        ("ما هو الشيء الذي يفتح ويغلق آلاف المرات في اليوم؟", "العين"),
        (
            "ما هو الشيء الذي يتكون من ستة أحرف وإذا عكسته أصبح اسماً لحيوان؟",
            "سنجاب",
        ),
        ("ما هو الشيء الذي له أجنحة ولا يملك ريشاً؟", "المروحة"),
        ("ما هو الشيء الذي لا يتكلم ولكنه يخبرك بكل الأخبار؟", "الكتاب"),
        ("ما هو الشيء الذي كلما بنيته هدمته؟", "الرمل"),
        ("ما هو الشيء الذي يسكن الجبال ويمشي بلا أقدام؟", "الصدى"),
    ]

    self.puzzles_en_100 = [
        ("What gets bigger the more you take away from it?", "Hole"),
        ("A famous programming language starting with P used for AI?", "Python"),
        ("What has an eye but cannot see?", "Needle"),
        ("What speaks all languages without a tongue?", "Echo"),
        ("What walks with no legs and enters through ears?", "Sound"),
        ("What animal scratches its ear with its nose?", "Elephant"),
        ("What door can never be opened?", "Open door"),
        ("What connects two people without touching them?", "Road"),
        ("What gets shorter the faster it runs?", "Age"),
        ("What flies if you remove its half?", "Train"),
        ("What is in the middle of Mecca?", "Letter"),
        ("What do you slaughter and cry over?", "Onion"),
        ("What pinches you without being seen?", "Hunger"),
        ("What house has no doors or windows?", "Poem"),
        ("What never falls even if thrown from a peak?", "Shadow"),
        ("What walks on four then two then three?", "Man"),
        ("What burns itself to help others?", "Candle"),
        ("What increases the more it decreases?", "Hole"),
        (
            "What do you see 3 times at night and 1 time in day?",
            "Letter",
        ),
        ("Who says 'I am water'?", "Cloud"),
        ("What has a cap and no head?", "Nail"),
        ("What loses part of its body with every step?", "Ink"),
        ("What is born big and dies small?", "Moon"),
        ("What belongs to you but others use it more?", "Name"),
        ("What lights your way and burns you if close?", "Sun"),
        (
            "What walks with no feet and flies with no wings?",
            "Cloud",
        ),
        ("What can only walk by being hit?", "Nail"),
        ("What eats to drown and drinks to starve?", "Fire"),
        ("What writes but cannot read?", "Pen"),
        ("What beats without a heart?", "Clock"),
        ("What carries you while you carry it?", "Shoe"),
        ("What has 5 fingers with no flesh or bone?", "Glove"),
        (
            "What has 4 letters and flies if first is removed?",
            "Bird",
        ),
        ("What has a neck and no head?", "Shirt"),
        ("What never gets wet even in the ocean?", "Shadow"),
        (
            "What does not change color or dissolve in water?",
            "Light",
        ),
        ("What do we eat before birth and after death?", "Egg"),
        ("What walks and stops with no legs?", "Clock"),
        ("What does not cool down in the fridge?", "Chili"),
        ("What has many teeth and does not bite?", "Comb"),
        ("What rises when rain falls?", "Umbrella"),
        ("What has one heart that never beats?", "Lettuce"),
        ("What has a beginning and no end?", "Circle"),
        ("What only walks if hit on the head?", "Nail"),
        ("What passes through glass without breaking it?", "Light"),
        ("What runs and cannot walk?", "Water"),
        ("What is in the North Pole and not South?", "Letter"),
        (
            "What always opens its door for you but you don't enter?",
            "Elevator",
        ),
        ("What is dry even when boiled?", "Egg"),
        ("What has two leaves and no roots?", "Book"),
        ("What penetrates walls leaving no trace?", "Light"),
        ("What runs at huge speed and never gets tired?", "Time"),
        ("What is made of wood and carries a bird?", "Ship"),
        ("What shrinks every time you use it?", "Soap"),
        ("What doesn't break when it hits the ground?", "Shadow"),
        ("What has teeth and neither eats nor drinks?", "Saw"),
        (
            "What is seen twice in a minute and never in a year?",
            "Letter",
        ),
        ("What brings a couple together and separates them?", "Lawyer"),
        ("What opens only with one key and is always locked?", "Lock"),
        ("What passes through fire and doesn't burn?", "Water"),
        ("What enters fire and doesn't burn?", "Water"),
        (
            "What rises above mountains and can't lift a fly?",
            "Smoke",
        ),
        ("What holds hundreds of people and not a child?", "Sea"),
        ("What is black and lives only in light?", "Shadow"),
        (
            "What benefits you if eaten whole and kills if half?",
            "Sesame",
        ),
        (
            "What decreases when abundant and increases when scarce?",
            "Money",
        ),
        ("What sleeps and never wakes?", "Dead"),
        ("What speaks without sound understood by the wise?", "Book"),
        ("What dies if it drinks water?", "Fire"),
        (
            "What is seen five times in winter and twice in summer?",
            "Letter",
        ),
        ("What carries you and you carry it?", "Boat"),
        ("What can never be broken in any way?", "Word"),
        ("What has a thumb and four fingers and isn't alive?", "Glove"),
        ("What is in early winter and late summer?", "Letter"),
        ("What yells at you if touched?", "Bell"),
        ("What runs like water and isn't water?", "Blood"),
        ("What do you burn to use its light?", "Candle"),
        ("What is born small and dies big?", "Fire"),
        ("What has a face with no eyes and back with no ears?", "Clock"),
        ("What makes you cry when cut and makes you laugh?", "Onion"),
        ("What animal regrows its tail if cut?", "Lizard"),
        ("What is red and has no blood?", "Apple"),
        ("What passes through glass without scratching it?", "Light"),
        ("What shrinks as you take from it?", "Pile"),
        ("What runs ahead of you and is never seen?", "Wind"),
        ("What has two wings and cannot fly?", "Hotel"),
        ("What pinches you without being touched?", "Cold"),
        ("What has many keys and opens no doors?", "Piano"),
        ("What burns to light for others?", "Lamp"),
        ("What stands still and guides people?", "Traffic light"),
        ("What has one head and four legs with no arms?", "Table"),
        ("What do we eat fresh and drink as juice?", "Orange"),
        ("What covers human face yet shows beauty?", "Smile"),
        ("What walks with you in light and hides in dark?", "Shadow"),
        ("What opens and closes thousands of times daily?", "Eye"),
        (
            "What has six letters and spells an animal when reversed?",
            "Squirrel",
        ),
        ("What has wings and no feathers?", "Fan"),
        ("What doesn't speak but tells all news?", "Book"),
        ("What do you build and destroy at once?", "Sand"),
        ("What lives on mountains with no feet?", "Echo"),
    ]

    brain = load_brain()
    if brain.get("logged_in") and brain.get("user"):
      self.create_lang_screen()
    else:
      self.create_login_screen()

  def clear_window(self):
    for widget in self.root.winfo_children():
      widget.destroy()

  def create_login_screen(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"

    tk.Label(
        self.root,
        text="Mostafa Hub",
        font=("Arial", 22, "bold"),
        fg="#00ffff",
        bg="#0b0f19",
    ).pack(pady=25)
    login_title = "تسجيل الدخول" if is_ar else "Login"
    tk.Label(
        self.root,
        text=login_title,
        font=("Arial", 14, "bold"),
        fg="#f1c40f",
        bg="#0b0f19",
    ).pack(pady=5)

    brain = load_brain()
    saved_user = brain.get("user", "")
    saved_pass = brain.get("pass", "")

    user_label = "اسم المستخدم:" if is_ar else "Username:"
    tk.Label(
        self.root,
        text=user_label,
        font=("Arial", 10),
        fg="white",
        bg="#0b0f19",
    ).pack(pady=2)
    user_entry = tk.Entry(
        self.root, font=("Arial", 12), width=22, justify="center"
    )
    user_entry.pack(pady=5)
    if saved_user:
      user_entry.insert(0, saved_user)

    pass_label = "كلمة المرور:" if is_ar else "Password:"
    tk.Label(
        self.root,
        text=pass_label,
        font=("Arial", 10),
        fg="white",
        bg="#0b0f19",
    ).pack(pady=2)
    pass_entry = tk.Entry(
        self.root, font=("Arial", 12), width=22, show="*", justify="center"
    )
    pass_entry.pack(pady=5)
    if saved_pass:
      pass_entry.insert(0, saved_pass)

    err_lbl = tk.Label(
        self.root, text="", font=("Arial", 9), fg="#e74c3c", bg="#0b0f19"
    )
    err_lbl.pack(pady=5)

    def verify_login():
      u = user_entry.get().strip()
      p = pass_entry.get().strip()
      if u and p:
        brain_data = load_brain()
        brain_data["user"] = u
        brain_data["pass"] = p
        brain_data["logged_in"] = True

        if u == "عمك" and p == "67":
          brain_data["dev_mode"] = True
        else:
          brain_data["dev_mode"] = False

        save_brain(brain_data)
        self.create_lang_screen()
      else:
        err_text = (
            "الرجاء إدخال اسم المستخدم وكلمة المرور"
            if is_ar
            else "Please enter username and password"
        )
        err_lbl.config(text=err_text)

    btn_text = "دخول وتذكرني" if is_ar else "Login & Remember"
    tk.Button(
        self.root,
        text=btn_text,
        bg="#27ae60",
        fg="white",
        font=("Arial", 11, "bold"),
        width=16,
        height=2,
        command=verify_login,
    ).pack(pady=10)

    def toggle_lang():
      self.current_lang = "en" if self.current_lang == "ar" else "ar"
      self.create_login_screen()

    tk.Button(
        self.root,
        text="English / العربية",
        bg="#34495e",
        fg="white",
        font=("Arial", 9),
        width=15,
        command=toggle_lang,
    ).pack(pady=5)

  def create_lang_screen(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"

    top_bar = tk.Frame(self.root, bg="#0b0f19")
    top_bar.pack(fill="x", padx=15, pady=10)

    def logout():
      brain = load_brain()
      brain["logged_in"] = False
      brain["user"] = ""
      brain["pass"] = ""
      brain["dev_mode"] = False
      save_brain(brain)
      self.create_login_screen()

    tk.Button(
        top_bar,
        text="تسجيل خروج" if is_ar else "Logout",
        bg="#c0392b",
        fg="white",
        font=("Arial", 8),
        command=logout,
    ).pack(side="right")

    brain = load_brain()
    dev_status = (
        ("وضع المطور الخارق مفعل" if is_ar else "Super Dev Mode Active")
        if brain.get("dev_mode")
        else ("وضع المطور غير مفعل" if is_ar else "Dev Mode Inactive")
    )
    tk.Label(
        self.root,
        text=dev_status,
        font=("Arial", 9),
        fg="#2ecc71" if brain.get("dev_mode") else "#e74c3c",
        bg="#0b0f19",
    ).pack(pady=5)

    tk.Label(
        self.root,
        text="Mostafa Hub",
        font=("Arial", 20, "bold"),
        fg="#00ffff",
        bg="#0b0f19",
    ).pack(pady=10)
    tk.Label(
        self.root,
        text="اختر لغة العرض" if is_ar else "Select Display Language",
        font=("Arial", 12, "bold"),
        fg="#f1c40f",
        bg="#0b0f19",
    ).pack(pady=20)

    btn_style = {
        "font": ("Arial", 12, "bold"),
        "fg": "white",
        "width": 20,
        "height": 2,
        "bd": 0,
        "cursor": "hand2",
    }
    tk.Button(
        self.root,
        text="العربية",
        bg="#27ae60",
        command=lambda: self.set_language("ar"),
        **btn_style,
    ).pack(pady=10)
    tk.Button(
        self.root,
        text="English",
        bg="#2980b9",
        command=lambda: self.set_language("en"),
        **btn_style,
    ).pack(pady=10)

  def set_language(self, lang):
    self.current_lang = lang
    self.create_main_menu()

  def create_main_menu(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"

    top_bar = tk.Frame(self.root, bg="#0b0f19")
    top_bar.pack(fill="x", padx=15, pady=5)

    def logout():
      brain = load_brain()
      brain["logged_in"] = False
      brain["user"] = ""
      brain["pass"] = ""
      brain["dev_mode"] = False
      save_brain(brain)
      self.create_login_screen()

    tk.Button(
        top_bar,
        text="تسجيل خروج" if is_ar else "Logout",
        bg="#c0392b",
        fg="white",
        font=("Arial", 8),
        command=logout,
    ).pack(side="right")

    brain = load_brain()
    if brain.get("dev_mode"):
      tk.Label(
          self.root,
          text="[ وضع المطور مفعل ]" if is_ar else "[ Dev Mode Active ]",
          font=("Arial", 9, "bold"),
          fg="#2ecc71",
          bg="#0b0f19",
      ).pack()

    tk.Label(
        self.root,
        text="منصة مصطفى البرمجية" if is_ar else "Mostafa Hub",
        font=("Arial", 16, "bold"),
        fg="#00ffff",
        bg="#0b0f19",
    ).pack(pady=5)

    extra_attempts = brain.get("extra_attempts", 0)
    tk.Label(
        self.root,
        text=(
            f"المحاولات الإضافية المكتسبة: {extra_attempts}"
            if is_ar
            else f"Extra Attempts Won: {extra_attempts}"
        ),
        font=("Arial", 10, "bold"),
        fg="#f1c40f",
        bg="#0b0f19",
    ).pack(pady=3)

    btn_style = {
        "font": ("Arial", 11, "bold"),
        "fg": "white",
        "width": 22,
        "height": 2,
        "bd": 0,
        "cursor": "hand2",
    }

    tk.Button(
        self.root,
        text="آلة حاسبة" if is_ar else "Calculator",
        bg="#16a085",
        command=self.open_calculator,
        **btn_style,
    ).pack(pady=2)
    tk.Button(
        self.root,
        text="لو خيروك (100 خيار)" if is_ar else "Would You Rather (100)",
        bg="#d35400",
        command=self.open_would_you_rather,
        **btn_style,
    ).pack(pady=2)
    tk.Button(
        self.root,
        text="اسأل الكرة" if is_ar else "Ask the Ball",
        bg="#9b59b6",
        command=self.open_magic_ball,
        **btn_style,
    ).pack(pady=2)
    tk.Button(
        self.root,
        text="الهروب من السجن (النصف الأول)"
        if is_ar
        else "Prison Escape (Part 1)",
        bg="#e67e22",
        command=self.open_escape_room_part1,
        **btn_style,
    ).pack(pady=2)

    part1_done = brain.get("part1_completed", False) or brain.get(
        "dev_mode", False
    )
    part2_bg = "#c0392b" if part1_done else "#555555"
    part2_text = (
        (
            "الهروب من السجن (النصف الثاني - 10k)"
            if is_ar
            else "Prison Escape (Part 2 - 10k)"
        )
        if part1_done
        else (
            "النصف الثاني (أنهِ الأول أولاً)"
            if is_ar
            else "Part 2 (Complete Part 1 first)"
        )
    )

    tk.Button(
        self.root,
        text=part2_text,
        bg=part2_bg,
        command=self.open_escape_room_part2,
        **btn_style,
    ).pack(pady=2)

    tk.Button(
        self.root,
        text="المذكرة الذكية" if is_ar else "Smart Notes",
        bg="#3498db",
        command=self.open_memory_notes,
        **btn_style,
    ).pack(pady=2)

    hub2_btn = tk.Button(
        self.root,
        text="★ Moustafa Hub 2 (قسم الألعاب) ★"
        if is_ar
        else "★ Moustafa Hub 2 (Games Hub) ★",
        bg="#ff007f",
        fg="#ffffff",
        font=("Arial", 12, "bold"),
        width=24,
        height=2,
        bd=4,
        relief="ridge",
        cursor="hand2",
        activebackground="#00ffff",
        activeforeground="#000000",
        highlightbackground="#00ffff",
        highlightcolor="#ff00ff",
        highlightthickness=4,
        command=self.open_mostafa_hub_2,
    )
    hub2_btn.pack(pady=6)

    def pulse_glow(step=0):
      if not hub2_btn.winfo_exists():
        return
      glow_colors = [
          ("#ff007f", "#00ffff", "#ffffff"),
          ("#00ff66", "#ff007f", "#000000"),
          ("#00ffff", "#ff0066", "#000000"),
          ("#ffcc00", "#00ff66", "#000000"),
      ]
      bg_col, hl_col, fg_col = glow_colors[step % len(glow_colors)]
      hub2_btn.config(bg=bg_col, highlightbackground=hl_col, fg=fg_col)
      self.root.after(400, pulse_glow, step + 1)

    pulse_glow()

    tk.Button(
        self.root,
        text="تغيير اللغة" if is_ar else "Change Language",
        bg="#7f8c8d",
        command=self.create_lang_screen,
        **btn_style,
    ).pack(pady=2)
    tk.Button(
        self.root,
        text="خروج" if is_ar else "Exit",
        bg="#e74c3c",
        command=self.root.quit,
        **btn_style,
    ).pack(pady=2)

  def open_memory_notes(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="المذكرة الذكية" if is_ar else "Smart Notes",
        font=("Arial", 16, "bold"),
        fg="#3498db",
        bg="#0b0f19",
    ).pack(pady=10)

    note_entry = tk.Entry(self.root, font=("Arial", 12), width=28)
    note_entry.pack(pady=5)

    notes_listbox = tk.Listbox(
        self.root, font=("Arial", 11), width=32, height=12
    )
    notes_listbox.pack(pady=5)

    brain = load_brain()
    for note in brain.get("notes", []):
      notes_listbox.insert(tk.END, note)

    def add_note():
      n = note_entry.get().strip()
      if n:
        notes_listbox.insert(tk.END, n)
        note_entry.delete(0, tk.END)
        b_data = load_brain()
        b_data["notes"] = list(notes_listbox.get(0, tk.END))
        save_brain(b_data)

    def delete_note():
      try:
        selected = notes_listbox.curselection()
        notes_listbox.delete(selected)
        b_data = load_brain()
        b_data["notes"] = list(notes_listbox.get(0, tk.END))
        save_brain(b_data)
      except:
        pass

    tk.Button(
        self.root,
        text="إضافة ملاحظة" if is_ar else "Add Note",
        bg="#27ae60",
        fg="white",
        font=("Arial", 10, "bold"),
        width=15,
        command=add_note,
    ).pack(pady=3)
    tk.Button(
        self.root,
        text="حذف المحددة" if is_ar else "Delete Selected",
        bg="#c0392b",
        fg="white",
        font=("Arial", 10),
        width=15,
        command=delete_note,
    ).pack(pady=3)
    tk.Button(
        self.root,
        text="عودة للرئيسية" if is_ar else "Main Menu",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=15,
        command=self.create_main_menu,
    ).pack(pady=10)

  def open_mostafa_hub_2(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"

    tk.Label(
        self.root,
        text=(
            "Moustafa Hub 2 (قسم الألعاب الذكية)"
            if is_ar
            else "Moustafa Hub 2 (Games Section)"
        ),
        font=("Arial", 15, "bold"),
        fg="#9b59b6",
        bg="#0b0f19",
    ).pack(pady=8)
    tk.Label(
        self.root,
        text=(
            "اختر إحدى الألعاب أو قسم التعليم أدناه:"
            if is_ar
            else "Choose a game or learning section below:"
        ),
        font=("Arial", 10),
        fg="#f1c40f",
        bg="#0b0f19",
    ).pack(pady=2)

    btn_style = {
        "font": ("Arial", 10, "bold"),
        "fg": "white",
        "width": 26,
        "height": 2,
        "bd": 0,
        "cursor": "hand2",
    }

    tk.Button(
        self.root,
        text="حجر، ورقة، مقص" if is_ar else "Rock, Paper, Scissors",
        bg="#2980b9",
        command=self.hub2_rps,
        **btn_style,
    ).pack(pady=4)
    tk.Button(
        self.root,
        text="تحدي تخمين الرقم (1-100)" if is_ar else "Number Guessing Game",
        bg="#d35400",
        command=self.hub2_guess,
        **btn_style,
    ).pack(pady=4)
    tk.Button(
        self.root,
        text="لعبة الألغاز الذكية (100 لغز)"
        if is_ar
        else "Word Puzzle Challenge (100)",
        bg="#c0392b",
        command=self.hub2_puzzle,
        **btn_style,
    ).pack(pady=4)
    tk.Button(
        self.root,
        text="لعبة الذاكرة السريعة" if is_ar else "Fast Memory Game",
        bg="#16a085",
        command=self.hub2_memory,
        **btn_style,
    ).pack(pady=4)
    tk.Button(
        self.root,
        text="لعبة حظ الأرقام" if is_ar else "Lucky Roll Game",
        bg="#8e44ad",
        command=self.hub2_lucky,
        **btn_style,
    ).pack(pady=4)
    tk.Button(
        self.root,
        text="لعبة الترجمة الفورية (100 سؤال)"
        if is_ar
        else "Translation Game (100 Q)",
        bg="#27ae60",
        command=self.hub2_translation,
        **btn_style,
    ).pack(pady=4)

    tk.Button(
        self.root,
        text="فيديو" if is_ar else "Video",
        bg="#e67e22",
        command=self.hub2_fido_turtle,
        **btn_style,
    ).pack(pady=4)

    # زر سيرفر الديسكورد الجديد
    tk.Button(
        self.root,
        text=" سيرفر الديسكورد (Discord)"
        if is_ar
        else "Discord Server",
        bg="#5865F2",
        command=lambda: webbrowser.open("https://discord.gg/J2BUTj689"),
        **btn_style,
    ).pack(pady=4)

    tk.Button(
        self.root,
        text="عودة إلى hub 1" if is_ar else "Back to Hub 1",
        bg="#7f8c8d",
        font=("Arial", 10, "bold"),
        width=20,
        height=2,
        command=self.create_main_menu,
    ).pack(pady=10)

  def hub2_fido_turtle(self):
    try:
      t_screen = turtle.Screen()
      t_screen.title("فيديو - Turtle Hub")
      t_screen.bgcolor("#0b0f19")

      sq = turtle.Turtle()
      sq.speed(0)
      sq.pensize(4)
      sq.color("#00ffff")
      sq.hideturtle()

      t_right = turtle.Turtle()
      t_right.shape("turtle")
      t_right.shapesize(6, 6, 6)
      t_right.color("#2ecc71")
      t_right.penup()
      t_right.goto(220, 0)
      t_right.setheading(90)

      t_left = turtle.Turtle()
      t_left.shape("triangle")
      t_left.shapesize(3, 2, 2)
      t_left.color("#e74c3c")
      t_left.penup()
      t_left.goto(-220, 0)
      t_left.setheading(60)

      t_left_wing = turtle.Turtle()
      t_left_wing.hideturtle()
      t_left_wing.pensize(2)
      t_left_wing.color("#f1c40f")
      t_left_wing.penup()
      t_left_wing.goto(-220, 30)
      t_left_wing.pendown()
      t_left_wing.circle(25)

      def animate_square(angle=0):
        try:
          sq.clear()
          sq.penup()
          sq.goto(0, 0)
          sq.setheading(angle)
          sq.pendown()

          size = 150
          for _ in range(4):
            sq.forward(size)
            sq.left(90)

          t_screen.ontimer(lambda: animate_square(angle + 5), 50)
        except:
          pass

      animate_square()

      writer = turtle.Turtle()
      writer.hideturtle()
      writer.color("white")
      writer.penup()
      writer.goto(0, -240)
      writer.write(
          "فيديو: مربع يدور في المنتصف + سلحفاة عملاقة جداً يمين ونسر يسار",
          align="center",
          font=("Arial", 11, "bold"),
      )

      t_screen.mainloop()
    except Exception as e:
      print("Turtle error:", e)

  def hub2_translation(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="لعبة الترجمة الفورية (100 سؤال)"
        if is_ar
        else "Translation Game (100 Q)",
        font=("Arial", 15, "bold"),
        fg="#27ae60",
        bg="#0b0f19",
    ).pack(pady=10)

    list_src = self.translation_list_ar if is_ar else self.translation_list_en
    if self.trans_index >= len(list_src):
      self.trans_index = 0

    pair = list_src[self.trans_index]

    tk.Label(
        self.root,
        text=f"ترجم الكلمة التالية ({self.trans_index + 1}/{len(list_src)}):"
        if is_ar
        else f"Translate the following ({self.trans_index + 1}/{len(list_src)}):",
        font=("Arial", 10),
        fg="white",
        bg="#0b0f19",
    ).pack(pady=5)

    word_lbl = tk.Label(
        self.root,
        text=pair[0],
        font=("Arial", 16, "bold"),
        fg="#00ffff",
        bg="#0b0f19",
    )
    word_lbl.pack(pady=10)

    ans_entry = tk.Entry(
        self.root, font=("Arial", 12), width=18, justify="center"
    )
    ans_entry.pack(pady=5)

    res_lbl = tk.Label(
        self.root, text="", font=("Arial", 10), fg="#f1c40f", bg="#0b0f19"
    )
    res_lbl.pack(pady=5)

    def check_trans():
      user_input = ans_entry.get().strip().lower()
      correct_ans = pair[1].lower()

      if user_input == correct_ans:
        res_lbl.config(
            text="إجابة صحيحة! (ربحت محاولة إضافية)"
            if is_ar
            else "Correct! (Extra attempt won)",
            fg="#2ecc71",
        )
        brain = load_brain()
        brain["extra_attempts"] = brain.get("extra_attempts", 0) + 1
        save_brain(brain)
        self.trans_index += 1
        self.root.after(700, self.hub2_translation)
      else:
        res_lbl.config(
            text=f"خطأ! الإجابة الصحيحة هي: {correct_ans}"
            if is_ar
            else f"Wrong! Correct was: {correct_ans}",
            fg="#e74c3c",
        )

    tk.Button(
        self.root,
        text="تحقق" if is_ar else "Check",
        bg="#27ae60",
        fg="white",
        font=("Arial", 10, "bold"),
        width=15,
        command=check_trans,
    ).pack(pady=5)

    tk.Button(
        self.root,
        text="عودة إلى hub 2" if is_ar else "Back to Hub 2",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=18,
        command=self.open_mostafa_hub_2,
    ).pack(pady=15)

  def hub2_rps(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="حجر، ورقة، مقص" if is_ar else "Rock, Paper, Scissors",
        font=("Arial", 15, "bold"),
        fg="#2980b9",
        bg="#0b0f19",
    ).pack(pady=10)

    res_lbl = tk.Label(
        self.root,
        text="اختر سلاحك واهزم الكمبيوتر" if is_ar else "Choose your weapon!",
        font=("Arial", 11),
        fg="white",
        bg="#0b0f19",
        wraplength=350,
        justify="center",
    )
    res_lbl.pack(pady=15)

    def play(user_choice):
      choices = ["حجر", "ورقة", "مقص"] if is_ar else ["Rock", "Paper", "Scissors"]
      comp_choice = random.choice(choices)

      if user_choice == comp_choice:
        msg = (
            f"تعادل! الكمبيوتر اختار: {comp_choice}"
            if is_ar
            else f"Tie! Computer chose: {comp_choice}"
        )
        color = "#f1c40f"
      elif (
          (
              user_choice == ("حجر" if is_ar else "Rock")
              and comp_choice == ("مقص" if is_ar else "Scissors")
          )
          or (
              user_choice == ("ورقة" if is_ar else "Paper")
              and comp_choice == ("حجر" if is_ar else "Rock")
          )
          or (
              user_choice == ("مقص" if is_ar else "Scissors")
              and comp_choice == ("ورقة" if is_ar else "Paper")
          )
      ):
        msg = (
            f"أنت الفائز! الكمبيوتر اختار: {comp_choice}"
            if is_ar
            else f"You Win! Computer chose: {comp_choice}"
        )
        color = "#2ecc71"
        brain = load_brain()
        brain["extra_attempts"] = brain.get("extra_attempts", 0) + 1
        save_brain(brain)
        msg += " (ربحت محاولة إضافية)" if is_ar else " (Extra attempt won)"
      else:
        msg = (
            f"فاز الكمبيوتر! الكمبيوتر اختار: {comp_choice}"
            if is_ar
            else f"Computer Wins! Computer chose: {comp_choice}"
        )
        color = "#e74c3c"
      res_lbl.config(text=msg, fg=color)

    btn_s = {
        "font": ("Arial", 11, "bold"),
        "fg": "white",
        "width": 18,
        "height": 2,
    }
    tk.Button(
        self.root,
        text="حجر" if is_ar else "Rock",
        bg="#34495e",
        command=lambda: play("حجر" if is_ar else "Rock"),
        **btn_s,
    ).pack(pady=5)
    tk.Button(
        self.root,
        text="ورقة" if is_ar else "Paper",
        bg="#27ae60",
        command=lambda: play("ورقة" if is_ar else "Paper"),
        **btn_s,
    ).pack(pady=5)
    tk.Button(
        self.root,
        text="مقص" if is_ar else "Scissors",
        bg="#8e44ad",
        command=lambda: play("مقص" if is_ar else "Scissors"),
        **btn_s,
    ).pack(pady=5)

    tk.Button(
        self.root,
        text="عودة إلى hub 2" if is_ar else "Back to Hub 2",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=18,
        command=self.open_mostafa_hub_2,
    ).pack(pady=15)

  def hub2_guess(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="تحدي تخمين الرقم (1-100)" if is_ar else "Number Guessing Game",
        font=("Arial", 15, "bold"),
        fg="#d35400",
        bg="#0b0f19",
    ).pack(pady=10)

    secret_num = random.randint(1, 100)

    hint_lbl = tk.Label(
        self.root,
        text="خمن رقماً بين 1 و 100:"
        if is_ar
        else "Guess a number between 1 and 100:",
        font=("Arial", 11),
        fg="white",
        bg="#0b0f19",
    )
    hint_lbl.pack(pady=5)

    guess_entry = tk.Entry(
        self.root, font=("Arial", 13), width=12, justify="center"
    )
    guess_entry.pack(pady=5)

    res_lbl = tk.Label(
        self.root,
        text="",
        font=("Arial", 10),
        fg="#f1c40f",
        bg="#0b0f19",
        wraplength=350,
        justify="center",
    )
    res_lbl.pack(pady=10)

    def check_guess():
      try:
        val = int(guess_entry.get().strip())
        if val < secret_num:
          res_lbl.config(
              text="الرقم صغير جداً، ارفع الرقم"
              if is_ar
              else "Too low, go higher!",
              fg="#e74c3c",
          )
        elif val > secret_num:
          res_lbl.config(
              text="الرقم كبير جداً، انزل بالرقم"
              if is_ar
              else "Too high, go lower!",
              fg="#e74c3c",
          )
        else:
          res_lbl.config(
              text="أنت بطل! لقد خمنت الرقم الصحيح"
              if is_ar
              else "Hero! You guessed the correct number!",
              fg="#2ecc71",
          )
          brain = load_brain()
          brain["extra_attempts"] = brain.get("extra_attempts", 0) + 1
          save_brain(brain)
      except ValueError:
        res_lbl.config(
            text="الرجاء إدخال رقم صحيح صالح"
            if is_ar
            else "Enter a valid number!",
            fg="#e74c3c",
        )

    tk.Button(
        self.root,
        text="تحقق" if is_ar else "Check",
        bg="#27ae60",
        fg="white",
        font=("Arial", 10, "bold"),
        width=15,
        command=check_guess,
    ).pack(pady=5)
    tk.Button(
        self.root,
        text="عودة إلى hub 2" if is_ar else "Back to Hub 2",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=18,
        command=self.open_mostafa_hub_2,
    ).pack(pady=15)

  def hub2_puzzle(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="لعبة الألغاز الذكية (100 لغز)"
        if is_ar
        else "Word Puzzle Challenge (100)",
        font=("Arial", 15, "bold"),
        fg="#c0392b",
        bg="#0b0f19",
    ).pack(pady=5)

    brain = load_brain()
    is_dev = brain.get("dev_mode", False)
    if is_dev:
      tk.Label(
          self.root,
          text=(
              "[ وضع المطور مفعل: الإجابات تظهر أدناه ]"
              if is_ar
              else "[ Dev Mode Active: Answers shown below ]"
          ),
          font=("Arial", 8, "bold"),
          fg="#2ecc71",
          bg="#0b0f19",
      ).pack(pady=2)

    list_src = self.puzzles_ar_100 if is_ar else self.puzzles_en_100

    if self.puzzle_index >= len(list_src):
      self.puzzle_index = 0

    current_p = list_src[self.puzzle_index]

    counter_text = (
        f"اللغز رقم: {self.puzzle_index + 1} / {len(list_src)}"
        if is_ar
        else f"Puzzle: {self.puzzle_index + 1} / {len(list_src)}"
    )
    tk.Label(
        self.root,
        text=counter_text,
        font=("Arial", 9, "bold"),
        fg="#f1c40f",
        bg="#0b0f19",
    ).pack(pady=2)

    tk.Label(
        self.root,
        text="السؤال:" if is_ar else "Question:",
        font=("Arial", 10),
        fg="#3498db",
        bg="#0b0f19",
    ).pack(pady=2)
    q_lbl = tk.Label(
        self.root,
        text=current_p[0],
        font=("Arial", 11, "bold"),
        fg="white",
        bg="#0b0f19",
        wraplength=350,
        justify="center",
    )
    q_lbl.pack(pady=5)

    if is_dev:
      dev_hint_text = (
          f"الإجابة (وضع المطور): {current_p[1]}"
          if is_ar
          else f"Answer (Dev Mode): {current_p[1]}"
      )
      tk.Label(
          self.root,
          text=dev_hint_text,
          font=("Arial", 9, "bold"),
          fg="#f1c40f",
          bg="#1a1823",
          padx=10,
          pady=4,
      ).pack(pady=5)

    ans_entry = tk.Entry(
        self.root, font=("Arial", 12), width=20, justify="center"
    )
    ans_entry.pack(pady=5)

    res_lbl = tk.Label(
        self.root,
        text="",
        font=("Arial", 10),
        fg="#f1c40f",
        bg="#0b0f19",
        wraplength=350,
        justify="center",
    )
    res_lbl.pack(pady=5)

    def check_ans():
      user_ans = ans_entry.get().strip().lower()
      correct_ans = current_p[1].lower()

      if correct_ans in user_ans:
        res_lbl.config(
            text=(
                "إجابة صحيحة! تم فتح السؤال التالي تلقائياً. (ربحت محاولة إضافية)"
                if is_ar
                else "Correct! Next puzzle unlocked. (Extra attempt won)"
            ),
            fg="#2ecc71",
        )
        b_data = load_brain()
        b_data["extra_attempts"] = b_data.get("extra_attempts", 0) + 1
        save_brain(b_data)

        self.puzzle_index += 1
        self.root.after(700, self.hub2_puzzle)
      else:
        res_lbl.config(
            text=f"خطأ! يجب حل هذا اللغز أولاً للانتقال. (يحتوي على: {current_p[1]})"
            if is_ar
            else f"Wrong! Must solve this first. (Contains: {current_p[1]})",
            fg="#e74c3c",
        )

    tk.Button(
        self.root,
        text="تحقق وانتقل للتالي" if is_ar else "Check & Next",
        bg="#27ae60",
        fg="white",
        font=("Arial", 10, "bold"),
        width=18,
        command=check_ans,
    ).pack(pady=5)
    tk.Button(
        self.root,
        text="عودة إلى hub 2" if is_ar else "Back to Hub 2",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=18,
        command=self.open_mostafa_hub_2,
    ).pack(pady=10)

  def hub2_memory(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="لعبة الذاكرة السريعة" if is_ar else "Fast Memory Game",
        font=("Arial", 15, "bold"),
        fg="#16a085",
        bg="#0b0f19",
    ).pack(pady=10)

    seq = [random.randint(1, 9) for _ in range(4)]
    seq_str = " - ".join(map(str, seq))

    info_lbl = tk.Label(
        self.root,
        text="احفظ هذا التسلسل سريعاً:"
        if is_ar
        else "Memorize this sequence quickly:",
        font=("Arial", 11),
        fg="white",
        bg="#0b0f19",
    )
    info_lbl.pack(pady=5)

    num_lbl = tk.Label(
        self.root,
        text=seq_str,
        font=("Arial", 20, "bold"),
        fg="#f1c40f",
        bg="#0b0f19",
    )
    num_lbl.pack(pady=15)

    res_lbl = tk.Label(
        self.root, text="", font=("Arial", 10), fg="white", bg="#0b0f19"
    )
    res_lbl.pack(pady=5)

    entry_box = tk.Entry(
        self.root, font=("Arial", 14), width=15, justify="center"
    )

    def hide_and_ask():
      num_lbl.config(text="****")
      info_lbl.config(
          text="اكتب التسلسل الذي حفظته:" if is_ar else "Enter the sequence:"
      )
      entry_box.pack(pady=5)
      check_btn.pack(pady=5)

    def verify_memory():
      user_val = entry_box.get().strip().replace(" ", "")
      target_val = "".join(map(str, seq))
      if user_val == target_val:
        res_lbl.config(
            text=(
                "ذاكرتك حديدية! إجابة صحيحة تماماً (ربحت محاولة إضافية)"
                if is_ar
                else "Amazing memory! Correct! (Extra attempt won)"
            ),
            fg="#2ecc71",
        )
        brain = load_brain()
        brain["extra_attempts"] = brain.get("extra_attempts", 0) + 1
        save_brain(brain)
      else:
        res_lbl.config(
            text=f"خطأ! التسلسل الصحيح كان: {target_val}"
            if is_ar
            else f"Wrong! Correct was: {target_val}",
            fg="#e74c3c",
        )

    check_btn = tk.Button(
        self.root,
        text="تحقق" if is_ar else "Check",
        bg="#27ae60",
        fg="white",
        font=("Arial", 10, "bold"),
        width=15,
        command=verify_memory,
    )

    self.root.after(3000, hide_and_ask)

    tk.Button(
        self.root,
        text="عودة إلى hub 2" if is_ar else "Back to Hub 2",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=18,
        command=self.open_mostafa_hub_2,
    ).pack(pady=20)

  def hub2_lucky(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="لعبة حظ الأرقام" if is_ar else "Lucky Roll Game",
        font=("Arial", 15, "bold"),
        fg="#8e44ad",
        bg="#0b0f19",
    ).pack(pady=10)

    self.luck_balance = 3

    balance_lbl = tk.Label(
        self.root,
        text=f"رصيد الحظ المتبقي: {self.luck_balance}"
        if is_ar
        else f"Remaining Luck Balance: {self.luck_balance}",
        font=("Arial", 11, "bold"),
        fg="#f1c40f",
        bg="#0b0f19",
    )
    balance_lbl.pack(pady=5)

    info_lbl = tk.Label(
        self.root,
        text=(
            "اضغط على زر جرب حظك لمعرفة النتيجة (الرقم الصغير يسبب أكبر خسارة):"
            if is_ar
            else "Test your luck (Small numbers bring the biggest loss):"
        ),
        font=("Arial", 10),
        fg="white",
        bg="#0b0f19",
        wraplength=350,
        justify="center",
    )
    info_lbl.pack(pady=5)

    result_box = tk.Label(
        self.root,
        text="---",
        font=("Arial", 13, "bold"),
        fg="#00ffff",
        bg="#0b0f19",
        wraplength=380,
        justify="center",
    )
    result_box.pack(pady=10)

    messages_ar = [
        "حظك رائع اليوم. ستبرمج لعبة عظيمة قريباً. (ربحت محاولة إضافية)",
        "استمر في السعي، حظك التقني في تصاعد مستمر. (ربحت محاولة إضافية)",
        "بداية موفقة لأقوى مشروع برمجيات. (ربحت محاولة إضافية)",
        "أنت محظوظ جداً اليوم، اصنع إنجازك. (ربحت محاولة إضافية)",
    ]
    messages_en = [
        "Great luck today. You will code a great game soon. (Extra attempt won)",
        "Keep going, your tech luck is rising. (Extra attempt won)",
        "Good start for a powerful software project. (Extra attempt won)",
        "You are very lucky today, build your success. (Extra attempt won)",
    ]

    roll_btn = tk.Button(
        self.root,
        text="جرب حظك الآن" if is_ar else "Test Luck",
        bg="#2980b9",
        fg="white",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
    )
    roll_btn.pack(pady=10)

    restart_btn = tk.Button(
        self.root,
        text="إعادة اللعب" if is_ar else "Play Again",
        bg="#27ae60",
        fg="white",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=self.hub2_lucky,
    )

    def roll_luck():
      if self.luck_balance > 0:
        num = random.randint(-100, 100)
        if num <= 50:
          loss_msg = (
              "خسارة فادحة. لقد ظهر لك رقم صغير وتكبدت أكبر نسبة خسارة."
              if is_ar
              else "Massive loss. Small number hit, biggest loss."
          )
          result_box.config(text=f"الرقم: {num}\n{loss_msg}", fg="#e74c3c")
        else:
          msg_list = messages_ar if is_ar else messages_en
          chosen_msg = random.choice(msg_list)
          result_box.config(text=f"الرقم: {num}\n{chosen_msg}", fg="#2ecc71")

          self.luck_balance += 1

          brain = load_brain()
          brain["extra_attempts"] = brain.get("extra_attempts", 0) + 1
          save_brain(brain)

        self.luck_balance -= 1
        balance_lbl.config(
            text=f"رصيد الحظ المتبقي: {self.luck_balance}"
            if is_ar
            else f"Remaining Luck Balance: {self.luck_balance}"
        )

        if self.luck_balance == 0:
          roll_btn.pack_forget()
          result_box.config(
              text=result_box.cget("text")
              + (
                  "\n\nانتهى رصيد حظك."
                  if is_ar
                  else "\n\nLuck balance finished."
              ),
              fg="#e74c3c",
          )
          restart_btn.pack(pady=10)

    roll_btn.config(command=roll_luck)
    tk.Button(
        self.root,
        text="عودة إلى hub 2" if is_ar else "Back to Hub 2",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=18,
        command=self.open_mostafa_hub_2,
    ).pack(pady=10)

  def open_calculator(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="آلة حاسبة" if is_ar else "Calculator",
        font=("Arial", 16, "bold"),
        fg="#16a085",
        bg="#0b0f19",
    ).pack(pady=15)

    entry = tk.Entry(self.root, font=("Arial", 18), justify="right", width=18)
    entry.pack(pady=10)

    def press(val):
      entry.insert(tk.END, val)

    def clear():
      entry.delete(0, tk.END)

    def calculate():
      try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
      except:
        entry.delete(0, tk.END)
        entry.insert(0, "خطأ" if is_ar else "Error")

    btns = [
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("0", ".", "C", "+"),
    ]
    frame = tk.Frame(self.root, bg="#0b0f19")
    frame.pack(pady=10)

    for row in btns:
      r_frame = tk.Frame(frame, bg="#0b0f19")
      r_frame.pack(pady=2)
      for char in row:
        if char == "C":
          b = tk.Button(
              r_frame,
              text=char,
              font=("Arial", 12, "bold"),
              width=4,
              height=2,
              bg="#c0392b",
              fg="white",
              command=clear,
          )
        elif char in ("/", "*", "-", "+"):
          b = tk.Button(
              r_frame,
              text=char,
              font=("Arial", 12, "bold"),
              width=4,
              height=2,
              bg="#d35400",
              fg="white",
              command=lambda c=char: press(c),
          )
        else:
          b = tk.Button(
              r_frame,
              text=char,
              font=("Arial", 12, "bold"),
              width=4,
              height=2,
              bg="#34495e",
              fg="white",
              command=lambda c=char: press(c),
          )
        b.pack(side="left", padx=2)

    tk.Button(
        self.root,
        text="=",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        bg="#27ae60",
        fg="white",
        command=calculate,
    ).pack(pady=5)
    tk.Button(
        self.root,
        text="عودة للرئيسية" if is_ar else "Main Menu",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=15,
        height=1,
        command=self.create_main_menu,
    ).pack(pady=10)

  def open_would_you_rather(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="لو خيروك (100 خيار)" if is_ar else "Would You Rather (100)",
        font=("Arial", 16, "bold"),
        fg="#d35400",
        bg="#0b0f19",
    ).pack(pady=10)

    self.wyR_list_ar = [
        ("تكون طياراً", "تكون رائد فضاء"),
        ("تأكل شوكولاتة", "تأكل فانيليا"),
        ("تعيش في الغابة", "تعيش في المدينة"),
        ("تتكلم مع الحيوانات", "تتكلم بكل لغات العالم"),
        ("تكون ذكياً جداً", "تكون غنياً جداً"),
        ("تطير", "تغوص تحت الماء"),
        ("تتحكم بالنار", "تتحكم بالماء"),
        ("تلعب ألعاب فيديو", "تلعب كرة قدم"),
        ("تستيقظ مبكراً", "تسهر لوقت متأخر"),
        ("تشاهد أفلام أكشن", "تشاهد أفلام كوميديا"),
        ("تكون بطلاً خارقاً", "تكون شريراً خارقاً"),
        ("ترسم لوحة", "تعزف بيانو"),
        ("تسافر بالقطار", "تسافر بالطائرة"),
        ("تأكل بيتزا", "تأكل برجر"),
        ("تدرس رياضيات", "تدرس علوم"),
        ("تقرأ كتاباً", "تشاهد فيلماً"),
        ("تستخدم الكمبيوتر", "تستخدم الهاتف"),
        ("تكون صغيراً في السن للأبد", "تكبر لتصبح حكيماً"),
        ("تعيش في الشتاء", "تعيش في الصيف"),
        ("تذهب إلى البحر", "تذهب إلى الجبل"),
        ("تمتلك سيارة سريعة", "تمتلك دراجة نارية"),
        ("تكتب قصة", "تصنع لعبة"),
        ("تحل لغزاً صعباً", "تفوز بمسابقة رياضية"),
        ("تأكل طعاماً حاراً", "تأكل طعاماً حلواً"),
        ("تنام بدون بطانية", "تنام بدون وسادة"),
        ("تلبس ملابس سوداء", "تلبس ملابس بيضاء"),
        ("تسمع موسيقى هادئة", "تسمع موسيقى حماسية"),
        ("تساعد صديقاً", "تعتمد على نفسك"),
        ("تزور الفضاء", "تزور قاع المحيط"),
        ("تخترع جهازاً جديداً", "تكتشف مكاناً جديداً"),
        ("تأكل تفاحة", "تأكل موزاً"),
        ("تحصل على مال", "تحصل على وقت فراغ"),
        ("تتحدث قليلاً", "تستمع كثيراً"),
        ("تدرس في الليل", "تدرس في الصباح"),
        ("تكون شجاعاً", "تكون ذكياً"),
        ("تزور بلداً عربياً", "تزور بلداً أجنبياً"),
        ("تستخدم القلم الرصاص", "تستخدم قلم الحبر"),
        ("تجلس في الظلام", "تجلس في النور الساطع"),
        ("تمتلك كلباً", "تمتلك قطة"),
        ("تلعب شطرنج", "تلعب مكعب روبيك"),
        ("تصعد سلالم", "تستخدم المصعد"),
        ("تأكل عسلاً", "تأكل مربى"),
        ("تحفظ القرآن الكريم كاملاً", "تتعلم 10 لغات برمجة"),
        ("تزور المستقبل", "تزور الماضي"),
        ("تكون قائد فريق", "تكون فرداً مميزاً"),
        ("تغني بصوت جميل", "ترقص بمهارة"),
        ("تعيش بلا تلفزيون", "تعيش بلا إنترنت منزلي"),
        ("تأكل أرزاً", "تأكل خبزاً"),
        ("تبني بيتاً من خشب", "تبني بيتاً من طوب"),
        ("تفوز بلعبة سهلة", "تتحدى نفسك في لعبة صعبة"),
        ("تسبح في نهر", "تسبح في محيط"),
        ("تنام تحت النجوم", "تنام في قصر فاخر"),
        ("تأكل كيك شوكولاتة", "تأكل كيك جبن"),
        ("تكتب بقلم رصاص", "تطبع بلوحة مفاتيح"),
        ("تزرع شجرة", "تبني سوراً"),
        ("تلبس قبعة", "تلبس نظارة شمسية"),
        ("تسمع طيوراً تغرد", "تسمع أمواج البحر"),
        ("تسافر وحدك", "تسافر مع مجموعة"),
        ("تكون مبرمجاً محترفاً", "تكون مهندساً معمارياً"),
        ("تصمم مواقع إنترنت", "تصمم تطبيقات جوال"),
        ("تلعب لعبة استراتيجية", "تلعب لعبة مغامرات"),
        ("تمتلك طائرة خاصة", "تمتلك يختاً بحرياً"),
        ("تأكل سمكاً", "تأكل لحماً"),
        ("تشرب عصيراً طازجاً", "تشرب شاياً بالحليب"),
        ("تستكشف كهفاً مظلماً", "تتسلق جبلاً عالياً"),
        ("ترتدي معطفاً ثقيلاً", "ترتدي قميصاً خفيفاً"),
        ("تجلس بجانب المدفأة", "تجلس أمام المكيف البارد"),
        ("تكتب باليد اليسرى", "تكتب باليد اليمنى"),
        ("تتعلم السباحة سريعاً", "تتعلم قيادة السيارات سريعاً"),
        ("تفوز بجائزة نوبل", "تفوز ببطولة العالم للرياضة"),
        ("تزور الأهرامات", "تزور برج إيفل"),
        ("تجلس على الشاطئ", "تجلس في حديقة خضراء"),
        ("تقفز بالمنطاد", "تقفز بالمظلة"),
        ("تأكل شطيرة جبن", "تأكل شطيرة بيض"),
        ("تستمع إلى بودكاست", "تستمع إلى كتاب صوتي"),
        ("تدرس تاريخ العالم", "تدرس مستقبل التكنولوجيا"),
        ("تغير لون عينيك", "تغير لون شعرك"),
        ("تكون قادراً على الاختفاء", "تكون قادراً على قراءة الأفكار"),
        ("تمتلك روبوت منزلي", "تمتلك قطاراً خاصاً"),
        ("تأكل بطاطس مقلية", "تأكل بطاطس مسلوقة"),
        ("تحل مسألة معقدة", "تؤلف مقطوعة موسيقيّة"),
        ("تسكن في منزل مصمم على شجرة", "تسكن في منزل زجاجي حديث"),
        ("تتعلم لغة جديدة كل شهر", "تتقن لغة واحدة بطلاقة تامة"),
        ("تصنع فيديو تعليمياً", "تصنع فيديو ترفيهياً"),
        ("تشتري حاسوباً خارقاً", "تشتري منصة ألعاب متطورة"),
        ("تزور جزيرة استوائية", "تزور القطب المتجمد"),
        ("تستيقظ على صوت منبه هادئ", "تستيقظ على صوت الطيور"),
        ("تتناول طعاماً صحياً دائماً", "تتناول طعامك المفضلة بدون قيود"),
        ("تشارك ألعابك مع أصدقائك", "تحتفظ بألعابك لنفسك"),
        ("تكتب مذكراتك كل يوم", "تترك ذكرياتك في عقلك فقط"),
        ("تحصل على ترقية مبكرة", "تبدأ مشروعك الخاص المستقل"),
        ("تساعد في تنظيف المنزل", "تطبخ وجبة العشاء للجميع"),
        ("تزور متحف العلوم", "تزور مدينة ملاهي كبرى"),
        ("تتحدث بهدوء دائم", "تتحمس وتتكلم بحماس"),
        ("تقرأ قصة قصيرة", "تشاهد مقطع فيديو قصيراً"),
        ("تبتكر لعبة جديدة", "تفوز ببطولة ألعاب جاهزة"),
        ("تعيش في عصر الديناصورات", "تعيش في عصر الفضاء المستقبلي"),
        ("تفتخر بإنجازاتك الكبيرة", "تستمر في العمل بصمت وهدوء"),
    ]

    self.wyR_list_en = [
        ("Be a pilot", "Be an astronaut"),
        ("Eat chocolate", "Eat vanilla"),
        ("Live in the forest", "Live in the city"),
        ("Talk to animals", "Speak all languages"),
        ("Be extremely smart", "Be extremely rich"),
        ("Fly", "Dive underwater"),
        ("Control fire", "Control water"),
        ("Play video games", "Play football"),
        ("Wake up early", "Stay up late"),
        ("Watch action movies", "Watch comedy movies"),
        ("Be a superhero", "Be a supervillain"),
        ("Paint a picture", "Play piano"),
        ("Travel by train", "Travel by plane"),
        ("Eat pizza", "Eat burger"),
        ("Study math", "Study science"),
        ("Read a book", "Watch a movie"),
        ("Use computer", "Use phone"),
        ("Stay young forever", "Grow wise"),
        ("Live in winter", "Live in summer"),
        ("Go to the beach", "Go to the mountain"),
        ("Own a fast car", "Own a motorbike"),
        ("Write a story", "Make a game"),
        ("Solve a hard puzzle", "Win a sports contest"),
        ("Eat spicy food", "Eat sweet food"),
        ("Sleep without a blanket", "Sleep without a pillow"),
        ("Wear black clothes", "Wear white clothes"),
        ("Listen to calm music", "Listen to epic music"),
        ("Help a friend", "Be independent"),
        ("Visit space", "Visit ocean floor"),
        ("Invent a new device", "Discover a new place"),
        ("Eat an apple", "Eat a banana"),
        ("Get money", "Get free time"),
        ("Talk a little", "Listen a lot"),
        ("Study at night", "Study in the morning"),
        ("Be brave", "Be smart"),
        ("Visit an Arab country", "Visit a foreign country"),
        ("Use a pencil", "Use an ink pen"),
        ("Sit in the dark", "Sit in bright light"),
        ("Own a dog", "Own a cat"),
        ("Play chess", "Solve Rubik's cube"),
        ("Climb stairs", "Use elevator"),
        ("Eat honey", "Eat jam"),
        ("Memorize the whole Quran", "Learn 10 programming languages"),
        ("Visit the future", "Visit the past"),
        ("Be team leader", "Be unique member"),
        ("Sing nicely", "Dance skillfully"),
        ("Live without TV", "Live without home internet"),
        ("Eat rice", "Eat bread"),
        ("Build a wooden house", "Build a brick house"),
        ("Win an easy game", "Challenge yourself in a hard game"),
        ("Swim in a river", "Swim in an ocean"),
        ("Sleep under the stars", "Sleep in a luxury palace"),
        ("Eat chocolate cake", "Eat cheesecake"),
        ("Write with a pencil", "Type on a keyboard"),
        ("Plant a tree", "Build a fence"),
        ("Wear a hat", "Wear sunglasses"),
        ("Hear birds singing", "Hear ocean waves"),
        ("Travel alone", "Travel with a group"),
        ("Be a professional coder", "Be an architect"),
        ("Design websites", "Design mobile apps"),
        ("Play strategy game", "Play adventure game"),
        ("Own a private jet", "Own a yacht"),
        ("Eat fish", "Eat meat"),
        ("Drink fresh juice", "Drink milk tea"),
        ("Explore dark cave", "Climb high mountain"),
        ("Wear heavy coat", "Wear light shirt"),
        ("Sit by fireplace", "Sit by AC"),
        ("Write with left hand", "Write with right hand"),
        ("Learn swimming fast", "Learn driving fast"),
        ("Win Nobel prize", "Win world sports championship"),
        ("Visit Pyramids", "Visit Eiffel Tower"),
        ("Sit on beach", "Sit in green park"),
        ("Bungee jump", "Sky dive"),
        ("Eat cheese sandwich", "Eat egg sandwich"),
        ("Listen to podcast", "Listen to audiobook"),
        ("Study world history", "Study future tech"),
        ("Change eye color", "Change hair color"),
        ("Turn invisible", "Read minds"),
        ("Own a home robot", "Own a private train"),
        ("Eat french fries", "Eat boiled potatoes"),
        ("Solve complex math", "Compose music"),
        ("Live in a treehouse", "Live in modern glass house"),
        ("Learn new language monthly", "Master one language fully"),
        ("Make educational video", "Make entertainment video"),
        ("Buy super computer", "Buy high-end gaming setup"),
        ("Visit tropical island", "Visit frozen pole"),
        ("Wake up to quiet alarm", "Wake up to birds"),
        ("Eat healthy always", "Eat favorite food freely"),
        ("Share games with friends", "Keep games to yourself"),
        ("Write diary daily", "Keep memories in mind"),
        ("Get early promotion", "Start independent business"),
        ("Help clean house", "Cook dinner for everyone"),
        ("Visit science museum", "Visit massive theme park"),
        ("Speak quietly always", "Speak with passion"),
        ("Read short story", "Watch short video clip"),
        ("Invent new game", "Win pre-made game championship"),
        ("Live in dinosaur era", "Live in future space era"),
        ("Be proud of big achievements", "Keep working in silence"),
    ]

    self.current_wyr_index = 0
    counter_lbl = tk.Label(
        self.root, text="", font=("Arial", 10), fg="#f1c40f", bg="#0b0f19"
    )
    counter_lbl.pack(pady=2)

    q_label = tk.Label(
        self.root,
        text="",
        font=("Arial", 11, "bold"),
        fg="white",
        bg="#0b0f19",
    )
    q_label.pack(pady=10)

    opt1_btn = tk.Button(
        self.root,
        text="",
        font=("Arial", 11, "bold"),
        bg="#2980b9",
        fg="white",
        width=30,
        height=3,
    )
    opt1_btn.pack(pady=8)

    or_lbl = tk.Label(
        self.root,
        text="--- OR ---" if not is_ar else "--- أو ---",
        font=("Arial", 10, "bold"),
        fg="#e74c3c",
        bg="#0b0f19",
    )
    or_lbl.pack(pady=2)

    opt2_btn = tk.Button(
        self.root,
        text="",
        font=("Arial", 11, "bold"),
        bg="#8e44ad",
        fg="white",
        width=30,
        height=3,
    )
    opt2_btn.pack(pady=8)

    feedback_lbl = tk.Label(
        self.root, text="", font=("Arial", 10), fg="#2ecc71", bg="#0b0f19"
    )
    feedback_lbl.pack(pady=5)

    def load_current_pair():
      list_src = self.wyR_list_ar if is_ar else self.wyR_list_en
      if self.current_wyr_index < len(list_src):
        pair = list_src[self.current_wyr_index]
        counter_lbl.config(
            text=f"السؤال {self.current_wyr_index + 1} من 100"
            if is_ar
            else f"Question {self.current_wyr_index + 1} of 100"
        )
        q_label.config(text="لو خيروك بين:" if is_ar else "Would you rather:")
        opt1_btn.config(text=pair[0], command=lambda: choose_option(pair[0]))
        opt2_btn.config(text=pair[1], command=lambda: choose_option(pair[1]))
        feedback_lbl.config(text="")
      else:
        counter_lbl.config(text="")
        q_label.config(
            text="أنهيت جميع الـ 100 اختياراً"
            if is_ar
            else "You finished all 100 options"
        )
        opt1_btn.pack_forget()
        opt2_btn.pack_forget()
        or_lbl.pack_forget()
        feedback_lbl.config(
            text="أنت أسطورة حقيقية (ربحت محاولة إضافية)"
            if is_ar
            else "You are a true legend (Extra attempt won)"
        )
        brain = load_brain()
        brain["extra_attempts"] = brain.get("extra_attempts", 0) + 1
        save_brain(brain)

    def choose_option(choice_text):
      feedback_lbl.config(
          text=(
              f"اختيار رائع: {choice_text}"
              if is_ar
              else f"Great choice: {choice_text}"
          )
      )
      self.current_wyr_index += 1
      self.root.after(700, load_current_pair)

    load_current_pair()
    tk.Button(
        self.root,
        text="عودة للرئيسية" if is_ar else "Main Menu",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=15,
        height=1,
        command=self.create_main_menu,
    ).pack(pady=10)

  def open_magic_ball(self):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    tk.Label(
        self.root,
        text="اسأل الكرة السحرية" if is_ar else "Ask the Magic Ball",
        font=("Arial", 16, "bold"),
        fg="#9b59b6",
        bg="#0b0f19",
    ).pack(pady=10)

    tk.Label(
        self.root,
        text="اكتب سؤالك أو أي جملة للكرة:"
        if is_ar
        else "Type your question or any text:",
        font=("Arial", 10),
        fg="white",
        bg="#0b0f19",
    ).pack(pady=2)
    question_entry = tk.Entry(
        self.root, font=("Arial", 12), width=28, justify="center"
    )
    question_entry.pack(pady=5)

    result_lbl = tk.Label(
        self.root,
        text="اكتب شيئاً واسأل الكرة..." if is_ar else "Type something and ask...",
        font=("Arial", 10),
        fg="#f1c40f",
        bg="#0b0f19",
        wraplength=350,
        justify="center",
    )
    result_lbl.pack(pady=15)

    ball_responses_ar = [
        "لم أفهم.. لكن مستقبلك في البرمجة والذكاء الاصطناعي مبهر وعظيم!",
        "لم أفهم شيئاً! واصل تطوير ألعابك فأنت تسير في الطريق الصحيح.",
        "لم أفهم.. فكرة برمجية عظيمة ستتحقق قريباً جداً فلا تتوقف.",
        "لم أفهم.. أنت مبرمج أسطوري وقادم بقوة لعالم التكنولوجيا.",
        "لم أفهم.. ثق بنفسك واصنع إنجازك القادم بنفسك.",
        "لم أفهم.. الخطوات الثابتة تصنع المجد والنجاح.",
        "لم أفهم.. اصنع عالمك الخاص ولا تنتظر أحداً ليكمله.",
        "لم أفهم.. النجاح يحتاج إلى صبر وتجربة متکررة.",
        "لم أفهم.. الإبداع يكمن في تفاصيل أفكارك الصغيرة.",
        "لم أفهم.. كل خطأ برمجي هو درس جديد يقربك من الاحتراف.",
    ]

    ball_responses_en = [
        "I didn't understand.. But your future in coding and AI is brilliant!",
        (
            "I didn't understand anything! Keep developing games, you're on the"
            " right track."
        ),
        (
            "I didn't understand.. A great coding idea will come to life very"
            " soon."
        ),
        "I didn't understand.. You are a legendary developer rising in tech.",
        "I didn't understand.. Trust yourself and build your own achievements.",
        "I didn't understand.. Steady steps create glory and success.",
        "I didn't understand.. Build your own world and wait for no one.",
        (
            "I didn't understand.. Success requires patience and repeated"
            " experiments."
        ),
        "I didn't understand.. Creativity lies in the details of your ideas.",
        "I didn't understand.. Every bug is a new lesson toward mastery.",
    ]

    def ask_ball():
      user_text = question_entry.get().strip()
      if not user_text:
        err_msg = (
            "الرجاء كتابة شيء أولاً!" if is_ar else "Please write something first!"
        )
        result_lbl.config(text=err_msg, fg="#e74c3c")
        return

      responses = ball_responses_ar if is_ar else ball_responses_en
      chosen_msg = random.choice(responses)
      result_lbl.config(text=chosen_msg, fg="#2ecc71")

    tk.Button(
        self.root,
        text="اسأل الكرة" if is_ar else "Ask Ball",
        bg="#9b59b6",
        fg="white",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=ask_ball,
    ).pack(pady=10)
    tk.Button(
        self.root,
        text="عودة للرئيسية" if is_ar else "Main Menu",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 10),
        width=15,
        height=1,
        command=self.create_main_menu,
    ).pack(pady=10)

  def open_escape_room_part1(self):
    self.run_escape_room_game(part=1)

  def open_escape_room_part2(self):
    brain = load_brain()
    is_ar = self.current_lang == "ar"
    if not brain.get("part1_completed", False) and not brain.get(
        "dev_mode", False
    ):
      self.clear_window()
      tk.Label(
          self.root,
          text="تنبيه قفل القسم" if is_ar else "Section Locked",
          font=("Arial", 16, "bold"),
          fg="#e74c3c",
          bg="#0b0f19",
      ).pack(pady=30)

      tk.Label(
          self.root,
          text="يجب عليك الانتهاء من النصف الأول (الهروب بنجاح) لكي تتمكن من فتح النصف الثاني!"
          if is_ar
          else "You must complete Part 1 (successfully escape) to unlock Part 2!",
          font=("Arial", 11),
          fg="white",
          bg="#0b0f19",
          wraplength=350,
          justify="center",
      ).pack(pady=15)

      tk.Button(
          self.root,
          text="العودة للقائمة" if is_ar else "Back to Menu",
          bg="#7f8c8d",
          fg="white",
          font=("Arial", 11, "bold"),
          width=18,
          height=2,
          command=self.create_main_menu,
      ).pack(pady=30)
      return

    self.run_escape_room_game(part=2)

  def run_escape_room_game(self, part):
    self.clear_window()
    is_ar = self.current_lang == "ar"
    brain = load_brain()
    is_dev = brain.get("dev_mode", False)

    map_width = 10000 if part == 2 else 3000

    title_text = (
        "الهروب من السجن - النصف الأول"
        if (part == 1 and is_ar)
        else (
            "Prison Escape - Part 1"
            if part == 1
            else (
                "الهروب من السجن - النصف الثاني (10k بكسل)"
                if is_ar
                else "Prison Escape - Part 2 (10,000px)"
            )
        )
    )
    tk.Label(
        self.root,
        text=title_text,
        font=("Arial", 9, "bold"),
        fg="#e67e22",
        bg="#0b0f19",
    ).pack(pady=2)

    if is_dev:
      tk.Label(
          self.root,
          text="وضع المطور مفعل: طيران وحارس بطيء"
          if is_ar
          else "Dev Mode Active: Flying & Slow Guard",
          font=("Arial", 8),
          fg="#2ecc71",
          bg="#0b0f19",
      ).pack()

    container_frame = tk.Frame(self.root, bg="#0b0f19")
    container_frame.pack(pady=2)

    canvas = tk.Canvas(
        container_frame,
        width=380,
        height=260,
        bg="#1a1823",
        scrollregion=(0, 0, map_width, 280),
        highlightthickness=1,
        highlightbackground="#444",
    )
    canvas.pack(side="top", fill="both")

    game_state = {
        "started": False,
        "running": False,
        "distance": 0,
        "is_jumping": False,
        "guard_slowed": False,
        "trap_activated": False,
        "last_use_time": 0,
    }

    wall_bg = []
    for i in range(0, map_width, 30):
      r = canvas.create_rectangle(
          i,
          30,
          i + 28,
          230,
          fill="#3d2212" if part == 1 else "#1b263b",
          outline="#111",
      )
      wall_bg.append(r)

    floor = canvas.create_rectangle(
        0, 230, map_width, 280, fill="#2c2c2c", outline="#111"
    )

    exit_door = canvas.create_rectangle(
        map_width - 200,
        50,
        map_width - 110,
        230,
        fill="#2c4c3b" if part == 1 else "#b71540",
        outline="#111",
    )
    exit_handle = canvas.create_rectangle(
        map_width - 125,
        135,
        map_width - 115,
        155,
        fill="#888",
        outline="#333",
    )

    trap_x = 4500 if part == 2 else 1200
    trap_item = canvas.create_oval(
        trap_x, 205, trap_x + 20, 225, fill="#f1c40f", outline="#e67e22"
    )

    if part == 1:
      obstacles_data = [
          (250, "red"),
          (450, "black"),
          (700, "red"),
          (1000, "black"),
          (1300, "red"),
          (1650, "black"),
          (2000, "red"),
          (2400, "black"),
      ]
    else:
      obstacles_data = []
      for pos_x in range(400, 9500, 450):
        o_type = "red" if (pos_x // 450) % 2 == 0 else "black"
        obstacles_data.append((pos_x, o_type))

    obs_items = []
    for pos, o_type in obstacles_data:
      color = "#e74c3c" if o_type == "red" else "#111111"
      outline_c = "#962d22" if o_type == "red" else "#444444"
      h_y = 210 if o_type == "red" else 190
      rect = canvas.create_rectangle(
          pos, h_y, pos + 25, 230, fill=color, outline=outline_c
      )
      obs_items.append((rect, o_type, pos))

    guard_parts = [
        canvas.create_rectangle(-10, 160, 15, 190, fill="#d4a373"),
        canvas.create_rectangle(
            -15, 150, 20, 162, fill="#c0392b" if part == 2 else "#1d3557"
        ),
        canvas.create_rectangle(
            -20, 190, 25, 230, fill="#e67e22" if part == 2 else "#457b9d"
        ),
        canvas.create_rectangle(-15, 230, 20, 245, fill="#111"),
    ]

    player_parts = [
        canvas.create_rectangle(150, 160, 180, 190, fill="#d4a373"),
        canvas.create_rectangle(150, 155, 180, 162, fill="#5c4033"),
        canvas.create_rectangle(140, 190, 190, 230, fill="#e67f51"),
        canvas.create_rectangle(145, 230, 185, 245, fill="#222"),
    ]

    status_lbl = tk.Label(
        self.root,
        text="اضغط بدء المطاردة" if is_ar else "Click Start",
        font=("Arial", 9, "bold"),
        fg="#f1c40f",
        bg="#0b0f19",
    )
    status_lbl.pack(pady=2)

    def start_chase():
      if game_state["started"]:
        return

      game_state["started"] = True
      game_state["running"] = True

      if part == 1:
        msg = (
            (
                "الحارس يطاردك بطيء جداً! احذر العقبات."
                if is_ar
                else "Guard chasing very slowly! Watch obstacles."
            )
            if not is_dev
            else "وضع المطور مفعل"
        )
      else:
        msg = (
            (
                (
                    "الحارس يطاردك! احذر العقبات والفخ أو استخدم زر إبطاء"
                    " الحارس (كل 30 ثانية)."
                    if is_ar
                    else (
                        "Guard chasing! Watch obstacles/trap or use slowdown"
                        " button (every 30s)."
                    )
                )
            )
            if not is_dev
            else "وضع المطور مفعل"
        )

      status_lbl.config(text=msg, fg="#e74c3c" if not is_dev else "#2ecc71")
      run_game_loop()

    def run_game_loop():
      if not game_state["running"]:
        return

      game_state["distance"] += 0.9

      step_speed = 4
      for r in wall_bg:
        canvas.move(r, -step_speed, 0)
      canvas.move(exit_door, -step_speed, 0)
      canvas.move(exit_handle, -step_speed, 0)
      canvas.move(trap_item, -step_speed, 0)
      for rect, o_type, pos in obs_items:
        canvas.move(rect, -step_speed, 0)

      t_coords = canvas.coords(trap_item)
      p_coords_box = canvas.coords(player_parts[2])
      if t_coords and p_coords_box:
        if (
            p_coords_box[2] > t_coords[0]
            and p_coords_box[0] < t_coords[2]
            and p_coords_box[3] > t_coords[1]
            and not game_state["trap_activated"]
        ):
          game_state["trap_activated"] = True
          status_lbl.config(
              text="لمست الفخ! أصبحت سرعة الحارس خارقة!"
              if is_ar
              else "Trap touched! Guard hyper speed!",
              fg="#f1c40f",
          )

      if game_state["guard_slowed"]:
        guard_speed = 0.05
      elif game_state["trap_activated"]:
        guard_speed = 3.5
      else:
        if part == 1:
          guard_speed = 0.1
        else:
          guard_speed = 0.12 if is_dev else 0.65

      for part_item in guard_parts:
        canvas.move(part_item, guard_speed, 0)

      g_coords = canvas.coords(guard_parts[0])
      p_coords = canvas.coords(player_parts[0])
      if g_coords and p_coords and g_coords[2] >= p_coords[0] and not is_dev:
        game_state["running"] = False
        status_lbl.config(
            text="قبض عليك الحارس! اضغط إعادة!"
            if is_ar
            else "Guard caught you! Restart!",
            fg="#e74c3c",
        )
        return

      for rect, o_type, pos in obs_items:
        r_coords = canvas.coords(rect)
        if r_coords and p_coords_box:
          if (
              p_coords_box[2] > r_coords[0]
              and p_coords_box[0] < r_coords[2]
              and p_coords_box[3] >= r_coords[1]
              and not game_state["is_jumping"]
          ):
            if o_type == "red" and not is_dev:
              game_state["running"] = False
              status_lbl.config(
                  text="اصطدمت بالعقبة الحمراء! اضغط إعادة!"
                  if is_ar
                  else "Hit red obstacle! Restart!",
                  fg="#e74c3c",
              )
              return

      door_coords = canvas.coords(exit_door)
      if door_coords and door_coords[0] <= 180:
        game_state["running"] = False
        status_lbl.config(
            text=(
                "تهانينا الأسطورية! هربت بنجاح! (ربحت محاولة إضافية)"
                if is_ar
                else (
                    "Legendary congrats! Escaped successfully! (Extra attempt"
                    " won)"
                )
            ),
            fg="#2ecc71",
        )
        b_data = load_brain()
        b_data["extra_attempts"] = b_data.get("extra_attempts", 0) + 1

        if part == 1:
          b_data["part1_completed"] = True

        save_brain(b_data)
        return

      if game_state["running"]:
        self.root.after(35, run_game_loop)

    def jump_action():
      if not game_state["running"] or game_state["is_jumping"]:
        return
      game_state["is_jumping"] = True

      jump_height = -120 if is_dev else -85
      for part_item in player_parts:
        canvas.move(part_item, 0, jump_height)

      for r in wall_bg:
        canvas.move(r, -20, 0)
      canvas.move(exit_door, -20, 0)
      canvas.move(exit_handle, -20, 0)
      canvas.move(trap_item, -20, 0)
      for rect, o_type, pos in obs_items:
        canvas.move(rect, -20, 0)

      def land():
        for part_item in player_parts:
          canvas.move(part_item, 0, -jump_height)
        game_state["is_jumping"] = False

      self.root.after(700, land)

    if part == 2:
      hack_frame = tk.Frame(self.root, bg="#0b0f19")
      hack_frame.pack(pady=2)

      tk.Label(
          hack_frame,
          text="زر إبطاء الحارس (كل 30 ثانية):"
          if is_ar
          else "Slow Guard Button (Every 30s):",
          font=("Arial", 8),
          fg="#f1c40f",
          bg="#0b0f19",
      ).pack(side="left", padx=2)

      def use_slow_hack():
        current_time = time.time()
        if current_time - game_state["last_use_time"] < 30:
          remaining = int(30 - (current_time - game_state["last_user_time"]))
          status_lbl.config(
              text=f"الزر قيد الانتظار! انتظر {remaining} ثانية"
              if is_ar
              else f"Cooldown! Wait {remaining}s",
              fg="#e74c3c",
          )
          return

        game_state["last_use_time"] = current_time
        game_state["guard_slowed"] = True

        for part_item in guard_parts:
          canvas.move(part_item, -20, 0)

        status_lbl.config(
            text="تم إبطاء الحارس وإبعاده 20 بكسل لمدة 10 ثوانٍ!"
            if is_ar
            else "Guard slowed & pushed back 20px for 10s!",
            fg="#2ecc71",
        )

        def restore_guard():
          game_state["guard_slowed"] = False

        self.root.after(10000, restore_guard)

      tk.Button(
          hack_frame,
          text="إبطاء الحارس" if is_ar else "Slow Guard",
          bg="#8e44ad",
          fg="white",
          font=("Arial", 8, "bold"),
          command=use_slow_hack,
      ).pack(side="left", padx=2)

    ctrl_frame = tk.Frame(self.root, bg="#0b0f19")
    ctrl_frame.pack(pady=4)

    tk.Button(
        ctrl_frame,
        text="بدء المطاردة" if is_ar else "Start Chase",
        bg="#27ae60",
        fg="white",
        font=("Arial", 9, "bold"),
        width=12,
        command=start_chase,
    ).pack(side="left", padx=3)
    tk.Button(
        ctrl_frame,
        text="قفز (Jump)" if is_ar else "Jump",
        bg="#2980b9",
        fg="white",
        font=("Arial", 9, "bold"),
        width=12,
        command=jump_action,
    ).pack(side="left", padx=3)
    tk.Button(
        ctrl_frame,
        text="إعادة" if is_ar else "Restart",
        bg="#c0392b",
        fg="white",
        font=("Arial", 9, "bold"),
        width=10,
        command=lambda: self.run_escape_room_game(part),
    ).pack(side="left", padx=3)

    tk.Button(
        self.root,
        text="عودة إلى hub 2" if is_ar else "Back to Hub 2",
        bg="#7f8c8d",
        fg="white",
        font=("Arial", 9),
        width=18,
        command=self.open_mostafa_hub_2,
    ).pack(pady=5)


if __name__ == "__main__":
  root = tk.Tk()
  app = MostafaGUIHub(root)
  root.mainloop()
