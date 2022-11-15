from collections import deque


def person_is_seller(name):
    return name[-1] == "m"


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    # Создание новой очереди
    search_queue = deque()
    # Все соседи добавляются в очередь поиска
    search_queue += graph[name]
    # Этот массив используется для отслеживания уже проверенных людей
    searched = []
    # Пока очередь не пуста...
    while search_queue:
        # Из очереди извлекается первый человек
        person = search_queue.popleft()
        # Человек проверяется только в том случае, если он не проверялся ранее
        if not person in searched:
            # Проверяем, является ли этот человек продавцом манго
            if person_is_seller(person):
                # Да, это продавец манго
                print(person + " is a mango seller!")
                return True
            else:
                # Нет, не является. Все друзья этого человека добавляются в
                # очередь поиска
                search_queue += graph[person]
                searched.append(person)
    # Если выполнение дошло до этой строки, значит, в очереди нет продавца манго
    return False


search("you")
