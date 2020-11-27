import collections

def solution(cacheSize, cities):
    elapsed = 0
    cache = collections.deque(maxlen=cacheSize) # maxlen maxlen maxlen
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            elapsed += 1
        else:
            cache.append(city)
            elapsed += 5
    
    
    return elapsed