def solution(bandage, health, attacks):
    now_health = health
    last_attack_time = 0
    attacks.sort()
    for i in range(len(attacks)) : 
        if i == 0 :
            now_health -= attacks[0][1]
            last_attack_time = attacks[0][0]
            continue
        
        now_time = attacks[i][0]
        if now_time - last_attack_time >= bandage[0]:
            now_health += ((now_time - last_attack_time -1) // bandage[0]) * bandage[2]
        now_health += (now_time - last_attack_time - 1) * bandage[1]
        now_health = min(now_health, health)

        now_health -= attacks[i][1]
        if now_health <= 0:
            now_health = -1
            break
        last_attack_time = now_time

    return now_health

bandage = [3, 2, 7]
health = 20
attacks = [[1, 15], [5,16], [8, 6]]
print(solution(bandage, health, attacks))