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

class getTools(Resource):

    def get(self):
        """
        This method responds to the GET request for this endpoint and the list of tools available
        ---
        tags:
        - get available tools
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: array
                                description: tools available
        """
               # Replace 'your_file_path.csv' with the actual path to your CSV file
        csv_file_path = 'ilsco_test.csv'
        # Get values from query parameters
        try:
            # Read CSV file into a Pandas DataFrame
            df = pd.read_csv(csv_file_path)
            df.set_index('LugSize', inplace=True)
            # Find the value at the specified row and column
            cable_list = list(df.columns[2::])
            
            return {"value": cable_list}, 200
        except Exception as e:
            return {"error": str(e)}, 400

        return jsonify({"text": text.upper()})

class getCables(Resource):

    def get(self):
        """
        This method responds to the GET and return the list of available cable sizes.
        ---
        tags:
        - get cable sizes
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: array
                                description: Available cable sizes
        """
               # Replace 'your_file_path.csv' with the actual path to your CSV file
        csv_file_path = 'ilsco_test.csv'
        # Get values from query parameters
        try:
            # Read CSV file into a Pandas DataFrame
            df = pd.read_csv(csv_file_path)
            df.set_index('LugSize', inplace=True)
            # Find the value at the specified row and column
            tools_list = list(df.index)
            
            return {"value": tools_list}, 200
        except Exception as e:
            return {"error": str(e)}, 400

        return jsonify({"text": text.upper()})

class getIlsco(Resource):

    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the crimp value for the cable and tool.
        ---
        tags:
        - Crimps lookup
        parameters:
            - name: cable
              in: query
              type: string
              required: true
              description: Cable size AWG use
            - name: tool
              in: query
              type: string
              required: true
              description: Tool to be used
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
        row = request.args.get('cable')
        col = request.args.get('tool')
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


#api.add_resource(UppercaseText, "/uppercase")
api.add_resource(getIlsco, "/getCrimps")
api.add_resource(getCables, "/getCableList")
api.add_resource(getTools, "/getTools")

if __name__ == "__main__":
    app.run(debug=True)