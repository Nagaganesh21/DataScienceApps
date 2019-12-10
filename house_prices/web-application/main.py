#!/usr/bin/env python
from flask import Flask, render_template, flash, request, jsonify, Markup

# model constants
# set up constants for our coefficients 
INTERCEPT = 3.702352
COEF_LOT = 0.000004   # lot area
COEF_LIV = 0.000315   # living area 
COEF_YR = 0.003580    # year built
COEF_QUAL = 0.121906  # quality of property

# data mean values
MEAN_LOT_AREA = 10429        # mean lot area
MEAN_GR_LIV_AREA = 1504  # grliv area
MEAN_YR_BUILT = 1971        # yr built
MEAN_OVERALL_QUAL = 6.1    # quality
 
app = Flask(__name__)
 
@app.route("/", methods=['POST', 'GET'])
def index():
    # on load set form with defaults
    return render_template('index.html',
            mean_lot_area = MEAN_LOT_AREA,
            mean_liv_area = MEAN_GR_LIV_AREA,
            mean_yr_built = MEAN_YR_BUILT,
            mean_quality = MEAN_OVERALL_QUAL,
            model_intercept = INTERCEPT,

			model_lot_area = COEF_LOT,    
			model_liv_area = COEF_LIV,         
			model_yr_built = COEF_YR,  
			model_quality = COEF_QUAL 

            )


# when running app locally
if __name__=='__main__':
      app.run(debug=True)