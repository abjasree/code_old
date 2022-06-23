class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        curr_col = image[sr][sc]
        def fill_color(row, col):
            nonlocal rows, cols, color, curr_col, image
            if row < 0 or col < 0 or row > rows-1 or col > cols-1 or image[row][col] == color or image[row][col] != curr_col:
                return
            image[row][col] = color
            fill_color(row-1, col)
            fill_color(row, col-1)
            fill_color(row+1, col)
            fill_color(row, col+1)
            
        fill_color(sr, sc)
        return image