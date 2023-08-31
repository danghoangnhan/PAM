import os

base_directory = os.getcwd()
static_dir = os.path.join(base_directory, "static")
csv_dir = os.path.join(static_dir, "csv")
audio_dir = os.path.join(static_dir, "audio")
font_dir = os.path.join(static_dir, "font", "Noto_Sans_TC", "static", "NotoSansTC-Black.ttf")
user_dir = os.path.join(csv_dir, "user.csv")
history_dir = os.path.join(csv_dir, "history.csv")
exam_dir = os.path.join(csv_dir, "exam.csv")




