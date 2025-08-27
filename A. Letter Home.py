def min_steps_to_visit_all(n, s, xs):
    # xs: list ของตำแหน่งที่ต้องเยือน (รับประกันว่าไม่ซ้ำ และเรียงจากน้อยไปมาก)
    mn = xs[0]
    mx = xs[-1]
    # ก้าวข้ามช่วงทั้งหมด
    span = mx - mn
    # ก้าวจาก s ไปยังปลายที่ใกล้กว่า
    to_end = min(abs(s - mn), abs(s - mx))
    return span + to_end

def main():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        xs = list(map(int, input().split()))
        print(min_steps_to_visit_all(n, s, xs))

if __name__ == "__main__":
    main()
