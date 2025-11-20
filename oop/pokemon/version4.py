import random as r
#for variation in randomness when rerunning code
r.seed()

class Creature:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
        self._lvl = self.lvl()
        #needs/uses lvl
        self._hp = self.hp()
        self._stats = self.stats()
        self._atk = self.atks()
        self._exp = self.exp()


    def __str__(self):
        return (f"{self.name}, {self.typ}, {self._hp} hp, {self._atk}, {self._stats}, level: {self._lvl}")

    def exp(self):
        #set exp_thresh (gradually increasing with level)
        exp_thresh = 100 + self._lvl*50
        #if no existing exp, set exp to 0
        if not self._exp:
            self._exp = 0
        #the higher the level the more exp for defeating
        expgrow = 30 + self._lvl*10
        self._exp += expgrow
        print(f"{self.name} received {expgrow} exp.")
        #reset threshold, level up and increase stats
        if self._exp >= exp_thresh:
            self._lvl += 1
            #stats
            self._stats["speed"] += r.randint(1,3)
            self._stats["atk"] += r.randint(1,3)
            self._stats["dfn"] += r.randint(1,3)
            #tell player
            print(f"{self.name} reached level {self._lvl}.")
            print(f"speed: {self._stats["speed"]}, atk: {self._stats["atk"]}, dfn: {self._stats["dfn"]}.")
            #reset exp for new lvl
            self._exp -= exp_thresh
        return self._exp


    def lvl(self):
        #starter pick
        if self.name in list(type_match_start.keys()):
            self._lvl = 5
            return self._lvl
        #other pokemon
        if self.name in list(type_match.keys()):
            self._lvl = r.randint(1,5)
            return self._lvl

    def hp(self):
        hp_base = r.randint(10, 30)
        #the higher the level the more hp
        self._hp = hp_base + (self._lvl * 4)
        return self._hp

    def stats(self):
        stats ={
            "speed" : r.randint(1,10),
            "atk" : r.randint(1,5),
            "dfn" : r.randint(1,5)
        }
        self._stats = stats
        return self._stats


    #create attacks
    def atks(self):
        key = r.choice(list(attacks_amount.keys()))
        self._atk = {key : attacks_amount[key]}
        return self._atk

    #count amounts of atks
    def use_atks(self, other):

        use = input(f"what should {self.name} do? {self._atk}: ")

#--player goes first---
        #-----------player turn------------------------

        if self._stats["speed"] >= other._stats["speed"]:

            #check usages left of atk
            if self._atk[use] < 1:
                print("no attacks left")
                return False
            else:
                self._atk[use] -= 1
                print(f"{self.name} used {use} against {other.name}. {self._atk[use]} uses left.")

            #compute and deal dmg of atks
                dmg = attacks_dmg[use]
                #---
                #add stats to dmg computation (if >= 0)
                if self._stats["atk"] - other._stats["dfn"] >= 0:
                    dmg = dmg + self._stats["atk"] - other._stats["dfn"]
                #chance for critical hit (1/50)
                crit = r.randint(1,50)
                if crit == 25:
                    dmg = dmg*2
                    print("critical hit!")
                #---
                other._hp -= dmg
                if other._hp <= 0:
                    print(f"\n{other.name} was defeated")
                    return 0
                print(f"{other.name} has {other._hp} left")

        #-------------------------enemy turn--------------

            print(f"\n {other.name}s turn")
            # pick and use random atk enemy
            amnt = len(list(other._atk.keys()))
            atk = r.randint(0,amnt-1)
            enemy_move = list(other._atk.keys())[atk]

            #check atk usages left
            if other._atk[enemy_move] < 1:
                print("no attacks left")
                return False
            else:
                other._atk[enemy_move] -= 1
                print(f"{other.name} used {enemy_move} against {self.name}. {other._atk[enemy_move]} uses left.")
            #compute and deal dmg of atks
                dmg = attacks_dmg[enemy_move]
                #---
                #add stats to dmg computation (if >= 0)
                if self._stats["atk"] - other._stats["dfn"] >= 0:
                    dmg = dmg + other._stats["atk"] - self._stats["dfn"]
                #chance for critical hit (1/50)
                crit = r.randint(1,50)
                if crit == 25:
                    dmg = dmg*2
                    print("crit")
                #---
                self._hp -= dmg
                if self._hp <= 0:
                    print(f"\n{self.name} was defeated")
                    return 1
                print(f"{self.name} has {self._hp} left")
                return False

#--enemy goes first---
            #---------enemy turn---------------
        else:

            print(f"\n {other.name}s turn")
            # pick and use random atk enemy
            amnt = len(list(other._atk.keys()))
            atk = r.randint(0,amnt-1)
            enemy_move = list(other._atk.keys())[atk]

            #check atk usages left
            if other._atk[enemy_move] < 1:
                print("no attacks left")
                return False
            else:
                other._atk[enemy_move] -= 1
                print(f"{other.name} used {enemy_move} against {self.name}. {other._atk[enemy_move]} uses left.")
                 #compute and deal dmg of atks
                dmg = attacks_dmg[enemy_move]
                #---
                #add stats to dmg computation (if >= 0)
                if self._stats["atk"] - other._stats["dfn"] >= 0:
                    dmg = dmg + other._stats["atk"] - self._stats["dfn"]
                #chance for critical hit (1/50)
                crit = r.randint(1,50)
                if crit == 25:
                    dmg = dmg*2
                    print("critical hit!")
                #---
                self._hp -= dmg
                if self._hp <= 0:
                    print(f"\n{self.name} was defeated")
                    return 1
                print(f"{self.name} has {self._hp} left")

            #------------------------------player turn----------------------
            #check usages left of atk
            if self._atk[use] < 1:
                print("no attacks left")
                return False
            else:
                self._atk[use] -= 1
                print(f"{self.name} used {use} against {other.name}. {self._atk[use]} uses left.")

            #compute and deal dmg of atks
                dmg = attacks_dmg[use]
                #---
                #add stats to dmg computation (if >= 0)
                if self._stats["atk"] - other._stats["dfn"] >= 0:
                    dmg = dmg + self._stats["atk"] - other._stats["dfn"]
                #chance for critical hit (1/50)
                crit = 1
                crit = r.randint(1,50)
                if crit == 25:
                    dmg = dmg*2
                    print("critical hit!")
                #---
                other._hp -= dmg
                if other._hp <= 0:
                    print(f"\n{other.name} was defeated")
                    return 0
                print(f"{other.name} has {other._hp} left")


#for later/making things more robust
#correct reading (getter) and prevent invalid changes (setter) after class created
    #getter

   # @property
   # def hp(self):
    #    return self._hp

   # @hp.setter
   # def hp(self, value):
       # if not isinstance(value, int):
        #    raise ValueError("hp not int")
       # self._hp = value






#starter pokemon
type_match_start = {
"bisasam" : "plant",
"glumanda" : "fire",
"schiggy" : "water",
}

#further pokemon
type_match = {
"taubsi" : "normal",
"raupy" : "bug",
"ratzfratz" : "normal"
}

#atks and their max usage
attacks_amount = {
    "kratzer" : 20,
    "tackle" : 20
}

attacks_dmg = {
    "kratzer" : r.randint(3,5),
    "tackle" : r.randint(3,6)
}


#debugging:

#def main():

    #c_name = input("pokemon name: ")
    #c_type = input("pokemon type: ")


    #C = Creature(c_name, c_type)
    #print(C)


#if __name__ == "__main__":
#    main()
