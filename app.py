from flask import Flask, request, render_template, jsonify
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData


app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route("/predict",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data=CustomData(
            Carat=float(request.form.get("carat")),
            Depth=float(request.form.get("depth")),
            Table=float(request.form.get("table")),
            x=float(request.form.get("x")),
            y=float(request.form.get("y")),
            z=float(request.form.get("z")),
            Cut=request.form.get("cut"),
            Color=request.form.get("color"),
            Clarity=request.form.get("clarity")
        )
        final_data=data.get_data_as_dataframe()

        predict_pipeline=PredictPipeline()

        pred=predict_pipeline.predict(final_data)

        result=round(pred[0],2)

        return render_template("result.html",final_result=result)

    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)