@app.route("/api/CheckForBadName", methods=["POST", "GET"])
def checkforbadname():
    rjson = request.get_json() 
    function_result = rjson["FunctionArgument"]
    playfab_id = rjson["CallerEntityProfile"]["Lineage"]["MasterPlayerAccountId"]
    name = function_result["name"].upper()
    forRoom = function_result["forRoom"]

    if forRoom == True:
        return jsonify({"result": 0})
