#CSIT 163 OL1 Spring
#Wyatt Robertson
#2/8/2026



#useful to movie things to text files later
import os




#opens the assignment text and parses into lines (with the total length)
#empty list for later
#x is an interation variable (there will be multiple)
#empty dictionary to be modified
access_text = open('movies.txt')
content = access_text.readlines()
length = len(list(content))
Empty_List = []
x = 0
dictionary={}

#serves as a loop so I can get all of the actors and movies in the text files
#Actor_portfolios is the actors name and Movie_Start
#fully entry is a string of each actor's indidual movies when iterated
#The first comma seperates the actor and his/her movies (unless its in some fringe cases)
for hfdfh in content :
    Actor_portfolios = list(content)
    Full_Entry = (str(Actor_portfolios[x]))
    Movie_Start = Full_Entry.find(',')+2

#My first and prettiest function. Iterates over the lines and returns the acts by fidning the comma.
    def actor() :
        Actor = Full_Entry[0:Full_Entry.find(',')]
        return (Actor)

#A few definition variables for my movie function.
#Movies is the movie side of the Actor_portfolios
#Movie_Portfolio divides the movies into seperate list entries
#FindN removes \n at the end of readlines
#NoN allows ns to be completely accounted for value in variable:
#RemovedN splits again similarly to Movie_Portfolio
#Find Space gets rid of the extra spaces
#Removed Space uses it
    pass
    Movies = Full_Entry[Movie_Start:]
    Movie_Portfolio = Movies.split(', ')
    FindN = str(Movie_Portfolio).find('/n')
    NoN = Movies[:FindN]
    RemovedN = (NoN).split(', ')
    FindSpace = str(RemovedN[1])
    RemovedSpace = FindSpace[1:]


#These are the fringe scenarios I talk about in my page
    if x == 17:
        RemovedN[1] = RemovedSpace
    if x == 21:
        RemovedN[1] = RemovedSpace
    if x == 29 :
        RemovedN = Movie_Portfolio



#Finds the movie number so iteration can be defined
    Movie_Number = len(RemovedN)


#Houses my second, much uglier function movies().
#Movies iteraties and adds actors to our empty dictionary based on movies they've starred in.
    z = -1
    while z < Movie_Number-1 :
        z += 1
        def movies() :
            Specific_Movie = RemovedN[z]
            if Specific_Movie in dictionary :
                dictionary[Specific_Movie].append(actor())
            else:
                Empty_List = [actor()]
                dictionary[Specific_Movie] = Empty_List
            return dictionary

        (movies())

#Iterates so more entries can be added throughout the list
    x += 1

#Serves as a stating ground for user input. Users can look through my beautufil dictionary if they wish to.
print(dictionary)
#Done with movies.txt now.
access_text.close()
#Another iteration variable to love
j = 0
while j == 0:
    #Iteration is used so user can repeatedly make mistakes and reinput
    Category = input('\nType "actor" if you want to search for actors.\nType "movie" if you would like to search for movies.\nType "q" if you would like to quit.\n')

#If actor is typed we use the dictionary's items (movies) to search throughout the entire dictionary and find actors/coactors
    if Category == 'actor' :
        List_Dictionary = list(dictionary.items())
        increment = 0

        Specific_Actor = input("\nWhat is the exact name of the actor whose co-actors you are looking for?\n")

        while increment <= 57 :
#Searches through the dictionary entry by entry


            if Specific_Actor in List_Dictionary[increment][1] :
                CoActors = (List_Dictionary[increment][1])
                if Specific_Actor in CoActors :
                    CoActors.remove(Specific_Actor)
                    if CoActors == []:
                        CoActors = 'none'


#Shows the results and adds them to a text file
                print(f"{Specific_Actor}'s co-actors in {List_Dictionary[increment][0]} are {(CoActors)}")
                desktop_path = os.path.expanduser("~/Desktop")

                with open(desktop_path + "answer.txt", "w") as file:

                    file.write(f"{Specific_Actor}'s co-actors in {List_Dictionary[increment][0]} are {(CoActors)}\n")



                continue




            increment += 1



        break


#Results the of movie category
    if Category == 'movie' :
        print('\n& will search for common actors between the movies.\n| will find all the actors in both movies.\n^ will find the actors unique to each movie.')
        Movie_Choice = input('\nType in the titles of both movies (with spaces and proper capitlization according to the above dictionary) seperated by "&,|,^"\n')
#Uses the titles of both movies to show every actor in each
#We know that the movie written before | is the first move and the one after is the second
#Then we iterate over the elements of one of the movies, where we can delete a common actor so they are only mentioned once
        if Movie_Choice.find('|') != -1 :
            Movie1 = Movie_Choice.split('|')[0]
            Movie2 = Movie_Choice.split('|')[1]
            for element in dictionary[Movie1] :
                if element not in dictionary[Movie2] :
                    continue

                else:
                    dictionary[Movie1].remove(element)
#This code adds the actors together to create the complete list
            All_Actors = dictionary[Movie1] + dictionary[Movie2]
#Prints out the list and add it to a text file
            print(f'All the people that have acted in {Movie1} and {Movie2} are {All_Actors}')
            desktop_path = os.path.expanduser("~/Desktop")

            with open(desktop_path + "answer.txt", "w") as file:

                file.write(f'All the people that have acted in {Movie1} and {Movie2} are {All_Actors}\n')
            break
#This code is used to find the actors exclusive to each movie.
#Splitting is similar to above code
#Main difference is that I go through twice to remove common actors from both movies so I can list each out seperately
        if Movie_Choice.find('^') != -1 :
            Movie1 = Movie_Choice.split('^')[0]
            Movie2 = Movie_Choice.split('^')[1]
            for element in dictionary[Movie1] :
                if element in dictionary[Movie2] :
                    dictionary[Movie1].remove(element)
                    dictionary[Movie2].remove(element)
                    if dictionary[Movie1] == [] :
                        dictionary[Movie1] = 'none'
                    if dictionary[Movie2] == [] :
                        dictionary[Movie2] = 'none'
                else:
                     continue

#Lists movies and actors unique to each movei then puts it in a text file
            print(f'The actors in exclusively {Movie1} are {dictionary[Movie1]}.\nThe actors in exclusively {Movie2} are {dictionary[Movie2]}')
            desktop_path = os.path.expanduser("~/Desktop")

            with open(desktop_path + "answer.txt", "w") as file:

                file.write(f'The actors in exclusively {Movie1} are {dictionary[Movie1]}.\nThe actors in exclusively {Movie2} are {dictionary[Movie2]}\n')
            break
#I will explain this once because this is a bulk of my code (I definitely should have used a function here but by the time I reliazed that it would have been too complicated)
#Returns the actors in both movies. First, this code checks to make sure there are not either of the movies with & in the title. Me-Myself & Irene or Mr & Mrs Smith.
#This one is the most straightforward
        if Movie_Choice.find('&') != -1 :
            if Movie_Choice.count('&') == 1 :
                Movie1 = Movie_Choice.split('&')[0]
                Movie2 = Movie_Choice.split('&')[1]
#Checks to see what movie has a longer list of actors. Whichever ones has a longer list we iterate over to remove each and then do the same over the second list, finally printing the second list.
                if len(dictionary[Movie1]) > len(dictionary[Movie2]) :

                    for element in dictionary[Movie1] :
                        if element not in dictionary[Movie2] :
                            dictionary[Movie1].remove(element)
                            for element in dictionary[Movie2] :
                                if element not in dictionary[Movie1] :
                                    dictionary[Movie2].remove(element)
                                    All_Actors = dictionary[Movie2]
                                    if All_Actors == [] :
                                        All_Actors = 'none'

                    print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')
                    desktop_path = os.path.expanduser("~/Desktop")

                    with open(desktop_path + "answer.txt", "w") as file:

                        file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')
                    quit()
    #Works the same as above but checks the other scenario where movie2 has more actors
                if len(dictionary[Movie2]) > len(dictionary[Movie1]) :

                    for element in dictionary[Movie2] :
                        if element not in dictionary[Movie1] :
                            dictionary[Movie2].remove(element)
                            for element in dictionary[Movie1] :
                                if element not in dictionary[Movie2] :
                                    dictionary[Movie1].remove(element)
                                    All_Actors = dictionary[Movie1]
                                    if All_Actors == [] :
                                        All_Actors = 'none'


                    print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                    desktop_path = os.path.expanduser("~/Desktop")

                    with open(desktop_path + "answer.txt", "w") as file:

                        file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')
                    quit()
#Works the same as above but checks if they have the same amount of actors
                if len(dictionary[Movie2]) == len(dictionary[Movie1]) :
                    for element in dictionary[Movie1] :
                        if element not in dictionary[Movie2] :
                            dictionary[Movie1].remove(element)
                            for element in dictionary[Movie2] :
                                if element not in dictionary[Movie1] :
                                    dictionary[Movie2].remove(element)
                                    for element in dictionary[Movie1] :
                                        if element not in dictionary[Movie2] :
                                            dictionary[Movie1].remove(element)
                                            for element in dictionary[Movie2] :
                                                if element not in dictionary[Movie1] :
                                                    dictionary[Movie2].remove(element)
                                                    All_Actors = dictionary[Movie1]
                                                    if All_Actors == [] :
                                                        All_Actors = 'none'


                                                    print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                                                    desktop_path = os.path.expanduser("~/Desktop")

                                                    with open(desktop_path + "answer.txt", "w") as file:

                                                        file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')

                                                    quit()





#This code works if only one of the & movies is mentioned. Functionally it is essentially the same otherwise.
            if Movie_Choice.count('&') == 2 :
                if Movie_Choice.find('&') == 10 :
                    #Since there are only two & movies, there are only 4 total positions to worry about. This checks one of them.
                    Movie1 = Movie_Choice[0:17]
                    Movie2 = Movie_Choice[18:]

                    if len(dictionary[Movie1]) > len(dictionary[Movie2]) :
                        for element in dictionary[Movie1] :
                            if element not in dictionary[Movie2] :
                                dictionary[Movie1].remove(element)
                                for element in dictionary[Movie2] :
                                    if element not in dictionary[Movie1] :
                                        dictionary[Movie2].remove(element)

                                All_Actors = dictionary[Movie2]
                                if All_Actors == [] :
                                    All_Actors = 'none'

                                print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                                desktop_path = os.path.expanduser("~/Desktop")

                                with open(desktop_path + "answer.txt", "w") as file:

                                    file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')

                                quit()



#Code similar to above code.
                    if len(dictionary[Movie2]) > len(dictionary[Movie1]) :
                        for element in dictionary[Movie2] :
                            if element not in dictionary[Movie1] :
                                dictionary[Movie2].remove(element)
                                for element in dictionary[Movie1] :
                                    if element not in dictionary[Movie2] :
                                        dictionary[Movie1].remove(element)
                                        for element in dictionary[Movie1] :
                                            if element not in dictionary[Movie2] :
                                                dictionary[Movie1].remove(element)
                                                All_Actors = dictionary[Movie1]
                                                if All_Actors == [] :
                                                    All_Actors = 'none'



                                print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                                desktop_path = os.path.expanduser("~/Desktop")

                                with open(desktop_path + "answer.txt", "w") as file:

                                    file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')

                                quit()

#Similar to above code. A fucntion would have helped (maybe) because there are slight changes in order throughout.
                    if len(dictionary[Movie2]) == len(dictionary[Movie1]) :
                        for element in dictionary[Movie1] :
                            if element not in dictionary[Movie2] :
                                dictionary[Movie1].remove(element)
                                for element in dictionary[Movie2] :
                                    if element not in dictionary[Movie1] :
                                        dictionary[Movie2].remove(element)
                                        for element in dictionary[Movie1] :
                                            if element not in dictionary[Movie2] :
                                                dictionary[Movie1].remove(element)
                                                for element in dictionary[Movie2] :
                                                    if element not in dictionary[Movie1] :
                                                        dictionary[Movie2].remove(element)
                                                        All_Actors = dictionary[Movie1]
                                                        if All_Actors == [] :
                                                            All_Actors = 'none'

                                                            print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                                                            desktop_path = os.path.expanduser("~/Desktop")

                                                            with open(desktop_path + "answer.txt", "w") as file:

                                                                file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')

                                                            quit()


#Checks for the other & movie (Mr & Mrs Smith)
#Other than that it is the same as above.
                if Movie_Choice.find('&') == 3 :

                    Movie1 = Movie_Choice[0:14]
                    Movie2 = Movie_Choice[15:]

                    if len(dictionary[Movie1]) > len(dictionary[Movie2]) :


                        if len(dictionary[Movie1]) > len(dictionary[Movie2]) :
                            for element in dictionary[Movie1] :
                                if element not in dictionary[Movie2] :
                                    dictionary[Movie1].remove(element)
                                    for element in dictionary[Movie2] :
                                        if element not in dictionary[Movie1] :
                                            dictionary[Movie2].remove(element)

                                    All_Actors = dictionary[Movie2]
                                    if All_Actors == [] :
                                        All_Actors = 'none'

                                    print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                                    desktop_path = os.path.expanduser("~/Desktop")

                                    with open(desktop_path + "answer.txt", "w") as file:

                                        file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')

                                    quit()

#Similar to above
                    if len(dictionary[Movie2]) > len(dictionary[Movie1]) :
                        for element in dictionary[Movie2] :
                            if element not in dictionary[Movie1] :
                                dictionary[Movie2].remove(element)
                                for element in dictionary[Movie1] :
                                    if element not in dictionary[Movie2] :
                                        dictionary[Movie1].remove(element)
                                        for element in dictionary[Movie1] :
                                            if element not in dictionary[Movie2] :
                                                dictionary[Movie1].remove(element)
                                                All_Actors = dictionary[Movie1]
                                                if All_Actors == [] :
                                                    All_Actors = 'none'

                                                print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')
                                                desktop_path = os.path.expanduser("~/Desktop")

                                                with open(desktop_path + "answer.txt", "w") as file:

                                                    file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')

                                                quit()

#Simialr to abvove
                    if len(dictionary[Movie2]) == len(dictionary[Movie1]) :
                        for element in dictionary[Movie1] :
                            if element not in dictionary[Movie2] :
                                dictionary[Movie1].remove(element)
                                for element in dictionary[Movie2] :
                                    if element not in dictionary[Movie1] :
                                        dictionary[Movie2].remove(element)
                                        for element in dictionary[Movie1] :
                                            if element not in dictionary[Movie2] :
                                                dictionary[Movie1].remove(element)
                                                for element in dictionary[Movie2] :
                                                    if element not in dictionary[Movie1] :
                                                        dictionary[Movie2].remove(element)
                                                        All_Actors = dictionary[Movie1]
                                                        if All_Actors == [] :
                                                            All_Actors = 'none'

                                                            print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')
                                                            desktop_path = os.path.expanduser("~/Desktop")

                                                            with open(desktop_path + "answer.txt", "w") as file:

                                                                file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')

                                                            quit()



#This works the same as above but checks if the and movies are in the second movie postion as oppsoed to the first.
                if Movie_Choice.find('&') != 3 and Movie_Choice.find('&') != 10 :

                    Movie1 = Movie_Choice[0:Movie_Choice.find('&')]
                    Movie2 = Movie_Choice[Movie_Choice.find('&')+1:]
#Works the same as above
                    if len(dictionary[Movie1]) > len(dictionary[Movie2]) :

                        for element in dictionary[Movie1] :
                            if element not in dictionary[Movie2] :
                                dictionary[Movie1].remove(element)
                                for element in dictionary[Movie2] :
                                    if element not in dictionary[Movie1] :
                                        dictionary[Movie2].remove(element)
                                        All_Actors = dictionary[Movie2]
                                        if All_Actors == [] :
                                            All_Actors = 'none'

                                            print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')
                                            desktop_path = os.path.expanduser("~/Desktop")

                                            with open(desktop_path + "answer.txt", "w") as file:

                                                file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')
                                            quit()
#Same as above
                    if len(dictionary[Movie2]) > len(dictionary[Movie1]) :

                        for element in dictionary[Movie1] :
                            if element not in dictionary[Movie2] :
                                dictionary[Movie1].remove(element)
                                for element in dictionary[Movie2] :
                                    if element not in dictionary[Movie1] :
                                        dictionary[Movie2].remove(element)
                                        All_Actors = dictionary[Movie2]
                                        if All_Actors == [] :
                                            All_Actors = 'none'

                                            print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                                            desktop_path = os.path.expanduser("~/Desktop")

                                            with open(desktop_path + "answer.txt", "w") as file:

                                                file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')
                                            quit()
#Same as above
                    if len(dictionary[Movie2]) == len(dictionary[Movie1]) :
                        for element in dictionary[Movie1] :
                            if element not in dictionary[Movie2] :
                                dictionary[Movie1].remove(element)
                                for element in dictionary[Movie2] :
                                    if element not in dictionary[Movie1] :
                                        dictionary[Movie2].remove(element)
                                        for element in dictionary[Movie1] :
                                            if element not in dictionary[Movie2] :
                                                dictionary[Movie1].remove(element)
                                                for element in dictionary[Movie2] :
                                                    if element not in dictionary[Movie1] :
                                                        dictionary[Movie2].remove(element)
                                                        All_Actors = dictionary[Movie1]
                                                        if All_Actors == [] :
                                                            All_Actors = 'none'
                                                            print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                                                            desktop_path = os.path.expanduser("~/Desktop")

                                                            with open(desktop_path + "answer.txt", "w") as file:

                                                                file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')
                                                            quit()
#Final scenario where the user inputs both & Movie_Start
#This case applies if Me-Myself & Irene) is First
#Code very similar to above
            if Movie_Choice.count('&') == 3 :
                if Movie_Choice.find('&') == 10 :

                    Movie1 = Movie_Choice[0:17]
                    Movie2 = Movie_Choice[18:]


                    for element in dictionary[Movie1] :
                        if element not in dictionary[Movie2] :

                            dictionary[Movie1].remove(element)

                        for element in dictionary[Movie2] :
                            if element not in dictionary[Movie1] :
                                dictionary[Movie2].remove(element)
                                for element in dictionary[Movie2] :
                                    if element not in dictionary[Movie1] :
                                        dictionary[Movie2].remove(element)


                                        All_Actors = dictionary[Movie2]
                                        if All_Actors == [] :
                                            All_Actors = 'none'
                    print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')
                    desktop_path = os.path.expanduser("~/Desktop")

                    with open(desktop_path + "answer.txt", "w") as file:

                        file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')
                    quit()




#Checsk to see if Mr & Mrs Smith is First
#Very similar to above code
                if Movie_Choice.find('&') == 3 :

                    Movie1 = Movie_Choice[0:14]
                    Movie2 = Movie_Choice[15:]

                    for element in dictionary[Movie2] :
                        if element not in dictionary[Movie1] :
                            dictionary[Movie2].remove(element)
                            for element in dictionary[Movie1] :
                                if element not in dictionary[Movie2] :
                                    dictionary[Movie1].remove(element)
                                    for element in dictionary[Movie1] :
                                        if element not in dictionary[Movie2] :
                                            dictionary[Movie1].remove(element)
                                            All_Actors = dictionary[Movie1]
                                            if All_Actors == [] :
                                                All_Actors = 'none'
                    print(f'All the actors in {Movie1} and {Movie2} are {All_Actors}')

                    desktop_path = os.path.expanduser("~/Desktop")

                    with open(desktop_path + "answer.txt", "w") as file:

                        file.write(f'All the actors in {Movie1} and {Movie2} are {All_Actors}\n')
                    quit()




            break


#If q is entered quits the program
    if Category == 'q' :
        print('have a good day!')
        quit()
#Uses loop to allow users to make errors
    if Category != 'actor' or Category != 'movie' or Category != 'q' :
        print('invalid category')
        continue

#Thank you for reading my messy comments!!
