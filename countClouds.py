def countClouds(skyMap):

    cloud_nums = dict()
    id = 0

    def flood_fill(this_cell):
        r, c = this_cell
        neighbors = [(r - 1, col_num),
                     (r, col_num - 1),
                     (r + 1, col_num),
                     (r, col_num + 1)]
        for that_cell in neighbors:
            r, c = that_cell
            try:
                that_cell_is_cloud = int(skyMap[r][c])
            except:
                that_cell_is_cloud = False
            if that_cell_is_cloud and that_cell not in cloud_nums:
                cloud_nums[that_cell] = id
                flood_fill(that_cell)

    for row_num, row in enumerate(skyMap):
        for col_num, cell_val in enumerate(row):
            this_cell = row_num, col_num
            if int(cell_val) and this_cell not in cloud_nums:
                flood_fill(this_cell)
                id += 1

    return(id)

def countClouds2(skyMap):

    cloud_nums = dict()
    id = 0

    for row_num, row in enumerate(skyMap):
        for col_num, cell in enumerate(row):
            if int(cell):
                cloud_nums[row_num, col_num] = id
                id += 1

    def flood_fill(this_cell):
        row_num, col_num = this_cell
        neighbors = [(row_num - 1, col_num),
                     (row_num, col_num - 1),
                     (row_num + 1, col_num),
                     (row_num, col_num + 1)]
        for that_cell in neighbors:
            if that_cell in cloud_nums:
                if cloud_nums[that_cell] < cloud_nums[this_cell]:
                    cloud_nums[this_cell] = cloud_nums[that_cell]
                    flood_fill(this_cell)
                if cloud_nums[that_cell] > cloud_nums[this_cell]:
                    cloud_nums[that_cell] = cloud_nums[this_cell]
                    flood_fill(that_cell)

    for cell in cloud_nums:
        flood_fill(cell)

    return(len(set(cloud_nums.values())))

if __name__ == '__main__':
    import cProfile

    skyMap= [["0", "1", "0", "0", "1"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "1"],
             ["0", "0", "1", "1", "0"],
             ["1", "0", "1", "1", "0"]]
    print(countClouds(skyMap))
    # cProfile.run('print(countClouds(skyMap))')
    # cProfile.run('print(countClouds2(skyMap))')
