import pandas as pd
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class UppercaseText(Resource):

    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        return jsonify({"text": text.upper()})


class getIlsco(Resource):

    def get(self):
        """
        This method responds to the GET request for this endpoint and returns a specific value from the CSV file.
        ---
        tags:
        - CSV Processing
        parameters:
            - name: row
              in: query
              type: string
              required: true
              description: The row value to search in the CSV file
            - name: column
              in: query
              type: string
              required: true
              description: The column value to search in the CSV file
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            value:
                                type: string
                                description: The value in the specified row and column
        """
        # Replace 'your_file_path.csv' with the actual path to your CSV file
        csv_file_path = 'ilsco_test.csv'
        # Get values from query parameters
        row = request.args.get('row')
        col = request.args.get('column')
        print(row,col)
        
        try:
            # Read CSV file into a Pandas DataFrame
            df = pd.read_csv(csv_file_path)
            df.set_index('LugSize', inplace=True)
            # Find the value at the specified row and column
            value = df.loc[row, col]
            
            return {"value": value}, 200
        except Exception as e:
            return {"error": str(e)}, 400


api.add_resource(UppercaseText, "/uppercase")
api.add_resource(getIlsco, "/get_csv_value")

if __name__ == "__main__":
    app.run(debug=True)