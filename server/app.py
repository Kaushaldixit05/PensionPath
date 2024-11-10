from flask import Flask, request, jsonify
from flask_cors import CORS
from investment_calculator import calculate_investment_strategy

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        retirement_age = int(data['retirementAge'])
        current_age = int(data['currentAge'])
        desired_fund = float(data['desiredFund'])
        monthly_investment = float(data['monthlyInvestment'])
        risk_category = int(data['riskCategory'])

        result = calculate_investment_strategy(
            retirement_age,
            current_age,
            desired_fund,
            monthly_investment,
            risk_category
        )
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
