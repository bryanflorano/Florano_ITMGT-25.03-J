def relationship_status(from_member, to_member, social_graph):
    from_member_following = social_graph[from_member]['following']
    to_member_following = social_graph[to_member]['following']
    if to_member in from_member_following and from_member in to_member_following:
        return 'friends'
    elif to_member in from_member_following:
        return 'follower'
    elif from_member in to_member_following:
        return 'followed by'
    else:
        return 'no relationship'

def tic_tac_toe(board):
    grid_count = len(board)
    rows = board
    cols = [[board[i][j] for i in range(grid_count)] for j in range(grid_count)]
    fwd_diag = [board[grid_count-1-i][i] for i in range(grid_count)]
    bwd_diag = [board[i][i] for i in range(grid_count)]
    lines = rows + cols + [fwd_diag] + [bwd_diag]
    for line in lines:
        if len(set(line)) == 1 and line[0] in {'X', 'O'}:
            return line[0]    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    leg_list = list(route_map)
    leg_count = len(leg_list)
    for leg in leg_list:
        if leg[0] == first_stop:
            start_leg = leg
            break
    travel_time = 0
    current_leg = start_leg
    while True:
        travel_time += route_map[current_leg]["travel_time_mins"]
        if current_leg[1] == second_stop:
            break
        next_leg_index = (leg_list.index(current_leg) + 1) % leg_count
        current_leg = leg_list[next_leg_index]
    return travel_time