# Factory 패턴
class MusicPlayerFactory:
    _instance = None

    def __new__(cls):
        # 새로운 인스턴스 생성 메소드
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_music_player(self):
        # 음악 재생기 인스턴스 생성해서 반환
        return MusicPlayer()


# Singleton 패턴
class MusicPlayer:
    _instance = None

    def __new__(cls):
        # 새로운 인스턴스 생성
        if not cls._instance:
            cls._instance = super().__new__(cls)
            # 음악 재생기의 부품들을 저장할 딕셔너리를 생성
            cls._instance._parts = {} 
        return cls._instance

    def add_part(self, part_type, part):
        # 음악 재생기의 부품 추가
        self._parts[part_type] = part

    def show(self):
        # 음악 재생기의 정보 출력
        for part_type, part in self._parts.items():
            print(f"{part_type}: {part}")


# Builder 패턴
class MusicPlayerBuilder:
    # 생성자
    def __init__(self):
        self.music_player = MusicPlayer() # 음악 재생기 객체 생성

    def build_playlist(self, playlist):
        # 플레이리스트 추가 메소드
        self.music_player.add_part("Playlist", playlist)

    def build_volume(self, volume):
        # 볼륨 추가 메소드
        self.music_player.add_part("Volume", volume)

    def build_equalizer(self, equalizer):
        # 이퀄라이저 추가 메소드
        self.music_player.add_part("Equalizer", equalizer)

    def get_result(self):
        # 완성된 음악 재생기 객체 반환 메소드
        return self.music_player


# Director 클래스
class MusicPlayerSetup:
    def __init__(self, builder):
        # 생성자
        self.builder = builder

    def construct(self):
        # 음악 재생기 설정
        # 플레이리스트 추가
        self.builder.build_playlist(["Song1", "Song2", "Song3"])
          # 볼륨 설정
        self.builder.build_volume(80)
        # 이퀄라이저 설정
        self.builder.build_equalizer("Rock")


# 클라이언트 코드
music_player_factory = MusicPlayerFactory()
builder = MusicPlayerBuilder()
music_player_setup = MusicPlayerSetup(builder)
music_player_setup.construct()
music_player = builder.get_result()

# 음악 재생기 정보 출력
music_player.show()
