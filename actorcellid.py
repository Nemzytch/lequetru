        # actorCellId = -1
        # for member in cs['myTeam']:
        #     if member['summonerId'] == summonerId:
        #         actorCellId = member['cellId']
        # if actorCellId == -1:
        #     continue
        # for action in cs['actions'][0]:
        #     if action['actorCellId'] != actorCellId:
        #         continue
        #     #pick yuumi
        # # if cs["timer"]["phase"] == "PLANNING":
        # #     print('planning the game')
        # #     url = '/lol-champ-select/v1/session/actions/%d' % action['id']
        # #     data = {'championId': 22}
        # #     # Chose champ to ban
        # #     r = request('patch', url, '', data)
        # #     print(r.status_code, r.text)
        # #     # # Ban champ
        # #     # if action['completed'] == False:
        # #     #     r = request('post', url+'/complete', '', data)
        # #     #     print(r.status_code, r.text)
        #     # if ['actions'][0]["isInProgress"] == False:
        #     if action['championId'] == 0:
        #         url = '/lol-champ-select/v1/session/actions/%d' % action['id']
        #         data = {'championId': 350}
        #         # Chose champ to pick
        #         r = request('patch', url, '', data)
        #         print(r.status_code, r.text)
        #         # Lock champ
        #         if action['completed'] == False:
        #             r = request('post', url+'/complete', '', data)
        #             print(r.status_code, r.text)