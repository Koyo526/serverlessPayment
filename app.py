from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import uuid

app = Flask(__name__)

DATA_FILE = 'data.json'
DN = "http://127.0.0.1:5000"

#関数系は後で別ファイルに記載する
#デプロイする際はできるだけハードコーディングは避けるようにする
#mapでハッシュにするところまでできるとなお良いが今回はサーバーレスアプリの開発がメインなのでそこまでは求めない
def read_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

#トップページ / も作ろう。index.htmlを活用
#できればbase.html などでトップバーやテイルバーも実装すると良き




#レジスターでPayPayIDの登録も追加する
#DBに登録した時間datatimeも追加する
#後で何日でデータを削除するかをユーザが指定できるようにする。
#example:1時間、12時間、1日、１週間、１ヶ月、１年、無期限
#UUIDがすでに使われていないかチェックするプログラムも欲しい
#CreateUUID return uuid 
#checkUUID while <uuid in DB> reCreate: else return uuid   
#登録が終わった後、登録完了画面とQRコード、select/uuidのURLを表示する
#登録完了画面も作ろう！

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        num = request.form['number']
        data = []
        unique_id = str(uuid.uuid4())
        for i in range(int(num)):
            name = request.form['name_'+str(i)]
            price = float(request.form['price_'+str(i)])
            item = {'name': name, 'price': price}
            data.append(item)
        
        json_data = read_data()
        json_data[unique_id] = data
        write_data(json_data)
        
        return redirect(url_for('show',uuid=unique_id))
    return render_template('register.html')


#登録完了画面
#URLとQRコードを表示
#Select画面への遷移も欲しい
#URLはコピぺできる
#QRはダウンロードできる
#共有機能もあるといいな
@app.route('/show/<uuid>',methods=['GET','POST'])
def show(uuid):
    URL = DN+"/select/"+uuid
    return render_template('show.html', URL = URL)


#UUIDからどの商品を表示するかが決まる
#UUIDがDBにない時の処理も考える
@app.route('/select/<uuid>', methods=['GET', 'POST'])
def select(uuid):
    json_data = read_data()
    print(uuid)
    
    if request.method == 'POST':
        quantities = request.form.to_dict()
        total = 0
        data = json_data[uuid]
        for item in data:
            quantity = int(quantities.get(item['name'], 0))
            total += item['price'] * quantity
        return redirect(url_for('total', total=total))
    else:
        #ここにuuidからselectページを生成するコードを書く
        pass
    print(json_data[uuid])
    return render_template('select.html', items=json_data[uuid],uuid=uuid)

@app.route('/total')
def total():
    #トータルで支払い金額を表示
    #PayPayの支払いボタンを表示してPayPayの画面に遷移

    total = request.args.get('total', 0)
    return render_template('total.html', total=total)


#支払い完了画面も欲しい
#いくらを誰に支払いました、ありがとう

#DB制御は後で考える
#ユーザが指定した期間でデータが消えるように制御する
#その時はUUIDからデータを削除
#