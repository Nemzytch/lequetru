 def LevelUP(self):

        if self.YuumiLevel == 1:
            if self.ELevel < 1:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 2:
            if self.QLevel < 1:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 3:
            if self.QLevel < 2:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 4:
            if self.ELevel < 2:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 5:
            if self.QLevel < 3:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 6:
            if self.RLevel < 1:
                self.ctrlr()
                print('level up R')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 7:
            if self.QLevel < 4:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 8:
            if self.WLevel < 2:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 9:
            if self.QLevel < 5:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 10:
            if self.WLevel < 3:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 11:
            if self.RLevel < 2:
                self.ctrlr()
                print('level up R')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 12:
            if self.QLevel < 6:
                self.ctrlq()
                print('level up Q')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 13:
            if self.WLevel < 4:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 14:
            if self.WLevel < 5:
                self.ctrlw()
                print('level up W')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 15:
            if self.ELevel < 3:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 16:
            if self.RLevel < 3:
                self.ctrlr()
                print('level up R')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 17:
            if self.ELevel < 4:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        if self.YuumiLevel == 18:
            if self.ELevel < 5:
                self.ctrle()
                print('level up E')
            else:
                print('Nothing To Level Up')
        print("Yuumi is level  "+str(self.YuumiLevel))