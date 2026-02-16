import random

secret = random.randint(1, 50)
attempts = 5

print("数字当てゲーム！")
print("1から50の間の数字を考えています。")
print(f"{attempts}回のチャンスがあります。\n")

while attempts > 0
    guess = input("数字を入力してください: ")
    if not guess.isdigit(
        print("有効な数字を入力してください。\n")
        continue

    guess = int(guess)
    attempts=attempts-1

    if guess==secret:
        print(f"正解です！答えは {secret} でした。")
        break
    elif guess > secret:  
        print("小さすぎます！\n")
    else:
        print("大きすぎます！\n")

    if attempts==0 and guess!=secret:
        print(f"チャンスがなくなりました。正解は {secret} でした。")