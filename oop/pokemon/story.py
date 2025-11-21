
import pokemon as p
#import random as r

def main():
    #create creature
    starter = input("choose pokemon to start with (bisasam, glumanda, schiggy): ")
    start = p.Creature(starter, p.type_match_start[starter])
    print(start)

    #create opponent
    name = "taubsi"
    sample = p.Creature("taubsi", p.type_match[name] )
    print(sample)

    #fight mechanic loop
    while True:

        suc = start.use_atks(sample)
        if suc == 3:
            print("your pokemon has been defeated")
            break
        if suc == 2:
            start.exp()
            break


    #final:
    # fix fighting loop and check use_atks dmg computation as well as return values --> push again if working


    #current: solid MVP, afterwards more additions/brighter variety
    #can be developed and enhanced further later on

    #in story.py write logic of continuously battling pokemon, once one opponent is defeated
    #items like potion, reviver, ... how to use them and how to get them
    # receive xp, add lvl as attribute (--> learn atks with higher levels, ...), (link atks strength to lvl?)
    # make random pokemons from type_match spawn (later in pokemons.py, not hard)
    # evolutions (with inheritance?)
    #(later maybe interface with directions to go to determine when and which pokemons to battle)
    #multiple pokemons and catch pokemons
    # adapt code in use_atks, so both turns (player and enemy) are the same and you can set self = self or self = other,
    # instead of using duplicated code the other way round
    #include very effective moves based on type




if __name__ == "__main__":
    main()
