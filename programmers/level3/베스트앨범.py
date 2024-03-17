def solution(genres, plays):
    answer = []
    play = {}
    music = {}
    for i in range(len(genres)) :
        play[genres[i]] = play.get(genres[i], 0) + plays[i]
        music[genres[i]] = music.get(genres[i], []) + [(i, plays[i])]
    sort_play = sorted(play.items(), key = lambda item: item[1], reverse=True)
    for i in sort_play :
        genre = i[0]
        gen_music = music.get(genre)
        gen_music.sort(key = lambda item : item[1], reverse=True)
        music_cnt = min(2, len(gen_music))
        for j in range(music_cnt) :
            answer.append(gen_music[j][0])
    return answer