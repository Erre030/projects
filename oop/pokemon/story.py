
import pokemon as p
import random as r

def main():
    #create creatures
    starter = input("choose pokemon to start with (bisasam, glumanda, schiggy): ")
    start = p.Creature(starter, p.type_match_start[starter])
    print(start)


    name = "taubsi"
    sample = p.Creature("taubsi", p.type_match[name] )
    print(sample)
    #sample._stats["speed"] = 15

    #fight mechanic
    while True:

        suc = start.use_atks(sample)
        if suc == 1:
            print("your pokemon has been defeated")
        if suc == 0:
            start.exp()


            break


    #next:

    #in story.py write logic of continuously battling pokemon, once one opponent is defeated (later maybe interface with directions to go to determine when and which pokemons to battle)


    # receive xp, add lvl as attribute (--> learn atks with higher levels, ...)
    # make random pokemons from type_match spawn (later in pokemons.py, not hard)
    # evolutions (with inheritance?)
    #items like potion, reviver, ...

    #first MVP, afterwards more additions/brighter variety





    #later:
    # adapt code in use_atks, so both turns (player and enemy) are the same and you can set self = self or self = other,
    # instead of using duplicated code the other way round

    #include very effective moves based on type



if __name__ == "__main__":
    main()
