# pylint: disable=missing-docstring

def sudoku_validator(grid):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if grid[i][j] != ".":
                num = int(grid[i][j])

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)

                box_index = (i // 3) * 3 + j // 3
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

    return True
