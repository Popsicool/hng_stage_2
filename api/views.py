from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def getData(request):
    if request.method == 'GET':
        me = {"slackUsername": "Popsicool","backend":True, "age":27, "bio": "I'm a fullstack developer in developments stage, i'm passionate about learning and willing to do hard things" }
        return Response(me)

    if request.method == 'POST':
        operation = request.data
        if (type(operation['x']) is not int or type(operation['y']) is not int):
            result = {"details": "X and Y must be integers only"}
            return Response(result)
        if (operation['operation_type'] not in ["addition", "subtraction", "multiplication"]):
            string = operation['operation_type']
            string = string.split()
            sign = 0
            for i in string:
                if i.lower() in ["addition", "additions", 'add', 'adds' "plus", "adding", "plusing", "summation"]:
                    sign = 1
                    break
                elif i in ["subtract", "subtracts", "subtraction", "minus", "remove", "deduct","subtractions", "deduction", "subtracting", "less"]:
                    sign = 2
                    break
                else:
                    sign = 3
            x = operation['x']
            y = operation['y']
            if sign == 1:
                operation_type = "addition"
                result = x + y
            elif sign == 2:
                operation_type = "subtraction"
                result = x - y
            else:
                operation_type = "multiplication"
                result = x * y

            result = {"slackUsername": "Popsicool", "operation_type" : operation_type, "result": result }
            return Response(result)

        operation_type = operation['operation_type']
        x = operation['x']
        y = operation['y']

        if operation_type == "addition":
            result = x + y
        elif operation_type == "subtraction":
            result = x - y
        else:
            result = x * y
        result = {"slackUsername": "Popsicool", "operation_type" : operation_type, "result": result }
        return Response(result)

