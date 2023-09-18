def solution(genres, plays):
    genre_dict = (
        {}
    )  # 장르 : [[총 스트리밍 횟수][(해당 고유번호 노래의 스트리밍 횟수, 노래 고유번호)...]]의 형태를 갖도록 할 것
    answer = []
    for i in range(len(genres)):  # 요소 하니씩 돌면서 확인
        try:  # 키 존재
            genre_dict[genres[i]][0][0] += plays[i]  # 총 스트리밍 수 추가
            genre_dict[genres[i]][1].append((plays[i], i))  # 노래 고유번호 당 스트리밍 수 저장
        except:  # 키 존재 x
            genre_dict[genres[i]] = [[plays[i]], [(plays[i], i)]]

    sorted_genre = sorted(
        genre_dict.values(), key=lambda x: x[0], reverse=True
    )  # 장르 별 스트리밍 수 기준 내림차순 정렬
    for total_stream, song_lst in sorted_genre:  # 장르 별 (스트리밍횟수,고유번호)의 리스트 받아옴
        song_lst = sorted(
            song_lst, key=lambda x: (x[0], -x[1]), reverse=True
        )  # 내림차순 정렬
        # 장르 내에서 재생 횟수가 같은 노래중에는 고유 번호가 낮은 노래를 먼저 수록하기 위해 정렬 조건 lambda로 추가 지정
        for song in song_lst[
            :2
        ]:  # 최대 두개까지만 수록 가능하므로 슬라이싱. 이때, song_lst요소 하나만 있어도 오류 발생 안함
            answer.append(song[1])
