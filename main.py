from api import Api


if __name__ == "__main__":
    api_shogi = Api()
    print(api_shogi.get_board())
    while True:
        coord = input("coord: ")
        board, move_array = api_shogi.play(coord)
        print(board)
        print(move_array)