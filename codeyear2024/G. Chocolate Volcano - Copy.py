def compute_area(x_coords, y_coords):
    """ คำนวณพื้นที่ของเค้กจากพิกัด x และ y โดยใช้สูตรของรูปหลายเหลี่ยม """
    n = len(x_coords)
    area = 0
    for i in range(n - 1):
        area += (x_coords[i + 1] - x_coords[i]) * (y_coords[i + 1] + y_coords[i]) / 2
    return area

def find_cut_positions(x_coords, y_coords, m):
    """ ค้นหาตำแหน่งการตัดที่จะให้พื้นที่เท่ากัน """
    total_area = compute_area(x_coords, y_coords)
    target_area = total_area / m
    
    cut_positions = []
    current_area = 0
    n = len(x_coords)
    
    for i in range(n - 1):
        x1, y1 = x_coords[i], y_coords[i]
        x2, y2 = x_coords[i + 1], y_coords[i + 1]
        
        segment_area = (x2 - x1) * (y1 + y2) / 2
        
        while current_area + segment_area >= target_area and len(cut_positions) < m - 1:
            remaining_area = target_area - current_area
            x_cut = x1 + (remaining_area / segment_area) * (x2 - x1)
            cut_positions.append(x_cut)
            current_area = 0
            segment_area = (x2 - x1) * (y1 + y2) / 2
            x1, y1 = x_cut, (remaining_area / (x2 - x1)) * (y2 - y1) + y1
            segment_area = (x2 - x1) * (y1 + y2) / 2
        
        current_area += segment_area
    
    return cut_positions

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Read n and m
    n = int(data[0])
    m = int(data[1])
    
    # Read x coordinates
    x_coords = list(map(int, data[2:2 + n]))
    
    # Read y coordinates
    y_coords = list(map(int, data[2 + n:2 + 2 * n]))
    
    # Find cut positions
    cut_positions = find_cut_positions(x_coords, y_coords, m)
    
    # Print cut positions
    for pos in cut_positions:
        print(f"{pos:.12f}")

if __name__ == "__main__":
    main()
