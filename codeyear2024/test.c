#include <stdio.h> // รวมไฟล์ส่วนหัวสำหรับ input/output

int main() {
    int rows, i, j, space; // ประกาศตัวแปร

    printf("Enter the number of rows: "); // ขอให้ผู้ใช้ป้อนจำนวนแถว
    scanf("%d", &rows); // รับค่าจำนวนแถว

    for (i = rows; i >= 1; i--) { // วนลูปตามจำนวนแถว
        for (space = 0; space < rows - i; ++space) { // วนลูปเพื่อพิมพ์ช่องว่าง
            printf(" ");
        }
        for (j = i; j <= 2 * i - 1; ++j) { // วนลูปเพื่อพิมพ์ดอกจัน
            printf("*");
        }
        for (j = 0; j < i - 1; ++j) { // วนลูปเพื่อพิมพ์ดอกจันในส่วนล่างของสามเหลี่ยม
            printf("*");
        }
        printf("\n"); // ขึ้นบรรทัดใหม่
    }

    return 0;
}