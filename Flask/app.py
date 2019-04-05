from flask import Flask, render_template, redirect,url_for, jsonify, send_from_directory
import yony_sector_data
import sector_ranking
import evaluations
import os

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/index.html")
def index_file():

    return render_template("index.html")


@app.route("/about.html")
def about():

    return render_template("about.html")

@app.route("/stocks.html")
def stocks():

    return render_template("stocks.html")


@app.route("/sector.html")
def sector():

    return render_template("sector.html")


@app.route("/disclaimer.html")
def disclaimer():

    return render_template("disclaimer.html")


@app.route("/services.html")
def services():

    return render_template("services.html")

@app.route("/sector_yony_df_all")
def yoy_route():
    to_return = yony_sector_data.sector_yony_df_all()
    # print(to_return)
    return jsonify(to_return)


@app.route("/sector_yoy_top4")
def sector_ranking_top4():
    to_return = yony_sector_data.sector_yony_df_top4()
    # print(to_return)
    return jsonify(to_return)

@app.route("/sector_yoy_bot4")
def sector_ranking_bot4():
    to_return = yony_sector_data.sector_yony_df_bot4()
    # print(to_return)
    return jsonify(to_return)

@app.route("/sector_rank_all")
def sector_rank_all():
    to_return = sector_ranking.sector_ranking_all()
    # print(to_return)
    return jsonify(to_return)

@app.route("/sector_rank_filter")
def sector_rank_filter():
    to_return = sector_ranking.sector_ranking_filtered()
    # print(to_return)
    return jsonify(to_return)

@app.route("/insights.html")
def insights():
	return render_template("insights.html")


@app.route("/ebitda_multiple")
def ebita_multiple():
    to_return = evaluations.ebitda_multiple_full()
    return jsonify(to_return)

@app.route("/ev_sales_multiple")
def ev_sales_multiple():
    to_return = evaluations.ev_sales_mutiple_full()
    return jsonify(to_return)

@app.route("/eps_multiple")
def eps_multiple():
    to_return = evaluations.eps_multiple_full()
    return jsonify(to_return)


@app.route("/book_value_to_revenue_multiple")
def book_value_to_revenue_multiple():
    to_return = evaluations.book_value_to_revenue_multiple_full()
    return jsonify(to_return)
book_value_to_revenue_multiple

@app.route("/top_bottom/<parmstoparse>")
def top_bottom(parmstoparse):
    print(parmstoparse)
    parmstoparse = str(parmstoparse)
    model,topORbottom = parmstoparse.split(',')
    print(model)
    print(topORbottom)
    to_return = evaluations.top_bottom(model,topORbottom)
    return jsonify(to_return)
    # return ("done")

@app.route("/table.html")
@app.route('/table')
def table():

    return render_template("table.html")

@app.route("/update_desc/<modelname>")
def update_desc(modelname):
    print(modelname)
    to_return = evaluations.update_desc(modelname)
    return jsonify(to_return)


if __name__ == "__main__":
    app.run(debug=True)
