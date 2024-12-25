from flask import Flask, render_template, request
import random

app = Flask(__name__)

# 生成随机数
secret_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def guess_game():
    global secret_number
    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form.get("guess"))
            if guess == secret_number:
                message = "恭喜你，答对了！"
                secret_number = random.randint(1, 100)  # 重置随机数
            elif guess > secret_number:
                message = "大了！"
            else:
                message = "小了！"
        except ValueError:
            message = "请输入有效的数字！"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)