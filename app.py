from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/footwear/")
def footwear():
    _footwear = [
        {
            "name": "Кросовки",
            "price": "5 $",
            "description": "Отличные кроссовки для спорта и активного отдыха",
        },
        {
            "name": "Кеды",
            "price": "3 $",
            "description": "Свободная и удобная повседневная обувь",
        },
        {
            "name": "Туфли",
            "price": "10 $",
            "description": "Не знаешь что обуть.... при выходе в свет, тогда бери наши туфли стоят дешево но по качеству не уступают дорогим",
        }
    ]
    return render_template("footwear.html", content=_footwear)


@app.route("/jacket/")
def jacket():
    _jacket = [
        {
            "name": "Ветровка",
            "price": "5 $",
            "description": "хорошая и удобная верхняя одежда на весну и осень",
        },
        {
            "name": "Дубленка",
            "price": "20 $",
            "description": "В ней тепло и уютно...",
        },
        {
            "name": "Пальто",
            "price": "15 $",
            "description": "Будь самым стильным на районе",
        }
    ]
    return render_template("jacket.html", content=_jacket)


@app.route("/clothes/")
def clothes():
    _clothes = [
        {
            "name": "Футболка",
            "price": "2 $",
            "description": "удобная повседневная одежда",
        },
        {
            "name": "Кепка",
            "price": "1 $",
            "description": "стильная кепка  для любого случая",
        }
        
    ]
    return render_template("clothes.html", content=_clothes)


if __name__ == "__main__":
    app.run(debug=True)
