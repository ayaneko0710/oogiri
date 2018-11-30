import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    
    # お題リスト
    odai = [
        "こんなデスノートは嫌だ！",
        "カピバラ大繁殖！そのとき、どうする",
        "スリランカの国技は？",
        "ネットオークションで史上最高額の落札品とは",
        "平安時代の悩み事相談とは？",
        "セレブな桃太郎にありがちなこと",
        "カンボジアで月に3回やってくる祭は？",
        "美女とイケメンの間に生まれた子どもに、偏見を言ってください。",
        "世間には知られていないペッパーくんの弊害を教えてください",
        "｢お疲れ様です｣に代わる業界用語を教えてください",
        "明日から変わる1万円札の肖像画の人物を教えてください",
        "大事な会議に遅刻しました 韻を踏みながら謝罪してください",
        "叶姉妹が唯一買えなかった商品とは",
        "Appleが新しいカードを発売なんていう名前？",
        "2154年に流行っているダイエット方法を教えてください",
        "スーパーで買った商品の裏にKの文字が何を意味している？",
        "家に帰ると部屋が荒らされていた家の防犯カメラに写っていたのは？",
        "マイクラを開くとあるMODがDLされていたどんなMOD？",
        "平成最後の日に島根県で起こった事件を教えてください",
        "使いそうで使わない言葉第56位はなに？",
        "毎日を楽しくする100のこと第13はなに？",
        "明治時代の月9ドラマを教えてください",
        "任天堂がファミマとコラボして作ったゲームを教えてください",
        "クリスマスでサンタさんのアクロバティックな登場を教えてください",
        "小学2年生がギリできる神業を教えてください",
        "53歳のタカシくんの転職先はどこ？",
        "「洗濯物はお父さんとは別にして」より3倍傷つく言葉を教えてください",
        "2065年の流行語大賞を教えてください",
        "やったら絶対嫌われる特技はなんですか？",
        "Pokemon GOが突然のサービス終了なぜ？",
        "3年後の福岡市長を教えてください",
        "日本にある1番学力が高い小学校を教えてください",
        "いるようでいらない画像を貼ってください",
        "先月の給料が払われてない理由を教えてください",
        "ドラえもんが唯一扱えなかった道具を教えてください",
        "マイケルジャクソンが世間に公表しなかった伝説の曲を教えてください",
        "2056年の小学1年生の世界チャンピオンを教えてください",
        "スタバが「えっ？」て思う新商品を発表、さてどんなの？",
        "2015年7月のジャンプの懸賞で一番雑魚いものはなんですか？",
        "HIKAKINがYoutubeで大炎上、なぜ？",
        "ある地域に伝わる独特なしゃっくりの止め方を教えてください",
        "一瞬信じてしまいそうな嘘をついてください。",
        "あなたのコンピュータがウイルスに感染したようです。何が起こった？",
        "悪者を退治してくれる正義のヒーローが現れましたが、みんな素直に応援できません。なぜ？",
        "けん玉の間違った使い方を答えよ。",
        "「SNS」何の略？",
        "「FPS」何の略？",
        "ひらがな５文字でかっこつけて下さい。",
        "サザエさんがフルマラソンに挑戦したいと言い出した。動機は？",
        "雪崩に巻き込まれたが奇跡的に生還。第一声は？",
        "「16%」何の確率？",
        "公園のトイレに貼り紙が貼ってあった。なんて書いてた？",
        "こんなツンデレはイヤだ！",
        "こんなディズニーランドはイヤだ！",
        "こんな親子丼はイヤだ！どんな親子丼？",
        "電車の遅延、その原因は？",
        "「GTO」何の略？",
        "アンパンマンが顔が変わった時にテンションが下がる理由を教えてください。",
        "こんな海水浴場はイヤだ！どんな海水浴場？",
        "ノストラダムスが予言を外した理由は？",
        "自動販売機で当たりが出た！何が出てきた！？",
        "新発売のスマートフォンにクレームが殺到。なぜ？",
        "しんちゃんの将来の夢を教えてください。",
        "2020年のハロウィンは盛り上がらなかった何故？",
    ]
    if message.content.startswith("おはよう"):
        if client.user !=message.author:
            m = "おはようございます" + message.author.name + "さん！"
            await client.send_message(message.channel, m)
    if message.content.startswith("こんにちわ"):
        if client.user !=message.author:
            m = "こんにちわ" + message.author.name + "さん！"
            await client.send_message(message.channel, m)
    if message.content.startswith("こんばんわ"):
        if client.user !=message.author:
            m = "こんばんわ" + message.author.name + "さん！"
            await client.send_message(message.channel, m)
    if message.content.startswith("さようなら"):
        if client.user !=message.author:
            m = "さようなら" + message.author.name + "さん(´Д⊂ｸﾞｽﾝ..."
            await client.send_message(message.channel, m)
    if message.content.startswith("ばいばい"):
        if client.user !=message.author:
            m = "さようなら" + message.author.name + "さん(´Д⊂ｸﾞｽﾝ..."
            await client.send_message(message.channel, m)
    if message.content.startswith("バイバイ"):
        if client.user !=message.author:
            m = "さようなら" + message.author.name + "さん(´Д⊂ｸﾞｽﾝ..."
            await client.send_message(message.channel, m)
    if message.content.startswith("おやすみ"):
        if client.user !=message.author:
            m = "おやすみなさい💤" + message.author.name + "さん！"
            await client.send_message(message.channel, m)
    if message.content.startswith("氏ね"):
        if client.user !=message.author:
            m = "暴言はやめましょう" + message.author.name + "さん..."
            await client.send_message(message.channel, m)
    if message.content.startswith("うるさい"):
        if client.user !=message.author:
            m = "は？なんやと" + message.author.name + "！"
            await client.send_message(message.channel, m)
    if message.content.startswith("お題"):
        if client.user != message.author:
            i = random.randint(0, len(odai)-1)
            m = odai[i]
            await client.send_message(message.channel, m)

client.run('NTA4OTA4OTM4NjUwMDU4NzYy.DtJ8VQ.FEv0b_v_hk9F6_8NEWVxd8SAiIQ')