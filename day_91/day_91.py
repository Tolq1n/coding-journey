#657. Robot Return to Origin
def judgeCircle(moves):
    if moves.count("R")==moves.count("L") and moves.count("U")==moves.count("D"):
        return True
    return False