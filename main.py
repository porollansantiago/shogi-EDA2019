from api import Api


if __name__ == "__main__":
    api_shogi = Api()
    print(api_shogi.get_board())
    while True:
        coord = input("coord: ")
        print(api_shogi.play(coord))