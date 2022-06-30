            # formula = match({"HWID": hwid})
            # formula2 = match({"HWID": "None"})
            # listOfNone = table.all(formula=formula2)
            # listOfAcc = table.all(formula=formula)
            
            # print("Number of acc for the HWID : " + str(len(listOfAcc)))
            # if len(listOfAcc) <5:
            #     print("You need more accounts")
            #     for i in range(5-len(listOfAcc)):
            #         print("Adding account")
            #         table.update(listOfNone[i]['id'], {"HWID": hwid})
            # if len(listOfAcc) >= 5:
            #     print("You have enough accounts")
            #     Personnage.account = table.first(formula=formula, sort=["Unban"])['fields']['Account']
            
            
            
                # hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()