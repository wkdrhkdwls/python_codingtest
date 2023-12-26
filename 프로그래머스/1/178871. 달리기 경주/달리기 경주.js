function solution(players, callings) {
    const array = new Map();
    
    players.forEach((key, value) => {
        array.set(key, value);
    })
    

    callings.forEach(key => {
        const currIdx = array.get(key);
        const front = players[currIdx - 1];

        [players[currIdx], players[currIdx -1]] = [players[currIdx -1], players[currIdx]];
        
        array.set(key, array.get(key) - 1);
        array.set(front, array.get(key) + 1);
    })
    
    
    return players;
}