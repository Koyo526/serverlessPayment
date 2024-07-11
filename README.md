# serverlessPayment

## 使用技術
<p style="display: inline">
    <img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=for-the-badge">
    <img src="https://img.shields.io/badge/-flask-000000.svg?logo=python&style=for-the-badge">
    <img src="https://img.shields.io/badge/-javascript-F7DF1E.svg?logo=python&style=for-the-badge">
    <img src="https://img.shields.io/badge/-Amazon%20aws-232F3E.svg?logo=amazon-aws&style=for-the-badge">
    <img src="https://img.shields.io/badge/-AWS%20lambda-232F3E.svg?logo=aws-lambda&style=for-the-badge">
    <img src="https://img.shields.io/badge/-amazon%20S3-232F3E.svg?logo=amazon-s3&style=for-the-badge">
</p>


## 開発の目的
<p>研究室においてエスプレッソマシンを運用しており、1杯50円で販売している。（身内の売買なので正確には豆の代金徴収と思ってください。）今までは現金で徴収していたが、運用者（主）の小銭が多くなりすぎたので、小規模な注文・決済システムが欲しいというのが開発の始まり。<br>イベント駆動型ペイメントシステム</p>

## プロダクトの詳細
<p>AWS Lambdaを用いたサーバーレスイベント駆動型システムになっている。開発フレームワークはFlask、バックエンドはPython、フロントはjavascript（フロントは現在開発中）<br>
キャッシュレス支払い方法としてPayPayを使用。(<a href="https://github.com/paypay/paypayopa-sdk-php">PayPay API</a>)
</p>

## Install
Python version : 3.12.0<br>


After clone
```
pip install -r requirements.txt
```

### start locally

```
python3 wsgi.py
```
After Access to "http://127.0.0.1:5000/"